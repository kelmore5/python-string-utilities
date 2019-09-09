<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# StringCheck


#### class kelmore_strings.strings.StringCheck()
A Python helper class used in `StringTools`

    containing functions to perform various checks on strings, like if a string has any
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
