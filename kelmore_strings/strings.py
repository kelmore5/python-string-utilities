from __future__ import annotations

import re
from typing import Optional, Iterable, List, Type


class StringArt:
    """A Python helper class used in :class:`StringTools <kelmore_strings.strings.StringTools>`
    that contains functions related to ascii art. Right now, the only functions include
    printing out a triangle to the console.

    Usage::

        >>> from kelmore_strings import StringTools as Strings
        >>>
        >>> Strings.art.backwards_triangle('△', 5)
        △△△△△
        △△△△
        △△△
        △△
        △

    """

    @staticmethod
    def backwards_triangle(char: str, size: int) -> None:
        """ Creates an upside triangle of given size and outputs it to Python's console

        Usage::
            >>> StringTools.art.backwards_triangle('△', 5)
            △△△△△
            △△△△
            △△△
            △△
            △

        :param char: The character that makes up the triangle
        :param size: How tall the triangle should be, in number of lines
        :return: Nothing, outputs to console

        :type char: str
        :type size: str
        :rtype: None
        """
        if size == 0:
            return

        print(char * size)
        StringArt.backwards_triangle(char, size - 1)

    @staticmethod
    def triangle(char: str, size: int) -> None:
        """ Creates a triangle of given size and outputs it to Python's console

        Usage::
            >>> StringTools.art.triangle('△', 5)
            △
            △△
            △△△
            △△△△
            △△△△△

        :param char: The character that makes up the triangle
        :param size: How tall the triangle should be, in number of lines
        :return: Nothing, outputs to console

        :type char: str
        :type size: int
        :rtype: None
        """
        if size == 0:
            return

        StringArt.triangle(char, size - 1)
        print(char * size)


# noinspection SpellCheckingInspection
class StringCheck:
    """A Python helper class used in :class:`StringTools <kelmore_strings.strings.StringTools>`
    that contains functions to perform various checks on strings, like if a string has any
    upper or lowercase letters.

    Usage::

        >>> from kelmore_strings import StringTools as Strings
        >>>
        >>> a = 'hello'
        >>> b = 'world'
        >>>
        >>> x = 'Am I ascii??'
        >>> y = 'How aьout mэ?'
        >>>
        >>> Strings.check.half_of_alphabet(a)
        >>> Strings.check.last_half_of_alphabet(b)
        >>> Strings.check.is_ascii(x)
        >>> Strings.check.is_ascii(y)
        True
        True
        True
        False

    """

    @staticmethod
    def array_in_string(check: str, compare_strings: Iterable[str]) -> bool:
        """ Checks whether a given string is contained within a given array

        Usage::
            >>> array_of_strings: Iterable[str] = ['do', 'I', 'contain', 'hello']
            >>> StringTools.check.array_in_string('hello', array_of_strings)
            True

        :param check: The string to check for
        :param compare_strings: The array to look for the string in
        :return: True if the string is inside the array else False

        :type check: str
        :type compare_strings: Iterable[str]
        :rtype: bool
        """
        for string in compare_strings:
            if string in check:
                return True

        return False

    @staticmethod
    def half_of_alphabet(string: str) -> bool:
        """ Takes a string and determines if it is within the first half of the alphabet

        Usage::

            >>> x = 'hello'
            >>> y = 'world'
            >>>
            >>> StringTools.check.half_of_alphabet(x)
            >>> StringTools.check.half_of_alphabet(y)
            True
            False

        :param string: Any string
        :return: True if the string is within the first half of the alphabet else False

        :type string: str
        :rtype: bool
        """
        return string.lower() < 'm'

    @staticmethod
    def has_numbers(string: str) -> bool:
        """ Checks if a given string contains any numbers

        Usage::

            >>> x = 'What do I owe ya?'
            >>> y = '$50 dollars'
            >>>
            >>> StringTools.check.has_numbers(x)
            >>> StringTools.check.has_numbers(y)
            True
            False

        :param string: Any string
        :return: True if the string contains any numbers else False

        :type string: str
        :rtype: bool
        """
        for char in string:
            if char.isdigit():
                return True
        return False

    @staticmethod
    def has_lowercase(string: str) -> bool:
        """ Checks if a given string contains any lowercase letters

        Usage::

            >>> x = 'WHO AM I'
            >>> y = 'jeb'
            >>>
            >>> StringTools.check.has_lowercase(x)
            >>> StringTools.check.has_lowercase(y)
            True
            False

        :param string: Any string
        :return: True if the string contains any lowercase letters else False

        :type string: str
        :rtype: bool
        """
        for char in string:
            if char.islower():
                return True
        return False

    @staticmethod
    def has_uppercase(string: str) -> bool:
        """ Checks whether a given string contains any uppercase letters

        Usage::

            >>> x = "i don't like uppercase"
            >>> y = "You need to learn some grammar"
            >>>
            >>> StringTools.check.has_uppercase(x)
            >>> StringTools.check.has_uppercase(y)
            True
            False

        :param string: Any string
        :return: True if the string contains any uppercase letters else False

        :type string: str
        :rtype: bool
        """
        for char in string:
            if char.isupper():
                return True
        return False

    # noinspection SpellCheckingInspection
    @staticmethod
    def is_ascii(string: str) -> bool:
        """ Checks whether a given string contains only ascii characters. If the string has all
        ascii characters, all the characters (as integers) will be less than 128.

        Usage::

            >>> x = 'Am I ascii??'
            >>> y = 'How aьout mэ?'
            >>>
            >>> StringTools.check.is_ascii(x)
            >>> StringTools.check.is_ascii(y)
            True
            False

        :param string: Any string
        :return: True if the string contains only ascii characters else False

        :type string: str
        :rtype: bool
        """
        return all(ord(c) < 128 for c in string)

    @staticmethod
    def last_half_of_alphabet(string: str) -> bool:
        """ Takes a string and determines if it is within the last half of the alphabet

        Usage::

            >>> x = 'hello'
            >>> y = 'world'
            >>>
            >>> StringTools.check.last_half_of_alphabet(x)
            >>> StringTools.check.last_half_of_alphabet(y)
            False
            True

        :param string: Any string
        :return: True if the string is within the last half of the alphabet else False

        :type string: str
        :rtype: bool
        """
        return string.lower() >= 'm'

    @staticmethod
    def string_ends_with_array(check: str, ends_with_checks: Iterable[str]) -> bool:
        """ Checks if a given strings ends with any of the strings contained within an array

        Usage::

            >>> x = 'some string'
            >>> y: Iterable[str] = ['?', '.', 'end', 'ng']
            >>>
            >>> StringTools.check.string_ends_with_array(x, y)
            True

        :param check: Any string
        :param ends_with_checks: An array of strings to check for in the passed string
        :return: True if the string ends with any of the strings in ends_with_checks else False

        :type check: str
        :type ends_with_checks: Iterable[str]
        :rtype: bool
        """
        for string in ends_with_checks:
            if check.lower().strip().endswith(string.lower()):
                return True
        return False


