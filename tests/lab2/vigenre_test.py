import unittest
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere


class TestVigenereCipher(unittest.TestCase):
    def test_encrypt_one(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), "PYTHON")

    def test_encrypt_two(self):
        self.assertEqual(encrypt_vigenere("python", "a"), "python")

    def test_encrypt_three(self):
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")

    def test_decrypt_one(self):
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), "PYTHON")

    def test_decrypt_two(self):
        self.assertEqual(decrypt_vigenere("python", "a"), "python")

    def test_decrypt_three(self):
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")


if __name__ == "__main__":
    unittest.main()
