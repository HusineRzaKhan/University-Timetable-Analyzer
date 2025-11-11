import re

# Sample extracted text containing course timing information
extracted_text = """
BSE-8A
FAST-NU
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
8:45 - 9:15 9:15 - 9:45 9:45 - 10:10 10:15 - 10:45 10:45 - 11:15 11:15 - 11:40 11:45 - 12:15 12:15 - 12:45 12:45 - 1:10 1:10 - 1:45 1:45 - 2:15 2:15 - 2:45 2:45 - 3:10 3:10 - 3:40 3:40 - 4:10 4:10 - 4:40
SE4001
MG4011 -
Tu
CS4036-Soft Software
Entrepreneur
ware Testing Re-Engineeri
ship
ng
R-18 Dr. Affan Rauf R-17 Dr. Saif Maqbool R-20 Mr. Awais Azam
SE4001
MG4011 - CS3002-Infor
We Software
Entrepreneur mation
Re-Engineeri
ship Security
ng
FSM#3Dr. Saif Maqbool RD-2r0. Qamar Uz Zaman R-20 Mr. Awais Azam
CS3002-Infor
Th
CS4036-Soft
mation
ware Testing
Security
RD-2r0. Qamar Uz Zaman R-17 Dr. Affan Rauf
Spring-2024 Time Table w.e.f Feb 06, 2024 (V-1.2) aSc TimetablesDepartment of Software Engineering.
"""

# Define a regular expression pattern to match days of the week
days_pattern = r"(Mo|Tu|We|Th|Fr|Sa|Su)"

# Find all matches of day patterns in the extracted text
days = re.findall(days_pattern, extracted_text)

# Extract course timing information for each day
course_timings = {}
for day in days:
    # Find the index of the day in the text
    index = extracted_text.find(day)
    
    # Extract the timing information following the day
    timing_info = extracted_text[index + len(day):].split('\n')[0].strip()
    
    # Store the timing information in the dictionary
    course_timings[day] = timing_info

# Print the extracted course timing information
print("Course Timing Information:")
for day, timing in course_timings.items():
    print(f"{day}: {timing}")
