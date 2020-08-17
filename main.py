# -*- coding: utf8 -*-
import os, datetime
from methods import *

rar="D:\\backup_1c\\rar.exe"
listbase = findbase()
count_base = len(listbase)
for key, value in listbase.items():
    print(key, value)
    os.system(rar+' a \"'+dir_backup+"\\"+key+"\\"+str(datetime.date.today())+'.rar\" ' '\"'+value+'\\1Cv8.1CD\"')
print('Найдено: ' +str(count_base) +' базы.')


