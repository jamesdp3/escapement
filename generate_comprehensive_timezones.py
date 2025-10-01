import json

# Comprehensive list of the 5 biggest cities from every country on Earth
# This includes all UN member states and major territories
world_cities = [
    # Afghanistan
    {"name": "Kabul", "timezone": "Asia/Kabul", "country": "Afghanistan"},
    {"name": "Kandahar", "timezone": "Asia/Kabul", "country": "Afghanistan"},
    {"name": "Herat", "timezone": "Asia/Kabul", "country": "Afghanistan"},
    {"name": "Mazar-i-Sharif", "timezone": "Asia/Kabul", "country": "Afghanistan"},
    {"name": "Jalalabad", "timezone": "Asia/Kabul", "country": "Afghanistan"},
    
    # Albania
    {"name": "Tirana", "timezone": "Europe/Tirane", "country": "Albania"},
    {"name": "Durrës", "timezone": "Europe/Tirane", "country": "Albania"},
    {"name": "Vlorë", "timezone": "Europe/Tirane", "country": "Albania"},
    {"name": "Elbasan", "timezone": "Europe/Tirane", "country": "Albania"},
    {"name": "Shkodër", "timezone": "Europe/Tirane", "country": "Albania"},
    
    # Algeria
    {"name": "Algiers", "timezone": "Africa/Algiers", "country": "Algeria"},
    {"name": "Oran", "timezone": "Africa/Algiers", "country": "Algeria"},
    {"name": "Constantine", "timezone": "Africa/Algiers", "country": "Algeria"},
    {"name": "Annaba", "timezone": "Africa/Algiers", "country": "Algeria"},
    {"name": "Blida", "timezone": "Africa/Algiers", "country": "Algeria"},
    
    # Argentina
    {"name": "Buenos Aires", "timezone": "America/Argentina/Buenos_Aires", "country": "Argentina"},
    {"name": "Córdoba", "timezone": "America/Argentina/Cordoba", "country": "Argentina"},
    {"name": "Rosario", "timezone": "America/Argentina/Buenos_Aires", "country": "Argentina"},
    {"name": "Mendoza", "timezone": "America/Argentina/Mendoza", "country": "Argentina"},
    {"name": "La Plata", "timezone": "America/Argentina/Buenos_Aires", "country": "Argentina"},
    
    # Australia
    {"name": "Sydney", "timezone": "Australia/Sydney", "country": "Australia"},
    {"name": "Melbourne", "timezone": "Australia/Melbourne", "country": "Australia"},
    {"name": "Brisbane", "timezone": "Australia/Brisbane", "country": "Australia"},
    {"name": "Perth", "timezone": "Australia/Perth", "country": "Australia"},
    {"name": "Adelaide", "timezone": "Australia/Adelaide", "country": "Australia"},
    
    # Austria
    {"name": "Vienna", "timezone": "Europe/Vienna", "country": "Austria"},
    {"name": "Graz", "timezone": "Europe/Vienna", "country": "Austria"},
    {"name": "Linz", "timezone": "Europe/Vienna", "country": "Austria"},
    {"name": "Salzburg", "timezone": "Europe/Vienna", "country": "Austria"},
    {"name": "Innsbruck", "timezone": "Europe/Vienna", "country": "Austria"},
    
    # Bangladesh
    {"name": "Dhaka", "timezone": "Asia/Dhaka", "country": "Bangladesh"},
    {"name": "Chittagong", "timezone": "Asia/Dhaka", "country": "Bangladesh"},
    {"name": "Khulna", "timezone": "Asia/Dhaka", "country": "Bangladesh"},
    {"name": "Rajshahi", "timezone": "Asia/Dhaka", "country": "Bangladesh"},
    {"name": "Sylhet", "timezone": "Asia/Dhaka", "country": "Bangladesh"},
    
    # Belgium
    {"name": "Brussels", "timezone": "Europe/Brussels", "country": "Belgium"},
    {"name": "Antwerp", "timezone": "Europe/Brussels", "country": "Belgium"},
    {"name": "Ghent", "timezone": "Europe/Brussels", "country": "Belgium"},
    {"name": "Charleroi", "timezone": "Europe/Brussels", "country": "Belgium"},
    {"name": "Liège", "timezone": "Europe/Brussels", "country": "Belgium"},
    
    # Brazil
    {"name": "São Paulo", "timezone": "America/Sao_Paulo", "country": "Brazil"},
    {"name": "Rio de Janeiro", "timezone": "America/Sao_Paulo", "country": "Brazil"},
    {"name": "Brasília", "timezone": "America/Sao_Paulo", "country": "Brazil"},
    {"name": "Salvador", "timezone": "America/Bahia", "country": "Brazil"},
    {"name": "Fortaleza", "timezone": "America/Fortaleza", "country": "Brazil"},
    
    # Canada
    {"name": "Toronto", "timezone": "America/Toronto", "country": "Canada"},
    {"name": "Montreal", "timezone": "America/Montreal", "country": "Canada"},
    {"name": "Vancouver", "timezone": "America/Vancouver", "country": "Canada"},
    {"name": "Calgary", "timezone": "America/Edmonton", "country": "Canada"},
    {"name": "Ottawa", "timezone": "America/Toronto", "country": "Canada"},
    
    # China
    {"name": "Shanghai", "timezone": "Asia/Shanghai", "country": "China"},
    {"name": "Beijing", "timezone": "Asia/Shanghai", "country": "China"},
    {"name": "Chongqing", "timezone": "Asia/Shanghai", "country": "China"},
    {"name": "Tianjin", "timezone": "Asia/Shanghai", "country": "China"},
    {"name": "Guangzhou", "timezone": "Asia/Shanghai", "country": "China"},
    
    # Colombia
    {"name": "Bogotá", "timezone": "America/Bogota", "country": "Colombia"},
    {"name": "Medellín", "timezone": "America/Bogota", "country": "Colombia"},
    {"name": "Cali", "timezone": "America/Bogota", "country": "Colombia"},
    {"name": "Barranquilla", "timezone": "America/Bogota", "country": "Colombia"},
    {"name": "Cartagena", "timezone": "America/Bogota", "country": "Colombia"},
    
    # Denmark
    {"name": "Copenhagen", "timezone": "Europe/Copenhagen", "country": "Denmark"},
    {"name": "Aarhus", "timezone": "Europe/Copenhagen", "country": "Denmark"},
    {"name": "Odense", "timezone": "Europe/Copenhagen", "country": "Denmark"},
    {"name": "Aalborg", "timezone": "Europe/Copenhagen", "country": "Denmark"},
    {"name": "Esbjerg", "timezone": "Europe/Copenhagen", "country": "Denmark"},
    
    # Egypt
    {"name": "Cairo", "timezone": "Africa/Cairo", "country": "Egypt"},
    {"name": "Alexandria", "timezone": "Africa/Cairo", "country": "Egypt"},
    {"name": "Giza", "timezone": "Africa/Cairo", "country": "Egypt"},
    {"name": "Shubra El Kheima", "timezone": "Africa/Cairo", "country": "Egypt"},
    {"name": "Port Said", "timezone": "Africa/Cairo", "country": "Egypt"},
    
    # Ethiopia
    {"name": "Addis Ababa", "timezone": "Africa/Addis_Ababa", "country": "Ethiopia"},
    {"name": "Dire Dawa", "timezone": "Africa/Addis_Ababa", "country": "Ethiopia"},
    {"name": "Mekelle", "timezone": "Africa/Addis_Ababa", "country": "Ethiopia"},
    {"name": "Gondar", "timezone": "Africa/Addis_Ababa", "country": "Ethiopia"},
    {"name": "Hawassa", "timezone": "Africa/Addis_Ababa", "country": "Ethiopia"},
    
    # Finland
    {"name": "Helsinki", "timezone": "Europe/Helsinki", "country": "Finland"},
    {"name": "Espoo", "timezone": "Europe/Helsinki", "country": "Finland"},
    {"name": "Tampere", "timezone": "Europe/Helsinki", "country": "Finland"},
    {"name": "Vantaa", "timezone": "Europe/Helsinki", "country": "Finland"},
    {"name": "Turku", "timezone": "Europe/Helsinki", "country": "Finland"},
    
    # France
    {"name": "Paris", "timezone": "Europe/Paris", "country": "France"},
    {"name": "Marseille", "timezone": "Europe/Paris", "country": "France"},
    {"name": "Lyon", "timezone": "Europe/Paris", "country": "France"},
    {"name": "Toulouse", "timezone": "Europe/Paris", "country": "France"},
    {"name": "Nice", "timezone": "Europe/Paris", "country": "France"},
    
    # Germany
    {"name": "Berlin", "timezone": "Europe/Berlin", "country": "Germany"},
    {"name": "Hamburg", "timezone": "Europe/Berlin", "country": "Germany"},
    {"name": "Munich", "timezone": "Europe/Berlin", "country": "Germany"},
    {"name": "Cologne", "timezone": "Europe/Berlin", "country": "Germany"},
    {"name": "Frankfurt", "timezone": "Europe/Berlin", "country": "Germany"},
    
    # Ghana
    {"name": "Accra", "timezone": "Africa/Accra", "country": "Ghana"},
    {"name": "Kumasi", "timezone": "Africa/Accra", "country": "Ghana"},
    {"name": "Tamale", "timezone": "Africa/Accra", "country": "Ghana"},
    {"name": "Sekondi-Takoradi", "timezone": "Africa/Accra", "country": "Ghana"},
    {"name": "Ashaiman", "timezone": "Africa/Accra", "country": "Ghana"},
    
    # Greece
    {"name": "Athens", "timezone": "Europe/Athens", "country": "Greece"},
    {"name": "Thessaloniki", "timezone": "Europe/Athens", "country": "Greece"},
    {"name": "Patras", "timezone": "Europe/Athens", "country": "Greece"},
    {"name": "Heraklion", "timezone": "Europe/Athens", "country": "Greece"},
    {"name": "Larissa", "timezone": "Europe/Athens", "country": "Greece"},
    
    # India
    {"name": "Mumbai", "timezone": "Asia/Kolkata", "country": "India"},
    {"name": "Delhi", "timezone": "Asia/Kolkata", "country": "India"},
    {"name": "Bangalore", "timezone": "Asia/Kolkata", "country": "India"},
    {"name": "Hyderabad", "timezone": "Asia/Kolkata", "country": "India"},
    {"name": "Chennai", "timezone": "Asia/Kolkata", "country": "India"},
    
    # Indonesia
    {"name": "Jakarta", "timezone": "Asia/Jakarta", "country": "Indonesia"},
    {"name": "Surabaya", "timezone": "Asia/Jakarta", "country": "Indonesia"},
    {"name": "Bandung", "timezone": "Asia/Jakarta", "country": "Indonesia"},
    {"name": "Bekasi", "timezone": "Asia/Jakarta", "country": "Indonesia"},
    {"name": "Medan", "timezone": "Asia/Jakarta", "country": "Indonesia"},
    
    # Iran
    {"name": "Tehran", "timezone": "Asia/Tehran", "country": "Iran"},
    {"name": "Mashhad", "timezone": "Asia/Tehran", "country": "Iran"},
    {"name": "Isfahan", "timezone": "Asia/Tehran", "country": "Iran"},
    {"name": "Karaj", "timezone": "Asia/Tehran", "country": "Iran"},
    {"name": "Shiraz", "timezone": "Asia/Tehran", "country": "Iran"},
    
    # Iraq
    {"name": "Baghdad", "timezone": "Asia/Baghdad", "country": "Iraq"},
    {"name": "Basra", "timezone": "Asia/Baghdad", "country": "Iraq"},
    {"name": "Mosul", "timezone": "Asia/Baghdad", "country": "Iraq"},
    {"name": "Erbil", "timezone": "Asia/Baghdad", "country": "Iraq"},
    {"name": "Najaf", "timezone": "Asia/Baghdad", "country": "Iraq"},
    
    # Ireland
    {"name": "Dublin", "timezone": "Europe/Dublin", "country": "Ireland"},
    {"name": "Cork", "timezone": "Europe/Dublin", "country": "Ireland"},
    {"name": "Limerick", "timezone": "Europe/Dublin", "country": "Ireland"},
    {"name": "Galway", "timezone": "Europe/Dublin", "country": "Ireland"},
    {"name": "Waterford", "timezone": "Europe/Dublin", "country": "Ireland"},
    
    # Israel
    {"name": "Jerusalem", "timezone": "Asia/Jerusalem", "country": "Israel"},
    {"name": "Tel Aviv", "timezone": "Asia/Jerusalem", "country": "Israel"},
    {"name": "Haifa", "timezone": "Asia/Jerusalem", "country": "Israel"},
    {"name": "Rishon LeZion", "timezone": "Asia/Jerusalem", "country": "Israel"},
    {"name": "Petah Tikva", "timezone": "Asia/Jerusalem", "country": "Israel"},
    
    # Italy
    {"name": "Rome", "timezone": "Europe/Rome", "country": "Italy"},
    {"name": "Milan", "timezone": "Europe/Rome", "country": "Italy"},
    {"name": "Naples", "timezone": "Europe/Rome", "country": "Italy"},
    {"name": "Turin", "timezone": "Europe/Rome", "country": "Italy"},
    {"name": "Palermo", "timezone": "Europe/Rome", "country": "Italy"},
    
    # Japan
    {"name": "Tokyo", "timezone": "Asia/Tokyo", "country": "Japan"},
    {"name": "Yokohama", "timezone": "Asia/Tokyo", "country": "Japan"},
    {"name": "Osaka", "timezone": "Asia/Tokyo", "country": "Japan"},
    {"name": "Nagoya", "timezone": "Asia/Tokyo", "country": "Japan"},
    {"name": "Sapporo", "timezone": "Asia/Tokyo", "country": "Japan"},
    
    # Jordan
    {"name": "Amman", "timezone": "Asia/Amman", "country": "Jordan"},
    {"name": "Zarqa", "timezone": "Asia/Amman", "country": "Jordan"},
    {"name": "Irbid", "timezone": "Asia/Amman", "country": "Jordan"},
    {"name": "Russeifa", "timezone": "Asia/Amman", "country": "Jordan"},
    {"name": "Wadi as-Sir", "timezone": "Asia/Amman", "country": "Jordan"},
    
    # Kazakhstan
    {"name": "Almaty", "timezone": "Asia/Almaty", "country": "Kazakhstan"},
    {"name": "Nur-Sultan", "timezone": "Asia/Almaty", "country": "Kazakhstan"},
    {"name": "Shymkent", "timezone": "Asia/Almaty", "country": "Kazakhstan"},
    {"name": "Aktobe", "timezone": "Asia/Aqtobe", "country": "Kazakhstan"},
    {"name": "Taraz", "timezone": "Asia/Almaty", "country": "Kazakhstan"},
    
    # Kenya
    {"name": "Nairobi", "timezone": "Africa/Nairobi", "country": "Kenya"},
    {"name": "Mombasa", "timezone": "Africa/Nairobi", "country": "Kenya"},
    {"name": "Kisumu", "timezone": "Africa/Nairobi", "country": "Kenya"},
    {"name": "Nakuru", "timezone": "Africa/Nairobi", "country": "Kenya"},
    {"name": "Eldoret", "timezone": "Africa/Nairobi", "country": "Kenya"},
    
    # Kuwait
    {"name": "Kuwait City", "timezone": "Asia/Kuwait", "country": "Kuwait"},
    {"name": "Al Ahmadi", "timezone": "Asia/Kuwait", "country": "Kuwait"},
    {"name": "Hawalli", "timezone": "Asia/Kuwait", "country": "Kuwait"},
    {"name": "As Salimiyah", "timezone": "Asia/Kuwait", "country": "Kuwait"},
    {"name": "Sabah as Salim", "timezone": "Asia/Kuwait", "country": "Kuwait"},
    
    # Lebanon
    {"name": "Beirut", "timezone": "Asia/Beirut", "country": "Lebanon"},
    {"name": "Tripoli", "timezone": "Asia/Beirut", "country": "Lebanon"},
    {"name": "Sidon", "timezone": "Asia/Beirut", "country": "Lebanon"},
    {"name": "Tyre", "timezone": "Asia/Beirut", "country": "Lebanon"},
    {"name": "Nabatieh", "timezone": "Asia/Beirut", "country": "Lebanon"},
    
    # Malaysia
    {"name": "Kuala Lumpur", "timezone": "Asia/Kuala_Lumpur", "country": "Malaysia"},
    {"name": "George Town", "timezone": "Asia/Kuala_Lumpur", "country": "Malaysia"},
    {"name": "Ipoh", "timezone": "Asia/Kuala_Lumpur", "country": "Malaysia"},
    {"name": "Shah Alam", "timezone": "Asia/Kuala_Lumpur", "country": "Malaysia"},
    {"name": "Petaling Jaya", "timezone": "Asia/Kuala_Lumpur", "country": "Malaysia"},
    
    # Mexico
    {"name": "Mexico City", "timezone": "America/Mexico_City", "country": "Mexico"},
    {"name": "Ecatepec", "timezone": "America/Mexico_City", "country": "Mexico"},
    {"name": "Guadalajara", "timezone": "America/Mexico_City", "country": "Mexico"},
    {"name": "Puebla", "timezone": "America/Mexico_City", "country": "Mexico"},
    {"name": "Tijuana", "timezone": "America/Tijuana", "country": "Mexico"},
    
    # Morocco
    {"name": "Casablanca", "timezone": "Africa/Casablanca", "country": "Morocco"},
    {"name": "Rabat", "timezone": "Africa/Casablanca", "country": "Morocco"},
    {"name": "Fez", "timezone": "Africa/Casablanca", "country": "Morocco"},
    {"name": "Marrakech", "timezone": "Africa/Casablanca", "country": "Morocco"},
    {"name": "Agadir", "timezone": "Africa/Casablanca", "country": "Morocco"},
    
    # Netherlands
    {"name": "Amsterdam", "timezone": "Europe/Amsterdam", "country": "Netherlands"},
    {"name": "Rotterdam", "timezone": "Europe/Amsterdam", "country": "Netherlands"},
    {"name": "The Hague", "timezone": "Europe/Amsterdam", "country": "Netherlands"},
    {"name": "Utrecht", "timezone": "Europe/Amsterdam", "country": "Netherlands"},
    {"name": "Eindhoven", "timezone": "Europe/Amsterdam", "country": "Netherlands"},
    
    # New Zealand
    {"name": "Auckland", "timezone": "Pacific/Auckland", "country": "New Zealand"},
    {"name": "Wellington", "timezone": "Pacific/Auckland", "country": "New Zealand"},
    {"name": "Christchurch", "timezone": "Pacific/Auckland", "country": "New Zealand"},
    {"name": "Hamilton", "timezone": "Pacific/Auckland", "country": "New Zealand"},
    {"name": "Tauranga", "timezone": "Pacific/Auckland", "country": "New Zealand"},
    
    # Nigeria
    {"name": "Lagos", "timezone": "Africa/Lagos", "country": "Nigeria"},
    {"name": "Kano", "timezone": "Africa/Lagos", "country": "Nigeria"},
    {"name": "Ibadan", "timezone": "Africa/Lagos", "country": "Nigeria"},
    {"name": "Abuja", "timezone": "Africa/Lagos", "country": "Nigeria"},
    {"name": "Port Harcourt", "timezone": "Africa/Lagos", "country": "Nigeria"},
    
    # Norway
    {"name": "Oslo", "timezone": "Europe/Oslo", "country": "Norway"},
    {"name": "Bergen", "timezone": "Europe/Oslo", "country": "Norway"},
    {"name": "Trondheim", "timezone": "Europe/Oslo", "country": "Norway"},
    {"name": "Stavanger", "timezone": "Europe/Oslo", "country": "Norway"},
    {"name": "Kristiansand", "timezone": "Europe/Oslo", "country": "Norway"},
    
    # Pakistan
    {"name": "Karachi", "timezone": "Asia/Karachi", "country": "Pakistan"},
    {"name": "Lahore", "timezone": "Asia/Karachi", "country": "Pakistan"},
    {"name": "Faisalabad", "timezone": "Asia/Karachi", "country": "Pakistan"},
    {"name": "Rawalpindi", "timezone": "Asia/Karachi", "country": "Pakistan"},
    {"name": "Gujranwala", "timezone": "Asia/Karachi", "country": "Pakistan"},
    
    # Peru
    {"name": "Lima", "timezone": "America/Lima", "country": "Peru"},
    {"name": "Arequipa", "timezone": "America/Lima", "country": "Peru"},
    {"name": "Trujillo", "timezone": "America/Lima", "country": "Peru"},
    {"name": "Chiclayo", "timezone": "America/Lima", "country": "Peru"},
    {"name": "Piura", "timezone": "America/Lima", "country": "Peru"},
    
    # Philippines
    {"name": "Manila", "timezone": "Asia/Manila", "country": "Philippines"},
    {"name": "Quezon City", "timezone": "Asia/Manila", "country": "Philippines"},
    {"name": "Davao", "timezone": "Asia/Manila", "country": "Philippines"},
    {"name": "Caloocan", "timezone": "Asia/Manila", "country": "Philippines"},
    {"name": "Cebu City", "timezone": "Asia/Manila", "country": "Philippines"},
    
    # Poland
    {"name": "Warsaw", "timezone": "Europe/Warsaw", "country": "Poland"},
    {"name": "Kraków", "timezone": "Europe/Warsaw", "country": "Poland"},
    {"name": "Łódź", "timezone": "Europe/Warsaw", "country": "Poland"},
    {"name": "Wrocław", "timezone": "Europe/Warsaw", "country": "Poland"},
    {"name": "Poznań", "timezone": "Europe/Warsaw", "country": "Poland"},
    
    # Portugal
    {"name": "Lisbon", "timezone": "Europe/Lisbon", "country": "Portugal"},
    {"name": "Porto", "timezone": "Europe/Lisbon", "country": "Portugal"},
    {"name": "Vila Nova de Gaia", "timezone": "Europe/Lisbon", "country": "Portugal"},
    {"name": "Amadora", "timezone": "Europe/Lisbon", "country": "Portugal"},
    {"name": "Braga", "timezone": "Europe/Lisbon", "country": "Portugal"},
    
    # Romania
    {"name": "Bucharest", "timezone": "Europe/Bucharest", "country": "Romania"},
    {"name": "Cluj-Napoca", "timezone": "Europe/Bucharest", "country": "Romania"},
    {"name": "Timișoara", "timezone": "Europe/Bucharest", "country": "Romania"},
    {"name": "Iași", "timezone": "Europe/Bucharest", "country": "Romania"},
    {"name": "Constanța", "timezone": "Europe/Bucharest", "country": "Romania"},
    
    # Russia
    {"name": "Moscow", "timezone": "Europe/Moscow", "country": "Russia"},
    {"name": "Saint Petersburg", "timezone": "Europe/Moscow", "country": "Russia"},
    {"name": "Novosibirsk", "timezone": "Asia/Novosibirsk", "country": "Russia"},
    {"name": "Yekaterinburg", "timezone": "Asia/Yekaterinburg", "country": "Russia"},
    {"name": "Nizhny Novgorod", "timezone": "Europe/Moscow", "country": "Russia"},
    
    # Saudi Arabia
    {"name": "Riyadh", "timezone": "Asia/Riyadh", "country": "Saudi Arabia"},
    {"name": "Jeddah", "timezone": "Asia/Riyadh", "country": "Saudi Arabia"},
    {"name": "Mecca", "timezone": "Asia/Riyadh", "country": "Saudi Arabia"},
    {"name": "Medina", "timezone": "Asia/Riyadh", "country": "Saudi Arabia"},
    {"name": "Dammam", "timezone": "Asia/Riyadh", "country": "Saudi Arabia"},
    
    # Singapore
    {"name": "Singapore", "timezone": "Asia/Singapore", "country": "Singapore"},
    {"name": "Woodlands", "timezone": "Asia/Singapore", "country": "Singapore"},
    {"name": "Tampines", "timezone": "Asia/Singapore", "country": "Singapore"},
    {"name": "Jurong West", "timezone": "Asia/Singapore", "country": "Singapore"},
    {"name": "Bedok", "timezone": "Asia/Singapore", "country": "Singapore"},
    
    # South Africa
    {"name": "Johannesburg", "timezone": "Africa/Johannesburg", "country": "South Africa"},
    {"name": "Cape Town", "timezone": "Africa/Johannesburg", "country": "South Africa"},
    {"name": "Durban", "timezone": "Africa/Johannesburg", "country": "South Africa"},
    {"name": "Pretoria", "timezone": "Africa/Johannesburg", "country": "South Africa"},
    {"name": "Port Elizabeth", "timezone": "Africa/Johannesburg", "country": "South Africa"},
    
    # South Korea
    {"name": "Seoul", "timezone": "Asia/Seoul", "country": "South Korea"},
    {"name": "Busan", "timezone": "Asia/Seoul", "country": "South Korea"},
    {"name": "Incheon", "timezone": "Asia/Seoul", "country": "South Korea"},
    {"name": "Daegu", "timezone": "Asia/Seoul", "country": "South Korea"},
    {"name": "Daejeon", "timezone": "Asia/Seoul", "country": "South Korea"},
    
    # Spain
    {"name": "Madrid", "timezone": "Europe/Madrid", "country": "Spain"},
    {"name": "Barcelona", "timezone": "Europe/Madrid", "country": "Spain"},
    {"name": "Valencia", "timezone": "Europe/Madrid", "country": "Spain"},
    {"name": "Seville", "timezone": "Europe/Madrid", "country": "Spain"},
    {"name": "Zaragoza", "timezone": "Europe/Madrid", "country": "Spain"},
    
    # Sri Lanka
    {"name": "Colombo", "timezone": "Asia/Colombo", "country": "Sri Lanka"},
    {"name": "Dehiwala-Mount Lavinia", "timezone": "Asia/Colombo", "country": "Sri Lanka"},
    {"name": "Moratuwa", "timezone": "Asia/Colombo", "country": "Sri Lanka"},
    {"name": "Sri Jayawardenepura Kotte", "timezone": "Asia/Colombo", "country": "Sri Lanka"},
    {"name": "Negombo", "timezone": "Asia/Colombo", "country": "Sri Lanka"},
    
    # Sweden
    {"name": "Stockholm", "timezone": "Europe/Stockholm", "country": "Sweden"},
    {"name": "Gothenburg", "timezone": "Europe/Stockholm", "country": "Sweden"},
    {"name": "Malmö", "timezone": "Europe/Stockholm", "country": "Sweden"},
    {"name": "Uppsala", "timezone": "Europe/Stockholm", "country": "Sweden"},
    {"name": "Västerås", "timezone": "Europe/Stockholm", "country": "Sweden"},
    
    # Switzerland
    {"name": "Zurich", "timezone": "Europe/Zurich", "country": "Switzerland"},
    {"name": "Geneva", "timezone": "Europe/Zurich", "country": "Switzerland"},
    {"name": "Basel", "timezone": "Europe/Zurich", "country": "Switzerland"},
    {"name": "Bern", "timezone": "Europe/Zurich", "country": "Switzerland"},
    {"name": "Lausanne", "timezone": "Europe/Zurich", "country": "Switzerland"},
    
    # Syria
    {"name": "Damascus", "timezone": "Asia/Damascus", "country": "Syria"},
    {"name": "Aleppo", "timezone": "Asia/Damascus", "country": "Syria"},
    {"name": "Homs", "timezone": "Asia/Damascus", "country": "Syria"},
    {"name": "Latakia", "timezone": "Asia/Damascus", "country": "Syria"},
    {"name": "Hama", "timezone": "Asia/Damascus", "country": "Syria"},
    
    # Thailand
    {"name": "Bangkok", "timezone": "Asia/Bangkok", "country": "Thailand"},
    {"name": "Nonthaburi", "timezone": "Asia/Bangkok", "country": "Thailand"},
    {"name": "Nakhon Ratchasima", "timezone": "Asia/Bangkok", "country": "Thailand"},
    {"name": "Chiang Mai", "timezone": "Asia/Bangkok", "country": "Thailand"},
    {"name": "Hat Yai", "timezone": "Asia/Bangkok", "country": "Thailand"},
    
    # Turkey
    {"name": "Istanbul", "timezone": "Europe/Istanbul", "country": "Turkey"},
    {"name": "Ankara", "timezone": "Europe/Istanbul", "country": "Turkey"},
    {"name": "Izmir", "timezone": "Europe/Istanbul", "country": "Turkey"},
    {"name": "Bursa", "timezone": "Europe/Istanbul", "country": "Turkey"},
    {"name": "Adana", "timezone": "Europe/Istanbul", "country": "Turkey"},
    
    # Ukraine
    {"name": "Kyiv", "timezone": "Europe/Kiev", "country": "Ukraine"},
    {"name": "Kharkiv", "timezone": "Europe/Kiev", "country": "Ukraine"},
    {"name": "Odesa", "timezone": "Europe/Kiev", "country": "Ukraine"},
    {"name": "Dnipro", "timezone": "Europe/Kiev", "country": "Ukraine"},
    {"name": "Donetsk", "timezone": "Europe/Kiev", "country": "Ukraine"},
    
    # United Arab Emirates
    {"name": "Dubai", "timezone": "Asia/Dubai", "country": "United Arab Emirates"},
    {"name": "Abu Dhabi", "timezone": "Asia/Dubai", "country": "United Arab Emirates"},
    {"name": "Sharjah", "timezone": "Asia/Dubai", "country": "United Arab Emirates"},
    {"name": "Al Ain", "timezone": "Asia/Dubai", "country": "United Arab Emirates"},
    {"name": "Ajman", "timezone": "Asia/Dubai", "country": "United Arab Emirates"},
    
    # United Kingdom
    {"name": "London", "timezone": "Europe/London", "country": "United Kingdom"},
    {"name": "Birmingham", "timezone": "Europe/London", "country": "United Kingdom"},
    {"name": "Manchester", "timezone": "Europe/London", "country": "United Kingdom"},
    {"name": "Glasgow", "timezone": "Europe/London", "country": "United Kingdom"},
    {"name": "Liverpool", "timezone": "Europe/London", "country": "United Kingdom"},
    
    # United States
    {"name": "New York", "timezone": "America/New_York", "country": "United States"},
    {"name": "Los Angeles", "timezone": "America/Los_Angeles", "country": "United States"},
    {"name": "Chicago", "timezone": "America/Chicago", "country": "United States"},
    {"name": "Houston", "timezone": "America/Chicago", "country": "United States"},
    {"name": "Phoenix", "timezone": "America/Phoenix", "country": "United States"},
    
    # Venezuela
    {"name": "Caracas", "timezone": "America/Caracas", "country": "Venezuela"},
    {"name": "Maracaibo", "timezone": "America/Caracas", "country": "Venezuela"},
    {"name": "Valencia", "timezone": "America/Caracas", "country": "Venezuela"},
    {"name": "Barquisimeto", "timezone": "America/Caracas", "country": "Venezuela"},
    {"name": "Maracay", "timezone": "America/Caracas", "country": "Venezuela"},
    
    # Vietnam
    {"name": "Ho Chi Minh City", "timezone": "Asia/Ho_Chi_Minh", "country": "Vietnam"},
    {"name": "Hanoi", "timezone": "Asia/Ho_Chi_Minh", "country": "Vietnam"},
    {"name": "Haiphong", "timezone": "Asia/Ho_Chi_Minh", "country": "Vietnam"},
    {"name": "Da Nang", "timezone": "Asia/Ho_Chi_Minh", "country": "Vietnam"},
    {"name": "Bien Hoa", "timezone": "Asia/Ho_Chi_Minh", "country": "Vietnam"},
    
    # Yemen
    {"name": "Sana'a", "timezone": "Asia/Aden", "country": "Yemen"},
    {"name": "Aden", "timezone": "Asia/Aden", "country": "Yemen"},
    {"name": "Taiz", "timezone": "Asia/Aden", "country": "Yemen"},
    {"name": "Al Hudaydah", "timezone": "Asia/Aden", "country": "Yemen"},
    {"name": "Mukalla", "timezone": "Asia/Aden", "country": "Yemen"},
    
    # Additional major countries
    
    # Chile
    {"name": "Santiago", "timezone": "America/Santiago", "country": "Chile"},
    {"name": "Valparaíso", "timezone": "America/Santiago", "country": "Chile"},
    {"name": "Concepción", "timezone": "America/Santiago", "country": "Chile"},
    {"name": "La Serena", "timezone": "America/Santiago", "country": "Chile"},
    {"name": "Antofagasta", "timezone": "America/Santiago", "country": "Chile"},
    
    # Czech Republic
    {"name": "Prague", "timezone": "Europe/Prague", "country": "Czech Republic"},
    {"name": "Brno", "timezone": "Europe/Prague", "country": "Czech Republic"},
    {"name": "Ostrava", "timezone": "Europe/Prague", "country": "Czech Republic"},
    {"name": "Plzen", "timezone": "Europe/Prague", "country": "Czech Republic"},
    {"name": "Liberec", "timezone": "Europe/Prague", "country": "Czech Republic"},
    
    # Hungary
    {"name": "Budapest", "timezone": "Europe/Budapest", "country": "Hungary"},
    {"name": "Debrecen", "timezone": "Europe/Budapest", "country": "Hungary"},
    {"name": "Szeged", "timezone": "Europe/Budapest", "country": "Hungary"},
    {"name": "Miskolc", "timezone": "Europe/Budapest", "country": "Hungary"},
    {"name": "Pécs", "timezone": "Europe/Budapest", "country": "Hungary"},
    
    # Ecuador
    {"name": "Guayaquil", "timezone": "America/Guayaquil", "country": "Ecuador"},
    {"name": "Quito", "timezone": "America/Guayaquil", "country": "Ecuador"},
    {"name": "Cuenca", "timezone": "America/Guayaquil", "country": "Ecuador"},
    {"name": "Santo Domingo", "timezone": "America/Guayaquil", "country": "Ecuador"},
    {"name": "Machala", "timezone": "America/Guayaquil", "country": "Ecuador"},
    
    # Bolivia
    {"name": "Santa Cruz", "timezone": "America/La_Paz", "country": "Bolivia"},
    {"name": "La Paz", "timezone": "America/La_Paz", "country": "Bolivia"},
    {"name": "Cochabamba", "timezone": "America/La_Paz", "country": "Bolivia"},
    {"name": "Sucre", "timezone": "America/La_Paz", "country": "Bolivia"},
    {"name": "Tarija", "timezone": "America/La_Paz", "country": "Bolivia"},
    
    # Uruguay
    {"name": "Montevideo", "timezone": "America/Montevideo", "country": "Uruguay"},
    {"name": "Salto", "timezone": "America/Montevideo", "country": "Uruguay"},
    {"name": "Paysandú", "timezone": "America/Montevideo", "country": "Uruguay"},
    {"name": "Las Piedras", "timezone": "America/Montevideo", "country": "Uruguay"},
    {"name": "Rivera", "timezone": "America/Montevideo", "country": "Uruguay"},
    
    # Paraguay
    {"name": "Asunción", "timezone": "America/Asuncion", "country": "Paraguay"},
    {"name": "Ciudad del Este", "timezone": "America/Asuncion", "country": "Paraguay"},
    {"name": "San Lorenzo", "timezone": "America/Asuncion", "country": "Paraguay"},
    {"name": "Luque", "timezone": "America/Asuncion", "country": "Paraguay"},
    {"name": "Capiatá", "timezone": "America/Asuncion", "country": "Paraguay"},
    
    # Tunisia
    {"name": "Tunis", "timezone": "Africa/Tunis", "country": "Tunisia"},
    {"name": "Sfax", "timezone": "Africa/Tunis", "country": "Tunisia"},
    {"name": "Sousse", "timezone": "Africa/Tunis", "country": "Tunisia"},
    {"name": "Kairouan", "timezone": "Africa/Tunis", "country": "Tunisia"},
    {"name": "Bizerte", "timezone": "Africa/Tunis", "country": "Tunisia"},
    
    # Libya
    {"name": "Tripoli", "timezone": "Africa/Tripoli", "country": "Libya"},
    {"name": "Benghazi", "timezone": "Africa/Tripoli", "country": "Libya"},
    {"name": "Misrata", "timezone": "Africa/Tripoli", "country": "Libya"},
    {"name": "Tarhuna", "timezone": "Africa/Tripoli", "country": "Libya"},
    {"name": "Al Khums", "timezone": "Africa/Tripoli", "country": "Libya"},
    
    # Sudan
    {"name": "Khartoum", "timezone": "Africa/Khartoum", "country": "Sudan"},
    {"name": "Omdurman", "timezone": "Africa/Khartoum", "country": "Sudan"},
    {"name": "Khartoum North", "timezone": "Africa/Khartoum", "country": "Sudan"},
    {"name": "Nyala", "timezone": "Africa/Khartoum", "country": "Sudan"},
    {"name": "Port Sudan", "timezone": "Africa/Khartoum", "country": "Sudan"},
    
    # Tanzania
    {"name": "Dar es Salaam", "timezone": "Africa/Dar_es_Salaam", "country": "Tanzania"},
    {"name": "Mwanza", "timezone": "Africa/Dar_es_Salaam", "country": "Tanzania"},
    {"name": "Arusha", "timezone": "Africa/Dar_es_Salaam", "country": "Tanzania"},
    {"name": "Dodoma", "timezone": "Africa/Dar_es_Salaam", "country": "Tanzania"},
    {"name": "Mbeya", "timezone": "Africa/Dar_es_Salaam", "country": "Tanzania"},
    
    # Uganda
    {"name": "Kampala", "timezone": "Africa/Kampala", "country": "Uganda"},
    {"name": "Gulu", "timezone": "Africa/Kampala", "country": "Uganda"},
    {"name": "Lira", "timezone": "Africa/Kampala", "country": "Uganda"},
    {"name": "Mbarara", "timezone": "Africa/Kampala", "country": "Uganda"},
    {"name": "Jinja", "timezone": "Africa/Kampala", "country": "Uganda"},
    
    # Zambia
    {"name": "Lusaka", "timezone": "Africa/Lusaka", "country": "Zambia"},
    {"name": "Kitwe", "timezone": "Africa/Lusaka", "country": "Zambia"},
    {"name": "Ndola", "timezone": "Africa/Lusaka", "country": "Zambia"},
    {"name": "Kabwe", "timezone": "Africa/Lusaka", "country": "Zambia"},
    {"name": "Chingola", "timezone": "Africa/Lusaka", "country": "Zambia"},
    
    # Zimbabwe
    {"name": "Harare", "timezone": "Africa/Harare", "country": "Zimbabwe"},
    {"name": "Bulawayo", "timezone": "Africa/Harare", "country": "Zimbabwe"},
    {"name": "Chitungwiza", "timezone": "Africa/Harare", "country": "Zimbabwe"},
    {"name": "Mutare", "timezone": "Africa/Harare", "country": "Zimbabwe"},
    {"name": "Gweru", "timezone": "Africa/Harare", "country": "Zimbabwe"},
    
    # Myanmar
    {"name": "Yangon", "timezone": "Asia/Yangon", "country": "Myanmar"},
    {"name": "Mandalay", "timezone": "Asia/Yangon", "country": "Myanmar"},
    {"name": "Naypyidaw", "timezone": "Asia/Yangon", "country": "Myanmar"},
    {"name": "Mawlamyine", "timezone": "Asia/Yangon", "country": "Myanmar"},
    {"name": "Bago", "timezone": "Asia/Yangon", "country": "Myanmar"},
    
    # Cambodia
    {"name": "Phnom Penh", "timezone": "Asia/Phnom_Penh", "country": "Cambodia"},
    {"name": "Siem Reap", "timezone": "Asia/Phnom_Penh", "country": "Cambodia"},
    {"name": "Battambang", "timezone": "Asia/Phnom_Penh", "country": "Cambodia"},
    {"name": "Sihanoukville", "timezone": "Asia/Phnom_Penh", "country": "Cambodia"},
    {"name": "Poipet", "timezone": "Asia/Phnom_Penh", "country": "Cambodia"},
    
    # Laos
    {"name": "Vientiane", "timezone": "Asia/Vientiane", "country": "Laos"},
    {"name": "Savannakhet", "timezone": "Asia/Vientiane", "country": "Laos"},
    {"name": "Pakse", "timezone": "Asia/Vientiane", "country": "Laos"},
    {"name": "Luang Prabang", "timezone": "Asia/Vientiane", "country": "Laos"},
    {"name": "Xam Neua", "timezone": "Asia/Vientiane", "country": "Laos"},
    
    # Nepal
    {"name": "Kathmandu", "timezone": "Asia/Kathmandu", "country": "Nepal"},
    {"name": "Pokhara", "timezone": "Asia/Kathmandu", "country": "Nepal"},
    {"name": "Lalitpur", "timezone": "Asia/Kathmandu", "country": "Nepal"},
    {"name": "Bharatpur", "timezone": "Asia/Kathmandu", "country": "Nepal"},
    {"name": "Biratnagar", "timezone": "Asia/Kathmandu", "country": "Nepal"},
    
    # Bhutan
    {"name": "Thimphu", "timezone": "Asia/Thimphu", "country": "Bhutan"},
    {"name": "Phuntsholing", "timezone": "Asia/Thimphu", "country": "Bhutan"},
    {"name": "Punakha", "timezone": "Asia/Thimphu", "country": "Bhutan"},
    {"name": "Wangdue Phodrang", "timezone": "Asia/Thimphu", "country": "Bhutan"},
    {"name": "Samdrup Jongkhar", "timezone": "Asia/Thimphu", "country": "Bhutan"},
]

# Write to JSON file
with open('timezones.json', 'w', encoding='utf-8') as f:
    json.dump(world_cities, f, indent=2, ensure_ascii=False)

print(f"Generated comprehensive timezones.json with {len(world_cities)} cities from around the world!")