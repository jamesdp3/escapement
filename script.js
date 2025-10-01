// Available timezones - loaded from external file
let AVAILABLE_TIMEZONES = [];
let showSeconds = true; // Default to showing seconds

// Load seconds preference from localStorage
function loadSecondsPreference() {
  const saved = localStorage.getItem('showSeconds');
  return saved !== null ? JSON.parse(saved) : true;
}

// Save seconds preference to localStorage
function saveSecondsPreference(show) {
  localStorage.setItem('showSeconds', JSON.stringify(show));
}

// Load timezones from external JSON file
async function loadTimezones() {
  console.log('Starting to load timezones...');
  try {
    const response = await fetch('./timezones.json');
    console.log('Fetch response:', response.status, response.ok);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    console.log('JSON data loaded, length:', data.length);
    
    // Map the JSON structure to match expected format
    AVAILABLE_TIMEZONES = data.map(city => ({
      name: city.name,
      zone: city.timezone,
      country: city.country,
      population: city.population
    }));
    
    console.log('AVAILABLE_TIMEZONES populated with', AVAILABLE_TIMEZONES.length, 'items');
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
    console.log('Using fallback timezones:', AVAILABLE_TIMEZONES.length, 'items');
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

  card.append(dial, label, digitalTime);

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

  let digitalFmtNoSeconds = new Intl.DateTimeFormat("en-GB", {
    timeZone: zone,
    hour: "2-digit",
    minute: "2-digit",
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
    
    // Show/hide second hand based on global setting
    if (showSeconds) {
      second.style.transform = `translate(-50%, -100%) rotate(${sAngle}deg)`;
      second.style.display = 'block';
      digitalTime.textContent = digitalFmt.format(new Date());
    } else {
      second.style.display = 'none';
      digitalTime.textContent = digitalFmtNoSeconds.format(new Date());
    }
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
  
  // Ensure AVAILABLE_TIMEZONES is properly initialized
  if (!Array.isArray(AVAILABLE_TIMEZONES) || AVAILABLE_TIMEZONES.length === 0) {
    console.error('AVAILABLE_TIMEZONES is not properly initialized:', AVAILABLE_TIMEZONES);
    return;
  }
  
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
  // Load seconds preference
  showSeconds = loadSecondsPreference();
  
  // Set checkbox state
  const showSecondsCheckbox = document.getElementById('showSeconds');
  showSecondsCheckbox.checked = showSeconds;
  
  // Add event listener for seconds toggle
  showSecondsCheckbox.addEventListener('change', (e) => {
    showSeconds = e.target.checked;
    saveSecondsPreference(showSeconds);
    
    // Update all existing clocks
    cards.forEach(card => {
      const secondHand = card.querySelector('.hand.second');
      const digitalTime = card.querySelector('.digital-time');
      
      if (showSeconds) {
        secondHand.style.display = 'block';
      } else {
        secondHand.style.display = 'none';
      }
    });
  });
  
  // Load timezones first
  await loadTimezones();
  
  // Initialize controls after timezones are loaded
  initializeTimezoneControls();
}

// Start the application
initializeApp();

// Cleanup on unload
window.addEventListener("beforeunload", () => cards.forEach(c => c.cleanup?.()));
