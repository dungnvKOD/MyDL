import os
import numpy as np
import cv2

images = []
import cv2

path = 'F:/AI/MyDL/src/project/FaceDetection/datatrain'
IMAGE_SIZE = 200


def get_padding_size(image):
    h, w, _ = image.shape
    longest_edge = max(h, w)
    print('longest_edge : ', longest_edge)
    top, bottom, left, right = (0, 0, 0, 0)
    if h < longest_edge:
        dh = longest_edge - h
        top = dh // 2
        bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass
    print('top : ', top, ' bottom : ', bottom)
    return top, bottom, left, right


def resize_with_pad(image, height=IMAGE_SIZE, width=IMAGE_SIZE):
    top, bottom, left, right = get_padding_size(image)
    BLACK = [0, 0, 0]
    constant = cv2.copyMakeBorder(image, top, left, right, cv2.BORDER_CONSTANT, value=BLACK)
    print('consatnt : ', constant)
    resized_image = cv2.resize(constant, (height, width))
    return resized_image


def read_image(file_path):
    image = cv2.imread(file_path)
    image = resize_with_pad(image, IMAGE_SIZE, IMAGE_SIZE)
    return image


def traverse_dir(path):
    for file_or_dir in os.listdir(path):
        abs_path = os.path.abspath(os.path.join(path, file_or_dir))
        print('abs_path : ', abs_path)
        if os.path.isdir(abs_path):
            traverse_dir(abs_path)
        else:
            if file_or_dir.endswith('.jpg'):
                # image =
