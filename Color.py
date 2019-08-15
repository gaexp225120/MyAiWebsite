#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests
# If you are using a Jupyter notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import json
subscription_key = "e0e05a5ad0eb4a9fb08b45d023f3840a"
assert subscription_key
vision_base_url = "https://SoutheastAsia.cognitiveservices.azure.com/vision/v2.0/analyze?visualFeatures=Color&language=en"
analyze_url = vision_base_url + "analyze"
#image_path = "C:/Users/user/Desktop/123.jpg"
str_targetImg = "https://down.om.cn/v3/Uploads/Pic/2017-03-04/1420875049597066022.jpg"
image_data = requests.get(str_targetImg)
# Read the image into a byte array

headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
#print(analysis)

img = Image.open(BytesIO(image_data.content))
plt.axis('off')
plt.imshow(img)

print('-----------------------------------------------')
print("背景色:"+analysis['color']['dominantColorBackground'])
print("前景色2:"+analysis['color']['dominantColorForeground'])
for i in range (len(analysis['color']['dominantColors'])):
    print("主色:"+analysis['color']['dominantColors'][i])

# Display the image and overlay it with the caption.



# In[ ]:




