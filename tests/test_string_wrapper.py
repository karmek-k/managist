from unittest import TestCase

from managist.string_wrapper import StringWrapper, WRAP_THRESHOLD


class StringWrapperTests(TestCase):
    def setUp(self) -> None:
        self.wrapper = StringWrapper(4)
        self.long_wrapper = StringWrapper()
        self.short_wrapper = StringWrapper(1)

    def test_wrapping_strings(self) -> None:
        self.assertEqual(
            self.wrapper.wrap('aaaaaaaaaaaaaaaaa'),
            'aaaa\naaaa\naaaa\naaaa\na'
        )
        self.assertEqual(self.wrapper.wrap('aaaaa'), 'aaaa\na')
        self.assertEqual(self.wrapper.wrap('aaaa'), 'aaaa')
        self.assertEqual(self.wrapper.wrap('a'), 'a')
        self.assertEqual(self.wrapper.wrap(''), '')

    def test_wrapping_long_strings(self) -> None:
        self.assertEqual(
            self.long_wrapper.wrap('a' * WRAP_THRESHOLD),
            'a' * WRAP_THRESHOLD
        )
        self.assertEqual(
            self.long_wrapper.wrap('a' * (WRAP_THRESHOLD + 1)),
            'a' * (WRAP_THRESHOLD) + '\na' 
        )
    
    def test_wrapping_short_strings(self) -> None:
        self.assertEqual(
            self.short_wrapper.wrap('aaaaa'),
            'a\na\na\na\na'
        )
        self.assertEqual(
            self.short_wrapper.wrap('a'),
            'a'
        )
        self.assertEqual(
            self.short_wrapper.wrap(''),
            ''
        )