# noinspection SpellCheckingInspection
class StringConvert:
    """ A Python helper class used in :class:`StringTools <kelmore_strings.strings.StringTools>`
    that contains functions to help with conversions of strings, like getting only the ascii
    characters, taking out all whitespace, or removing all vowels.

    Usage::

        >>> from kelmore_strings import StringTools as Strings
        >>>
        >>> x = 'Please take out my vowels!'
        >>> y = 'I only want my money, $19.99'
        >>> z = "     There's too many      spaces.   "
        >>>
        >>> Strings.convert.consonants(x)
        >>> Strings.convert.only_numeric(y, keep_decimal_point=True)
        >>> Strings.convert.replace_whitespace(z, replacement=' ')
        'Plstktmvwls'
        '19.99'
        "There's too many spaces."

    """

    @staticmethod
    def consonants(string: str) -> str:
        """ Takes a string and returns all the consonants inside of it without vowels

        Usage::

            >>> x = 'Please take out my vowels!'
            >>> StringTools.convert.consonants(x)
            'Plstktmvwls'

        :param string: Any string
        :return: The given string with only consonants

        :type string: str
        :rtype: str
        """
        vowels: List[str] = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

        split_string: List[str] = [char for char in string if char not in vowels]
        string = ''.join(split_string)

        return StringConvert.only_alphabetical(string)

    @staticmethod
    def normalize(string: str) -> str:
        """ Takes a string and returns it in all lowercase with its spaces replaced with
        underscores. Mostly used for dictionaries and database fields

        Usage::

            >>> StringTools.convert.normalize('Some Database Field')
            'some_database_field'

        :param string: Any string
        :return: The given string with spaces replaced with underscores and changed to lowercase

        :type string: str
        :rtype: str
        """
        return StringConvert.only_word_characters(string.replace(' ', '_')).lower()

    @staticmethod
    def only_alphabetical(string: str, plus_space: Optional[bool] = False) -> str:
        """ Takes a string and removes all characters except alphabetical ones.
            The returned string will only have A-Z, a-z, and optionally, spaces ( ).

        Usage::

            >>> x = "There's too many numbers here 4594102"
            >>> StringTools.convert.only_alphabetical(x, plus_space=True)
            'Theres too many numbers here '

        :param string: Any string
        :param plus_space: True if the output should include spaces else False
        :return: The given string with all non-alphabetical characters removed

        :type string: str
        :type plus_space: Optional[bool]
        :rtype: str
        """
        if plus_space:
            regex: str = r'[^a-zA-Z ]+'
        else:
            regex = r'[^A-Za-z]'

        return re.sub(regex, '', string)

    @staticmethod
    def only_ascii(string: str) -> str:
        """ Takes a string and removes all non-ascii characters from it

        Usage::

            >>> x = "Ϊ cȃήʹΤ put this in Excel!"
            >>> StringTools.convert.only_ascii(x)
            ' put this in Excel!'

        :param string: Any string
        :return: The given string stripped of all non-ascii characters

        :type: string: str
        :rtype: str
        """
        return ''.join([i if ord(i) < 128 else ' ' for i in string])

    @staticmethod
    def only_numeric(string: str, keep_decimal_point: Optional[bool] = False) -> str:
        """ Takes a string and removes all characters except numerical ones. You can
        optionally include the decimal point as well.

        Usage::

            >>> x = 'I only want my money, $19.99'
            >>> StringTools.convert.only_numeric(x, keep_decimal_point=True)
            '19.99'

        :param string: Any string
        :param keep_decimal_point: True if the output string should have decimal points else False
        :return: The given string with all characters stripped except numerical ones

        :type string: str
        :type keep_decimal_point: Optional[bool]
        :rtype: str
        """
        if keep_decimal_point:
            return re.sub('[^.0-9]', '', string)

        return re.sub('[^0-9]', '', string)

    @staticmethod
    def only_word_characters(string: str,
                             include_space: Optional[bool] = False,
                             include_underscore: Optional[bool] = True) -> str:
        """ Takes a string and returns it with only word characters. Word characters are
        A-Z, a-z, 0-9, and underscore (_). In other words, this function removes things like
        commas (,), apostrophes ('), periods (.), etc from a string.

        You can optionally choose to include spaces and remove underscores, if desired

        Usage::

            >>> x = "I don't want all these characters!"
            >>> StringTools.convert.only_word_characters(x, include_space=True)
            'I dont want all these characters'

        :param string: Any string
        :param include_space: True if output should include spaces ( ) else False
        :param include_underscore: True if output should include underscore (_) else False
        :return: The given string with all non-word characters removed

        :type string: str
        :type include_space: Optional[bool]
        :type include_underscore: Optional[bool]
        :rtype: str
        """
        if include_space and include_underscore:
            regex: str = r'[^\s\w]+'
        elif include_space:
            regex = r'([^\s\w]|_)+'
        elif include_underscore:
            regex = r'[^\w]+'
        else:
            regex = r'([^\w]|_)+'

        return re.sub(regex, '', string)

    @staticmethod
    def regularize(string: str) -> str:
        """ Takes a string in all lowercase and separated by underscores and returns the string
        with spaces, titled. This is mostly used to "undo" dictionary keys and database fields.

        Usage::

            >>> x = 'some_database_field'
            >>> StringTools.convert.regularize(x)
            'Some Database Field'

        :param string: A lowercase string separated by underscores
        :return: The string with its underscores replaced by spaces and titled

        :type string: str
        :rtype: str
        """
        return string.replace('_', ' ').title().replace('Url', 'URL')

    @staticmethod
    def remove_whitespace(string: str) -> str:
        """ Removes all whitespace from a string

        Usage::

            >>> x = 'I hate whitespace.'
            >>> StringTools.convert.remove_whitespace(x)
            'Ihatewhitespace.'

        :param string: Any string
        :return: The string without any whitespace

        :type string: str
        :rtype: str
        """
        return ''.join(string.split())

    @staticmethod
    def replace_non_ascii(string: str,
                          replacement: str = ' ',
                          with_space: Optional[bool] = True) -> str:
        """ Similar to :func:`only_ascii <kelmore_strings.strings.StringConvert.only_ascii>`,
        takes a string and replaces all non-ascii characters with a given replacement string.
        You can optionally include or remove spaces as well.

        Usage::

            >>> x = "Thϝs doesn't lϼϼk rϝght"
            >>> StringTools.convert.replace_non_ascii(x, replacement='|', with_space=True)
            "Th|s doesn't l||k r|ght'

        :param string: Any string
        :param replacement: A string to replace non-ascii characters with
        :param with_space: True if the output string should include spaces ( ) else False
        :return: The given string with all non-ascii characters replaced with replacement

        :type string: str
        :type replacement: str
        :type with_space: Optional[bool]
        :rtype: str
        """
        if with_space:
            regex: str = '[^0-9a-zA-Z ]+'
        else:
            regex = '[^0-9a-zA-Z]+'

        return re.sub(re.compile(regex, re.I), replacement, string)

    @staticmethod
    def replace_null(string: Optional[str]) -> str:
        """ Takes a string or None and returns a string. Used to force the None type into a string
        when the type of a string is unknown.

        Usage::

            >>> StringTools.convert.replace_null(None)
            ''

        :param string: Any string or None
        :return: The given string or '' if the string is None

        :type string: str
        :rtype: str
        """
        if not string:
            return ''

        return string.strip()

    @staticmethod
    def replace_whitespace(string: str, replacement: str = ' ') -> str:
        """ Similar to :func:`only_ascii <kelmore_strings.strings.StringConvert.remove_whitespace>`,
        replaces any whitespace within a given string with a replacement one. This is helpful
        when you have a string with a variable number of spaces within it.

        Usage::

            >>> x = "     There's too many      spaces.   "
            >>> StringTools.convert.replace_whitespace(x, replacement=' ')
            "There's too many spaces."

        :param string: Any string with extraneous whitespace
        :param replacement: The string to replace any whitespace with
        :return: The given string with all whitespace replaced with replacement

        :type string: str
        :type replacement: str
        :rtype: str
        """
        return re.sub(r'\s+', replacement, string).strip()

    @staticmethod
    def strip_or_none(string: Optional[str]) -> Optional[str]:
        """ Takes in a string or None and returns None if the given string is None. Otherwise,
        it returns the string with it's extraneous whitespace stripped.

        Usage::

            >>> StringTools.convert.strip_or_none('  Get rid of whitespace please  ')
            >>> StringTools.convert.strip_or_none(None)
            'Get rid of whitespace please'
            None

        :param string: Any string or None
        :return: The given string, stripped, or None if the string is None

        :type string: Optional[str]
        :rtype: Optional[str]
        """
        if string is not None:
            return string.strip()

        return None

    @staticmethod
    def unique(string: str) -> str:
        """ Takes a string and returns all the unique characters within it.

        Usage::

            >>> x = 'I need uniqueness!'
            >>> StringTools.convert.unique(x)
            'I neduiqs!'

        :param string: Any string
        :return: The given string with only its unique character set

        :type string: str
        :rtype: str
        """
        return ''.join(set(string))

    @staticmethod
    def vowels(string: str) -> str:
        """ Takes a string and returns all the vowels inside of it

        Usage::

            >>> x = 'Please take out my consonants!'
            >>> StringTools.convert.vowels(x)
            'eaeaeouyooa'

        :param string: Any string
        :return: The given string with only vowels

        :type string: str
        :rtype: str
        """
        vowels: List[str] = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

        split_string: List[str] = [char for char in string if char in vowels]
        return ''.join(split_string)


