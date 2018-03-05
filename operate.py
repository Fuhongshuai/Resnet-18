import os
import numpy as np
import os


current_dir = os.getcwd()
train_dir = current_dir + '/train/'
test_dir = current_dir + '/test/'
train_txt = current_dir + '/scripts/train_shuffle.txt'
test_txt = current_dir + '/scripts/val.txt'

train_file = []
for file in os.listdir(train_dir):
    name = file.split('_')
    train_file.append(file+' '+str(name[0])+'\n')

fo = open(train_txt, "w")
print(fo.name)
fo.writelines(train_file)
fo.close()

test_file = []
for file in os.listdir(test_dir):
    name = file.split('_')
    test_file.append(file+' '+str(name[0])+'\n')

fo = open(test_txt,"w")
print(fo.name)
fo.writelines(test_file)
fo.close()
