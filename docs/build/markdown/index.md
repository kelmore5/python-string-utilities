<!-- StringTools documentation master file, created by
sphinx-quickstart on Sun Sep  8 22:24:54 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# kelmore_strings

* StringTools

* StringArt

* StringCheck

* StringConvert

* StringSize

* StringSpecials


## Strings

Strings is a small library of string utility functions compiled for personal needs. There’s
nothing too fancy nor anything you can’t find from another library, but Strings consists of
smaller functions to be used rather than relying on larger packages.

The functions include things like checking if a string contains all ascii characters, converting
strings to only numbers or alphabetical, and removing extraneous whitespace.

### Personal Note

Strings is only on Github because I reference it in other projects. I don’t have any plans
to maintain this project, but I will update it from time to time.

## Install

You can install this project directly from Github via:

```
$ pip3.7 install git+https://github.com/kelmore5/python-string-utilities.git
```

### Dependencies

* Python 3.7

## Usage

Once installed, you can import the main class like so:

```
>>> from kelmore_strings import StringTools as Strings
>>>
>>> x = 'My phone number is 252-555-5555'
>>> y = 'This is a paragraph           with incorrect         spacing.
>>> z = 'I want a count of all the times I is used in this sentence.
>>>
>>> Strings.convert.only_numeric(x)             # '252-555-5555'
>>> Strings.convert.replace_whitespace(y)       # 'This is a paragraph with incorrect spacing'
>>> Strings.size.count_substring(z, 'I')        # 2
.
.
.
```

## Documentation

* [Main](docs/build/markdown/index.md)

* [StringTools](docs/build/markdown/pages/strings.md)

* [StringArt](docs/build/markdown/pages/tools/art.md)

* [StringCheck](docs/build/markdown/pages/tools/check.md)

* [StringConvert](docs/build/markdown/pages/tools/convert.md)

* [StringSize](docs/build/markdown/pages/tools/size.md)

* [StringSpecials](docs/build/markdown/pages/tools/special.md)

<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
## StringTools


#### class kelmore_strings.strings.StringTools()
A Python class to hold various utility tools to help deal with strings in Python

There’s five sections to StringTools: Art, Check, Convert, Size, and Special. Each helper
class contains their own tools for strings. In order, they are:

`Art`

    Contains functions to create ascii art

`Check`

    Contains function to perform checks on strings, like seeing if a string only contains
    upper or lowercase letters

`Convert`

    Contains functions to convert strings. For example, removing all non-ascii characters,
    removing all whitespace, or finding all the unique characters within a string

`Size`

    Contains functions to determine different things relating to a string’s size, like finding
    the largest word or counting the number of substrings within a string

`Special`

    This class is for any extraneous function that doesn’t fit within the four other classes.
    Right now, the only function inside of it is one to get the last character of a string.

Usage:

```
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
```


#### art()
Contains functions for ascii art

alias of `StringArt`


#### check()
Contains functions for performing checks on strings

alias of `StringCheck`


#### convert()
Contains functions for converting strings

alias of `StringConvert`


#### size()
Contains functions related to string size

alias of `StringSize`


#### special()
Contains extraneous string utility functions

alias of `StringSpecials`

<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
## StringArt


#### class kelmore_strings.strings.StringArt()
A Python helper class used in `StringTools`
that contains functions related to ascii art. Right now, the only functions include
printing out a triangle to the console.

Usage:

```
>>> from kelmore_strings import StringTools as Strings
>>>
>>> Strings.art.backwards_triangle('△', 5)
△△△△△
△△△△
△△△
△△
△
```


#### static backwards_triangle(char: str, size: int)
Creates an upside triangle of given size and outputs it to Python’s console

Usage::

    ```python
    >>> StringTools.art.backwards_triangle('△', 5)
    △△△△△
    △△△△
    △△△
    △△
    △
    ```


* **Parameters**

    * **char** (*str*) – The character that makes up the triangle

    * **size** (*str*) – How tall the triangle should be, in number of lines



* **Returns**

    Nothing, outputs to console



* **Return type**

    None



#### static triangle(char: str, size: int)
Creates a triangle of given size and outputs it to Python’s console

Usage::

    ```python
    >>> StringTools.art.triangle('△', 5)
    △
    △△
    △△△
    △△△△
    △△△△△
    ```


* **Parameters**

    * **char** (*str*) – The character that makes up the triangle

    * **size** (*int*) – How tall the triangle should be, in number of lines



* **Returns**

    Nothing, outputs to console



* **Return type**

    None


<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
## StringCheck


