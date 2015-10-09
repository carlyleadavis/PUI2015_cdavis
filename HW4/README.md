# PUI2015_cdavis
# Week 4 Homework


This folder contains the homework for week 3 of PUI.  It consists of 3 seperate ipython notebooks.

Since I am running my notebooks in Python 3, it might be useful to have the following imports to run the notebooks:

- To run the python3 style print statements:

from __future__ import print_function

- to download the data from a zip file on a website I use the package io but a Python 2 user would use StringIO, and the alternate Z line that I have commented out in each of the notebooks


* For example, for Python 3 users:
import zipfile, requests, io
r = requests.get('https://s3.amazonaws.com/tripdata/201409-citibike-tripdata.zip')
z = zipfile.ZipFile(io.BytesIO(r.content))
df = pd.read_csv(z.open('201409-citibike-tripdata.csv'))

* For Python 2 users:
import zipfile, requests, StringIO
r = requests.get('https://s3.amazonaws.com/tripdata/201409-citibike-tripdata.zip')
z = zipfile.ZipFile(StringIO.StringIO(r.content))
df = pd.read_csv(z.open('201409-citibike-tripdata.csv'))

Packages used:


import math

import pandas as pd

import numpy as np

import scipy

import scipy.stats

import datetime as dt

import statsmodels.formula.api as smf

import matplotlib.pyplot as pl

import requests

import zipfile

import io

- if using python 2 to import the data, comment out io and uncomment the following lines:

import StringIO

from __future__ import print_function
