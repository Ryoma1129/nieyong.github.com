#!/usr/bin/python
# -*- coding:UTF-8 -*-
import glob,os
import shutil

file_names=glob.glob('*.wiki')

f=open('wikiword.wiki','w')
name=""
print >>f,'����ʹ��new_wikiword.py�ű��Զ����ɣ��㼯�˱�wiki�����е�wiki��Ŀ'
for file_name in file_names:
    splited_name= file_name.rsplit('.',1)
    name=splited_name[0]
    print >>f,'# [['+name+']]'
f.close()