#### class kelmore_strings.strings.StringCheck()
A Python helper class used in `StringTools`
that contains functions to perform various checks on strings, like if a string has any
upper or lowercase letters.

Usage:

```
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
```


#### static array_in_string(check: str, compare_strings: Iterable[str])
Checks whether a given string is contained within a given array

Usage::

    ```python
    >>> array_of_strings: Iterable[str] = ['do', 'I', 'contain', 'hello']
    >>> StringTools.check.array_in_string('hello', array_of_strings)
    True
    ```


* **Parameters**

    * **check** (*str*) – The string to check for

    * **compare_strings** (*Iterable**[**str**]*) – The array to look for the string in



* **Returns**

    True if the string is inside the array else False



* **Return type**

    bool



#### static half_of_alphabet(string: str)
Takes a string and determines if it is within the first half of the alphabet

Usage:

```
>>> x = 'hello'
>>> y = 'world'
>>>
>>> StringTools.check.half_of_alphabet(x)
>>> StringTools.check.half_of_alphabet(y)
True
False
```


* **Parameters**

    **string** (*str*) – Any string



* **Returns**

    True if the string is within the first half of the alphabet else False



* **Return type**

    bool



#### static has_lowercase(string: str)
Checks if a given string contains any lowercase letters

Usage:

```
>>> x = 'WHO AM I'
>>> y = 'jeb'
>>>
>>> StringTools.check.has_lowercase(x)
>>> StringTools.check.has_lowercase(y)
True
False
```


* **Parameters**

    **string** (*str*) – Any string



* **Returns**

    True if the string contains any lowercase letters else False



* **Return type**

    bool



#### static has_numbers(string: str)
Checks if a given string contains any numbers

Usage:

```
>>> x = 'What do I owe ya?'
>>> y = '$50 dollars'
>>>
>>> StringTools.check.has_numbers(x)
>>> StringTools.check.has_numbers(y)
True
False
```


* **Parameters**

    **string** (*str*) – Any string



* **Returns**

    True if the string contains any numbers else False



* **Return type**

    bool



#### static has_uppercase(string: str)
Checks whether a given string contains any uppercase letters

Usage:

```
>>> x = "i don't like uppercase"
>>> y = "You need to learn some grammar"
>>>
>>> StringTools.check.has_uppercase(x)
>>> StringTools.check.has_uppercase(y)
True
False
```


* **Parameters**

    **string** (*str*) – Any string



* **Returns**

    True if the string contains any uppercase letters else False



* **Return type**

    bool



#### static is_ascii(string: str)
Checks whether a given string contains only ascii characters. If the string has all
ascii characters, all the characters (as integers) will be less than 128.

Usage:

```
>>> x = 'Am I ascii??'
>>> y = 'How aьout mэ?'
>>>
>>> StringTools.check.is_ascii(x)
>>> StringTools.check.is_ascii(y)
True
False
```


* **Parameters**

    **string** (*str*) – Any string



* **Returns**

    True if the string contains only ascii characters else False



* **Return type**

    bool



#### static last_half_of_alphabet(string: str)
Takes a string and determines if it is within the last half of the alphabet

Usage:

```
>>> x = 'hello'
>>> y = 'world'
>>>
>>> StringTools.check.last_half_of_alphabet(x)
>>> StringTools.check.last_half_of_alphabet(y)
False
True
```


* **Parameters**

    **string** (*str*) – Any string



* **Returns**

    True if the string is within the last half of the alphabet else False



* **Return type**

    bool



#### static string_ends_with_array(check: str, ends_with_checks: Iterable[str])
Checks if a given strings ends with any of the strings contained within an array

Usage:

```
>>> x = 'some string'
>>> y: Iterable[str] = ['?', '.', 'end', 'ng']
>>>
>>> StringTools.check.string_ends_with_array(x, y)
True
```


* **Parameters**

    * **check** (*str*) – Any string

    * **ends_with_checks** (*Iterable**[**str**]*) – An array of strings to check for in the passed string



* **Returns**

    True if the string ends with any of the strings in ends_with_checks else False



* **Return type**

    bool


<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
## StringConvert


#### class kelmore_strings.strings.StringConvert()
A Python helper class used in `StringTools`
that contains functions to help with conversions of strings, like getting only the ascii
characters, taking out all whitespace, or removing all vowels.

Usage:

```
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
```


#### static consonants(string: str)
Takes a string and returns all the consonants inside of it without vowels

Usage:

```
>>> x = 'Please take out my vowels!'
>>> StringTools.convert.consonants(x)
'Plstktmvwls'
```


