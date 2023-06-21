# tampilkan kedua gambar
import cv2
import numpy as np
from matplotlib import pyplot as plt
# panggil dan konversi warna agar sesuai dengan Matplotlib
einstein = cv2.imread('einstein.jpg')
einstein = cv2.cvtColor(einstein, cv2.COLOR_BGR2RGB) # simpan dengan nama yang sama = ditumpuk
# panggil dan konversi warna agar sesuai dengan Matplotlib
solvay = cv2.imread('solvayconference.jpg')
solvay = cv2.cvtColor(solvay, cv2.COLOR_BGR2RGB)
plt.subplot(121),plt.imshow(einstein), plt.title('Einstein')
plt.subplot(122),plt.imshow(solvay), plt.title('Solvay Conference 1927')
plt.show()