# noinspection SpellCheckingInspection
class StringSize:
    """A Python helper class used in :class:`StringTools <kelmore_strings.strings.StringTools>`
    that contains functions that relate to string sizes, including finding the largest word and
    counting the substrings within a string

    Usage::

        >>> from kelmore_strings import StringTools as Strings
        >>>
        >>> x = 'How many times do I, will I, can I, say...I?'
        >>> y = "What's the longest word within this question?"
        >>> z = "What's the size of the longest word within this question?"
        >>>
        >>> Strings.size.count_substring(x, 'I')
        >>> Strings.size.largest_word(x)
        >>> Strings.size.largest_word_size(x)
        4
        'question'
        8

    """

    @staticmethod
    def count_substring(string: str, search: str) -> int:
        """ Counts all the instances of search within the given string

        Usage::

            >>> x = 'How many times do I, will I, can I, say...I?'
            >>> StringTools.size.count_substring(x, 'I')
            4

        :param string: Any string
        :param search: The string to search for within string
        :return: The number of times the search appears within the given string

        :type string: str
        :type search: str
        :rtype: int
        """
        return string.count(search)

    @staticmethod
    def largest_word(string: str) -> str:
        """ Finds the largest word within a given string. This will only check against word
        characters, so things like commas, apostrophes, and question marks are ignored.

        Usage::

            >>> x = "What's the longest word within this question?"
            >>> StringTools.size.largest_word(x)
            'question'

        :param string: Any string
        :return: The largest word within the given string

        :type string: str
        :rtype: str
        """
        split_string: List[str] = string.split(' ')

        largest_word: str = split_string[0]
        for string in split_string[1:]:
            string = StringConvert.only_word_characters(string, include_underscore=False)
            if len(string) > len(largest_word):
                largest_word = string

        return largest_word

    @staticmethod
    def largest_word_size(string: str) -> int:
        """ Finds the size of the largest word within a given string.  This will only check
        against word characters, so things like commas, apostrophes, and question marks are
        ignored.

        Usage::

            >>> x = "What's the size of the longest word within this question?"
            >>> StringTools.size.largest_word_size(x)
            8

        :param string: Any string
        :return: The length of the largest word within the given string

        :type string: str
        :rtype: int
        """
        return len(StringSize.largest_word(string))


