# KeySprint - Typing Speed Test

A modern, feature-rich typing speed test application built with Python and CustomTkinter. Test your typing speed, accuracy, and improve your skills with a clean, intuitive interface.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-Non--Commercial-red.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

---

## Table of Contents

* [Features](#features)
* [Screenshots](#screenshots)
* [Installation](#installation)
* [Usage](#usage)
* [Controls](#controls)
* [Technical Details](#technical-details)
* [File Structure](#file-structure)
* [Contributing](#contributing)
* [Roadmap](#roadmap)
* [System Requirements](#system-requirements)
* [Troubleshooting](#troubleshooting)
* [License](#license)
* [Author](#author)
* [Acknowledgments](#acknowledgments)
* [Support](#support)

---

## Features

### ⌨️ Core Functionality

* Real-time typing test with live feedback
* Multiple time options: 30s, 60s, 120s
* Instant results with comprehensive statistics
* Custom text input for personalized practice

### 📊 Detailed Statistics

* Words Per Minute (WPM)
* Typing accuracy percentage
* Total characters typed
* Mistake count
* Word count
* Time elapsed

### 🖥️ Modern UI/UX

* Dark theme with orange accent colors
* Real-time visual feedback (green for correct, red for incorrect)
* Adjustable font size (10-24px)
* Scrollable text area for long passages
* Responsive layout

### 🔧 Customization Options

* Adjustable font size slider
* Multiple test duration options
* Custom text input capability
* Auto-generated practice text using Faker library

---

## Screenshots

![image](https://github.com/user-attachments/assets/91244ff4-05fe-4e24-b416-9fe8ce563c90)
![image](https://github.com/user-attachments/assets/11e9a60d-85ba-4150-969d-78ea5c597bb6)


---

## Installation

### Prerequisites

* Python 3.7 or higher
* pip package manager

### Steps

```bash
git clone https://github.com/vidhun05/keysprint.git
cd keysprint
pip install -r requirements.txt
python keysprint.py
```

---

## Usage

### Starting a Test

1. Launch the application
2. Choose your preferred test duration (30s, 60s, or 120s)
3. Adjust font size if needed using the slider
4. Click anywhere and start typing - the timer starts automatically

### Custom Text

1. Click the "Custom Text" button
2. Enter your desired text in the input field
3. Press Enter to set the custom text

### Viewing Results

* Results appear automatically when the test completes
* View your WPM, accuracy, mistakes, and other statistics
* Click "Restart" to begin a new test

---

## Controls

| Action          | Control                            |
| --------------- | ---------------------------------- |
| Start Test      | Begin typing                       |
| Restart Test    | Click "Restart" button             |
| Custom Text     | Click "Custom Text" button         |
| Change Duration | Select radio button (30s/60s/120s) |
| Adjust Font     | Use font size slider               |

---

## Technical Details

### Built With

* **Python 3.x** - Core programming language
* **CustomTkinter** - Modern UI framework
* **Tkinter** - Standard GUI toolkit
* **Faker** - Random text generation

### Architecture

* Event-driven design with real-time updates
* Modular functions for easy maintenance
* Global state management for test tracking
* Responsive grid layout system

### Key Components

* `on_keypress()` - Handles real-time typing feedback
* `start_timer()` - Manages test timing
* `show_results()` - Calculates and displays statistics
* `restart()` - Resets application state

---

## File Structure

```
keysprint/
├── main.py               # Main application file
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── text_generator.py     # text generator
└── icon.ico              # application icon file

```

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contributions

* Add different typing modes (paragraph vs random words)
* Add profile saving and statistics tracking
* Support themes/light/dark toggle
* Add typing sounds for feedback
* Implement leaderboard integration

---

## Roadmap

* [ ] User Profiles: Save and track progress
* [ ] Multiple Color Themes
* [ ] Text Difficulty Levels
* [ ] Historical Statistics Dashboard
* [ ] Audio Typing Feedback
* [ ] Online Leaderboards
* [ ] Exportable Results

---

## System Requirements

* OS: Windows 10+, macOS 10.14+, Linux
* Python: 3.7 or higher
* RAM: 50MB minimum
* Storage: 10MB available space

---

## Troubleshooting

### Application won't start

* Make sure Python 3.7+ is installed
* Ensure all dependencies are installed: `pip install -r requirements.txt`

### Text not displaying correctly

* Try adjusting the font size using the slider
* Restart the application

### Timer not working

* Make sure typing starts in the correct area
* Click restart and try again

---

## License

This project is licensed under a **custom Non-Commercial License based on the MIT License**.

You are free to:

* Use the software for personal or educational purposes
* Modify and improve the code
* Contribute via pull requests

You are **not allowed** to:

* Sell or use this software for commercial purposes
* Distribute modified versions for profit

See the [LICENSE](LICENSE) file for full terms.

---

## Author

**Vidhun Roshan** - *Initial work*

---

## Acknowledgments

* CustomTkinter for UI components
* Faker for random text generation
* Python community for extensive support

---

## Support

If you encounter any problems or have questions, please:

1. Check the [Issues](https://github.com/vidhun05/keysprint/issues) page
2. Create a new issue if your problem isn't listed
3. Provide details about your environment and the issue

---

⭐ **If you found this project helpful, give it a star!** ⭐
