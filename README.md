tinycolor
=========

![tinycolor usage](http://i.imgur.com/XzqoNAr.gif)

tinycolor is a tiny python2 and python3 standalone module for color output for unix terminals. It works by appending [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code) to a given string.

Usage
-----

Just call `tinycolor.color.COLOR_NAME(string)`. Examples:

```python
from tinycolor import color as c

print("Hey, this is {}!".format(c.green("cool")))
# Will print a green "cool"

print("It also works with {} colors".format(c.green_on_blue("background")))
# Will print "background" in green text on blue background

print("And with {} colors".format(c.bright_green("bright")))
# Will print a bright green "bright"

```

Available colors
----------------

- `black`
- `red`
- `green`
- `yellow`
- `blue`
- `magenta`
- `cyan`
- `white`
- `bright_` prefix can be added to any color

Installation
------------

Just drop `tinycolor.py` inside your project and import it as in the example above.

License
-------

Public domain

