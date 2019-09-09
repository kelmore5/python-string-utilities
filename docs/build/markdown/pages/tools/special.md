<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# StringSpecials


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
