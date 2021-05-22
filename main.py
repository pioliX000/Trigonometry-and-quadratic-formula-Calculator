#!/usr/bin/env python3

from trigonometry import costher, sinther
from pq import pq
from clear import clear

clear()

def HAHALMAO():
	try:
		def t():
			lmao = input("\nCosine Theorem(ct), Sine Theorem(st) or back?: ")
			if lmao == "ct":
				clear()
				costher()
			elif lmao == "st":
				clear()
				sinther()
			elif lmao == "back":
				clear()
				lol()
			else:
				print("bruh")
				t()

		def ta():
			t()
			XD = input("\nAgain?(Y/n): ")
			if XD == "n":
				clear()
				lol()
			else:
				clear()
				ta()

		def pqa():
			pq()
			XD = input("\nAgain?(Y/n): ")
			if XD == "n":
				clear()
				lol()
			else:
				clear()
				pqa()

		def lol():
			xdlol = input("\ntrigonometry(t), pq(pq) or exit?: ")
			if xdlol == "pq":
				clear()
				pqa()	
			elif xdlol == "t":
				clear()
				ta()
			elif xdlol == "exit":
				clear()
				exit()
			elif xdlol == "credits":
				clear()
				print("Made by pioliX000")
				lol()

		while True:
			lol()

	except KeyboardInterrupt:
		stfu = input("\n\nexit? (Y/n): ")
		if stfu == "n":
			clear()
			HAHALMAO()
		else:
			clear()
			print("Made my pioliX000")
HAHALMAO()