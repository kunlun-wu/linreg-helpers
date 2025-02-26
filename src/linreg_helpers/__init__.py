#!/usr/bin/env python
##############################################################################
#
# (c) 2025 The Trustees of Columbia University in the City of New York.
# All rights reserved.
#
# File coded by: Billinge Group members and community contributors.
#
# See GitHub contributions for a more detailed list of contributors.
# https://github.com/kunlun-wu/linreg-helpers/graphs/contributors
#
# See LICENSE.rst for license information.
#
##############################################################################
"""Simple helper functions for linear regression"""

# package version
from .version import __version__

# silence the pyflakes syntax checker
assert __version__ or True

from .core import plot_sloping_line, plot_linreg, train_linreg

__all__ = ["plot_sloping_line", "plot_linreg", "train_linreg"]


# End of file