class StringSpecials:
    """A Python helper class used in :class:`StringTools <kelmore_strings.strings.StringTools>`
    that holds all extraneous utility functions for strings in Python. Right now, the only
    function is finding the last character within a string

    Usage::

        >>> from kelmore_strings import StringTools as Strings
        >>>
        >>> Strings.special.last_char('hello world')
        >>> Strings.special.last_char('   hello world   ', ignore_whitespace=True)
        'd'
        'd'

    """

    @staticmethod
    def last_char(string: str, ignore_whitespace: Optional[bool] = False) -> str:
        """ Finds the last character within a string

        Usage::

            >>> StringTools.special.last_char('hello world')
            >>> StringTools.special.last_char('   hello world   ', ignore_whitespace=True)
            'd'
            'd'

        :param string: Any string
        :param ignore_whitespace: True if whitespace should be ignored else False
        :return: The last character in the string

        :type string: str
        :type ignore_whitespace: Optional[bool]
        :rtype: str
        """
        if ignore_whitespace:
            string = string.strip()

        return string[-1]


class StringTools:
    """ A Python class to hold various utility tools to help deal with strings in Python

    There's five sections to StringTools: Art, Check, Convert, Size, and Special. Each helper
    class contains their own tools for strings. In order, they are:

    :class:`Art <kelmore_strings.strings.StringArt>`
        Contains functions to create ascii art

    :class:`Check <kelmore_strings.strings.StringCheck>`
        Contains function to perform checks on strings, like seeing if a string only contains
        upper or lowercase letters

    :class:`Convert <kelmore_strings.strings.StringConvert>`
        Contains functions to convert strings. For example, removing all non-ascii characters,
        removing all whitespace, or finding all the unique characters within a string

    :class:`Size <kelmore_strings.strings.StringSize>`
        Contains functions to determine different things relating to a string's size, like finding
        the largest word or counting the number of substrings within a string

    :class:`Special <kelmore_strings.strings.StringSpecial>`
        This class is for any extraneous function that doesn't fit within the four other classes.
        Right now, the only function inside of it is one to get the last character of a string.

    Usage::

        >>> from kelmore_strings import StringTools as Strings
        >>>
        >>> x = 'AM I YELLING?!'
        >>> y = 'I need this to be ascii!'
        >>> z = "What's my largest word?"
        >>>
        >>> Strings.check.has_uppercase(x)
        >>> Strings.convert.only_ascii(y)
        >>> Strings.size.largest_word(z)
        True
        'I need this to be ascii!'
        'largest'

    """
    art: Type[StringArt] = StringArt
    """Contains functions for ascii art"""
    check: Type[StringCheck] = StringCheck
    """Contains functions for performing checks on strings"""
    convert: Type[StringConvert] = StringConvert
    """Contains functions for converting strings"""
    size: Type[StringSize] = StringSize
    """Contains functions related to string size"""
    special: Type[StringSpecials] = StringSpecials
    """Contains extraneous string utility functions"""

    @staticmethod
    def join(strings: List[str], param: Optional[str] = '\n'):
        return param.join(strings)


