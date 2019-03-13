import sys
import csv
import pandas as pd


f = open("1825.txt", 'r')
lines = f.readlines()
list= {}
f.close()

for line in lines:
    line.rstrip("\n")
    temp = []
    temp = line.split(":")
    if temp[0] == "\n":
        break
    list[temp[0]] = temp[1]

    data = pd.DataFramge(list)

    data.to_csv("/home/jiwonjeong/PycharmProjects/KMU_MARCH/venv", header=False, index=False)

print(list)