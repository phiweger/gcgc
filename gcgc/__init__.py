# (c) Copyright 2018 Trent Hauck
# All Rights Reserved
"""Top-level GCGC module."""

import warnings as _warnings

from gcgc.cli import cli

__version__ = "0.12.0-dev.8"

_warnings.simplefilter(action="ignore", category=PendingDeprecationWarning)
