#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#**********************************************************************
#********************** Program Note Description **********************
#**********************************************************************
#
# Description: set out the rules of comments and coding
# [Name] -- camelCase_classify
# -- Program File Name: 'Suject'_'date(if need)'_'subtitle(if need)'
# -- Variable Name: 'dataType(if is known)'_'Objective'_'number/diff. obj(if need)'
# [Rules] -- comments
# -- every code file should include this description at the top
# -- every code file should indicate the creator, subject and start date
# -- ### (subject of a cell)
# -- #-- (describe the purpose of below section)
# -- #---- (second level description)(every level get two moer '-' and so on)
# -- notice there is always a space between the sign and characters
#
#**********************************************************************

#-- Function Format --

#*************************
#** Function *************
#*************************
#**
#** Function Name: func(str, str, str)
#** Description: ...
#** Parameters: 
#** -- str_xxx: ...
#** -- str_yyy: ...
#** -- str_zzz: ...
#**
#*************************

# def func():
#     ...

#*************************


# In[ ]:


#**********************************************************************
#****************************** NEW WIDE ******************************
#**********************************************************************
#** Project: FaceRecog_Basic_Library                                 **
#** Creator: Judy Tang                                               **
#** Start Date: 2019/07/23                                           **
#** Description: basic functions of face api                         **
#**********************************************************************


# In[ ]:


#*************************
#** Content **************
#*************************
#**
#** -- Main --
#** M - 1 Detect(str_targetImg)
#**   - 2 FindSimilar(str_faceId, str_faceListId, int_maxNum, str_mode)
#**   - 3 Group()
#**   - 4 Identify(li_targetFaces, str_groupId)
#**   - 5 Verify()
#** -- Operate --
#** O - 1 getRectangle(dic_face)
#**   - 2 drawRect(str_targetImg, j_faces)
#**   - 3 getIdentifyName(li_targetFaces, str_groupId)
#**   - 4 showName(li_targetFaces, str_targetImg, j_faces)
#**   - 5 getSimilarImgUrl(str_FLfaceId, str_faceListId)
#**   - 6 showAge(str_targetImg, j_faces)
#**   - 7 showEmotions(str_targetImg, j_faces)
#**   - 8 saveImg(img, str_fileName)
#**
#*************************


# In[2]:


### Basic Setting

import requests
import json
#from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import cognitive_face as CF
from io import BytesIO #for open graphics??
from PIL import Image, ImageDraw, ImageFont
import FaceRecog_PersonGroup_Library as gl
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


# In[5]:


#*************************
#** Function *************
#*************************
#** M - 1
#** Function Name: Detect(str)
#** Description: Detect human faces in an image
#** Parameters: 
#** -- str_targetImg: url of the image want to detect faces.
#**
#*************************

def Detect(str_targetImg):
    
    #-- Request body
    body = dict()
    body["url"] = str_targetImg
    body = str(body)
    
    #-- Request parameters
    params_detect = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'recognitionModel': 'recognition_02',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

    #-- Requet url
    str_apiUrl_Detect = BASE_URL + 'detect'

    #-- call api
    response_detect = requests.post(str_apiUrl_Detect, params=params_detect, data=body, headers=headers)
    
    return response_detect

#*************************


# In[4]:


#*************************
#** Function *************
#*************************
#** M - 2
#** Function Name: FindSimilar(str, str, int, str)
#** Description: search the similar-looking faces from a faceId array
#** Parameters: 
#** -- str_faceId: faceId of the query face.
#** -- str_faceListId: An existing user-specified unique candidate face list.
#** -- int_maxNum: (optional)The number of top similar faces returned.
#** -- str_mode: (optional)Similar face searching mode.It can be "matchPerson"(defaults) or "matchFace".
#**
#*************************

def FindSimilar(str_faceId, str_faceListId, int_maxNum, str_mode):
    
    body = dict()
    body["faceId"] = str_faceId
    body["faceListId"] = str_faceListId
    body["maxNumOfCandidatesReturned"] = int_maxNum
    body["mode"] = str_mode
    body = str(body)

    #-- api url
    str_apiUrl_findSimilar = (BASE_URL + 'findsimilars')

    response_findSimilar = requests.post(str_apiUrl_findSimilar, data=body, headers=headers)
    
    return response_findSimilar

