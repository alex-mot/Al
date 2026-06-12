# DigiCore Password Manager — Pseudocode

Purpose: simple CLI password manager with a separated module structure for menu, main loop, credentials storage, and ROT3-style encryption.

---

Project structure:
- `main.py` : application entry point and main loop
- `menu.py` : display menu and validate menu input
- `Passy_Master.py` : credential storage operations, file handling, add/view functionality
- `cryptonius.py` : ROT3 encryption and decryption utilities

Main (main.py):
1. Import `ensure_credentials_file_exists`, `add_credentials`, `view_credentials` from `Passy_Master.py`.
2. Import `display_menu`, `get_user_choice` from `menu.py`.
3. Ensure credentials file exists.
4. Loop until user exits:
   a. Display main menu options with emojis.
   b. Read and validate user choice (1-3).
   c. If choice == 1: call `add_credentials()`.
   d. If choice == 2: call `view_credentials()`.
   e. If choice == 3: print goodbye and break loop.
5. Catch `KeyboardInterrupt` and exit gracefully.

Menu utilities (menu.py):
- `display_menu()` prints the menu options and emoji decorations.
- `get_user_choice()` prompts for input and accepts only '1', '2', or '3'.

Cryptography utilities (cryptonius.py):
- Defines a full custom `CHARSET` of 94 characters.
- `rot3_encrypt(text)`:
  - For each character in text:
    - If character exists in `CHARSET`, shift its index forward by 5 positions modulo charset length.
    - Otherwise, keep the character unchanged.
  - Return the joined encrypted string.
- `rot3_decrypt(text)`:
  - For each character in text:
    - If character exists in `CHARSET`, shift its index backward by 5 positions modulo charset length.
    - Otherwise, keep the character unchanged.
  - Return the joined decrypted string.

Credential storage logic (Passy_Master.py):
- `ensure_credentials_file_exists()`:
  - If `credentials.txt` does not exist, create an empty file.
- `add_credentials()`:
  - Prompt user for username, password, and URL/resource.
  - Validate that no field is empty; if empty, print an error and return.
  - Encrypt each field using `rot3_encrypt()` from `cryptonius.py`.
  - Write a new line to `credentials.txt` in the format: `encrypted_username|encrypted_password|encrypted_url`.
  - Print success message.
- `view_credentials()`:
  - If the file does not exist or is empty, print "No credentials stored yet." and wait for Enter.
  - Read all lines from the credentials file.
  - For each non-empty line:
    - Split by '|' into three parts; if there are not exactly three parts, print invalid format.
    - Decrypt each part with `rot3_decrypt()`.
    - Print formatted entry details.
  - After listing entries, pause for user input before returning to the menu.

Input validation:
- Menu input: only accept '1', '2', '3'.
- Credential fields: must be non-empty after stripping whitespace.

Error handling:
- Wrap file and parsing operations in try/except and print friendly messages.
- Catch `KeyboardInterrupt` in the main loop and exit cleanly.

Storage format:
- Plain text file, one credential per line.
- Fields separated by `|`.
- Fields are ROT3-encrypted using the custom charset and shift amount.

Security notes:
- ROT3-style obfuscation is not secure; use proper encryption for production.
- Consider file permissions and encrypted storage for real applications.

---

