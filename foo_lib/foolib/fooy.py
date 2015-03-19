#!/usr/bin/env python
from __future__ import print_function

import sys

import foolib.foo_utils

if __name__ == '__main__':
    try:
        print(foolib.foo_utils.fooify('abc'))
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)
