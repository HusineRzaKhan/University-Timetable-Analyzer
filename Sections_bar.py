def parse_time_slot(time_slot):
    """Parses a time slot string (e.g., "08:45 - 10:15") into datetime objects."""
    start_time, end_time = time_slot.split(" - ")
    start_hour, start_minute = map(int, start_time.split(":"))
    end_hour, end_minute = map(int, end_time.split(":"))
    return datetime.time(start_hour, start_minute), datetime.time(end_hour, end_minute)

def extract_free_time_slots(section_data):
    """Extracts the free time slots for a given section."""
    free_time_slots = {}
    for day, time_slots in section_data["free_slots"].items():
        free_time_slots[day] = []
        for time_slot in time_slots:
            start_time, end_time = parse_time_slot(time_slot)
            free_time_slots[day].append((start_time, end_time))
    return free_time_slots

def print_free_time_slots(section_name, free_time_slots):
    """Prints the free time slots for a given section in a user-friendly format."""
    print(f"Free time slots for {section_name}:")
    for day, slots in free_time_slots.items():
        print(f"  - {day}:")
        for start_time, end_time in slots:
            print(f"      - {start_time:%H:%M} - {end_time:%H:%M}")

section_data = {
      "BSE-8A": {
        "free_slots": [
          {
            "day": "Tuesday",
            "time": "08:45 - 10:15"
          },
          {
            "day": "Tuesday",
            "time": "13:10 - 13:45"
          },
          {
            "day": "Tuesday",
            "time": "15:10 - 16:40"
          },
          {
            "day": "Wednesday",
            "time": "11:45 - 15:10"
          },
          {
            "day": "Thursday",
            "time": "08:45 - 10:15"
          },
          {
            "day": "Thursday",
            "time": "13:10 - 16:40"
          },
          {
            "day": "Friday",
            "time": "08:45 - 16:40"
          }
        ]
      },
      "BSE-8B": {
        "free_slots": [
          {
            "day": "Monday",
            "time": "08:45 - 13:45"
          },
          {
            "day": "Tuesday",
            "time": "08:45 - 10:15"
          },
          {
            "day": "Tuesday",
            "time": "13:10 - 15:10"
          },
          {
            "day": "Wednesday",
            "time": "10:15 - 16:40"
          },
          {
            "day": "Thursday",
            "time": "08:45 - 10:15"
          },
          {
            "day": "Thursday",
            "time": "11:40 - 13:45"
          },
          {
            "day": "Thursday",
            "time": "15:10 - 16:40"
          },
          {
            "day": "Friday",
            "time": "08:45 - 16:40"
          }
        ]
      },
      "BSE-6A": {
        "free_slots": [
          {
            "day": "Monday",
            "time": "12:45 - 13:45"
          },
          {
            "day": "Tuesday",
            "time": "13:10 - 13:15"
          },
          {
            "day": "Tuesday",
            "time": "15:10 - 16:40"
          },
          {
            "day": "Wednesday",
            "time": "13:10 - 13:45"
          },
          {
            "day": "Thursday",
            "time": "08:45 - 11:45"
          },
          {
            "day": "Thursday",
            "time": "13:10 - 13:45"
          },
          {
            "day": "Friday",
            "time": "08:45 - 16:40"
          }
        ]
      },
      "BSE-6B": {
        "free_slots": [
          {
            "day": "Monday",
            "time": "13:10 - 16:40"
          },
          {
            "day": "Tuesday",
            "time": "12:45 - 13:45"
          },
          {
            "day": "Wednesday",
            "time": "08:45 - 10:10"
          },
          {
            "day": "Wednesday",
            "time": "13:10 - 13:45"
          },
          {
            "day": "Thursday",
            "time": "13:10 - 13:45"
          },
          {
            "day": "Friday",
            "time": "11:40 - 16:40"
          }
        ]
      },
      "BSE-4A": {
        "free_slots": [
          {
            "day": "Monday",
            "time": "08:45 - 10:10"
          },
          {
            "day": "Monday",
            "time": "13:10 - 13:45"
          },
          {
            "day": "Tuesday",
            "time": "11:45 - 13:45"
          },
          {
            "day": "Tuesday",
            "time": "15:10 - 16:40"
          },
          {
            "day": "Wednesday",
            "time": "13:10 - 13:45"
          },
          {
            "day": "Thursday",
            "time": "13:10 - 13:45"
          },
          {
            "day": "Friday",
            "time": "11:40 - 16:40"
          }
        ]
      },
      "BSE-4B": {
        "free_slots": [
          {
            "day": "Monday",
            "time": "13:10 - 15:10"
          },
          {
            "day": "Monday",
            "time": "16:10 - 16:40"
          },
          {
            "day": "Tuesday",
            "time": "13:10 - 13:45"
          },
          {
            "day": "Wednesday",
            "time": "10:15 - 11:45"
          },
          {
            "day": "Wednesday",
            "time": "13:10 - 13:45"
          },
          {
            "day": "Thursday",
            "time": "13:10 - 13:45"
          },
          {
            "day": "Friday",
            "time": "13:10 - 15:10"
          }
        ]
      },
      "BSE-2A": {
        "free_slots": [
          {
            "day": "Monday",
            "time": "11:40 - 13:45"
          },
          {
            "day": "Monday",
            "time": "15:10 - 16:40"
          },
          {
            "day": "Tuesday",
            "time": "11:40 - 13:45"
          },
          {
            "day": "Wednesday",
            "time": "11:40 - 13:45"
          },
          {
            "day": "Thursday",
            "time": "11:40 - 13:45"
          },
          {
            "day": "Friday",
            "time": "08:45 - 13:45"
          }
        ]
      },
      "BSE-2B": {
        "free_slots": [
          {
            "day": "Monday",
            "time": "08:45 - 10:15"
          },
          {
            "day": "Monday",
            "time": "13:10 - 13:45"
          },
          {
            "day": "Tuesday",
            "time": "10:15 - 11:40"
          },
          {
            "day": "Tuesday",
            "time": "13:10 - 13:45"
          },
          {
            "day": "Wednesday",
            "time": "10:15 - 11:40"
          },
          {
            "day": "Wednesday",
            "time": "13:10 - 13:45"
          },
          {
            "day": "Thursday",
            "time": "13:10 - 13:45"
          },
          {
            "day": "Friday",
            "time": "08:45 - 13:45"
          }
        ]
      }
    }

# Process each section's data
for section_name, section_data in section_data.items():
    free_time_slots = extract_free_time_slots(section_data)
    print_free_time_slots(section_name, free_time_slots)
