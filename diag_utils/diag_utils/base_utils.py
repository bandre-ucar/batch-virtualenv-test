#!/usr/bin/env python
"""FIXME: A nice python program to do something useful.

Author: Ben Andre <andre@ucar.edu>

"""

from __future__ import print_function

import cesm_utils


def foo_ify(message):
    """This function foo-ifies a message
    """
    return "FOO: {0}".format(message)


def foobar_ify(message):
    """This function foobar-ifies a message
    """
    msg = cesm_utils.bar_util.bar_ify(message)
    msg = foo_ify(msg)
    return msg


if __name__ == '__main__':
    print("This script does nothing when called directly.")

