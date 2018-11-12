#!/usr/bin/python3
from time import sleep

with open('funkcja.txt', 'r') as file:
    txt = file.read()
    
txt_linie = txt.splitlines()

tekst = []
for i in txt_linie:
    tekst.append(list(i))


for linijka in tekst:
    for znak in linijka:
        print(znak, end='')
    sleep(0.01)
    print()
