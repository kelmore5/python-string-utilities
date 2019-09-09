# Strings

Strings is a small library of string utility functions compiled for personal needs. There's 
nothing too fancy nor anything you can't find from another library, but Strings consists of
smaller functions to be used rather than relying on larger packages.

The functions include things like checking if a string contains all ascii characters, converting
strings to only numbers or alphabetical, and removing extraneous whitespace.

## Personal Note

Strings is only on Github because I reference it in other projects. I don't have any plans 
to maintain this project, but I will update it from time to time. 

# Install

You can install this project directly from Github via:

```bash
$ pip3.7 install git+https://github.com/kelmore5/python-string-utilities.git
```

## Dependencies

- Python 3.7

# Usage

Once installed, you can import the main class like so:

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

# Documentation

* [Main](docs/build/markdown/index.md)
* [StringTools](docs/build/markdown/pages/strings.md)
* [StringArt](docs/build/markdown/pages/tools/art.md)
* [StringCheck](docs/build/markdown/pages/tools/check.md)
* [StringConvert](docs/build/markdown/pages/tools/convert.md)
* [StringSize](docs/build/markdown/pages/tools/size.md)
* [StringSpecials](docs/build/markdown/pages/tools/special.md)
