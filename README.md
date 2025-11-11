# University Timetable Free Slots Analyzer

A Python-based utility to extract and analyze university academic timetables, identifying free time slots for teachers and class sections. Designed for educational institutions using PDF-based timetable systems.

## 🎯 Overview

This project automates the extraction of free time slots from university timetables, making it easy for:
- **Teachers** to find available meeting times
- **Administrators** to identify scheduling gaps
- **Students** to understand section availability

The system parses complex PDF timetables and generates structured JSON data for easy integration with scheduling systems.

## ✨ Features

- 📄 **PDF Timetable Extraction**: Parses academic timetables from PDF documents
- 👨‍🏫 **Teacher Availability Analysis**: Identifies free slots for each instructor
- 🏫 **Section Availability Analysis**: Determines free periods for each class section
- 🔄 **Multiple Format Support**: Handles complex multi-page timetables
- 💾 **JSON Export**: Structured output for further processing
- 🎓 **Multi-section Support**: Manages multiple class sections (BSE-2 through BSE-8)
- ⏰ **Time Slot Analysis**: Detailed time-based scheduling information

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/HusineRzaKhan/university-timetable-analyzer.git
cd university-timetable-analyzer
```

2. Install required dependencies:
```bash
pip install PyPDF2 pdfplumber
```

### Requirements

The project uses the following libraries:

| Library | Purpose | Version |
|---------|---------|---------|
| `PyPDF2` | PDF reading and text extraction | Latest |
| `pdfplumber` | Advanced PDF table parsing | Latest |
| `re` | Regular expression pattern matching | Built-in |
| `json` | JSON data serialization | Built-in |


## 🔍 Technical Details

### Regex Patterns Used
- **Time Pattern**: `r'(\d{1,2}:\d{2})\s*-\s*(\d{1,2}:\d{2})'`
- **Day Pattern**: `r'(Mo|Tu|We|Th|Fr)'`
- **Course Code**: `r'[A-Z]+\d+[A-Z]*'`

### Time Format
- Standard 24-hour format with AM/PM indicators
- 30-minute and 25-minute slot variations
- Lunch breaks factored into analysis


## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- Support for additional university formats
- Performance optimizations
- Unit tests and documentation
- Error handling improvements
- Visualization features

## 📝 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Hussain Raza Khan**
- GitHub: [@HusineRzaKhan](https://github.com/HusineRzaKhan)

## 📧 Contact & Support

For questions, suggestions, or bug reports:
- Open an issue on GitHub
- Email: HussainRazaKhanBaloch@gmail.com
- Check existing issues before opening new ones

## 📚 References

- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/)
- [pdfplumber Documentation](https://github.com/jsvine/pdfplumber)
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [JSON Format Specification](https://www.json.org/)

---

**Made with ❤️ for educational institutions**

⭐ If you find this project helpful, please consider giving it a star!