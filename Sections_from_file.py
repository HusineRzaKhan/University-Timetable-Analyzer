import json

# Path to the JSON file
json_file = r'D:\Codings\Whatsapp_Projects\Sections.json'

# Open the JSON file and load the data
with open(json_file, 'r') as file:
    data = json.load(file)

# Extract time slots for each section
for section, info in data['Sections'].items():
    print(f"Section: {section}")
    for slot in info['free_slots']:
        print(f"Day: {slot['day']}, Time: {slot['time']}")
    print()
