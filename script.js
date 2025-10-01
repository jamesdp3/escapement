// Available timezones - loaded from external file
let AVAILABLE_TIMEZONES = [];

// Load timezones from external JSON file
async function loadTimezones() {
  try {
    const response = await fetch('./timezones.json');
    const data = await response.json();
    AVAILABLE_TIMEZONES = data.timezones;
  } catch (error) {
    console.error('Failed to load timezones:', error);
    // Fallback to a minimal set if loading fails
    AVAILABLE_TIMEZONES = [
      { name: "UTC", zone: "UTC" },
      { name: "London", zone: "Europe/London" },
      { name: "New York", zone: "America/New_York" },
      { name: "Paris", zone: "Europe/Paris" },
      { name: "Tokyo", zone: "Asia/Tokyo" },
      { name: "Sydney", zone: "Australia/Sydney" }
    ];
  }
}

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
  const timezoneSearch = document.getElementById('timezoneSearch');
  const timezoneDropdown = document.getElementById('timezoneDropdown');
  
  let filteredTimezones = [...AVAILABLE_TIMEZONES];
  let selectedIndex = -1;
  let currentSelectedClockIndex = 0;
  
  // Update search input when clock is selected
  function updateSearchInput() {
    currentSelectedClockIndex = parseInt(clockSelector.value);
    const currentZone = ZONES[currentSelectedClockIndex].zone;
    const currentTimezone = AVAILABLE_TIMEZONES.find(tz => tz.zone === currentZone);
    timezoneSearch.value = currentTimezone ? currentTimezone.name : '';
    hideDropdown();
  }
  
  // Filter timezones based on search input
  function filterTimezones(searchTerm) {
    if (!searchTerm.trim()) {
      filteredTimezones = [...AVAILABLE_TIMEZONES];
    } else {
      const term = searchTerm.toLowerCase();
      filteredTimezones = AVAILABLE_TIMEZONES.filter(tz => 
        tz.name.toLowerCase().includes(term)
      );
    }
    selectedIndex = -1;
    renderDropdown();
  }
  
  // Render dropdown items
  function renderDropdown() {
    timezoneDropdown.innerHTML = '';
    
    if (filteredTimezones.length === 0) {
      const noResults = document.createElement('div');
      noResults.className = 'no-results';
      noResults.textContent = 'No cities found';
      timezoneDropdown.appendChild(noResults);
    } else {
      filteredTimezones.forEach((tz, index) => {
        const item = document.createElement('div');
        item.className = 'dropdown-item';
        if (index === selectedIndex) {
          item.classList.add('highlighted');
        }
        item.textContent = tz.name;
        item.dataset.zone = tz.zone;
        item.dataset.index = index;
        
        item.addEventListener('click', () => selectTimezone(tz));
        timezoneDropdown.appendChild(item);
      });
    }
  }
  
  // Show dropdown
  function showDropdown() {
    timezoneDropdown.classList.add('show');
  }
  
  // Hide dropdown
  function hideDropdown() {
    timezoneDropdown.classList.remove('show');
    selectedIndex = -1;
  }
  
  // Select a timezone
  function selectTimezone(timezone) {
    timezoneSearch.value = timezone.name;
    hideDropdown();
    
    // Update the ZONES array
    ZONES[currentSelectedClockIndex] = {
      city: timezone.name,
      zone: timezone.zone
    };
    
    // Save to localStorage
    saveZones(ZONES);
    
    // Remove old clock card
    const oldCard = cards[currentSelectedClockIndex];
    if (oldCard.cleanup) oldCard.cleanup();
    grid.removeChild(oldCard);
    
    // Create and insert new clock card
    const newCard = createClockCard(ZONES[currentSelectedClockIndex], currentSelectedClockIndex);
    cards[currentSelectedClockIndex] = newCard;
    
    // Insert at correct position
    const nextSibling = grid.children[currentSelectedClockIndex];
    if (nextSibling) {
      grid.insertBefore(newCard, nextSibling);
    } else {
      grid.appendChild(newCard);
    }
  }
  
  // Handle keyboard navigation
  function handleKeyNavigation(e) {
    if (!timezoneDropdown.classList.contains('show')) return;
    
    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        selectedIndex = Math.min(selectedIndex + 1, filteredTimezones.length - 1);
        renderDropdown();
        break;
      case 'ArrowUp':
        e.preventDefault();
        selectedIndex = Math.max(selectedIndex - 1, -1);
        renderDropdown();
        break;
      case 'Enter':
        e.preventDefault();
        if (selectedIndex >= 0 && filteredTimezones[selectedIndex]) {
          selectTimezone(filteredTimezones[selectedIndex]);
        }
        break;
      case 'Escape':
        hideDropdown();
        timezoneSearch.blur();
        break;
    }
  }
  
  // Event listeners
  clockSelector.addEventListener('change', updateSearchInput);
  
  timezoneSearch.addEventListener('input', (e) => {
    filterTimezones(e.target.value);
    showDropdown();
  });
  
  timezoneSearch.addEventListener('focus', () => {
    filterTimezones(timezoneSearch.value);
    showDropdown();
  });
  
  timezoneSearch.addEventListener('keydown', handleKeyNavigation);
  
  // Hide dropdown when clicking outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.search-container')) {
      hideDropdown();
    }
  });
  
  // Initialize with first clock selected
  updateSearchInput();
}

// Initialize the application
async function initializeApp() {
  // Load timezones first
  await loadTimezones();
  
  // Initialize controls after timezones are loaded
  initializeTimezoneControls();
}

// Start the application
initializeApp();

// Cleanup on unload
window.addEventListener("beforeunload", () => cards.forEach(c => c.cleanup?.()));
