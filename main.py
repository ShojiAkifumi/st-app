import streamlit as st
from PIL import Image
import cv2
import os

def file_save(image, file_path):
    image = Image.open(image)
    image.save(file_path)

image = st.file_uploader("ファイルアップロード", type='jpg')

if image is not None:
    file_path = image.name
    
    file_save(image, file_path)
    
    image = cv2.imread(file_path)
    cascead_file = "cascade/haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascead_file)
    face_list = cascade.detectMultiScale(image)
    
    color = (0,0,255)
    
    if len(face_list) > 0:
        for face in face_list:
            x, y, w, h = face
            cv2.rectangle(image, (x,y), (x+w, y+h), color, thickness=10)
    else:
        st.write("顔が認識されませんでした。")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    st.image(image)
    
    os.remove(file_path)