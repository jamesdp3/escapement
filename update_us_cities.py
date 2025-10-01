import json

# Load current timezones.json
with open('timezones.json', 'r', encoding='utf-8') as f:
    current_cities = json.load(f)

# Top 20 biggest US cities by population (2023 data)
top_20_us_cities = [
    {"name": "New York", "timezone": "America/New_York", "country": "United States"},
    {"name": "Los Angeles", "timezone": "America/Los_Angeles", "country": "United States"},
    {"name": "Chicago", "timezone": "America/Chicago", "country": "United States"},
    {"name": "Houston", "timezone": "America/Chicago", "country": "United States"},
    {"name": "Phoenix", "timezone": "America/Phoenix", "country": "United States"},
    {"name": "Philadelphia", "timezone": "America/New_York", "country": "United States"},
    {"name": "San Antonio", "timezone": "America/Chicago", "country": "United States"},
    {"name": "San Diego", "timezone": "America/Los_Angeles", "country": "United States"},
    {"name": "Dallas", "timezone": "America/Chicago", "country": "United States"},
    {"name": "San Jose", "timezone": "America/Los_Angeles", "country": "United States"},
    {"name": "Austin", "timezone": "America/Chicago", "country": "United States"},
    {"name": "Jacksonville", "timezone": "America/New_York", "country": "United States"},
    {"name": "Fort Worth", "timezone": "America/Chicago", "country": "United States"},
    {"name": "Columbus", "timezone": "America/New_York", "country": "United States"},
    {"name": "Charlotte", "timezone": "America/New_York", "country": "United States"},
    {"name": "San Francisco", "timezone": "America/Los_Angeles", "country": "United States"},
    {"name": "Indianapolis", "timezone": "America/Indiana/Indianapolis", "country": "United States"},
    {"name": "Seattle", "timezone": "America/Los_Angeles", "country": "United States"},
    {"name": "Denver", "timezone": "America/Denver", "country": "United States"},
    {"name": "Washington", "timezone": "America/New_York", "country": "United States"}
]

# Remove existing US cities from the current list
non_us_cities = [city for city in current_cities if city.get("country") != "United States"]

# Combine non-US cities with the top 20 US cities
updated_cities = non_us_cities + top_20_us_cities

# Sort by country then by name for better organization
updated_cities.sort(key=lambda x: (x["country"], x["name"]))

# Write updated list back to timezones.json
with open('timezones.json', 'w', encoding='utf-8') as f:
    json.dump(updated_cities, f, indent=2, ensure_ascii=False)

print(f"Updated timezones.json with top 20 US cities!")
print(f"Total cities: {len(updated_cities)}")
print(f"US cities: {len([city for city in updated_cities if city.get('country') == 'United States'])}")
print(f"Other countries: {len(set(city['country'] for city in updated_cities if city.get('country') != 'United States'))}")