from __future__ import annotations

import re
from typing import Optional, Iterable, List, Type


class StringArt:

    @staticmethod
    def triangle(char: str, size: int) -> None:
        if size == 0:
            return

        StringArt.triangle(char, size - 1)
        print(char * size)

    @staticmethod
    def triangle_backwards(char: str, size: int) -> None:
        if size == 0:
            return

        print(char * size)
        StringArt.triangle_backwards(char, size - 1)


class StringCheck:

    @staticmethod
    def array_in_string(check: str, compare_strings: Iterable[str]) -> bool:
        for string in compare_strings:
            if string in check:
                return True
        return False

    @staticmethod
    def is_ascii(string) -> bool:
        """ prec: s is a string
            postc: returns true if all characters in the string are ascii values,
                false otherwise"""
        return all(ord(c) < 128 for c in string)

    @staticmethod
    def string_ends_with_array(check: str, ends_with_checks: Iterable[str]) -> bool:
        for string in ends_with_checks:
            if check.lower().strip().endswith(string.lower()):
                return True
        return False


class StringConvert:

    @staticmethod
    # Mostly used for database stuff
    def normalize(string: str) -> str:
        return StringConvert.only_alpha(string.replace(' ', '_')).lower()

    @staticmethod
    def only_alpha(string: str, plus_space: Optional[bool] = False) -> str:
        if plus_space:
            regex: str = r'([^\s\w]|_)+'
        else:
            regex = r'\W+'

        return re.sub(regex, '', string)

    @staticmethod
    def only_alphabetical(string: str, plus_space: Optional[bool] = False) -> str:
        if plus_space:
            regex: str = r'[^a-zA-Z ]+'
        else:
            regex = r'[^A-Za-z]'

        return re.sub(regex, '', string)

    @staticmethod
    def only_ascii(string: str) -> str:
        return ''.join([i if ord(i) < 128 else ' ' for i in string])

    @staticmethod
    def only_numeric(string: str, keep_decimal_point: bool = False) -> str:
        if keep_decimal_point:
            return re.sub('[^.0-9]', '', string)

        return re.sub('[^0-9]', '', string)

    @staticmethod
    # Mostly used for database stuff
    def regularize(string: str) -> str:
        return string.replace('_', ' ').title().replace('Url', 'URL')

    @staticmethod
    def remove_whitespace(string: str) -> str:
        return ''.join(string.split())

    @staticmethod
    def replace_non_ascii(string: str, replacement: str = ' ', with_space: bool = True) -> str:
        if with_space:
            regex: str = '[^0-9a-zA-Z ]+'
        else:
            regex = '[^0-9a-zA-Z]+'

        return re.sub(re.compile(regex, re.I), replacement, string)

    @staticmethod
    def replace_null(string: Optional[str]) -> str:
        if not string:
            return ''

        return string.strip()

    @staticmethod
    def replace_whitespace(string: str, replacement: str = ' ') -> str:
        return re.sub(r'\s+', replacement, string).strip()

    @staticmethod
    def strip_or_none(string: Optional[str]) -> Optional[str]:
        if string is not None:
            return string.strip()

        return None


class StringSize:

    @staticmethod
    def count_substring(string: str, search: str) -> int:
        return string.count(search)

    @staticmethod
    def largest_word(string: str) -> str:
        """ precondition:  string is a string
            postcondition: returns the the longest word in x (do not worry about punctuation)"""
        split_string: List[str] = string.split(' ')

        largest_word: str = split_string[0]
        for string in split_string[1:]:
            if len(string) > len(largest_word):
                largest_word = string

        return largest_word

    @staticmethod
    def largest_word_size(string: str) -> int:
        """ precondition:  string is a string
            postcondition: returns the length of the longest word in x
                (do not worry about punctuation)"""
        return len(StringSize.largest_word(string))


