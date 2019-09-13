#! /usr/bin/python3
import datetime
import sys

print(datetime.datetime.strptime(sys.argv[1], '%Y-%m-%d') + datetime.timedelta(days=int(sys.argv[2])))