#*************************


# In[ ]:


#*************************
#** Function *************
#*************************
#** M - 3
#** Function Name: Group()
#** Description: Divide candidate faces into groups based on face similarity
#** Parameters: 
#** -- str_targetImg: url of the image want to detect faces.
#**
#*************************

def Group():
    
#     #-- Request body
#     body = dict()
#     body["url"] = str_targetImg
#     body = str(body)
    
#     #-- Request parameters
#     params_detect = {
#         'returnFaceId': 'true',
#         'returnFaceLandmarks': 'false',
#         'recognitionModel': 'recognition_02',
#         'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
#     }

#     #-- Requet url
#     str_apiUrl_Detect = BASE_URL + 'detect'

#     #-- call api
#     response_detect = requests.post(str_apiUrl_Detect, params=params_detect, data=body, headers=headers)
    
     return None

#*************************


# In[5]:


#*************************
#** Function *************
#*************************
#** M - 4
#** Function Name: Identify(li, str)
#** Description: identify all faces in target image
#** Parameters: 
#** -- li_targetFaces: list of target faces.
#** -- str_groupId: personGroupId of the target person group.
#**
#*************************

def Identify(li_targetFaces, str_groupId):
        
    #-- get the target id list 
    li_faceIds = []
    
    for i in range(len(li_targetFaces)):
        li_faceIds.append(li_targetFaces[i]["faceId"])

    #-- Request Body
    body = dict()
    body["personGroupId"] = str_groupId
    body["faceIds"] = li_faceIds
    body["maxNumOfCandidatesReturned"] = 1
    body["confidenceThreshold"] = 0.5
    body = str(body)

    #-- Request URL
    str_apiUrl_identify = BASE_URL + 'identify'

    #-- call api
    response_identify = requests.post(str_apiUrl_identify, data=body, headers=headers) 

    #-- save candidates back to li_targetFaces
    json_response = response_identify.json()
    for i in range(len(json_response)):
        if len(json_response[i]["candidates"]) != 0 :
            li_targetFaces[i]['candidatesId'] = json_response[i]["candidates"][0]["personId"]
            
    return li_targetFaces

#*************************


# In[4]:


#*************************
#** Function *************
#*************************
#** M - 5
#** Function Name: Verify()
#** Description: Verify whether two faces belong to a same person
#** Parameters: 
#** -- str_targetImg: url of the image want to detect faces.
#**
#*************************

def Verify(str_faceId1, str_faceId2):
    
    #-- Request body
    body = dict()
    body["faceId1"] = str_faceId1
    body["faceId2"] = str_faceId2
    body = str(body)
    
    #-- Requet url
    str_apiUrl_Verify = BASE_URL + 'verify'

    #-- call api
    response_verify = requests.post(str_apiUrl_Verify, data=body, headers=headers)
    
    return response_verify

#*************************


# In[ ]:


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ MAIN ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV OPERATE VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV


# In[79]:


#*************************
#** Function *************
#*************************
#** O - 1
#** Function Name: getRectangle(dic)
#** Description: get detected face's coordinates
#** Parameters: 
#** -- dic_face: single face from Detect().
#**
#*************************

def getRectangle(dic_face):
    
    faceRect = dic_face['faceRectangle']
    left = faceRect['left']
    top = faceRect['top']
    bottom = top + faceRect['height']
    right = left + faceRect['width']
    
    #print("GR left: "+str(left) + ", bottom: "+str(bottom))
    
    return ((left, top), (right, bottom))

#*************************


# In[72]:


#*************************
#** Function *************
#*************************
#** O - 2
#** Function Name: drawRect(str, json)
#** Description: get detected face's coordinates
#** Parameters: 
#** -- str_targetImg: url of the image want to locate faces.
#** -- j_faces: result in json format from Detect().
#**
#*************************

