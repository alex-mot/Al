from pathlib import Path
from menu import display_menu, get_user_choice

# Configuration
CREDENTIALS_FILE = "credentials.txt"
CHARSET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{["\':;?/>.<, '


def rot3_encrypt(text):
    """
    Encrypt text using ROT3 cipher over the full custom character set.
    """
    encrypted = []
    for char in text:
        if char in CHARSET:
            index = CHARSET.find(char)
            encrypted.append(CHARSET[(index + 5) % len(CHARSET)])
        else:
            encrypted.append(char)
    return ''.join(encrypted)


def rot3_decrypt(text):
    """
    Decrypt text using ROT3 cipher over the full custom character set.
    """
    decrypted = []
    for char in text:
        if char in CHARSET:
            index = CHARSET.find(char)
            decrypted.append(CHARSET[(index - 5) % len(CHARSET)])
        else:
            decrypted.append(char)
    return ''.join(decrypted)


def ensure_credentials_file_exists():
    """
    Create credentials file if it does not already exist
    """
    if not Path(CREDENTIALS_FILE).exists():
        Path(CREDENTIALS_FILE).touch()
        print(f"✓ Created new credentials file: {CREDENTIALS_FILE}")


def add_credentials():
    """
    Add new credentials to the storage file
    Prompts user for username, password, and URL/resource
    """
    print("\n" + "=" * 50)
    print("ADD NEW CREDENTIALS")
    print("=" * 50)
    
    try:
        # Get user input
        username = input("Enter username: ").strip()
        if not username:
            print("✗ Username cannot be empty.")
            return
        
        password = input("Enter password: ").strip()
        if not password:
            print("✗ Password cannot be empty.")
            return
        
        url = input("Enter URL/resource: ").strip()
        if not url:
            print("✗ URL/resource cannot be empty.")
            return
        
        # Encrypt the credentials
        encrypted_username = rot3_encrypt(username)
        encrypted_password = rot3_encrypt(password)
        encrypted_url = rot3_encrypt(url)
        
        # Append to credentials file
        with open(CREDENTIALS_FILE, 'a') as file:
            file.write(f"{encrypted_username}|{encrypted_password}|{encrypted_url}\n")
        
        print("\n✓ Credentials added successfully!")
        
    except Exception as e:
        print(f"\n✗ Error adding credentials: {e}")


def view_credentials():
    """
    Display all stored credentials in a visually presentable format
    Decrypts and displays each credential entry
    """
    print("\n" + "=" * 70)
    print("STORED CREDENTIALS")
    print("=" * 70)
    
    try:
        # Check if file exists and has content
        if not Path(CREDENTIALS_FILE).exists() or Path(CREDENTIALS_FILE).stat().st_size == 0:
            print("No credentials stored yet.")
            input("\nPress Enter to return to main menu...")
            return
        
        # Read and display credentials
        with open(CREDENTIALS_FILE, 'r') as file:
            credentials = file.readlines()
        
        if not credentials:
            print("No credentials stored yet.")
            input("\nPress Enter to return to main menu...")
            return
        
        # Display each credential with formatting
        print(f"\nTotal credentials: {len(credentials)}\n")
        
        for index, line in enumerate(credentials, 1):
            line = line.strip()
            if not line:
                continue
            
            # Parse and decrypt credentials
            try:
                parts = line.split('|')
                if len(parts) != 3:
                    print(f"Entry {index}: [Invalid format]")
                    continue
                
                username = rot3_decrypt(parts[0])
                password = rot3_decrypt(parts[1])
                url = rot3_decrypt(parts[2])
                
                # Display with formatting
                print(f"\n  Entry {index}:")
                print(f"  {'-' * 60}")
                print(f"  Username:  {username}")
                print(f"  Password:  {password}")
                print(f"  URL/Resource: {url}")
                
            except Exception as e:
                print(f"Entry {index}: [Error decrypting - {e}]")
        
        print(f"\n{'=' * 70}\n")
        input("\nPress Enter to return to main menu...")
        
    except Exception as e:
        print(f"\n✗ Error viewing credentials: {e}")





def main():
    """
    Main application loop
    Ensures credentials file exists and handles user menu interactions
    """
    # Initialize credentials file
    ensure_credentials_file_exists()
    
    # Main loop - return to menu after each action
    while True:
        try:
            display_menu()
            choice = get_user_choice()
            
            if choice == '1':
                add_credentials()
            elif choice == '2':
                view_credentials()
            elif choice == '3':
                print("\n✓ Thank you for using DigiCore Password Manager. Goodbye!")
                break
        
        except KeyboardInterrupt:
            print("\n\n✓ Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n✗ Unexpected error: {e}")


if __name__ == "__main__":
    main()
