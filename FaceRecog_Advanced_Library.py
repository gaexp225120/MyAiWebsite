

import requests
import json
from matplotlib.pyplot import imshow
import cognitive_face as CF
from io import BytesIO #for open graphics??
from PIL import Image, ImageDraw, ImageFont
import FaceRecog_PersonGroup_Library as gl
import FaceRecog_Basic_Library as bl
import FaceRecog_FaceList_Library as fl

#-- set up congnitive_face
KEY = '883a1c8f768b44eab69c81fab29fd41b'#face recognization
CF.Key.set(KEY)

BASE_URL = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

#-- Global variable
str_personGroupId_test01 = 'groupid_test01'
str_personId_Sunny = 'd5cbe201-2f6b-460e-be93-d504edfc18e9'
str_personId_Angela = '1df5b077-8fc5-4f2b-a28f-a173b516ff84'

str_personGroupId_test02 = 'groupid_test02'
str_personId_Rachel = '9b4f25f6-4896-4c75-ad58-be436eeee107'
str_personId_Monica = '1d83ad25-5589-4d14-b41c-18c946f6dc4c'
str_personId_Phoebe = '2012e88c-de56-4b66-a626-d782006e3d80'

str_targetImg = "https://i1.wp.com/popbee.com/image/2019/07/fhdhdfhdfh.jpg"

str_faceListId = "tmepfacelistid"

#-- Request headers
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': KEY,
}


# In[2]:


#*************************
#** Function *************
#*************************
#** A - 1
#** Function Name: IdentifyPerson(str, str)
#** Description: Complete process of identify. Input url of target image and get indicated image as result.
#** Parameters: 
#** -- str_targetImg: url of target image.
#** -- str_groupId: the group(id) of those known people want to recognize on target image.
#**
#*************************

def IdentifyPerson(str_targetImg, str_groupId):
    
    #-- 1. detect
    result_detect = bl.Detect(str_targetImg)
    j_faces = result_detect.json()
    
    #-- 2. identify(get candidates id)
    li_targetFaces = list()
    for i in range(len(j_faces)):
        li_targetFaces.append({'faceId': j_faces[i]["faceId"],
                               'faceRectangle': j_faces[i]["faceRectangle"],
                               'candidatesId': '',
                               'name': ''})#record faceID with their corresponding name
    
    li_targetFaces = bl.Identify(li_targetFaces, str_groupId)
    
    #-- 3. get name
    li_targetFaces = bl.getIdentifyName(li_targetFaces, str_groupId)

    #-- 4. show name on image
    result_img = bl.showName(li_targetFaces, str_targetImg, j_faces)
    #imshow(result_img)
    #result_img.show()
    
    return result_img

#*************************


# In[7]:


### identify
#-- parameters
# #str_targetImg = str_targetImg
# str_groupId = str_personGroupId_test02

# recogImg = IdentifyPerson(str_targetImg, str_groupId)

# imshow(recogImg)
# recogImg.show()


# In[2]:


#*************************
#** Function *************
#*************************
#** A - 2
#** Function Name: DetectFace(str, int, str)
#** Description: Complete process of detect. Input url of target image and show detected information on image.
#** Parameters: 
#** -- str_targetImg: url of target image.
#** -- detectMode: diffrient mode for different result on image.
#** -- str_fileName: specifying the name to save the result image.
#**
#*************************

def DetectFace(str_targetImg, detectMode, str_fileName):
    
    #-- 1. detect
    result_detect = bl.Detect(str_targetImg)
    j_faces = result_detect.json()
    
    #-- 2. deal with different mode
    #---- mode 0: only draw retangle on the image
    if detectMode == 0:
        result_img =  bl.drawRect(str_targetImg, j_faces)
    #---- mode 1: show age on the image
    elif detectMode == 1:
        result_img =  bl.showAge(str_targetImg, j_faces)
    #---- mode 2: show emotions on the image
    elif detectMode == 2:
        result_img =  bl.showEmotions(str_targetImg, j_faces)
    else:
        return "please input valid mode."  

    bl.saveImg(result_img, str_fileName)
    
    return result_img

#*************************


# In[5]:


# recogImg = DetectFace(str_targetImg, 2, "test0805-3")

# imshow(recogImg)
# recogImg.show()


# In[4]:


#*************************
#** Function *************
#*************************
#** A - 3
#** Function Name: FindTheMostSimilar(str, str)
#** Description: Complete process of find similar. Input url of target image and get the most similar image.
#** Parameters: 
#** -- str_targetImg: url of target image.
#** -- str_faceListId: the group(id) of those known people want to recognize on target image.
#**
#*************************

def FindTheMostSimilar(str_targetImg, str_faceListId):
    
    int_maxNum = 1
    str_mode = "matchFace"
    
    #-- 1. detect
    result_detect = bl.Detect(str_targetImg)
    j_faces = result_detect.json()
    
    str_faceId = j_faces[0]['faceId']
    
    #-- 2. find similar(get candidates id)
    response_findSimilar = bl.FindSimilar(str_faceId, str_faceListId, int_maxNum, str_mode)
    
    str_FLfaceId = response_findSimilar.json()[0]["persistedFaceId"]
    
    #-- 3. get img url
    getSimilarURL = bl.getSimilarImgUrl(str_FLfaceId, str_faceListId)

    #-- 4. open the image
    response_img = requests.get(getSimilarURL)
    result_img = Image.open(BytesIO(response_img.content))
    
    return result_img

#*************************


# In[5]:


# str_targetImg = "http://www.newwide.com/AI/Angela1.jpg"

# smrImg = FindTheMostSimilar(str_targetImg, str_faceListId)
# imshow(smrImg)
# # recogImg.show()


# In[ ]:




