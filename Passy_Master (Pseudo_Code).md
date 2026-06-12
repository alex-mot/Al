# DigiCore Password Manager — Pseudocode

Purpose: simple CLI password manager storing ROT3-encrypted credentials in a text file.

---

Main:
1. Ensure credentials file exists (create if missing).
2. Loop until user exits:
   a. Display main menu:
      - 1. Add stored credentials
      - 2. View stored credentials
      - 3. Exit
   b. Read and validate user choice (1-3).
   c. If choice == 1: call AddCredentials()
   d. If choice == 2: call ViewCredentials()
   e. If choice == 3: print goodbye and break loop

Functions:

rot3_encrypt(text):
  - For each character in text:
    - If lowercase letter: rotate forward by 5 within 'a'..'z'
    - If uppercase letter: rotate forward by 5 within 'A'..'Z'
    - Else: keep character unchanged
  - Return joined encrypted string

rot3_decrypt(text):
  - Same as rot3_encrypt but rotate backward by 5
  - Return joined decrypted string

ensure_credentials_file_exists():
  - If credentials file does not exist: create empty file

AddCredentials():
  - Prompt user for username, password, URL/resource
  - Validate none are empty; if empty, print error and return
  - Encrypt each field with rot3_encrypt
  - Append a line to credentials file in format: encrypted_username|encrypted_password|encrypted_url
  - Print success message

ViewCredentials():
  - If credentials file missing or empty: print "No credentials" and pause for user (press Enter)
  - Read all lines from file
  - For each non-empty line:
    - Split by '|' into three parts; if parts != 3: mark invalid and continue
    - Decrypt each part with rot3_decrypt
    - Print formatted entry (index, username, password, URL)
  - After listing, print separator and pause for user (press Enter)

Input validation:
  - Menu input: only accept '1', '2', '3'
  - Credential fields: must be non-empty strings after strip()

Error handling:
  - Wrap file and parsing operations in try/except and print friendly errors
  - Catch KeyboardInterrupt in main loop and exit gracefully

Storage format:
  - Plain text file, one credential per line
  - Fields separated by '|' character
  - Fields are ROT3-encrypted for simple obfuscation (not secure encryption)

Security notes (pseudo):
  - ROT3 is NOT secure; use proper encryption for real use
  - Consider file permissions and encrypted storage in production

---

