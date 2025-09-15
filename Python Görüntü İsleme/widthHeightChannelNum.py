import cv2

res = cv2.imread("forest.png")
height, width, channel_number = res.shape
print("Height: {}  Width: {}  Channel Number: {}".format(height, width, channel_number))
#görüntünün yükseklik, genişlik, ve kanal sayısına ulaşmak, bütünsel düşünebilmek için önemlidir.
# Bu işlemler makine öğrenmesinde örneğin bir el modeli oluşturrurken elimizin baş parmağımızın üst kısmına bir nokta koydurmak isteyelim.
# Bunu doğru ve istenilen şekilde yapabilmek için bu işlemler gereklidir.