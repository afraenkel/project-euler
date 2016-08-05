#!/usr/bin/env python

from __future__ import print_function

import datetime

begin = datetime.datetime(1901, 1, 1)
end = datetime.datetime(2000, 12, 31)
delta = end - begin

isSunday = lambda x: (begin + datetime.timedelta(x)).weekday() == 6
isFirst = lambda x: (begin + datetime.timedelta(x)).day == 1

if __name__ == '__main__':
    s = sum(1 for x in range(delta.days) if isSunday(x) and isFirst(x))
    print(s)

