#!/usr/bin/py
# -*- coding: iso-8859-1 -*-
"""
   Copyright (C) 2010 Jef Oliver jgoliver _at_ jeago _dot_ com

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
"""standard imports"""
import sys, os, shutil, subprocess, shlex, ConfigParser
import __builtin__

config= ConfigParser.ConfigParser()
config.optionxform=str
config.read(kitchenpath+slashadd+"conf"+slashadd+"kitchen.ini")

sys.path.append(kitchenpath+slashadd+"include")

if os.name == "nt":
  import ctypes
  STD_OUTPUT_HANDLE = -11
  FOREGROUND_RED    = 0x0004
  FOREGROUND_BLUE   = 0x0001
  def get_csbi_attributes(handle):
    # Based on IPython's winconsole.py, written by Alexander Belchenko
    import struct
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
    assert res
    (bufx, bufy, curx, cury, wattr, left, top,
    right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    return wattr
  handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
  reset = get_csbi_attributes(handle)
  def formoutput( so ):
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_BLUE)
    print "  "+so
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
    return
  def verboseoutput( so ):
    if config.get("general", "verbose") == "y":
      ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_BLUE)
      print "  "+so
      ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
    return
  def pverboseoutput( so ):
    if config.get("general", "patchverbose") == "y":
      ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_BLUE)
      print "   ** "+so
      ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
    return
  def erroroutput( so ):
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_RED)
    print "  ERROR: "+so
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
    return
else:
  def formoutput( so ):
    print '\033[94m  '+so+'\033[0m'
    return
  def verboseoutput( so ):
    if config.get("general", "verbose") == "y":
      print '\033[94m  '+so+'\033[0m'
    return
  def pverboseoutput( so ):
    if config.get("general", "patchverbose") == "y":
      print '\033[94m   ** '+so+'\033[0m'
    return
  def erroroutput( so ):
    print '\033[91m  ERROR: '+so+'\033[0m'
    return

"""**************************************************************************"""
"""function similar to sed for a file"""
"""**************************************************************************"""
def fstrrep( filen, smatch, sreplace ):
  nfilen = filen+".new"
  o = open(nfilen, "a")
  for line in open(filen):
    line = line.replace(smatch, sreplace)
    o.write(line)
  o.close()
  os.remove(filen)
  os.rename(nfilen, filen)
  return