
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

Here’s a sample README content for `options_screen.py`, explaining the functionality and usage of the `OptionsScreen` class in your Kivy application.

---

# `options_screen.py`

## Overview

The `OptionsScreen` class defines a screen in a Kivy application that provides navigation options for the user. This screen is part of a multi-screen application and allows the user to choose between different functionalities such as Budget, Insurance, Financial Advisors, and Investment.

## Features

- **Background Color**: The background color of the screen is set to white.
- **Image**: Displays an image at the top of the screen.
- **Navigation Buttons**: Provides buttons to navigate to different screens.
- **Back Button**: Allows the user to navigate back to the previous screen.

## Components

### 1. **Background and Layout**
- The screen uses a `FloatLayout` to manage the position and size of its child widgets.
- The background color is set to white using Kivy's `Canvas` instructions.

### 2. **Image**
- An `Image` widget is positioned at the top center of the screen.
- The image size and position are set using `size_hint` and `pos_hint`.

### 3. **Navigation Buttons**
- A vertical `BoxLayout` is used to arrange the navigation buttons.
- Each button is created with a green background and white text.
- Buttons are used to navigate to different screens: Budget, Insurance, Financial Advisors, and Investment.

### 4. **Back Button**
- A back button is provided to navigate back to the previous screen (LandingScreen).
- The button is styled with a green background and white text.

## Class Definition

### `OptionsScreen(Screen)`

#### Initialization (`__init__`)
- Initializes the `FloatLayout` and sets the background color.
- Adds an image at the top of the screen.
- Creates and adds navigation buttons in a vertical layout.
- Adds a back button at the bottom of the screen.

#### Methods

- **`_update_bg_rect(self, instance, value)`**: Updates the background rectangle size and position when the layout size changes.
- **`go_to_screen(self, button_text)`**: Navigates to the screen corresponding to the button text.
- **`go_back(self, instance)`**: Navigates back to the previous screen (LandingScreen).

## Usage

To use `OptionsScreen` in your Kivy application:

1. Import the `OptionsScreen` class in your `main.py` or the script where you manage screen transitions.
2. Add an instance of `OptionsScreen` to your `ScreenManager`.
3. Ensure that the `OptionsScreen` is properly connected to your navigation logic.

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