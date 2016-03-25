#! /usr/bin/env python
import os
import subprocess
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt



def run_cyclus():
  cmd = 'rm cyclus.sqlite >/dev/null'
  os.system(cmd)
  #output = subprocess.check_output(cmd.split())
  cmd2 = 'cyclus main.xml >/dev/null 2>&1'
  os.system(cmd2)

def count():
  counting_cmd = 'cyan -db cyclus.sqlite inv PWR_Upu_limited_source |grep " 0" |wc -l'
  ps = subprocess.Popen(counting_cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  output = ps.communicate()[0]
  return int(output)

def main():
  val = []
  for i in range(1000):
    run_cyclus()
    val.append(count())
    print(i)
  bins , edge = np.histogram(val)
  print(bins)
  plt.hist(val)
  plt.savefig('results_1.png')
  plt.show()




main()
