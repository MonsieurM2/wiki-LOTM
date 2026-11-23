import { useEffect, useState } from 'react';

const STORAGE_KEY = 'lotm-veil';
const BODY_CLASS = 'veil-on';

export default function SpoilerVeil() {
  const [on, setOn] = useState(false);

  useEffect(() => {
    let stored = false;
    try {
      stored = window.localStorage.getItem(STORAGE_KEY) === 'on';
    } catch {
      // Storage can be blocked; the veil stays off.
    }
    setOn(stored);
    document.body.classList.toggle(BODY_CLASS, stored);
    return () => document.body.classList.remove(BODY_CLASS);
  }, []);

  function toggle() {
    const next = !on;
    setOn(next);
    try {
      window.localStorage.setItem(STORAGE_KEY, next ? 'on' : 'off');
    } catch {
      // Storage can be blocked; keep the in-memory state.
    }
    document.body.classList.toggle(BODY_CLASS, next);
  }

  return (
    <aside className="veil-control" aria-label="Spoiler veil">
      <label className="veil-toggle">
        <input type="checkbox" checked={on} onChange={toggle} />
        <span>Hide spoilers</span>
      </label>
      <p className="veil-note">The veil is not a guarantee — search indexes the text.</p>
    </aside>
  );
}