# noinspection SpellCheckingInspection
class StringCheckWrapper:
    """A Python helper/wrapper class
    used in :class:`StringTools <kelmore_strings.strings.StringWrapper>`
    that contains functions to perform various checks on the internal string.
    This includes things like if a string has any upper or lowercase letters.

    Usage::

        >>> from kelmore_strings import StringWrapper
        >>>
        >>> wrapper_a = StringWrapper('hello')
        >>> wrapper_b = StringWrapper('world')
        >>>
        >>> wrapper_x = StringWrapper('Am I ascii??')
        >>> wrapper_y = StringWrapper('How aьout mэ?')
        >>>
        >>> wrapper_a.check.half_of_alphabet()
        >>> wrapper_b.check.last_half_of_alphabet()
        >>> wrapper_x.check.is_ascii()
        >>> wrapper_y.check.is_ascii()
        True
        True
        True
        False

    """
    _wrapper: StringWrapper

    def __init__(self, wrapper: StringWrapper):
        self._wrapper = wrapper

    def array_in_string(self, compare_strings: Iterable[str]) -> bool:
        """ Checks whether the internal string is contained within a given array

        Usage::
            >>> wrapper = StringWrapper('hello')
            >>> array_of_strings: Iterable[str] = ['do', 'I', 'contain', 'hello']
            >>>
            >>> wrapper.check.array_in_string(array_of_strings)
            True

        :param compare_strings: The array to look for the internal string in
        :return: True if the internal string is inside the array else False

        :type compare_strings: Iterable[str]
        :rtype: bool
        """
        return StringCheck.array_in_string(self.string(), compare_strings)

    def half_of_alphabet(self) -> bool:
        """ Determines if the internal string is within the first half of the alphabet

        Usage::

            >>> wrapper_x = StringWrapper('hello')
            >>> wrapper_y = StringWrapper('world')
            >>>
            >>> wrapper_x.check.half_of_alphabet()
            >>> wrapper_y.check.half_of_alphabet()
            True
            False

        :return: True if the internal string is within the first half of the alphabet else False
        :rtype: bool
        """
        return StringTools.check.half_of_alphabet(self.string())

    def has_numbers(self) -> bool:
        """ Checks if the internal string has any numbers inside of it

        Usage::

            >>> wrapper = StringWrapper('$50 dollars')
            >>> wrapper.check.has_numbers()
            True

        :return: True if the internal string has any numbers else False
        :rtype: bool
        """
        return StringTools.check.has_numbers(self.string())

    def has_lowercase(self) -> bool:
        """ Checks if the internal string contains any lowercase letters

        Usage::

            >>> wrapper = StringWrapper('Hello World')
            >>> wrapper.check.has_lowercase()
            True

        :return: True if the internal string has any lowercase letters else False
        :rtype: bool
        """
        return StringTools.check.has_lowercase(self.string())

    def has_uppercase(self) -> bool:
        """ Checks whether the internal string contains any uppercase letters

        Usage::

            >>> wrapper = StringWrapper('Hello World')
            >>> wrapper.check.has_uppercase()
            True

        :return: True if the internal string contains any uppercase letters else False
        :rtype: bool
        """
        return StringTools.check.has_uppercase(self.string())

    def is_ascii(self) -> bool:
        """ Checks whether the internal string string contains only ascii characters. If the
        string has all ascii characters, all the characters (as integers) will be less than 128.

        Usage::

            >>> wrapper_x = StringWrapper('Am I ascii??')
            >>> wrapper_y = StringWrapper('How aьout mэ?')
            >>>
            >>> wrapper_x.check.is_ascii()
            >>> wrapper_y.check.is_ascii()
            True
            False

        :return: True if the internal string contains only ascii characters else False
        :rtype: bool
        """
        return StringCheck.is_ascii(self.string())

    def last_half_of_alphabet(self) -> bool:
        """ Checks if the internal string is within the last half of the alphabet

        Usage::

            >>> wrapper_x = StringWrapper('hello')
            >>> wrapper_y = StringWrapper('world')
            >>>
            >>> wrapper_x.check.last_half_of_alphabet()
            >>> wrapper_y.check.last_half_of_alphabet()
            False
            True

        :return: True if the string is within the last half of the alphabet else False
        :rtype: bool
        """
        return StringTools.check.last_half_of_alphabet(self.string())

    def string_ends_with_array(self, ends_with_checks: Iterable[str]) -> bool:
        """ Checks if the internal string ends with any of the strings contained within a given
            array

        Usage::

            >>> array_of_strings: Iterable[str] = ['?', '.', 'end', 'ng']
            >>> wrapper = StringWrapper('some string')
            >>>
            >>> wrapper.check.string_ends_with_array(array_of_strings)
            True

        :param ends_with_checks: An array of strings to check for in the internal string
        :return: True if the internal string ends with any of the strings in ends_with_checks
                else False

        :type ends_with_checks: Iterable[str]
        :rtype: bool
        """
        return StringCheck.string_ends_with_array(self.string(), ends_with_checks)

    def string(self) -> str:
        """ Used to get the string from a StringWrapperCheck wrapper

        Usage::

            >>> wrapper = StringWrapper('some string')
            >>> wrapper.check.string()
            'some string'

        :return: The string contained within the wrapper
        :rtype: str
        """
        return self._wrapper.string


