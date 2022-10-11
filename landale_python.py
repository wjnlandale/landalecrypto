#!/usr/bin/env python

import os,sys
import re
import ctypes
from ctypes import cdll

landale_python_bindir = os.path.abspath(os.path.dirname(__file__))
buildtype="opt"

if ("_" in os.environ and (os.environ["_"] == "gdb" or re.match(".*/gdb$",os.environ["_"]) or re.match(".*/valgrind$", os.environ["_"]) or
    ("USE_DEBUG" in os.environ))):
  print("%s: Loading debug version of landale_python_l" % os.path.basename(__file__), file=sys.stderr)
  buildtype="debug"

loadpath=None
for p in ["%s/%s/landale_python_l.so" % (landale_python_bindir,buildtype), "%s/landale_python_l.so" % (landale_python_bindir)]:
  if (os.path.exists(p)):
     loadpath = os.path.dirname(p)
     break

if loadpath: 
  sys.path.append(loadpath)
else:
  raise "Unable to get path to landale_python_l.so"

from landale_python_l import *
