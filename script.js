// Available timezones for dropdown selection
const AVAILABLE_TIMEZONES = [
  { name: "UTC", zone: "UTC" },
  { name: "London", zone: "Europe/London" },
  { name: "Paris", zone: "Europe/Paris" },
  { name: "Berlin", zone: "Europe/Berlin" },
  { name: "Rome", zone: "Europe/Rome" },
  { name: "Moscow", zone: "Europe/Moscow" },
  { name: "New York", zone: "America/New_York" },
  { name: "Los Angeles", zone: "America/Los_Angeles" },
  { name: "Chicago", zone: "America/Chicago" },
  { name: "Denver", zone: "America/Denver" },
  { name: "Toronto", zone: "America/Toronto" },
  { name: "Mexico City", zone: "America/Mexico_City" },
  { name: "São Paulo", zone: "America/Sao_Paulo" },
  { name: "Buenos Aires", zone: "America/Argentina/Buenos_Aires" },
  { name: "Tokyo", zone: "Asia/Tokyo" },
  { name: "Shanghai", zone: "Asia/Shanghai" },
  { name: "Hong Kong", zone: "Asia/Hong_Kong" },
  { name: "Singapore", zone: "Asia/Singapore" },
  { name: "Mumbai", zone: "Asia/Kolkata" },
  { name: "Dubai", zone: "Asia/Dubai" },
  { name: "Seoul", zone: "Asia/Seoul" },
  { name: "Bangkok", zone: "Asia/Bangkok" },
  { name: "Sydney", zone: "Australia/Sydney" },
  { name: "Melbourne", zone: "Australia/Melbourne" },
  { name: "Perth", zone: "Australia/Perth" },
  { name: "Auckland", zone: "Pacific/Auckland" },
  { name: "Honolulu", zone: "Pacific/Honolulu" },
  { name: "Cairo", zone: "Africa/Cairo" },
  { name: "Lagos", zone: "Africa/Lagos" },
  { name: "Johannesburg", zone: "Africa/Johannesburg" }
];

// Default configuration for six clocks
const DEFAULT_ZONES = [
  { city: "London", zone: "Europe/London" },
  { city: "New York", zone: "America/New_York" },
  { city: "Paris", zone: "Europe/Paris" },
  { city: "Tokyo", zone: "Asia/Tokyo" },
  { city: "Sydney", zone: "Australia/Sydney" },
  { city: "UTC", zone: "UTC" }
];

// Load saved preferences or use defaults
function loadSavedZones() {
  try {
    const saved = localStorage.getItem('worldClockZones');
    return saved ? JSON.parse(saved) : DEFAULT_ZONES;
  } catch {
    return DEFAULT_ZONES;
  }
}

// Save current zones to localStorage
function saveZones(zones) {
  try {
    localStorage.setItem('worldClockZones', JSON.stringify(zones));
  } catch {
    // Ignore storage errors
  }
}

let ZONES = loadSavedZones();

const grid = document.getElementById("grid");

// Build one clock card
function createClockCard({ city, zone }, index) {
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
  let fmt = new Intl.DateTimeFormat("en-GB", {
    timeZone: zone,
    hour: "numeric",
    minute: "numeric",
    second: "numeric",
    hour12: false
  });

  let digitalFmt = new Intl.DateTimeFormat("en-GB", {
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
let cards = ZONES.map((zone, index) => createClockCard(zone, index));
cards.forEach(c => grid.appendChild(c));

// Initialize timezone controls
function initializeTimezoneControls() {
  const clockSelector = document.getElementById('clockSelector');
  const timezoneSelector = document.getElementById('timezoneSelector');
  
  // Populate timezone dropdown
  AVAILABLE_TIMEZONES.forEach(tz => {
    const option = document.createElement('option');
    option.value = tz.zone;
    option.textContent = tz.name;
    timezoneSelector.appendChild(option);
  });
  
  // Update timezone selector when clock is selected
  function updateTimezoneSelector() {
    const selectedClockIndex = parseInt(clockSelector.value);
    const currentZone = ZONES[selectedClockIndex].zone;
    timezoneSelector.value = currentZone;
  }
  
  // Handle clock selection change
  clockSelector.addEventListener('change', updateTimezoneSelector);
  
  // Handle timezone change
  timezoneSelector.addEventListener('change', function() {
    const selectedClockIndex = parseInt(clockSelector.value);
    const newTimezone = timezoneSelector.value;
    const newTimezoneData = AVAILABLE_TIMEZONES.find(tz => tz.zone === newTimezone);
    
    if (newTimezoneData) {
      // Update the ZONES array
      ZONES[selectedClockIndex] = {
        city: newTimezoneData.name,
        zone: newTimezoneData.zone
      };
      
      // Save to localStorage
      saveZones(ZONES);
      
      // Remove old clock card
      const oldCard = cards[selectedClockIndex];
      if (oldCard.cleanup) oldCard.cleanup();
      grid.removeChild(oldCard);
      
      // Create and insert new clock card
      const newCard = createClockCard(ZONES[selectedClockIndex], selectedClockIndex);
      cards[selectedClockIndex] = newCard;
      
      // Insert at correct position
      const nextSibling = grid.children[selectedClockIndex];
      if (nextSibling) {
        grid.insertBefore(newCard, nextSibling);
      } else {
        grid.appendChild(newCard);
      }
    }
  });
  
  // Initialize with first clock selected
  updateTimezoneSelector();
}

// Initialize controls after DOM is ready
initializeTimezoneControls();

// Cleanup on unload
window.addEventListener("beforeunload", () => cards.forEach(c => c.cleanup?.()));
