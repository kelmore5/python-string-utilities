<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# StringArt


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
