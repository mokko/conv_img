"""Yet another CLI util to convert images"""

__version__ = "0.0.2"  # move arguments from __init__ to script

from conv_img.conv_img import arg as cv_arg


def conv_img():
    cv_arg()
