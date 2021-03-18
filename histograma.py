#Se hacen los imports de las librerias necesarias
import cv2
import numpy as np
from matplotlib import pyplot as plt

#se carga la imagen en formato jpg por medio de la libreria cv2
img = cv2.imread('nombreImagen.jpg')#Nota, el nombre de la imagen debe de coincidir con el mostrado en el codigo
cv2.imshow('nombreImagen.jpg', img)

#Se declara una lista con el espectro a revisar, en este caso es rgb
color = ('b','g','r')

#Se crea un ciclo for para realizar el histograma rgb en base a la imagen dada arriba
for i, c in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])

#Se muestra el histograma terminado
plt.show()

cv2.destroyAllWindows()