def drawRect(str_targetImg, j_faces):
        
    #-- open the image
    response_img = requests.get(str_targetImg)
    img_rect = Image.open(BytesIO(response_img.content))

    #-- for each face returned use the face rectangle and draw a red box.
    draw = ImageDraw.Draw(img_rect)
    
    for face in j_faces:
        draw.rectangle(getRectangle(face), outline='red', width=5)
        
    return img_rect

#*************************


# In[8]:


#*************************
#** Function *************
#*************************
#** O - 3
#** Function Name: getIdentifyName(li, str)
#** Description: get detected face's coordinates
#** Parameters: 
#** -- li_targetFaces: list of target faces.
#** -- str_groupId: personGroupId of the target person group.
#**
#*************************

def getIdentifyName(li_targetFaces, str_groupId):
    
    for i in range(len(li_targetFaces)):
        if li_targetFaces[i]['candidatesId'] != '':
            str_personId = li_targetFaces[i]['candidatesId']
            
            #get the name by GetPerson()
            result_getPerson = gl.getPerson(str_groupId, str_personId)
            
            #-- Requet url
#             str_apiUrl_getPerson_temp = BASE_URL + 'persongroups/' + str_personGroupId_test02 + '/persons/' + personId

#             response_GetPerson_temp = requests.get(str_apiUrl_getPerson_temp, headers=headers)
            #print(response_GetPerson_temp)
            
            #-- save the name back to li_faces
            getPersonName = result_getPerson.json()["name"]
            li_targetFaces[i]['name'] = getPersonName
        
    return li_targetFaces

#*************************


# In[9]:


#*************************
#** Function *************
#*************************
#** O - 4
#** Function Name: showName(li, str, json)
#** Description: get detected face's coordinates
#** Parameters: 
#** -- li_targetFaces: list of target faces.
#** -- str_targetImg: parameter for drawRect()
#** -- j_faces: parameter for drawRect()
#**
#*************************

def showName(li_targetFaces, str_targetImg, j_faces):
    
    img = drawRect(str_targetImg, j_faces)
    
    for i in range(len(li_targetFaces)):
        if li_targetFaces[i]['name'] != '':
            coordinates = getRectangle(li_targetFaces[i])
            #rect = li_faces[i]['faceRectangle']
            left = coordinates[0][0]
            top = coordinates[0][1]
            right = coordinates[1][0]
            bottom = coordinates[1][1]

            largefont = ImageFont.truetype("calibri.ttf",20)
            draw = ImageDraw.Draw( img )
            draw.text( (left, top-20), li_targetFaces[i]['name'], font = largefont, fill=(255,0,0,255))


    return img

#*************************


# In[10]:


#*************************
#** Function *************
#*************************
#** O - 5
#** Function Name: getSimilarImgUrl(li, str)
#** Description: get the most similar person's image
#** Parameters: 
#** -- str_FLfaceId: faceId of the most similar person.
#** -- str_faceListId: Specifying the FaceList containing the target faceId.
#**
#*************************

def getSimilarImgUrl(str_FLfaceId, str_faceListId):
    
    result_Img = "No Match"
    
    #-- 1.get all faces in facelist
    result_getFL = fl.getFaceList(str_faceListId)
    j_getFLfaces = result_getFL.json()['persistedFaces']
    
    for i in range(len(j_getFLfaces)):
        if j_getFLfaces[i]['persistedFaceId'] == str_FLfaceId:
            result_Img = j_getFLfaces[i]['userData']
        
    return result_Img

#*************************


# In[73]:


#*************************
#** Function *************
#*************************
#** O - 6
#** Function Name: showAge(str, json)
#** Description: show detected face's age
#** Parameters: 
#** -- str_targetImg: url of target image.
#** -- j_faces: result in json format from Detect().
#**
#*************************

def showAge(str_targetImg, j_faces):
    
    img = drawRect(str_targetImg, j_faces)
    
    for face in j_faces:
        coordinates = getRectangle(face)
        left = coordinates[0][0]
        top = coordinates[0][1]
        bottom = coordinates[1][1]
        