# noinspection SpellCheckingInspection
class StringConvertWrapper:
    """ A Python helper/wrapper class
    used in :class:`StringTools <kelmore_strings.strings.StringWrapper>`
    that contains functions to help with converting the internal string. This includes
    getting only the ascii characters, taking out all whitespace, or removing all vowels.

    Usage::

        >>> from kelmore_strings import StringWrapper
        >>>
        >>> wrapper_x = StringWrapper('Please take out my vowels!')
        >>> wrapper_y = StringWrapper('I only want my money, $19.99')
        >>> wrapper_z = StringWrapper("     There's too many      spaces.   ")
        >>>
        >>> wrapper_x.convert.consonants()
        >>> wrapper_y.convert.only_numeric(keep_decimal_point=True)
        >>> wrapper_z.convert.replace_whitespace(replacement=' ')
        'Plstktmvwls'
        StringWrapper('19.99')
        StringWrapper("There's too many spaces.")

    """
    _wrapper: StringWrapper

    def __init__(self, wrapper: StringWrapper):
        self._wrapper = wrapper

    def consonants(self) -> str:
        """ Takes the internal string, removes all its vowels, and returns it transformed to
        only consonants

        Usage::

            >>> wrapper = StringWrapper('Please take out my vowels!')
            >>> wrapper.convert.consonants()
            StringWrapper('Plstktmvwls')

        :return: The current internal string, transformed to only consonants
        :rtype: str
        """
        return StringTools.convert.consonants(self.string())

    def normalize(self) -> StringWrapper:
        """ Takes the internal string and returns it in all lowercase with its spaces replaced with
        underscores. Mostly used for dictionaries and database fields

        Usage::

            >>> wrapper = StringWrapper('Some Database Field')
            >>> wrapper.convert.normalize()
            StringWrapper('some_database_field')

        :return: A new StringWrapper containing the current internal string with its spaces
            replaced with underscores and changed to lowercase
        :rtype: StringWrapper
        """
        return StringWrapper(StringConvert.normalize(self.string()))

    def only_alphabetical(self, plus_space: Optional[bool] = False) -> StringWrapper:
        """ Takes the internal string and removes all characters except alphabetical ones.
        The returned string will only have A-Z, a-z, and optionally, spaces ( ).

        Usage::

            >>> wrapper = StringWrapper("There's too many numbers here 4594102")
            >>> wrapper.convert.only_alphabetical(plus_space=True)
            StringWrapper('Theres too many numbers here ')

        :param plus_space: True if the output should include spaces else False
        :return: A new StringWrapper containing the current internal string with all
            non-alphabetical characters removed

        :type plus_space: Optional[bool]
        :rtype: StringWrapper
        """
        return StringWrapper(StringConvert.only_alphabetical(self.string(), plus_space=plus_space))

    def only_ascii(self) -> StringWrapper:
        """ Takes the internal string and removes all non-ascii characters from it

        Usage::

            >>> wrapper = StringWrapper("Ϊ cȃήʹΤ put this in Excel!")
            >>> wrapper.convert.only_ascii()
            StringWrapper(' put this in Excel!')

        :return: A new StringWrapper containing the current internal string stripped of
            all non-ascii characters
        :type: string: StringWrapper
        """
        return StringWrapper(StringConvert.only_ascii(self.string()))

    def only_numeric(self, keep_decimal_point: bool = False) -> StringWrapper:
        """ Takes the internal string and removes all characters except numerical ones. You can
        optionally include the decimal point as well.

        Usage::

            >>> wrapper = StringWrapper('I only want my money, $19.99')
            >>> wrapper.convert.only_numeric(keep_decimal_point=True)
            StringWrapper('19.99')

        :param keep_decimal_point: True if the output string should have decimal points else False
        :return: A new StringWrapper containing the current internal string with all characters
            stripped except numerical ones

        :type keep_decimal_point: Optional[bool]
        :rtype: StringWrapper
        """
        return StringWrapper(
            StringConvert.only_numeric(self.string(), keep_decimal_point=keep_decimal_point))

    def only_word_characters(self,
                             include_space: Optional[bool] = False,
                             include_underscore: Optional[bool] = True) -> StringWrapper:
        """ Takes the internal string string and removes everything except word characters.
        Word characters are A-Z, a-z, 0-9, and underscore (_). In other words, this function
        removes things like commas (,), apostrophes ('), periods (.), etc from a string.

        You can optionally choose to include spaces and remove underscores, if desired

        Usage::

            >>> wrapper = StringWrapper("I don't want all these characters!")
            >>> wrapper.convert.only_word_characters(include_space=True)
            StringWrapper('I dont want all these characters')

        :param include_space: True if the new string should include spaces ( ) else False
        :param include_underscore: True if the new string should include underscore (_) else False
        :return: A new StringWrapper containing the current internal string with all
            non-word characters removed

        :type include_space: Optional[bool]
        :type include_underscore: Optional[bool]
        :rtype: StringWrapper
        """
        return StringWrapper(
            StringConvert.only_word_characters(self.string(),
                                               include_space=include_space,
                                               include_underscore=include_underscore))

    def regularize(self) -> StringWrapper:
        """ Takes the internal string in all lowercase and separated by underscores, replaces
        all underscores with spaces, and titles the string. This is mostly used to "undo"
        dictionary keys and database fields.

        Usage::

            >>> wrapper = StringWrapper('some_database_field')
            >>> wrapper.convert.regularize()
            StringWrapper('Some Database Field')

        :return: A new StringWrapper containing the current internal string with its underscores
            replaced by spaces and titled
        :rtype: StringWrapper
        """
        return StringWrapper(StringConvert.regularize(self.string()))

    def remove_whitespace(self) -> StringWrapper:
        """ Removes all whitespace from the internal string

        Usage::

            >>> wrapper = StringWrapper('I hate whitespace.')
            >>> wrapper.convert.remove_whitespace()
            StringWrapper('Ihatewhitespace.')

        :return: A new StringWrapper containing the current internal string without any whitespace
        :rtype: StringWrapper
        """
        return StringWrapper(StringConvert.remove_whitespace(self.string()))

    def replace_non_ascii(self, replacement: str = ' ', with_space: bool = True) -> StringWrapper:
        """ Similar to :func:`only_ascii <kelmore_strings.strings.StringConvertWrapper.only_ascii>`,
        takes the internal string and replaces all non-ascii characters with a given replacement
        string. You can optionally include or remove spaces as well.

        Usage::

            >>> wrapper = StringWrapper("Thϝs doesn't lϼϼk rϝght")
            >>> wrapper.convert.replace_non_ascii(replacement='|', with_space=True)
            StringWrapper("Th|s doesn't l||k r|ght')

        :param replacement: A string to replace non-ascii characters with
        :param with_space: True if the output string should include spaces ( ) else False
        :return: A new StringWrapper containing the current internal string with all
            non-ascii characters replaced with replacement

        :type replacement: str
        :type with_space: Optional[bool]
        :rtype: StringWrapper
        """
        return StringWrapper(StringConvert.replace_non_ascii(self.string(),
                                                             replacement=replacement,
                                                             with_space=with_space))

    def replace_null(self) -> StringWrapper:
        """ Takes the internal string and replaces it with a String object if the current
        object is None. Used to force the None type into a string when the type of the
        current string is unknown.

        Usage::

            >>> wrapper = StringWrapper(None)
            >>> wrapper.convert.replace_null()
            StringWrapper('')

        :return: A new StringWrapper with the either the current internal string
            or '' if the current string is None
        :rtype: StringWrapper
        """
        return StringWrapper(StringConvert.replace_null(self.string()))

    def replace_whitespace(self, replacement: str = ' ') -> StringWrapper:
        """ Similar to
        :func:`only_ascii <kelmore_strings.strings.StringWrapperConvert.remove_whitespace>`,
        replaces any whitespace within the internal string with a replacement one. This is helpful
        when you have a string with a variable number of spaces within it.

        Usage::

            >>> wrapper = StringWrapper("     There's too many      spaces.   ")
            >>> wrapper.convert.replace_whitespace(replacement=' ')
            StringWrapper("There's too many spaces.")

        :param replacement: The string to replace any whitespace with
        :return: A new StringWrapper containing the current internal string with all whitespace
            replaced with replacement

        :type replacement: str
        :rtype: StringWrapper
        """
        return StringWrapper(
            StringConvert.replace_whitespace(self.string(),
                                             replacement=replacement))

    def string(self) -> str:
        """A helper function to get the string inside a StringConvertWrapper wrapper

        :return: The internal string inside the wrapper
        :rtype: str
        """
        return self._wrapper.string

    def unique(self) -> StringWrapper:
        """ Takes the internal string and returns all the unique characters within it,
        as a StringWrapper.

        Usage::

            >>> wrapper = StringWrapper('I need uniqueness!')
            >>> wrapper.convert.unique()
            StringWrapper('I neduiqs!')

        :return: A new StringWrapper containing the current internal string with only its
            unique character set
        :rtype: StringWrapper
        """
        return StringWrapper(StringConvert.unique(self.string()))

    def vowels(self) -> str:
        """ Takes the internal string and returns all the vowels inside of it

        Usage::

            >>> wrapper = StringWrapper('Please take out my consonants!')
            >>> wrapper.convert.vowels()
            'eaeaeouyooa'

        :return: The current internal string, transformed to only vowels
        :rtype: str
        """
        return StringTools.convert.vowels(self.string())


