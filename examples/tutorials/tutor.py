# -------------------------------------------------------------------------
#
#  Copyright (c) 2007, Enthought, Inc.
#  All rights reserved.
#
#  This software is provided without warranty under the terms of the BSD
#  license included in enthought/LICENSE.txt and may be redistributed only
#  under the conditions described in the aforementioned license.  The license
#  is also available online at http://www.enthought.com/licenses/BSD.txt
#
#  Thanks for using Enthought open source!
#
# -------------------------------------------------------------------------

""" Script to run the tutorial.
"""

from __future__ import absolute_import, print_function

import os
import sys

from traitsui.extras.tutor import Tutor

# Correct program usage information:
usage = """
Correct usage is: tutor.py [root_dir]
where:
    root_dir = Path to root of the tutorial tree

If omitted, 'root_dir' defaults to the current directory."""


def main(home_dir, root_dir):
    # Create a tutor and display the tutorial:
    tutor = Tutor(home=os.path.dirname(home_dir)).trait_set(
        path=root_dir)
    if tutor.root is not None:
        tutor.configure_traits()
    else:
        raise NameError("No traits tutorial found in %s" % root_dir)


if __name__ == '__main__':

    # Validate the command line arguments:
    if len(sys.argv) > 2:
        print(usage)
        sys.exit(1)

    home_dir = os.path.dirname(sys.argv[0])

    # Determine the root path to use for the tutorial files:
    if len(sys.argv) == 2:
        root_dir = sys.argv[1]
    else:
        root_dir = os.getcwd()

    try:
        main(home_dir, root_dir)
    except NameError as e:
        print(e)
        print(usage)
