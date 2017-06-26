import os
import sys
import random as rnd
from PIL import Image

def steganalyse(img):
	"""
	Steganlysis LSB
	"""
	imagencodificada = img.copy()
	ancho, altura = img.size

	for row in range(altura):
		for col in range(ancho):
			r, g, b = img.getpixel((col, row))
			r = 0 if (r % 2 == 0) else 255
			g = 0 if (g % 2 == 0) else 255
			b = 0 if (b % 2 == 0) else 255
			#---Colocando los nuevos pixeles en la imagen
			imagencodificada.putpixel((col, row), (r, g , b))
	
	return imagencodificada


if __name__ == "__main__":
    os.system('clear')
    while True:
        print ("------------------------------------Menu------------------------------------")
        print ("1. Estegoanalisis")
        print ("0. Exit")
        print ("----------------------------------------------------------------------------")
        menu_opcion = int(raw_input("Opcion: "))
        
        
        if menu_opcion == 1:
            print ("\nAnalizando una imagen")
            nombre_archivo = raw_input("Nombre del archivo(imagen): ")
            try:
                img_file = Image.open(nombre_archivo)
            except IOError:
                print ("El archivo '" + nombre_archivo + "' no se pudo abrir")
                continue
            
            #---Llamada a la funcion para el analisis
            analysisImg = steganalyse(img_file)
            analysisImg.show()
            saveTo = raw_input("Resultado")
            if saveTo != "":
                if saveTo.find(".png") == -1: saveTo += ".png"
                analysisImg.save(saveTo)
        
        elif menu_opcion == 0:
            break
        else:
            print ('Opcion invalida')
    os.system('clear')
