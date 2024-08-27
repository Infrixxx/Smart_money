
# Smart Money App Readme 
# Created by BC Rachoshi

## Overview

This project is a Kivy-based application designed to provide a dynamic and adaptable user interface. The application features multiple screens with a consistent theme, including a landing page with an interactive design.

## Files

### `main.py`

**Purpose**: This is the entry point of the Kivy application. It initializes the Kivy application, sets up the screen manager, and loads different screens.

**Key Responsibilities**:
- Initializes the Kivy application instance.
- Configures the `ScreenManager` to handle multiple screens.
- Loads and displays the `LandingScreen` and other screens.

**Usage**:
1. Run the script using Python:
   ```bash
   python main.py
   ```

### `landing_page.py`

**Purpose**: Defines the layout and behavior of the landing page screen within the application.

**Key Responsibilities**:
- Creates a `LandingScreen` class that inherits from Kivy’s `Screen`.
- Sets up the layout using `FloatLayout` and adds widgets such as labels, buttons, and images.
- Handles the background color and updates its size and position based on the window size.
- Provides a method to transition to another screen (e.g., `go_to_options`).

**Usage**:
- This file is imported and used by `main.py` to display the landing page when the application starts.

## Installation

1. Ensure you have Python and Kivy installed. You can install Kivy using pip:
   ```bash
   pip install kivy
   ```

2. Clone the repository or download the project files.

3. Run the application:
   ```bash
   python main.py
   ```

## Configuration

- The application uses a dynamic layout that adjusts to different screen sizes. Ensure that the assets (e.g., `smart_money.png`) are in the correct directory or update the path in `landing_page.py`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---