#!/usr/bin/env python
"""FIXME: A nice python program to do something useful.

Author: Ben Andre <andre@ucar.edu>

"""

from __future__ import print_function

import sys

if sys.hexversion < 0x02070000:
    print(70 * "*")
    print("ERROR: {0} requires python >= 2.7.x. ".format(sys.argv[0]))
    print("It appears that you are running python {0}".format(
        ".".join(str(x) for x in sys.version_info[0:3])))
    print(70 * "*")
    sys.exit(1)

#
# built-in modules
#
from pkg_resources import Requirement, resource_filename, resource_stream
import traceback
import xml.etree.ElementTree as etree

#
# installed dependencies
#
from mpi4py import MPI

from jinja2 import Environment, PackageLoader

#
# other modules in this package
#
from diag_utils.diag_base import fooy, numpy_sqrt, sympy_quad


# -------------------------------------------------------------------------------
#
# main
#
# -------------------------------------------------------------------------------
def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Demonstration of accessing an installed data file...
    if rank == 0:
        filename = resource_filename('diagnostics', 'Config/diags.xml')
        print("Here is your resource file: '{0}'".format(filename))

        stream = resource_stream('diagnostics', 'Config/diags.xml')
        xml = etree.parse(stream)
        etree.dump(xml)
    comm.barrier()

    # Demonstration of access installed jinja2 templates...
    env = Environment(loader=PackageLoader('diagnostics', 'Templates'))
    template = env.get_template('hello.tmpl')
    msg = template.render({'rank': rank, 'size': size})
    print(msg)
    comm.barrier()

    # mpi broadcast data and modify it with a utility imported from
    # one of our packages.
    if rank == 0:
        msg = "This is a message from process"
    else:
        msg = None
    msg = comm.bcast(msg, root=0)
    print("{0} {1} of {2}".format(fooy(msg), rank, size))
    comm.barrier()

    # call a functon from one of our packages that depends on a
    # bootstrap package.
    print("sqrt({0}) = {1}".format(rank, numpy_sqrt(rank)))
    if rank == 0:
        print("Rank 0 says : {0}".format(sympy_quad()))
    return 0


if __name__ == "__main__":
    try:
        status = main()
        sys.exit(status)
    except Exception as error:
        print(str(error))
        traceback.print_exc()
        sys.exit(1)
