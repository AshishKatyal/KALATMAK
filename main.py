#Core Packages
import streamlit as st
from PIL import Image
st.title("Welcome to KALATMAK - An Image Processing App")
img=Image.open("plane.jpg")
st.image(img)
img1=Image.open("clock1.jpg")
st.image(img1)
img2=Image.open("sky.jpg")
st.image(img2)
img3=Image.open("hand.jpg")
st.image(img3)
#Statistical Detail of Image

st.write("Your Entered File **Name** is:",img.filename)
st.write("Your Entered File **Size** is:",img.size)
st.write("Your Entered File **Format** is:",img.format)
st.write("Your Entered File **Width** is:",img.width)
st.write("Your Entered File **Height** is:",img.height)
st.write("Your Entered File **Mode** is:",img.mode)

#Image Resizing
resized1=img.resize((round(img.size[0]*0.5),round(img.size[1]*0.5)))
#st.image(resized1)
resized2=img1.resize((round(img1.size[0]*0.5),round(img1.size[1]*0.5)))
#st.image(resized2)
resized3=img2.resize((round(img2.size[0]*0.5),round(img2.size[1]*0.5)))
#st.image(resized3)
resized4=img3.resize((round(img3.size[0]*0.5),round(img3.size[1]*0.5)))
#st.image(resized4)
#Image Merging
new_image=Image.new('RGB',(img.size[0],img.size[1]),(0,0,0))
new_image.paste(resized1,(2320,1044))
new_image.paste(resized2,(0,0))
new_image.paste(resized3,(0,1044))
new_image.paste(resized4,(2320,0))

st.header("**Image Merging**")
st.image(new_image)

#Image Blending
blend=Image.blend(img,img1,0.6)
st.header("The Blended Image")
st.image(blend)
blend.save("blend.jpeg")

#Image Rotation
#img3=Image.open("hand.jpg")
#st.image(img3.rotate(270))

#Image Blurring
#from PIL import Image,ImageFilter
#img1=Image.open("clock1.jpg")
#blurred=img1.filter(ImageFilter.BLUR)
#st.header("The Blurred Image")
#st.image(blurred)

#Image Filters-CONTOUR- For Sketching
from PIL import Image,ImageFilter
img=Image.open("clock1.jpg")
sketch=img.filter(ImageFilter.CONTOUR)
st.header("The Sketch")
st.image(sketch)
sketch.save("clocksketch.jpeg")

#Image Filters-DETAIL- For Focus
#img=Image.open("clock1.jpg")
#sketch1=img.filter(ImageFilter.DETAIL)
#st.header("The Focused Image")
#st.image(sketch1)

#Image Filters-FIND_EDGES
img=Image.open("clock1.jpg")
sketch2=img.filter(ImageFilter.FIND_EDGES)
st.header("The DARK EDGES")
st.image(sketch2)
sketch2.save("DarkSketch.jpeg")

#Image Filters-EDGE_ENHANCE
#img=Image.open("clock1.jpg")
#sketch3=img.filter(ImageFilter.EDGE_ENHANCE)
#st.header("The EDGE Enhancing")
#st.image(sketch3)

#Image Filters-EDGE_ENHANCE
#img=Image.open("clock1.jpg")
#sketch4=img.filter(ImageFilter.EDGE_ENHANCE_MORE)
#st.header("The MORE EDGE Enhancing")
#st.image(sketch4)

#Image Filters-EMBOSS
#img=Image.open("clock1.jpg")
#sketch5=img.filter(ImageFilter.EMBOSS)
#st.header("The EMBOSS")
#st.image(sketch5)

#Image Filters-SHARPEN
#img=Image.open("clock1.jpg")
#sketch6=img.filter(ImageFilter.SHARPEN)
#st.header("The SHARPEN")
#st.image(sketch6)

#Image Filters-SMOOTH
#img=Image.open("clock1.jpg")
#sketch7=img.filter(ImageFilter.SMOOTH)
#st.header("The SMOOTH")
#st.image(sketch7)

#Flipping and Cropping
#img=Image.open("plane.jpg")
#cropped=img.crop((10,30,200,400))
#st.image(cropped)

#Flipping Horizontally
#flipped_img=img1.transpose(Image.FLIP_LEFT_RIGHT)
#st.header("The Filpped Image Horizontally")
#st.image(flipped_img)

#Flipping Vertically
#flipped_img1=img.transpose(Image.FLIP_TOP_BOTTOM)
#st.header("The Filpped Image Vertically")
#st.image(flipped_img1)

#Rotating
#img3=Image.open("hand.jpg")
#Rotate_img=img3.transpose(Image.ROTATE_270)
#st.image(Rotate_img)

#Different Shapes and Lines on Images
#from PIL import Image, ImageDraw
#draw_img=ImageDraw.Draw(img)
#draw_img.line((0,0,4640,2088),width=10,fill=(255,0,0))
#draw_img.line((0,4640,0,2088),width=10,fill=(255,0,0))
#st.image(img)

#Different ARC on Images
#from PIL import Image, ImageDraw
#draw_img1=ImageDraw.Draw(img)
#draw_img1.arc((1000,1000,2440,1088), 90, 270, width=10,fill=(0,0,0))
#st.image(img)

#Color Conversion
#from PIL import Image, ImageDraw, ImageColor
#rgb_color=ImageColor.getrgb("red")
#st.write(rgb_color)

#new_img=Image.new('RGB',(1000,1000),ImageColor.getrgb("red"))
#st.image(new_img)

#Writing Text on Images

#from PIL import Image, ImageDraw, ImageColor,ImageFont
#newimg=Image.new('RGB',(1000,1000))