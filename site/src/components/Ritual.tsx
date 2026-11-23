import { useEffect, useState } from 'react';

type Card = { roman: string; name: string };

const ARCANA: readonly Card[] = [
  { roman: '0', name: 'The Fool' },
  { roman: 'I', name: 'The Magician' },
  { roman: 'II', name: 'The High Priestess' },
  { roman: 'III', name: 'The Empress' },
  { roman: 'IV', name: 'The Emperor' },
  { roman: 'V', name: 'The Hierophant' },
  { roman: 'VI', name: 'The Lovers' },
  { roman: 'VII', name: 'The Chariot' },
  { roman: 'VIII', name: 'Strength' },
  { roman: 'IX', name: 'The Hermit' },
  { roman: 'X', name: 'Wheel of Fortune' },
  { roman: 'XI', name: 'Justice' },
  { roman: 'XII', name: 'The Hanged Man' },
  { roman: 'XIII', name: 'Death' },
  { roman: 'XIV', name: 'Temperance' },
  { roman: 'XV', name: 'The Devil' },
  { roman: 'XVI', name: 'The Tower' },
  { roman: 'XVII', name: 'The Star' },
  { roman: 'XVIII', name: 'The Moon' },
  { roman: 'XIX', name: 'The Sun' },
  { roman: 'XX', name: 'Judgement' },
  { roman: 'XXI', name: 'The World' },
];

function seedFromDate(date: string): number {
  let hash = 2166136261;
  for (let i = 0; i < date.length; i += 1) {
    hash ^= date.charCodeAt(i);
    hash = Math.imul(hash, 16777619);
  }
  return hash >>> 0;
}

function mulberry32(seed: number): () => number {
  let state = seed >>> 0;
  return () => {
    state = (state + 0x6d2b79f5) | 0;
    let t = Math.imul(state ^ (state >>> 15), 1 | state);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function drawForDate(date: string): Card[] {
  const random = mulberry32(seedFromDate(date));
  const indices = ARCANA.map((_, index) => index);
  for (let i = indices.length - 1; i > 0; i -= 1) {
    const j = Math.floor(random() * (i + 1));
    [indices[i], indices[j]] = [indices[j], indices[i]];
  }
  return indices.slice(0, 3).map((index) => ARCANA[index]);
}

export default function Ritual() {
  const [spread, setSpread] = useState<Card[]>([]);
  const [date, setDate] = useState('');
  const [revealed, setRevealed] = useState(false);
  const [still, setStill] = useState(false);

  useEffect(() => {
    const today = new Date().toISOString().slice(0, 10);
    setSpread(drawForDate(today));
    setDate(today);
    setStill(window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  }, []);

  return (
    <section className={still ? 'ritual ritual-still' : 'ritual'} aria-labelledby="ritual-title">
      <h2 id="ritual-title" className="ritual-title">
        Daily spread
      </h2>
      <p className="ritual-date">{date}</p>
      {!revealed && (
        <button className="ritual-reveal" type="button" onClick={() => setRevealed(true)}>
          Reveal the spread
        </button>
      )}
      <ul className="ritual-cards">
        {spread.map((card) => (
          <li className="ritual-card" key={card.roman}>
            <span className="ritual-card-number">{card.roman}</span>
            <span className="ritual-card-name">{revealed ? card.name : '•••'}</span>
          </li>
        ))}
      </ul>
    </section>
  );
}
