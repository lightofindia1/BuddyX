import React, { useEffect, useRef } from "react";

type Props = {
  selectedDate: Date;
  content: string;
  setContent: (s: string) => void;
  onSave: () => void;
  onClear: () => void;
  cipherOn: boolean;
  setCipherOn: (b: boolean) => void;
};

function caesarEncrypt(str: string, shift = 3) {
  return str.replace(/[a-zA-Z]/g, (c) => {
    const base = c <= "Z" ? 65 : 97;
    return String.fromCharCode(((c.charCodeAt(0) - base + shift) % 26) + base);
  });
}

function caesarDecrypt(str: string, shift = 3) {
  return caesarEncrypt(str, 26 - (shift % 26));
}

export default function JournalEditor({
  selectedDate,
  content,
  setContent,
  onSave,
  onClear,
  cipherOn,
  setCipherOn,
}: Props) {
  const ref = useRef<HTMLTextAreaElement | null>(null);
  const selRef = useRef<{ start: number; end: number } | null>(null);

  function setDisplayedFromDecrypted(decrypted: string, caretPos?: number | null) {
    if (!ref.current) return;
    const displayed = cipherOn ? caesarEncrypt(decrypted) : decrypted;
    ref.current.value = displayed;
    if (typeof caretPos === "number") {
      const pos = Math.min(displayed.length, Math.max(0, caretPos));
      ref.current.setSelectionRange(pos, pos);
    }
  }

  useEffect(() => {
    setDisplayedFromDecrypted(content, selRef.current ? selRef.current.end : null);
  }, [content, cipherOn]);

  function handleBeforeInput(e: React.FormEvent<HTMLTextAreaElement>) {
    if (!cipherOn) return;
    const ne = e.nativeEvent as InputEvent;
    const data = (ne as any).data as string | null;
    if (!ref.current) return;
    // ignore composition and control inputs
    if (!data) return;
    // allow ctrl/meta shortcuts
    if ((ne as any).ctrlKey || (ne as any).metaKey) return;
    e.preventDefault();

    const ta = ref.current;
    const start = ta.selectionStart || 0;
    const end = ta.selectionEnd || 0;
    const inserted = data;

    const newDecrypted = content.slice(0, start) + inserted + content.slice(end);
    const newCaret = start + inserted.length;
    setContent(newDecrypted);
    selRef.current = { start: newCaret, end: newCaret };
    // displayed will update via effect
  }

  function handlePaste(e: React.ClipboardEvent<HTMLTextAreaElement>) {
    if (!cipherOn) return;
    e.preventDefault();
    const pasted = e.clipboardData.getData("text") || "";
    if (!ref.current) return;
    const ta = ref.current;
    const start = ta.selectionStart || 0;
    const end = ta.selectionEnd || 0;
    const newDecrypted = content.slice(0, start) + pasted + content.slice(end);
    const newCaret = start + pasted.length;
    setContent(newDecrypted);
    selRef.current = { start: newCaret, end: newCaret };
  }

  function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (!cipherOn) return;
    if (!ref.current) return;
    const ta = ref.current;
    const start = ta.selectionStart || 0;
    const end = ta.selectionEnd || 0;

    // allow navigation + modifiers
    if (e.ctrlKey || e.metaKey || e.altKey) return;

    if (e.key === "Backspace") {
      e.preventDefault();
      if (start !== end) {
        const newDecrypted = content.slice(0, start) + content.slice(end);
        setContent(newDecrypted);
        selRef.current = { start, end: start };
      } else if (start > 0) {
        const newDecrypted = content.slice(0, start - 1) + content.slice(end);
        const newCaret = start - 1;
        setContent(newDecrypted);
        selRef.current = { start: newCaret, end: newCaret };
      }
    } else if (e.key === "Delete") {
      e.preventDefault();
      if (start !== end) {
        const newDecrypted = content.slice(0, start) + content.slice(end);
        setContent(newDecrypted);
        selRef.current = { start, end: start };
      } else if (start < content.length) {
        const newDecrypted = content.slice(0, start) + content.slice(start + 1);
        setContent(newDecrypted);
        selRef.current = { start, end: start };
      }
    }
    // arrows and other keys -- let browser handle selection
  }

  function handleChange(e: React.ChangeEvent<HTMLTextAreaElement>) {
    const raw = e.target.value || "";
    if (cipherOn) {
      // displayed is ciphered; decrypt to internal content
      setContent(caesarDecrypt(raw));
    } else {
      setContent(raw);
    }
    selRef.current = { start: e.target.selectionStart || 0, end: e.target.selectionEnd || 0 };
  }

  return (
    <main className="w-[70%] p-6 overflow-auto">
      <div className="max-w-4xl">
        <div className="flex items-center justify-between">
          <h1 className="text-2xl font-semibold mb-2">Journal — {selectedDate.toDateString()}</h1>
          <div className="flex items-center gap-3">
            <label className="flex items-center gap-2 text-sm">
              <input
                type="checkbox"
                checked={cipherOn}
                onChange={(e) => setCipherOn(e.target.checked)}
              />
              Obfuscate (Caesar)
            </label>
          </div>
        </div>

        <textarea
          ref={ref}
          onBeforeInput={handleBeforeInput}
          onKeyDown={handleKeyDown}
          onPaste={handlePaste}
          onChange={handleChange}
          placeholder="Write your thoughts..."
          className="w-full h-[60vh] p-4 border rounded resize-none focus:ring focus:ring-blue-200"
        />

        <div className="flex items-center gap-3 mt-4">
          <button onClick={onSave} className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
            Save
          </button>
          <button onClick={onClear} className="px-3 py-2 border rounded hover:bg-gray-50">
            Clear
          </button>
        </div>
      </div>
    </main>
  );
}
