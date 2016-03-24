#! /usr/bin/env python
from __future__ import print_function, unicode_literals
import xlwings as xw
import os
import sys
import subprocess
import io
import numpy as np
import re


def run_cyclus():
  cmd = 'rm cyclus.sqlite >/dev/null'
  os.system(cmd)
  #output = subprocess.check_output(cmd.split())
  cmd2 = 'cyclus main.xml >/dev/null 2>&1'
  os.system(cmd2)
  print("run done!")

def count():
  counting_cmd = 'cyan -db cyclus.sqlite inv PWR_Upu_limited_source |grep " 0" |wc -l'
  ps = subprocess.Popen(counting_cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  output = ps.communicate()[0]
  return int(output)

def main():
  run_cyclus()
  print("count", count())



main()