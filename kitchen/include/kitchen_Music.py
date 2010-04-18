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
playerbackground="293e66"

"""add your custom commands here"""
def custom_commands_run( apkname, apkpath, kitchenpath, apktool, smali, baksmali ):
  os.chdir(apkpath)
  zargs=shlex.split(apktool+" d "+apkname+".apk toold")
  if subprocess.Popen(zargs, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait() != 0:
    kitfuns.erroroutput("Could Not apktool"+apkname+".apk")
    sys.exit()
  os.chdir("toold"+slashadd+"res"+slashadd+"color")
  kitfuns.fstrrep("tab_indicator_text.xml", "808080", playerbackground)
  os.chdir(apkpath+slashadd+"toold"+slashadd+"res"+slashadd+"layout-finger")
  kitfuns.fstrrep("audio_player_common.xml", "5a5a5a", playerbackground)
  os.chdir(apkpath)
  zargs=shlex.split(apktool+" b toold")
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
  shutil.move("toold"+slashadd+"res"+slashadd+"color"+slashadd+"tab_indicator_text.xml",
              apkname+slashadd+"res"+slashadd+"color"+slashadd+"tab_indicator_text.xml")
  shutil.move("toold"+slashadd+"res"+slashadd+"layout-finger"+slashadd+"audio_player_common.xml",
              apkname+slashadd+"res"+slashadd+"layout-finger"+slashadd+"audio_player_common.xml")
  shutil.rmtree("toold")