from src.python_library.ciphers.caesar_cipher import caesar_cipher


class TestCaesarCipher:

    def test_basic_shift(self):
        assert caesar_cipher("abc", 3) == "def"
        assert caesar_cipher("xyz", 3) == "abc"

    def test_wrap_around(self):
        assert caesar_cipher("xyz", 3) == "abc"
        assert caesar_cipher("XYZ", 3) == "ABC"

    def test_mixed_case(self):
        assert caesar_cipher("AbC", 2) == "CdE"
        assert caesar_cipher("Hello, World!", 3) == "Khoor, Zruog!"

    def test_no_shift(self):
        assert caesar_cipher("Hello, World!", 0) == "Hello, World!"

    def test_full_rotation(self):
        assert caesar_cipher("Hello, World!", 26) == "Hello, World!"
        assert caesar_cipher("abc", 26) == "abc"

    def test_non_alphabetic_characters(self):
        assert caesar_cipher("123!@#", 3) == "123!@#"
        assert caesar_cipher("Hello, World!", 3) == "Khoor, Zruog!"

    def test_negative_shift(self):
        assert caesar_cipher("def", -3) == "abc"
        assert caesar_cipher("ABC", -3) == "XYZ"