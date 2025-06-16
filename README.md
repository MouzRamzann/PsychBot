# PsychBot

PsychBot is a web-based dashboard and analytics platform. It provides interactive data visualizations, statistics, and real-time UI components for monitoring and managing information. The project leverages modern web technologies and libraries for dynamic charts, maps, and responsive layouts.

## Features

- Interactive and animated charts (Morris.js, Chartist.js)
- Real-time world map visualization with markers
- Responsive and modern UI design with SCSS/CSS customization
- Sidebar navigation and multiple dashboard widgets
- Progress bars, sparkline charts, and team/task visual components
- Dark and light theme support
- Extensible structure for adding new pages and widgets

## Technologies Used

- **JavaScript** (Core dashboard logic, charts, maps, UI interaction)
- **HTML** (Dashboard structure and views)
- **SCSS / CSS** (Custom themes and styling)
- **Python** (Minor backend/data processing roles)
- **jQuery** (DOM manipulation and UI effects)
- **Libraries**: Morris.js, Chartist.js, jQuery Vector Map, SlickNav, WOW.js

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/MouzRamzann/PsychBot.git
    cd PsychBot
    ```

2. **Install dependencies:**
    - For Python (if used on backend):  
      If a `requirements.txt` is present:
      ```bash
      pip install -r requirements.txt
      ```

3. **Run the project:**
    - ```bash
      python manage.py runserver
      ```

## Folder Structure

- `static/assets/js/` & `static/dark_assets/js/`: JavaScript files for charts, maps, and UI logic.
- `static/dark_assets/scss/`: SCSS files for theme and widget styling.
- `static/assets/css/`: Compiled CSS files.
- `static/dark_assets/pages/`: Page-specific scripts and styles.

## Contribution

Contributions, bug reports, and feature requests are welcome!  
Please open an issue or submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

---

*Feel free to expand this README with more details as your project grows!*
