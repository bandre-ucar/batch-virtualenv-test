#!/usr/bin/env python
"""FIXME: A nice python program to do something useful.

Author: Ben Andre <andre@ucar.edu>

"""

from __future__ import print_function

import numpy
import sympy

import diag_utils


def numpy_sqrt(x):
    """
    """
    return numpy.sqrt(x)


def sympy_quad():
    """
    """
    x = sympy.symbols('x')
    ans = sympy.solve('x**2 - 2', x)
    return ans


def fooy(message):
    """
    """
    return diag_utils.base_utils.foobar_ify(message)


if __name__ == '__main__':
    print("This script does nothing when called directly.")
