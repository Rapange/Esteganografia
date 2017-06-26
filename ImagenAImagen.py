import numpy as np
import cv2
import math

def changeLSB(number1, number2):
	cont = 0
	newNumber = ""
	for i in range(0,len(number1) - len(number2)):
		newNumber += number1[i]
	return newNumber + number2
		
	
def cifrarCanal(canalOriginal, canalFinal, alpha):
	currentI = 0
	currentJ = 0
	canalPixel = format(canalOriginal[currentI][currentJ],'08b')
	
	lastFor = 0
	nextK = ""
	for i in range(1, len(canalFinal)-1):
		for j in range(1 + i % 2, len(canalFinal[i])-1,2):
			x = canalFinal[i-1][j] ^ canalFinal[i+1][j] ^ canalFinal[i][j+1] ^ canalFinal[i][j-1]
			if x <= alpha:
				LSB = 1
			else:
				LSB = int(math.ceil(alpha/2))
			
			for k in range(lastFor, min(lastFor + LSB,8)):
				nextK += canalPixel[k]

			if lastFor + LSB < 8:
				
				canalFinal[i][j] = int(changeLSB(format(canalFinal[i][j],'08b'),nextK),2)
				nextK = ""
				lastFor = k+1
			else:

				LSB = LSB - (8 - lastFor)
				lastFor = 0
				currentJ += 1
				if currentJ == len(canalOriginal[0]):
					currentI += 1
					currentJ = 0
					if currentI == len(canalOriginal):
						canalFinal[i][j] = int(changeLSB(format(canalFinal[i][j],'08b'),nextK),2)
						return canalFinal
				canalPixel = format(canalOriginal[currentI][currentJ],'08b')
				for k in range(lastFor, min(lastFor + LSB,8)):
					nextK += canalPixel[k]
				canalFinal[i][j] = int(changeLSB(format(canalFinal[i][j],'08b'),nextK),2)
				nextK = ""
				if LSB == 0:
					k = -1
				lastFor = k+1
				
	print "NO"
	return "no completado"
			
def descifrarCanal(n, m, canalFinal, alpha):
	canalOriginal = np.zeros((n,m))
	currentI = 0
	currentJ = 0
	total = n*m*8
	nextK = ""
	for i in range(1, len(canalFinal)-1):
		for j in range(1 + i % 2, len(canalFinal[i])-1,2):
			x = canalFinal[i-1][j] ^ canalFinal[i+1][j] ^ canalFinal[i][j+1] ^ canalFinal[i][j-1]
			
			#x = 1
			if x <= alpha:
				LSB = 1
			else:
				LSB = int(math.ceil(alpha/2))
			
			if total - LSB < 0:
				LSB = total
			nextK += format(canalFinal[i][j], '08b')[-LSB:]
			total -= LSB
			if len(nextK) >= 8:
				canalOriginal[currentI][currentJ] = int(nextK[:8],2)
				if len(nextK) == 8:
					nextK = ""
				else:
					nextK = nextK[8 - len(nextK):]
				currentJ += 1
				if currentJ == m:
					currentJ = 0
					currentI += 1
					if currentI == n:
						return canalOriginal	
	print "NO"
	return "no completado"
	
def cifrarImagen(nombreOriginal, nombreFinal, nuevoNombreFinal, alpha):
	imagenOriginal = cv2.imread(nombreOriginal,cv2.IMREAD_COLOR)
	m = len(imagenOriginal)
	n = len(imagenOriginal[0])
	
	imagenFinal = cv2.imread(nombreFinal, cv2.IMREAD_COLOR)	
	b,g,r = cv2.split(imagenOriginal)
	bs,gs,rs = cv2.split(imagenFinal)

	bs = cifrarCanal(b,bs,alpha)
	gs = cifrarCanal(g,gs,alpha)
	rs = cifrarCanal(r,rs,alpha)
	
	imagenFinal = cv2.merge((bs,gs,rs))
	
	cv2.imwrite(nuevoNombreFinal, imagenFinal)

def descifrarImagen(n, m, nombreCifrado, nombreDescifrado, alpha):
	
	imagenCifrada = cv2.imread(nombreCifrado, cv2.IMREAD_COLOR)	
	bs,gs,rs = cv2.split(imagenCifrada)
	
	b = descifrarCanal(m,n,bs,8)
	g = descifrarCanal(m,n,gs,8)
	r = descifrarCanal(m,n,rs,8)

	imagenDescifrada = cv2.merge((b,g,r))
	
	cv2.imwrite(nombreDescifrado, imagenDescifrada)

	
cifrarImagen("test2.png", "suspicious2.png", "stegoimagen.png", 8)
descifrarImagen(128,128, "stegoimagen.png", "peligro.png",8)
	
