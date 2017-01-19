#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  helppo_soitin.py
#  
#  Copyright 2016  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys
import os
from time import sleep

#ladataan audiokirjasto
try:
	import pygame
except RuntimeError:
	print("Pygame-moduulin lataus epaonnistui")

#ladataan GPIO-moduuli
try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("GPIO-moduulin lataus epaonnistui")

#GPIO asetukset 3 ja 5 pinni lahdoiksi ledeille
GPIO.setwarnings(False) #poistaa GPIO virhetulsoteen, toimii ilmankin
GPIO.setmode(GPIO.BOARD) #numerointitavan valinta

GPIO.setup(3,GPIO.OUT) #LED
GPIO.setup(5,GPIO.OUT) #LED
GPIO.setup(7,GPIO.IN) #painike1
GPIO.setup(11,GPIO.IN) #painike2


#pygame-audiomoduulin alustus
pygame.mixer.init()

loppu = False

def main():
	
	soitettava_nro = 0
	
	soittolista = ["kappale.mp3","rammstein.mp3","piipaa.mp3", "rolli.mp3"]
	kappaleiden_maara = len(soittolista)
	print("biiseja" )
	print(kappaleiden_maara)
		
	nappi1_pohjassa = False
	
	#pygame.mixer.music.play()		
	laskuri = 0
	while (1==1):
		
		#tarkkaillaan pyoriiko ohjelma
		musiikki_soi = pygame.mixer.music.get_busy()
		laskuri = laskuri +1
		
		GPIO.output(3,musiikki_soi)
		print (musiikki_soi)+laskuri
		
	
		#painikkeesta musiikki soimaan
		
		if(GPIO.input(7) == True and musiikki_soi ==False and 
		nappi_pohjassa == False):
			pygame.mixer.music.load(open("kappale.mp3","rb"))
			pygame.mixer.music.play()	
		#soiton pysäytys	
		if(GPIO.input(11) == True and nappi2_pohjassa == False):
			if musiikki_soi == True:
				pygame.mixer.music.stop()
			
		#seuraava kappale
		if((GPIO.input(7) == True and nappi1_pohjassa == False)	):
			
			if(soitettava_nro == kappaleiden_maara):
				soitettava_nro =0
				
			pygame.mixer.music.load(open(soittolista[soitettava_nro],"rb"))
			pygame.mixer.music.play()	
			soitettava_nro=soitettava_nro+1
			
		nappi1_pohjassa = GPIO.input(7)	
		nappi2_pohjassa = GPIO.input(11)			
		
		sleep(0.2)

	
	
	return 0

if __name__ == '__main__':
	main()

