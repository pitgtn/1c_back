# -*- coding: utf8 -*-
import codecs, os, configparser
#get a list of databases from a file ibases.v8i your user
def findbase ():
    result = {}
    path = os.getenv('APPDATA')
    array = path+'\\1C\\1CEStart\\ibases.v8i'
    f = codecs.open(array, 'r', 'utf-8')
    i=f.read().splitlines()
    for name_base in i:
        if "[" and "]" in name_base:
            index = i.index(name_base)
            path_base = i[index+1]
            name_base=name_base.replace('[', '')
            name_base = name_base.replace(']', '')
            name_base = name_base.replace('\ufeff', '')
            path_base=path_base.replace('Connect=File="', '')
            path_base = path_base.replace('";', '')
            result[name_base]=path_base
    return result
config = configparser.ConfigParser()
config.read('config.ini')
dir_backup=(config.get('Main', 'dir_backup'))