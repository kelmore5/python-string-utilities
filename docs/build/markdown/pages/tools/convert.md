<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# StringConvert


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
