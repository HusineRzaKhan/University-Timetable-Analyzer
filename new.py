import PyPDF2
import re

def extract_timetable(file_path):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        timetable_text = ''

        # Extract text from each page
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            timetable_text += page.extract_text()
            print(timetable_text)

    return timetable_text

def extract_free_time_slots(timetable_text):
    # Split the timetable text into lines
    lines = timetable_text.split('\n')

    # Regular expression to match time slots
    time_pattern = re.compile(r'(\d{1,2}:\d{2})\s*-\s*(\d{1,2}:\d{2})')

    # Dictionary to store free time slots for each teacher and section
    free_time_slots = {'teachers': {}, 'sections': {}}

    current_teacher = None
    current_section = None

    for line in lines:
        if line.strip().startswith('Teacher:'):
            current_teacher = line.strip().split(':')[-1].strip()
            free_time_slots['teachers'][current_teacher] = []

        elif line.strip().startswith('Section:'):
            current_section = line.strip().split(':')[-1].strip()
            free_time_slots['sections'][current_section] = []

        # Check for time slots
        matches = time_pattern.findall(line)
        for match in matches:
            if current_teacher is not None:
                free_time_slots['teachers'][current_teacher].append(match)
            if current_section is not None:
                free_time_slots['sections'][current_section].append(match)

    return free_time_slots


if __name__ == "__main__":
    # Path to the timetable PDF file
    pdf_file_path = rb'D:\Codings\Whatsapp_Projects\Classwise_Timetable_SE_2024.pdf'

    # Extract timetable text
    timetable_text = extract_timetable(pdf_file_path)

    # Extract free time slots
    free_time_slots = extract_free_time_slots(timetable_text)

    # Print free time slots for each teacher
    print("Free Time Slots for Teachers:")
    for teacher, time_slots in free_time_slots['teachers'].items():
        print(f"{teacher}: {time_slots}")

    # Print free time slots for each section
    print("\nFree Time Slots for Sections:")
    for section, time_slots in free_time_slots['sections'].items():
        print(f"{section}: {time_slots}")
