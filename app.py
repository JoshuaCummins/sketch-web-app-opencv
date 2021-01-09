import streamlit as st
import cv2
from PIL import Image
import numpy as np





def sketch(img):
    
	img = np.array(img)
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)    
	canny_edges = cv2.Canny(img_gray_blur, 10, 70)
	ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
	return mask
	
	


st.title("sketch generation")

html_temp = """
<body style="background-color:red;">
<div style="background-color:teal ;padding:10px">
<h2 style="color:white;text-align:center;">Sketch WebApp</h2>
</div>
</body>
"""
st.markdown(html_temp, unsafe_allow_html=True)

image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
if image_file is not None:
	img = Image.open(image_file)
	st.text("Original Image")
	st.image(img)

if st.button("Compute"):
	result_img= sketch(img)
	st.image(result_img)
	