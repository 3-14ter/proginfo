import cv2

im = cv2.imread('GolyoAlszik_rs.jpg', cv2.IMREAD_COLOR)

# Képkivágás; sor és oszlop tartomány megadása, macska fej rész
im_cropped = im[82:172, 396:486]
# Kivágott rész képbe másolása új, egyező méretű helyre
im[10:100, 20:110] = im_cropped

cv2.imshow('image', im)
cv2.imshow('cropped', im_cropped)

cv2.waitKey(0)
