import unittest
from src.lab2.caesar import encrypt_caesar, decrypt_caesar


class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_one(self):
        self.assertEqual(encrypt_caesar("PYTHON"), "SBWKRQ")

    def test_encrypt_two(self):
        self.assertEqual(encrypt_caesar("python"), "sbwkrq")

    def test_encrypt_three(self):
        self.assertEqual(encrypt_caesar("Python3.6"), "Sbwkrq3.6")

    def test_encrypt_empty(self):
        self.assertEqual(encrypt_caesar(""), "")

    def test_decrypt_one(self):
        self.assertEqual(decrypt_caesar("SBWKRQ"), "PYTHON")

    def test_decrypt_two(self):
        self.assertEqual(decrypt_caesar("sbwkrq"), "python")

    def test_decrypt_three(self):
        self.assertEqual(decrypt_caesar("Sbwkrq3.6"), "Python3.6")

    def test_decrypt_empty(self):
        self.assertEqual(decrypt_caesar(""), "")


if __name__ == "__main__":
    unittest.main()
