#!/usr/bin/python3
"""
Moduł generuje efekt pisania tekstu na klawiaturze
"""
from pynput.keyboard import Key, Controller
from time import sleep
from random import shuffle, choice


keyboard = Controller()
sleep(2)


def type_text(txt):
	'''
	Funkcja dzieli podany tekst na linijki, znaki
	i emuluje pisanie ich na klawiaturze

	in:
	txt [str] - tekst do podziału
	'''
	czas = [1, 0.5, 0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.2, 0.2]
	shuffle(czas)
	linijki = txt.splitlines()
	znaki = []
	for linia in linijki:
		znaki.append(list(linia))

	for linia in linijki:
		for znak in linia: 
			if znak == '\t':
				keyboard.press(Key.tab)
				keyboard.release(Key.tab)
			else:
				keyboard.press(znak)
				keyboard.release(znak)
			x = choice(czas)
			sleep(x/10)
		sleep(x/10)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		keyboard.press(Key.home)
		keyboard.release(Key.home)
	keyboard.press(Key.home)
	keyboard.release(Key.home)


def main():
	'''
	Główna funkcja modułu.
	'''
	with open('txt.py', 'r') as file:
		txt = file.read()
	type_text(txt)
	pass
	

if __name__ == '__main__':
	main()
