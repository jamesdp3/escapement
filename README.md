# Six Black & White World Clocks - Firefox Extension

A beautiful new tab page extension featuring six customizable analog world clocks in elegant black and white design.

## Features
- Six analog world clocks with customizable cities
- Global database of 435+ cities from 83+ countries
- Clean, minimalist black and white design
- Replaces your new tab page with the clock interface

## Installation Instructions

### Method 1: Temporary Installation (Development/Testing)
1. Open Firefox
2. Type `about:debugging` in the address bar and press Enter
3. Click "This Firefox" in the left sidebar
4. Click "Load Temporary Add-on..."
5. Navigate to the extension folder and select the `manifest.json` file
6. The extension will be loaded temporarily (until Firefox is restarted)

### Method 2: Permanent Installation (Signed Extension)
*Note: For permanent installation, the extension needs to be signed by Mozilla or installed as a developer edition.*

1. **For Firefox Developer Edition or Nightly:**
   - Set `xpinstall.signatures.required` to `false` in `about:config`
   - Follow Method 1 steps above

2. **For Release Firefox:**
   - The extension needs to be submitted to Mozilla Add-ons store for signing
   - Or use Firefox Developer Edition for testing

## File Structure
```
Escapement/
├── manifest.json          # Extension manifest
├── newtab.html           # Main new tab page
├── style.css             # Styling for the clocks
├── script.js             # Clock functionality
├── timezones.json        # City and timezone database
└── README_Firefox_Installation.md
```

## Customization
- Open the new tab page after installation
- Click on any city name to change it to a different city
- Choose from 435+ cities worldwide including the top 20 US cities

## Troubleshooting
- If clocks don't appear, check the browser console (F12) for errors
- Ensure all files are in the same directory as manifest.json
- For permission issues, try reloading the extension in about:debugging

## Technical Details
- **Manifest Version: 3** (Modern Firefox standard)
- **Minimum Firefox Version: 109.0** (First version with full Manifest V3 support)
- No special permissions required
- Pure HTML/CSS/JavaScript implementation
- Compatible with both Chrome and Firefox browsers