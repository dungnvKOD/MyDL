import os
import cv2
from mtcnn.mtcnn import MTCNN

workDirextory = os.path.dirname(__file__)

trainDiretory = os.path.join(workDirextory, 'images')
celebrityTrainFolder = [os.path.join(trainDiretory,f) for f in os.listdir(trainDiretory)]

count = 0


def rect_to_bb(rect):
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y

    return (x, y, w, h)


def get_face_detect(imagePath):
    print(count, imagePath)
    image = cv2.imread(imagePath)
    detector = MTCNN()
    result = detector.detect_faces(image)

    for face in result:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (x, y, w, h) = face['box']

        image = cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
        crop_img = image[y:y + h, x:x + w]
        crop_img = cv2.resize(crop_img, (200, 200), interpolation=cv2.INTER_CUBIC)
        return crop_img


for i in celebrityTrainFolder:
    imagePath = [os.path.join(i, f) for f in os.listdir(i)]
    for f in imagePath:
        sub_face = get_face_detect(f)
        celebrity = None

        if 'chipu' in f:
            celebrity = 'chipu'

        else:
            celebrity = 'dung'
        face_file_name = workDirextory + '/datatrain/' + celebrity + '/' + celebrity + '_' + str(count) + '.jpg'
        count = count + 1
        cv2.imwrite(face_file_name, sub_face)
