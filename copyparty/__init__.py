#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function

import platform
import sys
import os

WINDOWS = platform.system() == "Windows"
PY2 = sys.version_info[0] == 2
if PY2:
    sys.dont_write_bytecode = True


class EnvParams(object):
    def __init__(self):
        if sys.platform == "win32":
            self.cfg = os.path.normpath(os.environ["APPDATA"] + "/copyparty")
        elif sys.platform == "darwin":
            self.cfg = os.path.expanduser("~/Library/Preferences/copyparty")
        else:
            self.cfg = os.path.normpath(
                os.getenv("XDG_CONFIG_HOME", os.path.expanduser("~/.config"))
                + "/copyparty"
            )


E = EnvParams()
