Here’s the updated README content, including the new files and details for `insurance.py`, `budget.py`, `investment_platforms.py`, and `financial_advisors.py`:

---

# Smart Money App README
**Created by BC Rachoshi**

## Overview
This Kivy-based application offers a dynamic user interface with multiple screens, each providing different functionalities related to personal finance. Screens include options for budget management, finding financial advisors, discovering investment platforms, and accessing insurance information.

## Files

### `main.py`

**Purpose**: Entry point of the application. Initializes Kivy, sets up the `ScreenManager`, and loads various screens.

**Key Responsibilities**:
- Initializes the Kivy app.
- Configures `ScreenManager` for screen transitions.
- Loads and displays different screens: LandingScreen, OptionsScreen, BudgetScreen, FinancialAdvisorsScreen, InvestmentScreen, InsuranceScreen.

**Usage**:
```bash
python main.py
```

### `landing_screen.py`

**Purpose**: Defines the landing page layout and behavior.

**Key Responsibilities**:
- Creates a landing page with interactive design.
- Includes navigation to other screens.

**Usage**:
- Imported and used by `main.py` to display the landing page.

### `options_screen.py`

**Purpose**: Provides navigation options for the user.

**Key Responsibilities**:
- Displays navigation buttons to other screens.
- Includes a back button to return to the landing page.

**Usage**:
- Imported and used by `main.py` for navigation purposes.

---

### `budget.py`

**Purpose**: Manages personal budgeting. Users can input income, add expenses, and view remaining income.

**Key Responsibilities**:
- Allows users to set and update their income.
- Enables adding and managing expenses.
- Displays remaining income and lists of expenses.
- Includes buttons to clear all expenses and navigate back.

**Usage**:
- Imported and used by `main.py` to manage budget-related functionality.

---

### `investment_platforms.py`

**Purpose**: Provides a screen for finding investment platforms based on user-entered or current location.

**Key Responsibilities**:
- Allows users to input a location or use their current location to search for investment platforms.
- Displays a list of platforms with clickable buttons.
- Redirects to the corresponding investment platform's website.

**Usage**:
- Imported and used by `main.py` to handle investment platform searches.

---

### `financial_advisors.py`

**Purpose**: Offers a screen to find financial advisors based on user-entered or current location.

**Key Responsibilities**:
- Users can enter a location or use their current location to find financial advisors.
- Displays a list of advisors with their contact details.
- Redirects to advisor websites for more information.

**Usage**:
- Imported and used by `main.py` to handle financial advisor searches.

---

### `insurance.py`

**Purpose**: Displays a list of insurance options available in South Africa.

**Key Responsibilities**:
- Shows a list of insurance providers with clickable buttons.
- Each button opens the corresponding insurance provider's website.

**Usage**:
- Imported and used by `main.py` to handle insurance-related functionality.

---

## Installation

1. Ensure Python and Kivy are installed. Install Kivy with:
   ```bash
   pip install kivy
   ```

2. Clone the repository or download the project files.

3. Run the application with:
   ```bash
   python main.py
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---