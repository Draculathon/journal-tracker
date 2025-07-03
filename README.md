# Journal Tracker

A simple, flexible Python app to record, manage, and explore your journal entries — now with a terminal version and a full GUI version.

## ✨ Versions
# 💻 Terminal Version (main.py)
- Run directly in the terminal or console.
- Simple text-based interaction.
- Core features: add, view, filter by date, keyword search.
# 💻 GUI Version (gui.py)
- Full graphical user interface (Tkinter).
- Clean design with colors, fonts, and clear layouts.
- Features:
    - Add entries with mood and weather.
    - View formatted metadata (entry, date, mood, weather).
    - Search entries by keyword (mood or weather, supports partial matches).
    - Filter entries by date.
    - Edit entries with safe field separation.
    - Delete entries with confirmation.
    - Exit confirmation prompt.
    - Input validation and prevention of invalid character.

## 🚀 How to Run
# Terminal version
```bash
python main.py
```
# GUI Version
```bash
python gui.py
```
## 📁 Folder Structure
```
journal-tracker/
├── main.py           # Terminal version
├── gui.py            # GUI version
├── journals/         # Folder for journal entry files
│   └── entries.txt   # Data file for entries
├── .gitignore
└── README.md         # Project documentation
```
# Notes
- Avoid using the ~ symbol in your journal text, mood, or weather. it's used as a separator internally.
- Make sure the journals folder exists before running either version.
## 🛠️ Installation
```bash
git clone https://github.com/Draculathon/journal-tracker.git
cd journal-tracker
pip install tk # (Tkinter is included by default by most python installations)
```
# Version
- Terminal: v1.1
- GUI: v1.4 Final stable release

## 🤝 Contributions
Pull requests, feature suggestions, and feedback are welcome!

## 📄 License
MIT License.
## 🧑🏽‍💻 Author

**[@Draculathon](https://github.com/Draculathon)**
MIT License © 2025