class StringSpecials:

    @staticmethod
    def half_of_alphabet(string: str) -> str:
        """ prec:  x is an alpha string
            postc:  returns "in the first half" if x is in the first half of the
                    alphabet; otherwise "in the second half" """
        # whole expression is one of two terms - first half or second half
        # depending on string x
        return "in the first half" if string.lower() < "m" else "in the second half"

    @staticmethod
    def last_char(string: str) -> str:
        """ prec: x is a string
            postc: returns the last character of the string."""
        return string[-1]  # method stub or function stub

    @staticmethod
    def last_non_whitespace_char(string: str) -> str:
        """ prec: x is a string
            postc: returns the last non-whitespace character"""
        string = string.rstrip()
        return string[-1]  # method stub or function stub

    @staticmethod
    def vowel_mole(string: str) -> str:
        """ prec: x is a string
            postc: returns a string with all all vowels (except y) in order in
                    the string.  Case must be preserved."""
        vowels: List[str] = ['a', 'e', 'i', 'o', 'u']
        string = [char for char in string if char in vowels]
        return "".join(string)


class StringTools:
    art: Type[StringArt] = StringArt
    check: Type[StringCheck] = StringCheck
    convert: Type[StringConvert] = StringConvert
    size: Type[StringSize] = StringSize
    special: Type[StringSpecials] = StringSpecials

    @staticmethod
    def join(strings: List[str], param: Optional[str] = '\n'):
        return param.join(strings)


class StringWrapperCheck:
    _wrapper: StringWrapper

    def __init__(self, wrapper: StringWrapper):
        self._wrapper = wrapper

    def array_in_string(self, compare_strings: Iterable[str]) -> bool:
        return StringCheck.array_in_string(self.string(), compare_strings)

    def is_ascii(self) -> bool:
        return StringCheck.is_ascii(self.string())

    def string_ends_with_array(self, ends_with_checks: Iterable[str]) -> bool:
        return StringCheck.string_ends_with_array(self.string(), ends_with_checks)

    def string(self) -> str:
        return self._wrapper.string


class StringWrapperConvert:
    _wrapper: StringWrapper

    def __init__(self, wrapper: StringWrapper):
        self._wrapper = wrapper

    def normalize(self) -> StringWrapper:
        return StringWrapper(StringConvert.normalize(self.string()))

    def only_alpha(self, plus_space: Optional[bool] = False) -> StringWrapper:
        return StringWrapper(StringConvert.only_alpha(self.string(), plus_space=plus_space))

    def only_alphabetical(self, plus_space: Optional[bool] = False) -> StringWrapper:
        return StringWrapper(StringConvert.only_alphabetical(self.string(), plus_space=plus_space))

    def only_ascii(self) -> StringWrapper:
        return StringWrapper(StringConvert.only_ascii(self.string()))

    def only_numeric(self, keep_decimal_point: bool = False) -> StringWrapper:
        return StringWrapper(StringConvert.only_numeric(self.string(),
                                                        keep_decimal_point=keep_decimal_point))

    def regularize(self) -> StringWrapper:
        return StringWrapper(StringConvert.regularize(self.string()))

    def remove_whitespace(self) -> StringWrapper:
        return StringWrapper(StringConvert.remove_whitespace(self.string()))

    def replace_non_ascii(self, replacement: str = ' ', with_space: bool = True) -> StringWrapper:
        return StringWrapper(StringConvert.replace_non_ascii(self.string(),
                                                             replacement=replacement,
                                                             with_space=with_space))

    def replace_null(self) -> StringWrapper:
        return StringWrapper(StringConvert.replace_null(self.string()))

    def replace_whitespace(self, replacement: str = ' ') -> StringWrapper:
        return StringWrapper(StringConvert.replace_whitespace(self.string(),
                                                              replacement=replacement))

    def string(self) -> str:
        return self._wrapper.string


class StringWrapperSize:
    _wrapper: StringWrapper

    def __init__(self, wrapper: StringWrapper):
        self._wrapper = wrapper

    def count_substring(self, search: str) -> int:
        return StringSize.count_substring(self.string(), search)

    def largest_word(self) -> str:
        return StringSize.largest_word(self.string())

    def largest_word_size(self) -> int:
        return StringSize.largest_word_size(self.string())

    def string(self) -> str:
        return self._wrapper.string


class StringWrapper:
    string: str

    check: StringWrapperCheck
    convert: StringWrapperConvert
    size: StringWrapperSize

    def __init__(self, string: str):
        self.string = string

        self.check = StringWrapperCheck(self)
        self.convert = StringWrapperConvert(self)
        self.size = StringWrapperSize(self)
