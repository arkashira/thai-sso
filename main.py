import unittest
from encryption import encrypt, decrypt

class TestEncryption(unittest.TestCase):
    def test_encrypt_decrypt(self):
        # Test that encrypting and then decrypting data results in the original data
        data = b"Hello, World!"
        encrypted_data = encrypt(data)
        decrypted_data = decrypt(encrypted_data)
        self.assertEqual(data, decrypted_data)

    def test_encrypt_empty_data(self):
        # Test that encrypting empty data results in empty encrypted data
        data = b""
        encrypted_data = encrypt(data)
        self.assertEqual(encrypted_data, b"")

    def test_decrypt_empty_data(self):
        # Test that decrypting empty encrypted data results in empty data
        encrypted_data = b""
        decrypted_data = decrypt(encrypted_data)
        self.assertEqual(decrypted_data, b"")

    def test_encrypt_large_data(self):
        # Test that encrypting large data results in correctly encrypted data
        data = b"Hello, World!" * 1000
        encrypted_data = encrypt(data)
        decrypted_data = decrypt(encrypted_data)
        self.assertEqual(data, decrypted_data)

if __name__ == '__main__':
    unittest.main()