class StringSizeWrapper:
    """A Python helper/wrapper class
    used in :class:`StringTools <kelmore_strings.strings.StringWrapper>`
    that contains functions relating to the size of an internal string. This includes
    things like finding  the largest word and counting substrings within the string

    Usage::

        >>> from kelmore_strings import StringWrapper
        >>>
        >>> wrapper_x = StringWrapper('How many times do I, will I, can I, say...I?')
        >>> wrapper_y = StringWrapper("What's the longest word within this question?")
        >>> wrapper_z = StringWrapper("What's the size of the longest word within this question?")
        >>>
        >>> wrapper_x.size.count_substring('I')
        >>> wrapper_y.size.largest_word()
        >>> wrapper_z.size.largest_word_size()
        4
        'question'
        9

    """
    _wrapper: StringWrapper

    def __init__(self, wrapper: StringWrapper):
        self._wrapper = wrapper

    def count_substring(self, search: str) -> int:
        """ Counts all instances of the search string within the current internal string

        Usage::

            >>> wrapper = StringWrapper('How many times do I, will I, can I, say...I?')
            >>> wrapper.size.count_substring('I')
            4

        :param search: The string to search for within the current internal string
        :return: The number of times the search appears within string

        :type search: str
        :rtype: int
        """
        return StringSize.count_substring(self.string(), search)

    def largest_word(self) -> str:
        """ Finds the largest word within a given string. This will only check against word
        characters, so things like commas, apostrophes, and question marks are ignored.

        Usage::

            >>> wrapper = StringWrapper("What's the longest word within this question?")
            >>> wrapper.size.largest_word()
            'question'

        :return: The largest word within the current internal string
        :rtype: str
        """
        return StringSize.largest_word(self.string())

    def largest_word_size(self) -> int:
        """ Finds the size of the largest word within the current internal string. This will only
        check against word characters, so things like commas, apostrophes, and question marks are
        ignored.

        Usage::

            >>> wrapper = StringWrapper("What's the size of the longest word within this question?")
            >>> wrapper.size.largest_word_size()
            8

        :return: The length of the largest word within the current internal string
        :rtype: int
        """
        return StringSize.largest_word_size(self.string())

    def string(self) -> str:
        """A helper function to get the string inside a StringSizeWrapper wrapper

        :return: The internal string inside the current wrapper
        :rtype: str
        """
        return self._wrapper.string


