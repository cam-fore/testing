#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import os


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))
