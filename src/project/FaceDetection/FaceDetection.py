import os
import cv2
from mtcnn.mtcnn import MTCNN

workDirextory = os.path.dirname(__file__)

trainDiretory = os.path.join(workDirextory, 'images')
celebrityTrainFolder = [os.path.join(trainDiretory.f) for f in os.listdir(trainDiretory)]

count = 0


def rect_to_bb(rect):
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y

    return (x, y, w, h)


def get_face_detect(imagePath):
    print(count,imagePath)
    image=cv2.imread(imagePath)