class StringWrapper:
    """A class that acts as a wrapper/builder for String objects in Python. If you have a String
    that needs a lot of transformations, this class helps by acting as a builder. It's designed
    for you to chain functions together and be able to execute all functions at once.

    StringWrapper is divided into three main internal classes:

    :class:`Check <kelmore_strings.strings.StringCheckWrapper>`
        Contains function to perform checks on the passed string, like seeing if the string only
        contains upper or lowercase letters

    :class:`Convert <kelmore_strings.strings.StringConvertWrapper>`
        Contains functions to convert the internal string. For example, removing all
        non-ascii characters, removing all whitespace, or finding all the unique
        characters within a string

    :class:`Size <kelmore_strings.strings.StringSizeWrapper>`
        Contains functions to determine different things relating to the given string's size,
        like finding the largest word or counting the number of substrings within the string

    Usage::

        >>> from kelmore_strings import StringWrapper
        >>>
        >>> wrapper = StringWrapper('This is some string!')
        >>> wrapper.check.is_ascii()
        >>> wrapper.convert.replace_whitespace(replacement='   ')
        >>> wrapper.size.largest_word()
        True
        'This   is   some   string!'
        'string'

    Chain Example::

        >>> from kelmore_strings import StringWrapper
        >>>
        >>> wrapper = StringWrapper('Hello    World')
        >>> wrapper = wrapper.convert.replace_null() \
                        .convert.only_ascii() \
                        .convert.replace_whitespace(replacement=' ') \
                        .string
        'Hello World'

    """

    string: str

    check: StringCheckWrapper
    """Contains functions for performing checks on the internal string"""
    convert: StringConvertWrapper
    """Contains functions for converting the internal string"""
    size: StringSizeWrapper
    """Contains functions related to the size of the internal string"""

    def __init__(self, string: Optional[str]):
        self.string = string

        self.check = StringCheckWrapper(self)
        self.convert = StringConvertWrapper(self)
        self.size = StringSizeWrapper(self)
