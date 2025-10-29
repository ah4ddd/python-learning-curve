import math

DELHI = (28.6139, 77.2090)
MUMBAI = (19.0760, 72.8777)
KOLKATA = (22.5726, 88.3639)
CHENNAI = (13.0827, 80.2707)

city_info = {
    DELHI: "Capital of India",
    MUMBAI: "Financial hub and home to Bollywood",
    KOLKATA: "Cultural capital of India",
    CHENNAI: "Gateway to South India"
}

def show_all_cities():
    print("\n🌍 List of Cities:")
    for coord, info in city_info.items():
        print(f"City: {info} | Coordinates: {coord}")

def find_city(coord):
    return city_info.get(coord, "City not found")

def calculate_distance(coord1, coord2):
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371
    return round(c * r, 2)

show_all_cities()
print("\n🔎 Finding a city:")
print(find_city(MUMBAI))

print("\n📏 Distance between Delhi and Mumbai:")
print(calculate_distance(DELHI, MUMBAI), "km")
