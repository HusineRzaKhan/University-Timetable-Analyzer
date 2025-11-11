import json

# JSON data
json_data = '''
{
    "Sections": {
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
}
'''

# Load JSON data
data = json.loads(json_data)

# Extract time slots for each section
for section, info in data['Sections'].items():
    print(f"Section: {section}")
    for slot in info['free_slots']:
        print(f"Day: {slot['day']}, Time: {slot['time']}")
    print()
