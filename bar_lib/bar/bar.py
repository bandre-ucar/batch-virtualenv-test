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

#
# other modules in this package
#
import foolib

def foobarify(message):
    """
    """
    return "BAR: {0}".format(foolib.foo_utils.fooify(message))


if __name__ == "__main__":
    try:
        print("This module does nothing when called directly")
        sys.exit(0)
    except Exception as error:
        print(str(error))
        sys.exit(1)
