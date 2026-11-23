import fs from 'node:fs';
import path from 'node:path';

export interface Alias { form: string; until?: number }
export interface Entity {
  id: string;
  canonical_name: string;
  primary_type: string;
  aliases?: Alias[];
  tags?: string[];
}
export interface Evidence {
  id: string;
  book: number;
  chapter: number;
  chapter_title: string;
  quote: string;
  offsets?: [number, number];
  verifier: string;
  status: string;
}
export interface Mention { id: string; entity: string; evidence_ids: string[] }
export interface Event {
  id: string;
  label: string;
  participants?: string[];
  evidence_ids: string[];
}
export interface Relation {
  id: string;
  type: string;
  inverse: string;
  source: string;
  target: string;
  evidence_ids: string[];
}
export interface Chapter {
  id: string;
  book: number;
  number: number;
  title: string;
  text: string;
  status: string;
  entities: Entity[];
  evidence: Evidence[];
  mentions: Mention[];
  events: Event[];
  relations: Relation[];
}

export interface Appearance {
  chapter: number;
  book: number;
  chapterTitle: string;
  evidence: { id: string; quote: string }[];
}

export interface EntityFiche extends Entity {
  appearances: Appearance[];
  first: { chapter: number; book: number; quote: string; evidenceId: string };
}

// Astro builds with cwd = site/; import.meta.url points at the bundled chunk, not the source.
const chaptersDir = path.resolve(process.cwd(), '..', 'data', 'chapters');

export function loadChapters(): Chapter[] {
  if (!fs.existsSync(chaptersDir)) return [];
  return fs.readdirSync(chaptersDir)
    .filter((f) => /^C\d{4}\.json$/.test(f))
    .sort()
    .map((f) => JSON.parse(fs.readFileSync(path.join(chaptersDir, f), 'utf8')) as Chapter)
    .filter((c) => c.status !== 'excluded');
}

export function loadEntityFiches(chapters: Chapter[]): EntityFiche[] {
  const byId = new Map<string, EntityFiche>();
  for (const c of chapters) {
    for (const e of c.entities) {
      if (!byId.has(e.id)) {
        byId.set(e.id, { ...e, appearances: [], first: { chapter: c.number, book: c.book, quote: '', evidenceId: '' } });
      }
      const fiche = byId.get(e.id)!;
      fiche.aliases = e.aliases ?? fiche.aliases;
      fiche.tags = e.tags ?? fiche.tags;
      const evidence = c.evidence.filter((ev) =>
        c.mentions.some((m) => m.entity === e.id && m.evidence_ids.includes(ev.id))
      );
      fiche.appearances.push({
        chapter: c.number,
        book: c.book,
        chapterTitle: c.title,
        evidence: evidence.map((ev) => ({ id: ev.id, quote: ev.quote })),
      });
      for (const ev of evidence) {
        const offset = ev.offsets?.[0] ?? c.text.indexOf(ev.quote);
        const current = fiche.first;
        const better = c.number < current.chapter ||
          (c.number === current.chapter && offset < c.text.indexOf(current.quote || '\u0000'));
        if (!current.quote || better) {
          fiche.first = { chapter: c.number, book: c.book, quote: ev.quote, evidenceId: ev.id };
        }
      }
    }
  }
  return [...byId.values()].sort((a, b) => a.canonical_name.localeCompare(b.canonical_name));
}

export function escapeHtml(value: string): string {
  return value.replace(/[&<>"']/g, (ch) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
  }[ch]!));
}

interface Mark { start: number; end: number; kind: 'evidence' | 'entity'; id: string }

/** First naming and literal evidence are marked in the chapter prose. */
export function annotateProse(chapter: Chapter): string {
  const marks: Mark[] = [];
  for (const ev of chapter.evidence) {
    const start = ev.offsets?.[0] ?? chapter.text.indexOf(ev.quote);
    if (start >= 0 && chapter.text.slice(start, start + ev.quote.length) === ev.quote) {
      marks.push({ start, end: start + ev.quote.length, kind: 'evidence', id: ev.id });
    }
  }
  for (const entity of chapter.entities) {
    const names = [entity.canonical_name, ...(entity.aliases ?? []).map((a) => a.form)];
    for (const name of names) {
      const at = chapter.text.indexOf(name);
      if (at >= 0 && !marks.some((m) => at >= m.start && at < m.end)) {
        marks.push({ start: at, end: at + name.length, kind: 'entity', id: entity.id });
        break;
      }
    }
  }
  marks.sort((a, b) => a.start - b.start || b.end - a.end);
  const kept: Mark[] = [];
  for (const mark of marks) {
    if (!kept.some((m) => mark.start < m.end && m.start < mark.end)) kept.push(mark);
  }
  let html = '';
  let cursor = 0;
  for (const mark of kept) {
    html += escapeHtml(chapter.text.slice(cursor, mark.start));
    const inner = escapeHtml(chapter.text.slice(mark.start, mark.end));
    html += mark.kind === 'evidence'
      ? `<span class="proofable" tabindex="0" role="button" data-evidence-id="${mark.id}">${inner}</span>`
      : `<a class="entity" href="/wiki-LOTM/entity/${mark.id}/" data-evidence-id="${mark.id}">${inner}</a>`;
    cursor = mark.end;
  }
  html += escapeHtml(chapter.text.slice(cursor));
  return html.split(/\n{2,}/).map((p) => `<p>${p.replace(/\n/g, '<br>')}</p>`).join('');
}
