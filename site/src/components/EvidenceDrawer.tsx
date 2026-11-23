import { useCallback, useEffect, useRef, useState } from 'react';

export type Evidence = {
  id: string;
  quote: string;
  book: number;
  chapter: number;
  chapterTitle: string;
};

export default function EvidenceDrawer({ evidence }: { evidence: Evidence[] }) {
  const [active, setActive] = useState<Evidence | null>(null);
  const triggerRef = useRef<HTMLElement | null>(null);
  const closeRef = useRef<HTMLButtonElement | null>(null);

  const close = useCallback(() => {
    setActive(null);
    triggerRef.current?.focus();
    triggerRef.current = null;
  }, []);

  useEffect(() => {
    function onClick(event: MouseEvent) {
      const target = event.target;
      if (!(target instanceof Element)) return;
      const node = target.closest('[data-evidence-id]');
      if (!node) return;
      const id = node.getAttribute('data-evidence-id');
      const found = id ? evidence.find((item) => item.id === id) : undefined;
      if (!found) return;
      triggerRef.current = node as HTMLElement;
      setActive(found);
    }
    document.addEventListener('click', onClick);
    return () => document.removeEventListener('click', onClick);
  }, [evidence]);

  useEffect(() => {
    if (!active) return;
    closeRef.current?.focus();
    function onKeyDown(event: KeyboardEvent) {
      if (event.key === 'Escape') close();
    }
    document.addEventListener('keydown', onKeyDown);
    return () => document.removeEventListener('keydown', onKeyDown);
  }, [active, close]);

  if (!active) return null;

  return (
    <aside className="evidence-drawer" role="dialog" aria-modal="true" aria-labelledby="evidence-drawer-title">
      <button
        ref={closeRef}
        className="evidence-drawer-close"
        type="button"
        onClick={close}
        aria-label="Close evidence"
      >
        Close
      </button>
      <h2 id="evidence-drawer-title" className="evidence-drawer-title">
        Evidence {active.id}
      </h2>
      <blockquote className="evidence-drawer-quote">{active.quote}</blockquote>
      <p className="evidence-drawer-source">
        Volume {active.book}, chapter {active.chapter}
      </p>
      <p className="evidence-drawer-chapter">{active.chapterTitle}</p>
    </aside>
  );
}
