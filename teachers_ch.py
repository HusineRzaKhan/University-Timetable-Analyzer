import json

# Load the JSON data
data = '''
{
  "Mr. Hafiz M. Zeeshan Raza": {
    "free_slots": [
      {
        "day": "Monday",
        "time": "11:45 - 13:10"
      },
      {
        "day": "Wednesday",
        "time": "10:15 - 11:40"
      },
      {
        "day": "Wednesday",
        "time": "11:45 - 13:10"
      },
      {
        "day": "Tuesday",
        "time": "14:45 - 15:10"
      },
      {
        "day": "Thursday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Friday",
        "time": "08:45 - 16:40"
      }
    ]
  },
  "Ms. Maham Saleem": {
    "free_slots": [
      {
        "day": "Monday",
        "time": "14:45 - 16:00"
      },
      {
        "day": "Tuesday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Wednesday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Thursday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Friday",
        "time": "08:45 - 16:40"
      }
    ]
  },
  "Dr. Sana Shahid": {
    "free_slots": [
      {
        "day": "Monday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Tuesday",
        "time": "14:45 - 15:10"
      },
      {
        "day": "Tuesday",
        "time": "15:10 - 16:00"
      },
      {
        "day": "Wednesday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Thursday",
        "time": "11:45 - 13:10"
      },
      {
        "day": "Thursday",
        "time": "10:15 - 11:40"
      },
      {
        "day": "Friday",
        "time": "08:45 - 16:40"
      }
    ]
  },
  "Ms. Nabeela Ashraf": {
    "free_slots": [
      {
        "day": "Monday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Tuesday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Wednesday",
        "time": "08:45 - 10:10"
      },
      {
        "day": "Wednesday",
        "time": "14:45 - 15:10"
      },
      {
        "day": "Thursday",
        "time": "14:45 - 15:10"
      },
      {
        "day": "Thursday",
        "time": "15:10 - 16:00"
      },
      {
        "day": "Friday",
        "time": "08:45 - 11:40"
      }
    ]
  },
  "Ms. Samia Aziz": {
    "free_slots": [
      {
        "day": "Monday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Wednesday",
        "time": "14:45 - 16:00"
      },
      {
        "day": "Thursday",
        "time": "14:45 - 16:00"
      },
      {
        "day": "Tuesday",
        "time": "14:45 - 16:00"
      },
      {
        "day": "Friday",
        "time": "08:45 - 16:40"
      }
    ]
  },
  "Mr. Tehreem Aslam": {
    "free_slots": [
      {
        "day": "Monday",
        "time": "08:45 - 11:40"
      },
      {
        "day": "Tuesday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Wednesday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Thursday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Friday",
        "time": "08:45 - 16:40"
      }
    ]
  },
  "Ms. Munazza Akhtar": {
    "free_slots": [
      {
        "day": "Monday",
        "time": "15:10 - 16:50"
      },
      {
        "day": "Tuesday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Wednesday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Thursday",
        "time": "15:10 - 16:50"
      },
      {
        "day": "Friday",
        "time": "08:45 - 16:40"
      }
    ]
  },
  "Mr. Khalid Mehmood Anjum": {
    "free_slots": [
      {
        "day": "Monday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Tuesday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Wednesday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Thursday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Friday",
        "time": "11:45 - 13:10"
      },
      {
        "day": "Friday",
        "time": "14:45 - 16:00"
      }
    ]
  },
  "Mr. Adeel Tahir": {
    "free_slots": [
      {
        "day": "Monday",
        "time": "08:45 - 10:10"
      },
      {
        "day": "Monday",
        "time": "14:45 - 15:10"
      },
      {
        "day": "Tuesday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Wednesday",
        "time": "10:15 - 11:40"
      },
      {
        "day": "Wednesday",
        "time": "08:45 - 10:10"
      },
      {
        "day": "Thursday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Friday",
        "time": "08:45 - 16:40"
      }
    ]
  },
  "Mr. Umer Iqbal": {
    "free_slots": [
      {
        "day": "Monday",
        "time": "10:15 - 11:40"
      },
      {
        "day": "Tuesday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Wednesday",
        "time": "08:45 - 10:10"
      },
      {
        "day": "Wednesday",
        "time": "14:45 - 15:10"
      },
      {
        "day": "Thursday",
        "time": "14:45 - 15:10"
      },
      {
        "day": "Friday",
        "time": "08:45 - 16:40"
      }
    ]
  },
  "Dr. Muhammad Ahmad": {
    "free_slots": [
      {
        "day": "Monday",
        "time": "14:45 - 15:10"
      },
      {
        "day": "Monday",
        "time": "11:45 - 13:10"
      },
      {
        "day": "Tuesday",
        "time": "10:15 - 11:40"
      },
      {
        "day": "Wednesday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Tuesday",
        "time": "11:45 - 13:10"
      },
      {
        "day": "Thursday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Friday",
        "time": "08:45 - 16:40"
      }
    ]
  },
  "Ms. Amna Shahbaz": {
    "free_slots": [
      {
        "day": "Monday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Tuesday",
        "time": "14:45 - 16:00"
      },
      {
        "day": "Wednesday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Thursday",
        "time": "08:45 - 11:40"
      },
      {
        "day": "Friday",
        "time": "08:45 - 16:40"
      }
    ]
  },
  "Mr. Muhammad Munawar": {
    "free_slots": [
      {
        "day": "Monday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Tuesday",
        "time": "08:45 - 16:40"
      },
      {
        "day": "Wednesday",
        "time": "14:45 - 15:10"
      },
      {
        "day": "Wednesday",
        "time": "10:15 - 11:40"
      },
      {
        "day": "Thursday",
        "time": "10:15 - 11:40"
      },
      {
        "day": "Thursday",
        "time": "11:45 - 13:10"
      },
      {
        "day": "Friday",
        "time": "08:45 - 16:40"
      }
    ]
  }
}
'''

# Parse JSON data
teachers_data = json.loads(data)

# Function to extract time slots of each teacher's free time slots for each day
def extract_time_slots(teachers_data):
    for teacher, slots_info in teachers_data.items():
        print(f"{teacher}:")
        for slot in slots_info["free_slots"]:
            print(f"Day: {slot['day']}, Time: {slot['time']}")
        print()

# Call the function to extract time slots
extract_time_slots(teachers_data)
