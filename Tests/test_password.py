def test_sanity():
    assert True == True, "Sanity check failed - True is not True"


def test_encrypt_decrypt():
    from cryptonius import rot3_encrypt, rot3_decrypt

    original = "HelloWorld123!@#"
    encrypted = rot3_encrypt(original)
    decrypted = rot3_decrypt(encrypted)

    assert (
        original == decrypted
    ), f"Decryption failed: expected '{original}', got '{decrypted}'"


def test_encrypt_decrypt_emojis():
    from cryptonius import rot3_encrypt, rot3_decrypt

    original = "😊😁😎🤳✔"
    encrypted = rot3_encrypt(original)
    decrypted = rot3_decrypt(encrypted)

    assert (
        original == decrypted
    ), f"Decryption failed: expected '{original}', got '{decrypted}'"


def test_non_ascii_characters():
    from cryptonius import rot3_encrypt, rot3_decrypt

    original = "こんにちは世界"  # "Hello World" in Japanese
    encrypted = rot3_encrypt(original)
    decrypted = rot3_decrypt(encrypted)

    assert (
        original == decrypted
    ), f"Decryption failed: expected '{original}', got '{decrypted}'"


def test_saving_and_viewing_credentials():
    from Passy_Master import (
        ensure_credentials_file_exists,
        add_credentials,
        view_credentials,
    )
    import os

    # Ensure credentials file exists
    ensure_credentials_file_exists()

    # Add test credentials
    test_username = "😁😎😎"
    test_password = "testpass123"
    test_url = "http://example.com"

    # Simulate user input for adding credentials
    inputs = iter([test_username, test_password, test_url])
    original_input = __builtins__.input
    __builtins__.input = lambda _: next(inputs)

    try:
        add_credentials()
        # Now view credentials to check if they were saved correctly
        view_credentials()
        # Note: This test is basic and relies on visual confirmation of output.
        # In a real unit test, we would want to capture the output and assert on it.
    finally:
        __builtins__.input = original_input
        # Clean up the credentials file after testing
        if os.path.exists("credentials.txt"):
            os.remove("credentials.txt")
