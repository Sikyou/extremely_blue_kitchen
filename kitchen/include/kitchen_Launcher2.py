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
import sys, os, shutil, subprocess, shlex
import __builtin__
import kitfuns

"""add your custom options here"""
l2pcolor="735d33"
l2fcolor="8c7c5e"

"""add your custom commands here"""
def custom_commands_run( apkname, apkpath, kitchenpath ):
  os.chdir(apkpath)
  zargs=shlex.split("apktool d "+apkname+".apk toold")
  if subprocess.Popen(zargs, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait() != 0:
    kitfuns.erroroutput("Could Not apktool"+apkname+".apk")
    sys.exit()
  os.chdir("toold"+slashadd+"smali"+slashadd+"com"+slashadd+"android"+slashadd+"launcher2")
  kitfuns.fstrrep("Utilities.smali", "const/16 v4, -0x3d00", "const v4, -0x"+l2pcolor)
  kitfuns.fstrrep("Utilities.smali", "const/16 v4, -0x7200", "const v4, -0x"+l2fcolor)
  os.chdir(apkpath)
  zargs=shlex.split("apktool b toold")
  if subprocess.Popen(zargs, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait() != 0:
    kitfuns.erroroutput("Could Not apktool Rebuild "+apkname+".apk")
    sys.exit()
  os.chdir("toold"+slashadd+"dist")
  shutil.move("out.apk", apkpath+slashadd+"out.apk")
  os.chdir(apkpath)
  shutil.rmtree("toold")
  zargs=shlex.split("unzip -qq out.apk -d toold")
  if subprocess.Popen(zargs).wait() != 0:
    kitfuns.erroroutput("Could Not Unzip out.apk")
    sys.exit()
  os.remove("out.apk")
  shutil.move("toold"+slashadd+"classes.dex",
              apkname+slashadd+"classes.dex")
  shutil.rmtree("toold")