from selenium import webdriver
from time import sleep 
from PIL import Image
import PIL 
import cv2

driver = webdriver.Chrome(executable_path="/Users/emily/InstagramPost/chromedriver")
driver.get("https://academic.microsoft.com/paper/2050928656/citedby/search?q=Efficiency%20enhancements%20in%20solid-state%20hybrid%20solar%20cells%20via%20reduced%20charge%20recombination%20and%20increased%20light%20capture.&qe=RId%253D2050928656&f=&orderBy=0")
sleep(1)
driver.get_screenshot_as_file("1.png")
driver.quit()
print("end")

im = Image.open("1.png")
left = 0
top = 100
right = 360 
bottom = 270 

iml = im.crop((left,top,right, bottom))
iml.save("new.png")
iml.show()
