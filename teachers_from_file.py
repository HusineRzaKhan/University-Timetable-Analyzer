import json

# Load the JSON data from the file
file_path = r"D:\Codings\Whatsapp_Projects\Teachers.json"

with open(file_path, 'r') as file:
    data = json.load(file)

# Function to extract time slots for each teacher
def extract_time_slots(teacher_data):
    for teacher, slots in teacher_data.items():
        print(f"\nTeacher: {teacher}")
        for slot in slots['free_slots']:
            print(f"Day: {slot['day']}, Time: {slot['time']}")
        print()

# Extract time slots for each teacher
extract_time_slots(data)