#         print("SA left: "+str(left) + ", bottom: "+str(bottom) + ", top: "+str(top))
#         print("height: "+str(face['faceRectangle']['height']))
        
        str_age = "Age: " + str(face['faceAttributes']['age'])

        largefont = ImageFont.truetype("calibri.ttf",30)
        draw = ImageDraw.Draw( img )
        draw.text( (left, bottom+10), str_age, font = largefont, fill=(255,0,0,255))
        
    return img

#*************************


# In[88]:


#*************************
#** Function *************
#*************************
#** O - 7
#** Function Name: showEmotions(str, json)
#** Description: show detected face's emotions
#** Parameters:
#** -- str_targetImg: url of target image.
#** -- j_faces: result in json format from Detect().
#**
#*************************

def showEmotions(str_targetImg, j_faces):
    
    img = drawRect(str_targetImg, j_faces)
    
    for face in j_faces:
        coordinates = getRectangle(face)
        left = coordinates[0][0]
        bottom = coordinates[1][1]
        
        temp_emotion = ""
        dic_emotion = face['faceAttributes']['emotion']
        
        for emotion in dic_emotion:
            if dic_emotion[emotion] != 0:
                temp_emotion = temp_emotion + emotion + ": " + str(dic_emotion[emotion]) + "\n"
        
        if len(temp_emotion) != 0:
            str_emotion = temp_emotion[:-2]
        else:
            str_emotion = temp_emotion
        
        largefont = ImageFont.truetype("calibri.ttf",18)
        draw = ImageDraw.Draw( img )
        draw.text( (left, bottom+5), temp_emotion, font = largefont, fill=(255,0,0,255))
        
    return img

#*************************


# In[115]:


#*************************
#** Function *************
#*************************
#** O - 8
#** Function Name: saveImg(img, str)
#** Description: save the image
#** Parameters:
#** -- img: temp img want to save as jpg file.
#** -- str_fileName: file name.
#**
#*************************

def saveImg(img, str_fileName):
    
    plt.figure(figsize = (8,6))
    plt.imshow(img)
    plt.axis('off')
    
    plt.gca().xaxis.set_major_locator(plt.NullLocator()) 
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1,bottom=0,left=0,right=1,hspace=0,wspace=0)
    plt.margins(0,0)
    
    #plt.show()
    
    str_fileName = str_fileName + ".jpg"
    
    # save
    plt.savefig(str_fileName,bbox_inches='tight',dpi=600,pad_inches=0.0)
    
    return None

#*************************


# In[17]:


# #-- 1 detect
# result_detect = Detect(str_targetImg)
# json_response_faces = result_detect.json()

# #-- 2 draw rectangle
# #str_targetImg = "https://i1.wp.com/popbee.com/image/2019/07/fhdhdfhdfh.jpg"
# j_faces = result_detect.json()

# #result_img = drawRect(str_targetImg, j_faces)
# #imshow(result_img)

# #-- 3 identify
# li_targetFaces = list()
# for i in range(len(json_response_faces)):
#     li_targetFaces.append({'faceId': json_response_faces[i]["faceId"], 
#                      'faceRectangle': json_response_faces[i]["faceRectangle"], 
#                      'candidatesId': '', 
#                      'name': ''})#record faceID with their corresponding name
    
# str_groupId = str_personGroupId_test02

# li_targetFaces = Identify(li_targetFaces, str_groupId)
# #print(json.dumps(li_targetFaces, sort_keys=True, indent=2))

# #-- 4 get name
# li_targetFaces = getIdentifyName(li_targetFaces, str_groupId)
# #print(json.dumps(li_targetFaces, sort_keys=True, indent=2))

# #-- 5 show name on image
# #img = result_img

# re_show = showName(li_targetFaces, str_targetImg, j_faces)
# imshow(re_show)
# re_show.show()


# In[9]:


#*************************
#** Test *****************
#*************************

#-- import
#import FaceRecog_0723_Group_Library as gl

# result = gl.listAllGroup("","","")
# print(json.dumps(result.json(), sort_keys=True, indent=2))

