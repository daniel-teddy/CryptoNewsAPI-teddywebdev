import json
import re

def extract_coordinates(href):
    match = re.search(r'!3d([^!]+)!4d([^!]+)', href)
    if match:
        latitude = match.group(1)
        longitude = match.group(2)
        return latitude, longitude
    else:
        return None, None

def process_officials():
    with open('officials.json', 'r') as file:
        officials_data = json.load(file)

    for museum in officials_data:
        href = museum['href']
        latitude, longitude = extract_coordinates(href)
        museum['latitude'] = latitude
        museum['longitude'] = longitude

    with open('officials.json', 'w') as file:
        json.dump(officials_data, file, indent=2)

if __name__ == "__main__":
    process_officials()