* **Parameters**

    **string** (*str*) – Any string



* **Returns**

    The given string with only consonants



* **Return type**

    str



#### static normalize(string: str)
Takes a string and returns it in all lowercase with its spaces replaced with
underscores. Mostly used for dictionaries and database fields

Usage:

```
>>> StringTools.convert.normalize('Some Database Field')
'some_database_field'
```


* **Parameters**

    **string** (*str*) – Any string



* **Returns**

    The given string with spaces replaced with underscores and changed to lowercase



* **Return type**

    str



#### static only_alphabetical(string: str, plus_space: Optional[bool] = False)
Takes a string and removes all characters except alphabetical ones.

    The returned string will only have A-Z, a-z, and optionally, spaces ( ).

Usage:

```
>>> x = "There's too many numbers here 4594102"
>>> StringTools.convert.only_alphabetical(x, plus_space=True)
'Theres too many numbers here '
```


* **Parameters**

    * **string** (*str*) – Any string

    * **plus_space** (*Optional**[**bool**]*) – True if the output should include spaces else False



* **Returns**

    The given string with all non-alphabetical characters removed



* **Return type**

    str



#### static only_ascii(string: str)
Takes a string and removes all non-ascii characters from it

Usage:

```
>>> x = "Ϊ cȃήʹΤ put this in Excel!"
>>> StringTools.convert.only_ascii(x)
' put this in Excel!'
```


* **Parameters**

    **string** – Any string



* **Returns**

    The given string stripped of all non-ascii characters



* **Type**

    string: str



* **Return type**

    str



#### static only_numeric(string: str, keep_decimal_point: Optional[bool] = False)
Takes a string and removes all characters except numerical ones. You can
optionally include the decimal point as well.

Usage:

```
>>> x = 'I only want my money, $19.99'
>>> StringTools.convert.only_numeric(x, keep_decimal_point=True)
'19.99'
```


* **Parameters**

    * **string** (*str*) – Any string

    * **keep_decimal_point** (*Optional**[**bool**]*) – True if the output string should have decimal points else False



* **Returns**

    The given string with all characters stripped except numerical ones



* **Return type**

    str



#### static only_word_characters(string: str, include_space: Optional[bool] = False, include_underscore: Optional[bool] = True)
Takes a string and returns it with only word characters. Word characters are
A-Z, a-z, 0-9, and underscore (_). In other words, this function removes things like
commas (,), apostrophes (‘), periods (.), etc from a string.

You can optionally choose to include spaces and remove underscores, if desired

Usage:

```
>>> x = "I don't want all these characters!"
>>> StringTools.convert.only_word_characters(x, include_space=True)
'I dont want all these characters'
```


* **Parameters**

    * **string** (*str*) – Any string

    * **include_space** (*Optional**[**bool**]*) – True if output should include spaces ( ) else False

    * **include_underscore** (*Optional**[**bool**]*) – True if output should include underscore (_) else False



* **Returns**

    The given string with all non-word characters removed



* **Return type**

    str



#### static regularize(string: str)
Takes a string in all lowercase and separated by underscores and returns the string
with spaces, titled. This is mostly used to “undo” dictionary keys and database fields.

Usage:

```
>>> x = 'some_database_field'
>>> StringTools.convert.regularize(x)
'Some Database Field'
```


* **Parameters**

    **string** (*str*) – A lowercase string separated by underscores



* **Returns**

    The string with its underscores replaced by spaces and titled



* **Return type**

    str



#### static remove_whitespace(string: str)
Removes all whitespace from a string

Usage:

```
>>> x = 'I hate whitespace.'
>>> StringTools.convert.remove_whitespace(x)
'Ihatewhitespace.'
```


* **Parameters**

    **string** (*str*) – Any string



* **Returns**

    The string without any whitespace



* **Return type**

    str



#### static replace_non_ascii(string: str, replacement: str = ' ', with_space: Optional[bool] = True)
Similar to `only_ascii`,
takes a string and replaces all non-ascii characters with a given replacement string.
You can optionally include or remove spaces as well.

Usage:

```
>>> x = "Thϝs doesn't lϼϼk rϝght"
>>> StringTools.convert.replace_non_ascii(x, replacement='|', with_space=True)
"Th|s doesn't l||k r|ght'
```


* **Parameters**

    * **string** (*str*) – Any string

    * **replacement** (*str*) – A string to replace non-ascii characters with

    * **with_space** (*Optional**[**bool**]*) – True if the output string should include spaces ( ) else False



* **Returns**

    The given string with all non-ascii characters replaced with replacement



* **Return type**

    str



#### static replace_null(string: Optional[str])
Takes a string or None and returns a string. Used to force the None type into a string
when the type of a string is unknown.

Usage:

```
>>> StringTools.convert.replace_null(None)
''
```


* **Parameters**

    **string** (*str*) – Any string or None



* **Returns**

    The given string or ‘’ if the string is None



* **Return type**

    str



#### static replace_whitespace(string: str, replacement: str = ' ')
Similar to `only_ascii`,
replaces any whitespace within a given string with a replacement one. This is helpful
when you have a string with a variable number of spaces within it.

Usage:

```
>>> x = "     There's too many      spaces.   "
>>> StringTools.convert.replace_whitespace(x, replacement=' ')
"There's too many spaces."
```


* **Parameters**

    * **string** (*str*) – Any string with extraneous whitespace

    * **replacement** (*str*) – The string to replace any whitespace with



* **Returns**

    The given string with all whitespace replaced with replacement



* **Return type**

    str



#### static strip_or_none(string: Optional[str])
Takes in a string or None and returns None if the given string is None. Otherwise,
it returns the string with it’s extraneous whitespace stripped.

Usage:

```
>>> StringTools.convert.strip_or_none('  Get rid of whitespace please  ')
>>> StringTools.convert.strip_or_none(None)
'Get rid of whitespace please'
None
```


* **Parameters**

    **string** (*Optional**[**str**]*) – Any string or None



* **Returns**

    The given string, stripped, or None if the string is None



* **Return type**

    Optional[str]



#### static unique(string: str)
Takes a string and returns all the unique characters within it.

Usage:

```
>>> x = 'I need uniqueness!'
>>> StringTools.convert.unique(x)
'I neduiqs!'
```


* **Parameters**

    **string** (*str*) – Any string



* **Returns**

    The given string with only its unique character set



* **Return type**

    str



#### static vowels(string: str)
Takes a string and returns all the vowels inside of it

Usage:

```
>>> x = 'Please take out my consonants!'
>>> StringTools.convert.vowels(x)
'eaeaeouyooa'
```


* **Parameters**

    **string** (*str*) – Any string



* **Returns**

    The given string with only vowels



* **Return type**

    str


<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
## StringSize


#### class kelmore_strings.strings.StringSize()
A Python helper class used in `StringTools`
that contains functions that relate to string sizes, including finding the largest word and
counting the substrings within a string

Usage:

```
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
```


#### static count_substring(string: str, search: str)
Counts all the instances of search within the given string

Usage:

```
>>> x = 'How many times do I, will I, can I, say...I?'
>>> StringTools.size.count_substring(x, 'I')
4
```


* **Parameters**

    * **string** (*str*) – Any string

    * **search** (*str*) – The string to search for within string



* **Returns**

    The number of times the search appears within the given string



* **Return type**

    int



#### static largest_word(string: str)
Finds the largest word within a given string. This will only check against word
characters, so things like commas, apostrophes, and question marks are ignored.

Usage:

```
>>> x = "What's the longest word within this question?"
>>> StringTools.size.largest_word(x)
'question'
```


* **Parameters**

    **string** (*str*) – Any string



* **Returns**

    The largest word within the given string



* **Return type**

    str



#### static largest_word_size(string: str)
Finds the size of the largest word within a given string.  This will only check
against word characters, so things like commas, apostrophes, and question marks are
ignored.

Usage:

```
>>> x = "What's the size of the longest word within this question?"
>>> StringTools.size.largest_word_size(x)
8
```


* **Parameters**

    **string** (*str*) – Any string



* **Returns**

    The length of the largest word within the given string



* **Return type**

    int


<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
## StringSpecials


#### class kelmore_strings.strings.StringSpecials()
A Python helper class used in `StringTools`
that holds all extraneous utility functions for strings in Python. Right now, the only
function is finding the last character within a string

Usage:

```
>>> from kelmore_strings import StringTools as Strings
>>>
>>> Strings.special.last_char('hello world')
>>> Strings.special.last_char('   hello world   ', ignore_whitespace=True)
'd'
'd'
```


#### static last_char(string: str, ignore_whitespace: Optional[bool] = False)
Finds the last character within a string

Usage:

```
>>> StringTools.special.last_char('hello world')
>>> StringTools.special.last_char('   hello world   ', ignore_whitespace=True)
'd'
'd'
```


* **Parameters**

    * **string** (*str*) – Any string

    * **ignore_whitespace** (*Optional**[**bool**]*) – True if whitespace should be ignored else False



* **Returns**

    The last character in the string



* **Return type**

    str
