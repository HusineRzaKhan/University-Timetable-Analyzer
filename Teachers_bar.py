import datetime

def parse_time_slot(time_slot):
    """Parses a time slot string (e.g., "08:45 - 10:10") into datetime objects."""
    start_time, end_time = time_slot.split(" - ")
    start_hour, start_minute = map(int, start_time.split(":"))
    end_hour, end_minute = map(int, end_time.split(":"))
    return datetime.time(start_hour, start_minute), datetime.time(end_hour, end_minute)

def extract_free_time_slots(teacher_data):
    """Extracts the free time slots for a given teacher."""
    free_time_slots = {}
    for slot in teacher_data["free_slots"]:
        day = slot["day"]
        time_slot = slot["time"]
        if day not in free_time_slots:
            free_time_slots[day] = []
        start_time, end_time = parse_time_slot(time_slot)
        free_time_slots[day].append((start_time, end_time))
    return free_time_slots


def print_free_time_slots(teacher_name, free_time_slots):
    """Prints the free time slots for a given teacher in a user-friendly format."""
    print(f"\nFree time slots for {teacher_name}:")
    for day, slots in free_time_slots.items():
        print(f"  - {day}:")
        for start_time, end_time in slots:
            print(f"      - {start_time:%H:%M} - {end_time:%H:%M}")

teacher_data = {
      "Dr. Affan Rauf": {
        "free_slots": [
          {
            "day": "Monday",
            "time": "Whole Day"
          },
          {
            "day": "Tuesday",
            "time": "08:45 - 10:15"
          },
          {
            "day": "Wednesday",
            "time": "08:45 - 16:40"
          },
          {
            "day": "Thursday",
            "time": "08:45 - 10:15"
          },
          {
            "day": "Friday",
            "time": "08:45 - 16:40"
          }
        ]
      },
      "Dr. Saif Maqbool": {
        "free_slots": [
            {
              "day": "Monday",
              "time": "08:45 - 16:40"
            },
          {
            "day": "Tuesday",
            "time": "11:10 - 12:45"
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
      "Mr. Awais Azam": {
        "free_slots": [
            {
              "day": "Monday",
              "time": "08:45 - 16:40"
            },
          {
            "day": "Tuesday",
            "time": "10:15 - 11:40"
          },
          {
            "day": "Tuesday",
            "time": "15:10 - 15:40"
          },
          {
            "day": "Wednesday",
            "time": "15:10 - 16:00"
          },
          {
            "day": "Thursday",
            "time": "15:10 - 15:40"
          },
          {
            "day": "Friday",
            "time": "08:45 - 16:40"
          }
        ]
      },
      "Dr. Qamar Uz Zaman": {
        "free_slots": [
            {
              "day": "Monday",
              "time": "08:45 - 16:40"
            },
          {
            "day": "Tuesday",
            "time": "10:15 - 11:40"
          },
          {
            "day": "Tuesday",
            "time": "15:10 - 15:40"
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
      },
      "Ms. Amna Babar": {
        "free_slots": [
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
      "Ms. Sumaira Mustafa": {
        "free_slots": [
          {
            "day": "Monday",
            "time": "15:10 - 16:00"
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
            "time": "08:45 - 16:40"
          },
          {
            "day": "Friday",
            "time": "08:45 - 16:40"
          }
        ]
      },
      "Mr. Tahir Farooq": {
        "free_slots": [
          {
            "day": "Monday",
            "time": "08:45 - 12:45"
          },
          {
            "day": "Tuesday",
            "time": "08:45 - 12:45"
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
      "Ms. Sahar Ajmal": {
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
            "time": "14:45 - 15:10"
          },
          {
            "day": "Tuesday",
            "time": "11:45 - 13:10"
          },
          {
            "day": "Tuesday",
            "time": "14:45 - 15:10"
          },
          {
            "day": "Wednesday",
            "time": "15:10 - 16:00"
          },
          {
            "day": "Wednesday",
            "time": "11:45 - 13:10"
          },
          {
            "day": "Wednesday",
            "time": "15:10 - 16:00"
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
      "Mr. Jawad Khalid": {
        "free_slots": [
          {
            "day": "Monday",
            "time": "15:10 - 16:00"
          },
          {
            "day": "Monday",
            "time": "10:15 - 11:40"
          },
          {
            "day": "Tuesday",
            "time": "08:45 - 10:10"
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
            "time": "08:45 - 10:10"
          },
          {
            "day": "Friday",
            "time": "08:45 - 11:40"
          }
        ]
      },
      "Ms. Farwa Ahmad": {
        "free_slots": [
            {
              "day": "Monday",
              "time": "08:45 - 16:40"
            },
          {
            "day": "Tuesday",
            "time": "08:45 - 11:40"
          },
          {
            "day": "Wednesday",
            "time": "08:45 - 16:40"
          },
          {
            "day": "Thursday",
            "time": "14:45 - 16:00"
          },
          {
            "day": "Thursday",
            "time": "14:45 - 16:00"
          },
          {
            "day": "Monday",
            "time": "08:45 - 11:40"
          },
          {
            "day": "Friday",
            "time": "08:45 - 16:40"
          }
        ]
      },
      "Dr. Shanza Abbas": {
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
            "time": "08:45 - 10:10"
          },
          {
            "day": "Wednesday",
            "time": "15:10 - 16:00"
          },
          {
            "day": "Thursday",
            "time": "08:45 - 10:10"
          },
          {
            "day": "Friday",
            "time": "08:45 - 16:40"
          }
        ]
      },
      "Mr. Saqib Ameer": {
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
            "time": "10:15 - 11:40"
          },
          {
            "day": "Thursday",
            "time": "10:15 - 11:40"
          },
          {
            "day": "Friday",
            "time": "14:45 - 16:00"
          }
        ]
      },
      "Dr. Muhammad Adnan": {
        "free_slots": [
            {
              "day": "Monday",
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
            "time": "11:45 - 13:10"
          },
          {
            "day": "Tuesday",
            "time": "15:10 - 16:00"
          },
          {
            "day": "Friday",
            "time": "08:45 - 16:40"
          }
        ]
      },
      "Dr. Sajid Anwar": {
        "free_slots": [
          {
            "day": "Monday",
            "time": "10:15 - 11:40"
          },
          {
            "day": "Monday",
            "time": "11:45 - 13:10"
          },
          {
            "day": "Wednesday",
            "time": "08:45 - 16:40"
          },
          {
            "day": "Thursday",
            "time": "10:15 - 11:40"
          },
          {
            "day": "Thursday",
            "time": "08:45 - 10:10"
          },
          {
            "day": "Tuesday",
            "time": "10:15 - 11:40"
          },
          {
            "day": "Tuesday",
            "time": "08:45 - 10:10"
          },
          {
            "day": "Friday",
            "time": "08:45 - 16:40"
          }
        ]
      },
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
  

# Process each teacher's data
for teacher_name, teacher_data in teacher_data.items():
    free_time_slots = extract_free_time_slots(teacher_data)
    print_free_time_slots(teacher_name, free_time_slots)