#-- M-1
#---- parameters
# str_targetImg = "https://i1.wp.com/popbee.com/image/2019/07/fhdhdfhdfh.jpg"

# result_detect = Detect(str_targetImg)
# json_response_faces = result_detect.json()
# print(json.dumps(json_response_faces, sort_keys=True, indent=2))

#-- M-2
# str_tempTaget = "http://www.newwide.com/AI/Angela1.jpg"

# #---- parameters
# str_faceId = Detect(str_tempTaget).json()[0]['faceId']
# str_faceListId = "tmepfacelistid"
# int_maxNum = 1
# str_mode = "matchFace"

# result_FS = FindSimilar(str_faceId, str_faceListId, int_maxNum, str_mode)
# print(json.dumps(result_FS.json(), sort_keys=True, indent=2))

#-- M-3

#-- M-4
#---- parameters
# li_targetFaces = list()
# for i in range(len(json_response_faces)):
#     li_targetFaces.append({'faceId': json_response_faces[i]["faceId"], 
#                      'faceRectangle': json_response_faces[i]["faceRectangle"], 
#                      'candidatesId': '', 
#                      'name': ''})#record faceID with their corresponding name
    
# str_groupId = str_personGroupId_test02

# li_targetFaces = Identify(li_targetFaces, str_groupId)
# print(json.dumps(li_targetFaces, sort_keys=True, indent=2))
# #print(len(li_targetFaces))

#-- M-5

#-- O-1
# j_faces = result_detect.json()
# temp = getRectangle(j_faces[0])

# print(temp)
# print(type(temp))
# print(temp[0][0])

#-- O-2
#---- parameters
# str_targetImg = "https://i1.wp.com/popbee.com/image/2019/07/fhdhdfhdfh.jpg"
# j_faces = result_detect.json()

# result_img = drawRect(str_targetImg, j_faces)
# imshow(result_img)

#-- O-3
#---- parameters

# str_groupId = str_personGroupId_test02

# li_targetFaces = getIdentifyName(li_targetFaces, str_groupId)
# print(json.dumps(li_targetFaces, sort_keys=True, indent=2))

#-- O-4
#---- parameters
# img = result_img
# #li_targetFaces = 

# re_show = showName(li_targetFaces, img)
# imshow(re_show)


# In[15]:


# str_faceListId = "tmepfacelistid"
# str_FLfaceId = "dc370326-1d2a-4d4a-a896-383cb0312c9d"

# getURL = getSimilarImgUrl(str_FLfaceId, str_faceListId)
# print(getURL)


# In[78]:


### test show age
#-- 1 detect
# result_detect = Detect(str_targetImg)
# j_faces = result_detect.json()

# #print(json.dumps(j_faces, sort_keys=True, indent=2))

# re_img = showAge(str_targetImg, j_faces)
# imshow(re_img)
# re_img.show()


# In[116]:


### test show emotion

# result_detect = Detect(str_targetImg)
# j_faces = result_detect.json()

#re_emo = showEmotions(str_targetImg, j_faces)
# plt.figure(figsize = (15,8))
# plt.axis('off')

# # plt.gca().xaxis.set_major_locator(plt.NullLocator()) 
# # plt.gca().yaxis.set_major_locator(plt.NullLocator()) 
# plt.subplots_adjust(top=1,bottom=0,left=0,right=1,hspace=0,wspace=0) 
# plt.margins(0,0)

# imshow(re_emo)
#re_emo.show()

# saveImg(re_emo, "test")


# In[6]:


### test verify

# img1 = "http://i.epochtimes.com/assets/uploads/2018/11/1811282149341487-600x400.jpg"
# img2 = "https://fpscdn.yam.com/news/201702/0e/b7/58a50182c0eb7.jpg"

# str_faceId1 = Detect(img1).json()[0]['faceId']
# str_faceId2 = Detect(img2).json()[0]['faceId']

# result_verify = Verify(str_faceId1, str_faceId2)

# print(json.dumps(result_verify.json()))


# In[ ]:




