<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# StringTools


#### class kelmore_strings.strings.StringTools()
A Python class to hold various utility tools to help deal with strings in Python

There’s five sections to StringTools: Art, Check, Convert, Size, and Special. Each helper
class contains their own tools for strings. In order,

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
