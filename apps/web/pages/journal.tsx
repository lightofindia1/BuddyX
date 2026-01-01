import React, { useEffect, useMemo, useState } from "react";
import { NextPage } from "next";
import JournalCalendar from "../components/JournalCalendar";
import JournalEditor from "../components/JournalEditor";

function formatKey(date: Date) {
	return date.toISOString().slice(0, 10);
}

const JournalPage: NextPage = () => {
	const today = useMemo(() => new Date(), []);
	const [viewYear, setViewYear] = useState(today.getFullYear());
	const [viewMonth, setViewMonth] = useState(today.getMonth());
	const [selectedDate, setSelectedDate] = useState<Date>(today);
	const [content, setContent] = useState("");
	const [cipherOn, setCipherOn] = useState(false);

	useEffect(() => {
		const key = formatKey(selectedDate);
		const saved = localStorage.getItem(`journal:${key}`) || "";
		let parsed = null;
		try {
			parsed = JSON.parse(saved);
		} catch (e) {
			parsed = null;
		}

		if (parsed && typeof parsed === "object" && "text" in parsed) {
			if (parsed.cipher) {
				// stored text is ciphered; decrypt into content and keep cipher on
				const decrypted = (() => {
					const s: string = parsed.text || "";
					// simple Caesar decrypt with shift 3
					return s.replace(/[a-zA-Z]/g, (c) => {
						const base = c <= "Z" ? 65 : 97;
						return String.fromCharCode(((c.charCodeAt(0) - base + 23) % 26) + base);
					});
				})();
				setContent(decrypted);
				setCipherOn(true);
			} else {
				setContent(parsed.text || "");
				setCipherOn(false);
			}
		} else {
			setContent(saved || "");
			setCipherOn(false);
		}
	}, [selectedDate]);

	function changeMonth(delta: number) {
		const newMonth = viewMonth + delta;
		const date = new Date(viewYear, newMonth, 1);
		setViewYear(date.getFullYear());
		setViewMonth(date.getMonth());
	}

	function onSave() {
		const key = formatKey(selectedDate);
		const toStore = cipherOn
			? { cipher: true, text: (() => {
					const s = content || "";
					return s.replace(/[a-zA-Z]/g, (c) => {
						const base = c <= "Z" ? 65 : 97;
						return String.fromCharCode(((c.charCodeAt(0) - base + 3) % 26) + base);
					});
				})() }
			: { cipher: false, text: content || "" };
		localStorage.setItem(`journal:${key}`, JSON.stringify(toStore));
	}

	function onClear() {
		setContent("");
		localStorage.removeItem(`journal:${formatKey(selectedDate)}`);
	}

	return (
		<div className="flex h-screen bg-gray-50 text-gray-900">
			<JournalCalendar
				viewYear={viewYear}
				viewMonth={viewMonth}
				onChangeMonth={changeMonth}
				selectedDate={selectedDate}
				setSelectedDate={setSelectedDate}
			/>

			<JournalEditor
				selectedDate={selectedDate}
				content={content}
				setContent={setContent}
				onSave={onSave}
				onClear={onClear}
				cipherOn={cipherOn}
				setCipherOn={setCipherOn}
			/>
		</div>
	);
};

export default JournalPage;
