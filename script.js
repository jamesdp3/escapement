// Configure six time zones and labels here
const ZONES = [
  { city: "London",      zone: "Europe/London" },
  { city: "New York",    zone: "America/New_York" },
  { city: "Paris",       zone: "Europe/Paris" },
  { city: "Tokyo",       zone: "Asia/Tokyo" },
  { city: "Sydney",      zone: "Australia/Sydney" },
  { city: "UTC",         zone: "UTC" }
];

const grid = document.getElementById("grid");

// Build one clock card
function createClockCard({ city, zone }) {
  const card = document.createElement("section");
  card.className = "clock-card";

  const dial = document.createElement("div");
  dial.className = "dial";

  // hour ticks (12) + minor ticks (60)
  for (let i = 0; i < 60; i++) {
    const t = document.createElement("div");
    t.className = "tick" + (i % 5 === 0 ? "" : " minor");
    t.style.transform = `translate(-50%, -50%) rotate(${i * 6}deg)`;
    dial.appendChild(t);
  }

  const hour = document.createElement("div");   hour.className = "hand hour";
  const minute = document.createElement("div"); minute.className = "hand minute";
  const second = document.createElement("div"); second.className = "hand second";
  const dot = document.createElement("div");    dot.className = "center-dot";

  dial.append(hour, minute, second, dot);

  const label = document.createElement("div");
  label.className = "label";
  label.textContent = city;

  const digitalTime = document.createElement("div");
  digitalTime.className = "digital-time";

  const sub = document.createElement("div");
  sub.className = "sub";
  sub.textContent = zone;

  card.append(dial, label, digitalTime, sub);

  // updater
  const fmt = new Intl.DateTimeFormat("en-GB", {
    timeZone: zone,
    hour: "numeric",
    minute: "numeric",
    second: "numeric",
    hour12: false
  });

  const digitalFmt = new Intl.DateTimeFormat("en-GB", {
    timeZone: zone,
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hour12: false
  });

  function update() {
    const parts = fmt.formatToParts(new Date());
    const get = k => Number(parts.find(p => p.type === k).value);

    const h = get("hour");
    const m = get("minute");
    const s = get("second");

    const hAngle = ((h % 12) + m / 60 + s / 3600) * 30;   // 360/12
    const mAngle = (m + s / 60) * 6;                      // 360/60
    const sAngle = s * 6;

    hour.style.transform   = `translate(-50%, -100%) rotate(${hAngle}deg)`;
    minute.style.transform = `translate(-50%, -100%) rotate(${mAngle}deg)`;
    second.style.transform = `translate(-50%, -100%) rotate(${sAngle}deg)`;

    // Update digital time display
    digitalTime.textContent = digitalFmt.format(new Date());
  }

  update();
  const timer = setInterval(update, 1000);
  // in case of unload
  card.cleanup = () => clearInterval(timer);

  return card;
}

// Render all clocks
const cards = ZONES.map(createClockCard);
cards.forEach(c => grid.appendChild(c));

// Cleanup on unload
window.addEventListener("beforeunload", () => cards.forEach(c => c.cleanup?.()));
