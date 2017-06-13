import keras
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import cv2
import sys
import numpy as np 
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

json_file = open('model.json', 'r')
model = json_file.read()
json_file.close()
model = model_from_json(model)
model.load_weights('first_try.h5')
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

img = cv2.imread(sys.argv[1])
img = cv2.resize(img,(150,150))
cv2.imshow('i', img)
cv2.waitKey(0)
img = np.reshape(img,[1,150,150,3])
classes = model.predict_classes(img)

if classes[0][0]==0:
	print('Cat')
else: 
	print('Dog')
