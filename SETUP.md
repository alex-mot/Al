# DigiCore Password Manager - Setup Guide

## Project Overview

This is a simple, secure password manager application developed for DigiCore by Apps2U. It allows employees to securely store and retrieve login credentials for websites and other login services.

## Requirements Met

✓ Options menu for user actions:
  - Add stored credentials (username, password, and URL/resource)
  - View stored credentials
  - Exit the program

✓ Return to menu after each action completed

✓ Creates a text file for credential storage if it doesn't exist

✓ Appends new records without overwriting previous entries

✓ Displays credentials in a visually presentable way with spacing and headings

✓ Handles user input with error handling

✓ Includes embedded explanatory comments throughout the code

✓ Implements ROT3 encryption on all written data and decryption on read

## Getting Started

### Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Installation

1. Clone or download the repository
2. Navigate to the project directory:
   ```bash
   cd /workspaces/Al
   ```

### Running the Application

Execute the password manager:
```bash
python3 password_manager.py
```

Or if executable permissions are set:
```bash
./password_manager.py
```

## Usage

### Main Menu

When you run the application, you'll see:
```
==================================================
DIGCORE PASSWORD MANAGER
==================================================

Options:
  1. Add stored credentials
  2. View stored credentials
  3. Exit
==================================================
```

### Adding Credentials

Select option **1** to add new credentials:
- Enter your username
- Enter your password
- Enter the URL or resource name
- The credentials will be encrypted and stored

### Viewing Credentials

Select option **2** to view all stored credentials:
- All stored credentials will be displayed
- Each entry shows username, password, and URL/resource
- Data is automatically decrypted for display

### Exiting

Select option **3** to exit the application safely.

## Security Notes

- Credentials are stored with **ROT3 encryption** for basic protection
- The storage file (`credentials.txt`) is created in the same directory as the script
- This is a demonstration password manager. For production use, consider stronger encryption methods and secure storage solutions

## File Structure

```
/workspaces/Al/
├── password_manager.py      # Main application
├── credentials.txt          # Auto-generated storage file (not tracked in git)
├── SETUP.md                 # This file
└── README.md                # Project information
```

## Error Handling

The application includes comprehensive error handling for:
- Empty input fields
- Invalid menu choices
- File I/O errors
- Malformed credential entries
- Unexpected runtime errors

## Code Features

- **Modular design**: Separate functions for encryption, file handling, and UI
- **Clear comments**: Each function and complex operation is well documented
- **User-friendly messages**: Visual feedback with checkmarks (✓) for success and crosses (✗) for errors
- **Input validation**: Checks for empty inputs and invalid selections
- **Menu-driven interface**: Always returns to the main menu after actions

## License

Developed for DigiCore by Apps2U Digital Development Agency
