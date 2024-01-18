# clean.py
# Andrew Poock
# Program for the data cleaning steps of CS 355 Project 2

import os
import sys
import fileinput
import csv
from itertools import izip

"""if os.path.exists('clean_ALL_AML_grow.train.orig.txt'):
    os.remove('clean_ALL_AML_grow.train.orig.txt')

if os.path.exists('clean_ALL_AML_grow.test.orig.txt'):
    os.remove('clean_ALL_AML_grow.test.orig.txt')"""

readtrain = open('ALL_AML_grow.train.orig.txt', 'r')
readtest = open('ALL_AML_grow.test.orig.txt', 'r')

#newtrainr = open('clean_ALL_AML_grow.train.orig.txt', 'r')
#newtestr = open('clean_ALL_AML_grow.test.orig.txt', 'r')


def removecontrol():
    newtrainw = open('clean_ALL_AML_grow.train.orig.txt', 'w')
    newtestw = open('clean_ALL_AML_grow.test.orig.txt', 'w')
    for line in readtrain.readlines():
        if 'control' not in line:
            newtrainw.write(line)
    for line in readtest.readlines():
        if 'control' not in line:
            newtestw.write(line)
    newtestw.close()
    newtrainw.close()

def replace_tab_with_comma():
    newtrainw = open('comma_ALL_AML_grow.train.orig.txt', 'w')
    newtestw = open('comma_ALL_AML_grow.test.orig.txt', 'w')
    for l in fileinput.input(files = 'clean_ALL_AML_grow.train.orig.txt'):
        l = l.replace('\t', ',')
        newtrainw.write(l)
    for l in fileinput.input(files = 'clean_ALL_AML_grow.test.orig.txt'):
        l = l.replace('\t', ',')
        newtestw.write(l)
    newtestw.close()
    newtrainw.close()

def flr_clg():
    newtrainw = open('step_e_ALL_AML_grow.train.orig.txt', 'w')
    newtestw = open('step_e_ALL_AML_grow.test.orig.txt', 'w')
    train_file = open('comma_ALL_AML_grow.train.orig.txt', 'r')
    test_file = open('comma_ALL_AML_grow.test.orig.txt', 'r')
    for l in train_file.readlines():
        for word in l.split(','):
            try:
                if int(word) < 20:
                    newtrainw.write('20 ')
                if int(word) > 16000:
                    newtrainw.write('16000 ')
                else:
                    newtrainw.write(word + ' ')
            except:
                newtrainw.write(word + ' ')
    for l in test_file.readlines():           
        for word in l.split(','):
            try:
                if int(word) < 20:
                    newtestw.write('20 ')
                if int(word) > 16000:
                    newtestw.write('16000 ')
                else:
                    newtestw.write(word + ' ')
            except:
                newtestw.write(word + ' ')
    newtestw.close()
    newtrainw.close()

def remove_last_char():
    file1 = open('step_e_ALL_AML_grow.test.orig.txt', 'r+')
    Lines1 = file1.readlines()
    file1.close()
    newlines1 = []
    for line in Lines1:
        res = line[:-1]
        newlines1.append(res)
    file1 = open('step_e_ALL_AML_grow.test.orig.txt', 'w')
    file1.writelines(Lines1)
    file1.close()

    file2 = open('step_e_ALL_AML_grow.train.orig.txt', 'r+')
    Lines2 = file2.readlines()
    file2.close()
    newlines2 = []
    for line in Lines2:
        res = line[:-1]
        newlines2.append(res)
    file2 = open('comma_ALL_AML_grow.train.orig.txt', 'w')
    file2.writelines(newlines2)
    file2.close()

def final():
    fin = open('final_train.csv', 'w', newline='')
    test2r = open('comma_ALL_AML_grow.train.orig.csv', 'r')
    writer = csv.writer(fin)
    test2lines=test2r.readlines()
    # test2lines.readline()
    for line in test2lines:
        ln = line.split(',')
        for i in range(len(ln)):
            try:
                if float(ln[i]) < 20:
                    ln[i] = '20'
                elif float(ln[i]) > 16000:
                    ln[i] = '16000'
            except:
                pass
        writer.writerow(ln)
    fin.close()
    test2r.close()
    
def final2():
    fin = open('final_test.csv', 'w', newline='')
    test2r = open('comma_ALL_AML_grow.test.orig.csv', 'r')
    writer = csv.writer(fin)
    test2lines=test2r.readlines()
    # test2lines.readline()
    for line in test2lines:
        ln = line.split(',')
        for i in range(len(ln)):
            try:
                if float(ln[i]) < 20:
                    ln[i] = '20'
                elif float(ln[i]) > 16000:
                    ln[i] = '16000'
            except:
                pass
        writer.writerow(ln)
    fin.close()
    test2r.close()

def transpose_test():
    a = izip(*csv.reader(open("final_test.csv", "rb")))
    csv.writer(open("final_test_tpose", "wb")).writerows(a)

def transpose_train():
    a = izip(*csv.reader(open("final_train.csv", "rb")))
    csv.writer(open("final_train_tpose", "wb")).writerows(a)