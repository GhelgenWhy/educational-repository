"""unit tests."""

import io
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, "src")

from word_counter import EmptyTextError, count_words, main  # noqa: E402


class CountWordsTests(unittest.TestCase):
    """Тести функції count_words."""

    def test_simple_sentence(self) -> None:
        """simple sentence"""
        self.assertEqual(count_words("Hello world"), 2)

    def test_single_word(self) -> None:
        """single word"""
        self.assertEqual(count_words("Python"), 1)

    def test_ukrainian_text(self) -> None:
        """ukrainian text"""
        self.assertEqual(count_words("Привіт як справи"), 3)

    def test_multiple_spaces(self) -> None:
        """multiple spaces"""
        self.assertEqual(count_words("one   two    three"), 3)

    def test_punctuation(self) -> None:
        """punctuation"""
        self.assertEqual(count_words("Hello, world! How are you?"), 5)

    def test_newlines_and_tabs(self) -> None:
        """newlines and tabs"""
        self.assertEqual(count_words("first\nsecond\tthird"), 3)

    def test_numbers_count_as_words(self) -> None:
        """numbers count as words"""
        self.assertEqual(count_words("test 123 abc"), 3)

    def test_apostrophes(self) -> None:
        """apostrophes"""
        self.assertEqual(count_words("don't can't won't"), 3)

    def test_leading_trailing_spaces(self) -> None:
        """leading and trailing spaces"""
        self.assertEqual(count_words("   hello world   "), 2)

    def test_empty_string_raises(self) -> None:
        """empty string"""
        with self.assertRaises(EmptyTextError):
            count_words("")

    def test_whitespace_only_raises(self) -> None:
        """whitespace only"""
        with self.assertRaises(EmptyTextError):
            count_words("   \n\t  ")

    def test_non_string_raises_type_error(self) -> None:
        """non string"""
        with self.assertRaises(TypeError):
            count_words(None)  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            count_words(123)  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            count_words(["a", "b"])  # type: ignore[arg-type]

    def test_punctuation_only_raises(self) -> None:
        """punctuation only"""
        self.assertEqual(count_words("hello !!! world"), 2)

    def test_long_text(self) -> None:
        """long text"""
        text = " ".join(["word"] * 1000)
        self.assertEqual(count_words(text), 1000)


class MainCliTests(unittest.TestCase):
    """cli tests."""

    def test_main_outputs_count(self) -> None:
        """main outputs count"""
        fake_stdin = io.StringIO("hello world\nfoo bar\n\n")
        captured = io.StringIO()
        with patch("sys.stdin", fake_stdin), patch("sys.stdout", captured):
            main()
        self.assertIn("Amount of words: 4", captured.getvalue())

    def test_main_raises_on_empty(self) -> None:
        """main raises on empty"""
        fake_stdin = io.StringIO("\n")
        captured = io.StringIO()
        with patch("sys.stdin", fake_stdin), patch("sys.stdout", captured):
            with self.assertRaises(EmptyTextError):
                main()


if __name__ == "__main__":
    unittest.main()
