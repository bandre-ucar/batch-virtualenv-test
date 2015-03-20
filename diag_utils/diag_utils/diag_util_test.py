#!/usr/bin/env python
from __future__ import print_function

import sys

from diag_utils.diag_base import fooy


if __name__ == '__main__':
    try:
        print(fooy('test test test'))
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)
