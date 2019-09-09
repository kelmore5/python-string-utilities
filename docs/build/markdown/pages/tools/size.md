<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# StringSize


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
