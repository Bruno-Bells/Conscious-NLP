#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:16:28 2019

@author: root
"""


my_list = ['skirt', 'shirt', 'pants', 'panks', 'slipers']

def did_you_mean(word):
    len_of_word = []
    for i in my_list:
        f_len = []
        for ii in word:
            if ii in i:
                f_len.append(ii)
        f_len.append(i)
        
        len_of_word.append(f_len)
    print(max(len_of_word, key=len)[-1])
    
    new_word = max(len_of_word, key=len)[-1]
    return new_word
#        
#
did_you_mean('sh')