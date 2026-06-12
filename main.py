#!/usr/bin/env python3
"""
Entry point for DigiCore Password Manager (extracted main function)
"""

from Passy_Master import (
    ensure_credentials_file_exists,
    add_credentials,
    view_credentials,
)
from menu import display_menu, get_user_choice


def main():
    """Main application loop: initialize and handle menu choices."""
    # Initialize credentials file
    ensure_credentials_file_exists()

    # Main loop - return to menu after each action
    while True:
        try:
            display_menu()
            choice = get_user_choice()

            if choice == "1":
                add_credentials()
            elif choice == "2":
                view_credentials()
            elif choice == "3":
                print("\n✓ Thank you for using Passy Master. Goodbye!")
                break

        except KeyboardInterrupt:
            print("\n\n✓ Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n✗ Unexpected error: {e}")


if __name__ == "__main__":
    main()
