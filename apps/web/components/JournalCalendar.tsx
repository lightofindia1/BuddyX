import React, { useMemo } from "react";

const MONTH_NAMES = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

const DAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

function formatKey(date: Date) {
  return date.toISOString().slice(0, 10);
}

function buildMonthGrid(year: number, month: number) {
  const first = new Date(year, month, 1);
  const startDay = first.getDay();
  const daysInMonth = new Date(year, month + 1, 0).getDate();

  const cells: (Date | null)[] = [];
  for (let i = 0; i < startDay; i++) cells.push(null);
  for (let d = 1; d <= daysInMonth; d++) cells.push(new Date(year, month, d));
  while (cells.length < 42) cells.push(null);
  return cells;
}

type Props = {
  viewYear: number;
  viewMonth: number;
  onChangeMonth: (delta: number) => void;
  selectedDate: Date;
  setSelectedDate: (d: Date) => void;
};

export default function JournalCalendar({
  viewYear,
  viewMonth,
  onChangeMonth,
  selectedDate,
  setSelectedDate,
}: Props) {
  const grid = useMemo(() => buildMonthGrid(viewYear, viewMonth), [viewYear, viewMonth]);

  return (
    <aside className="w-[30%] border-r bg-white p-4 overflow-auto">
      <div className="flex items-center justify-between mb-3">
        <button
          aria-label="Previous month"
          className="px-2 py-1 rounded hover:bg-gray-100"
          onClick={() => onChangeMonth(-1)}
        >
          ‹
        </button>
        <div className="text-lg font-medium">
          {MONTH_NAMES[viewMonth]} {viewYear}
        </div>
        <button
          aria-label="Next month"
          className="px-2 py-1 rounded hover:bg-gray-100"
          onClick={() => onChangeMonth(1)}
        >
          ›
        </button>
      </div>

      <div className="grid grid-cols-7 text-sm text-center text-gray-500">
        {DAYS.map((d) => (
          <div key={d} className="py-1">
            {d}
          </div>
        ))}
      </div>

      <div className="grid grid-cols-7 gap-1 mt-2">
        {grid.map((cell, idx) => {
          if (!cell) return <div key={idx} className="h-12" />;
          const isSelected = formatKey(cell) === formatKey(selectedDate);
          const isToday = formatKey(cell) === formatKey(new Date());
          return (
            <button
              key={idx}
              onClick={() => setSelectedDate(cell)}
              className={`h-12 flex items-center justify-center rounded focus:outline-none ${
                isSelected ? "bg-blue-600 text-white" : "hover:bg-gray-100"
              } ${isToday && !isSelected ? "border border-blue-300" : ""}`}
            >
              {cell.getDate()}
            </button>
          );
        })}
      </div>

      <div className="mt-4 text-sm text-gray-600">
        <div className="font-medium mb-1">Selected</div>
        <div>{selectedDate.toDateString()}</div>
      </div>
    </aside>
  );
}
