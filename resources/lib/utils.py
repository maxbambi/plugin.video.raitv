# -*- coding: utf-8 -*-
import datetime

def sortedDictKeys(adict):
    keys = list(adict.keys())
    keys.sort()
    return keys

def daterange(start_date, end_date):
    for n in range((end_date - start_date).days + 1):
        yield end_date - datetime.timedelta(n)

def checkStr(txt):
    # convert variable to type str both in Python 2 and 3
    if type(txt) == type(bytes()):
        txt = txt.decode('utf-8')
    elif type(txt) == type(unicode()):
        txt = txt.encode('utf-8')
    
    return txt