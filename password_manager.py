#!/usr/bin/env python3
"""
DigiCore Password Manager
A secure password manager application for Apps2U
Stores and retrieves login credentials with ROT3 encryption
"""

import os
from pathlib import Path


# Configuration
CREDENTIALS_FILE = "credentials.txt"


def rot3_encrypt(text):
    """
    Encrypt text using ROT3 cipher (rotate each letter by 3 positions)
    """
    encrypted = []
    for char in text:
        if 'a' <= char <= 'z':
            # Rotate lowercase letters
            encrypted.append(chr((ord(char) - ord('a') + 3) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            # Rotate uppercase letters
            encrypted.append(chr((ord(char) - ord('A') + 3) % 26 + ord('A')))
        else:
            # Keep non-alphabetic characters unchanged
            encrypted.append(char)
    return ''.join(encrypted)


def rot3_decrypt(text):
    """
    Decrypt text using ROT3 cipher (rotate each letter back by 3 positions)
    """
    decrypted = []
    for char in text:
        if 'a' <= char <= 'z':
            # Rotate lowercase letters backwards
            decrypted.append(chr((ord(char) - ord('a') - 3) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            # Rotate uppercase letters backwards
            decrypted.append(chr((ord(char) - ord('A') - 3) % 26 + ord('A')))
        else:
            # Keep non-alphabetic characters unchanged
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
            return
        
        # Read and display credentials
        with open(CREDENTIALS_FILE, 'r') as file:
            credentials = file.readlines()
        
        if not credentials:
            print("No credentials stored yet.")
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
        
    except Exception as e:
        print(f"\n✗ Error viewing credentials: {e}")


def display_menu():
    """
    Display the main options menu
    """
    print("\n" + "=" * 50)
    print("DIGCORE PASSWORD MANAGER")
    print("=" * 50)
    print("\nOptions:")
    print("  1. Add stored credentials")
    print("  2. View stored credentials")
    print("  3. Exit")
    print("=" * 50)


def get_user_choice():
    """
    Get and validate user menu choice
    """
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice in ['1', '2', '3']:
            return choice
        print("✗ Invalid choice. Please enter 1, 2, or 3.")


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
