#!/usr/bin/env python
"""FIXME: A nice python program to do something useful.

Author: Ben Andre <andre@ucar.edu>

"""

from __future__ import print_function

import sys

#
# built-in modules
#

#
# installed dependencies
#
import numpy

#
# other modules in this package
#


def bar_ify(message):
    """
    """
    return "BAR: {0}".format(message)


def bar_sqrt(x):
    """
    """
    return numpy.sqrt(x)


if __name__ == "__main__":
    try:
        print("This module does nothing when called directly")
        sys.exit(0)
    except Exception as error:
        print(str(error))
        sys.exit(1)
