# -*- coding: utf-8 -*-

COLORMAP = {
    "black": 0,
    "red": 1,
    "green": 2,
    "yellow": 3,
    "blue": 4,
    "magenta": 5,
    "cyan": 6,
    "white": 7,
}

COLOR_PARAMETERS = {
    "fg": 30,
    "bg": 40,
    "bright_increment": 60,
}


class ColorNotFoundException(Exception):
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return u"Color {} not found.".format(self.color)


class C(type):

    def __getattr__(self, colors_string):
        colors_string = colors_string.lower().replace("_","")

        fg_desc, bg_desc = colors_string.split("on") if "on" in colors_string \
                                     else (colors_string, None)

        self.escape_code = self._get_escape_code(fg_desc, bg_desc)

        return self._get_color_string

    def _get_color_string(self, string):
        return u"{}{}{}".format(
            self.escape_code,
            string,
            self._get_reset_escape_code()
        )

    def _get_escape_code(self, fg_desc, bg_desc):
        fg_code = self._desc_to_code(fg_desc, is_fg=True)
        bg_code = self._desc_to_code(bg_desc, is_fg=False)
        return u"\033[{}m".format(str(fg_code)+((";{}".format(bg_code)) if bg_code else ""))

    def _get_reset_escape_code(self):
        return u"\033[0m"

    def _desc_to_code(self, color_description, is_fg=True):

        if not color_description:
            return 0

        color_code = COLOR_PARAMETERS["fg" if is_fg else "bg"]

        if "bright" in color_description:
            color_code += COLOR_PARAMETERS["bright_increment"]
            color_description = color_description.replace("bright", "")

        try:
            color_code += COLORMAP[color_description]
            return color_code

        except KeyError as ex:
            raise ColorNotFoundException(color_description)


# Trick to make a metaclass that is both python2 and python3 compatible
# Syntax: C(class_name, base_classes, new_attribues)
color = C(str('color'), (), {})

if __name__ == "__main__":
    print("This is the {} module!".format(color.green("colors")))

