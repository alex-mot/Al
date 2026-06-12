#!/usr/bin/env python3
"""
Menu utilities for DigiCore Password Manager
"""

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
