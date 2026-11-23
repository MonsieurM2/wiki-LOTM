import { useEffect, useState } from 'react';

type PagefindData = {
  url: string;
  excerpt: string;
  meta?: Record<string, string>;
};

type PagefindResult = { data: () => Promise<PagefindData> };

type Pagefind = {
  init?: () => Promise<void>;
  search: (query: string) => Promise<{ results: PagefindResult[] }>;
};

type Hit = { href: string; title: string; excerpt: string };

function targetFor(rawUrl: string): { href: string; title: string } {
  let path = rawUrl || '';
  try {
    path = new URL(rawUrl, window.location.origin).pathname;
  } catch {
    path = rawUrl.split(/[?#]/)[0] || '';
  }
  const base = (import.meta.env.BASE_URL || '/').replace(/\/$/, '');
  const chapter = path.match(/\/chapter\/(\d+)/);
  if (chapter) return { href: `${base}/chapter/${chapter[1]}/`, title: `Chapter ${chapter[1]}` };
  const entity = path.match(/\/entity\/([^/?#]+)/);
  if (entity) return { href: `${base}/entity/${entity[1]}/`, title: `Entity ${entity[1]}` };
  return { href: path, title: 'Record' };
}

export default function SearchIsland() {
  const [pagefind, setPagefind] = useState<Pagefind | null>(null);
  const [unavailable, setUnavailable] = useState(false);
  const [query, setQuery] = useState('');
  const [hits, setHits] = useState<Hit[]>([]);

  useEffect(() => {
    let cancelled = false;
    async function load() {
      try {
        // Vite serves index.html for unknown paths in dev, so probe before importing.
        const base = (import.meta.env.BASE_URL || '/').replace(/\/$/, '');
        const probe = await fetch(`${base}/pagefind/pagefind.js`);
        const type = probe.headers.get('content-type') || '';
        if (!probe.ok || !/javascript|ecmascript/i.test(type)) {
          if (!cancelled) setUnavailable(true);
          return;
        }
        // @ts-ignore: Pagefind exists only in the built site, not at typecheck time.
        const pagefindModule = `${base}/pagefind/pagefind.js`;
        const mod = await import(/* @vite-ignore */ pagefindModule);
        const api: Pagefind = (mod as { default?: Pagefind }).default ?? (mod as Pagefind);
        if (api.init) await api.init();
        if (!cancelled) setPagefind(api);
      } catch {
        // No index in development: leave the discreet note, never log.
        if (!cancelled) setUnavailable(true);
      }
    }
    void load();
    return () => {
      cancelled = true;
    };
  }, []);

  useEffect(() => {
    const term = query.trim();
    if (!pagefind || !term) {
      setHits([]);
      return;
    }
    let cancelled = false;
    void pagefind
      .search(term)
      .then(async (search) => {
        const next: Hit[] = await Promise.all(
          search.results.slice(0, 10).map(async (result) => {
            const data = await result.data();
            const target = targetFor(data.url);
            return {
              href: target.href,
              title: data.meta?.title || target.title,
              excerpt: (data.excerpt || '').replace(/<[^>]*>/g, ''),
            };
          }),
        );
        if (!cancelled) setHits(next);
      })
      .catch(() => {
        if (!cancelled) setHits([]);
      });
    return () => {
      cancelled = true;
    };
  }, [pagefind, query]);

  return (
    <section className="search-island" aria-label="Search the case files">
      <label className="search-label" htmlFor="site-search">
        Search
      </label>
      <input
        id="site-search"
        className="search-input"
        type="search"
        value={query}
        onChange={(event) => setQuery(event.target.value)}
        placeholder="Names, places, events"
      />
      {unavailable && <p className="search-note">Search index unavailable in development.</p>}
      {hits.length > 0 && (
        <ul className="search-results">
          {hits.map((hit, index) => (
            <li className="search-result" key={`${hit.href}-${index}`}>
              <a className="search-result-link" href={hit.href}>
                <span className="search-result-title">{hit.title}</span>
                <span className="search-result-excerpt">{hit.excerpt}</span>
              </a>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}
