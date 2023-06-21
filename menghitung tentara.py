# tampilkan kedua gambar
import cv2
from matplotlib import pyplot as plt
# panggil dan konversi warna agar sesuai dengan Matplotlib
tentara = cv2.imread('tentara.png')
tentara = cv2.cvtColor(tentara, cv2.COLOR_BGR2RGB)
# panggil dan konversi warna agar sesuai dengan Matplotlib
pasukan = cv2.imread('pasukan.jpg')
pasukan = cv2.cvtColor(pasukan, cv2.COLOR_BGR2RGB)
plt.subplot(121),plt.imshow(tentara), plt.title('tentara')
plt.subplot(122),plt.imshow(pasukan), plt.title('pasukan')
plt.show()