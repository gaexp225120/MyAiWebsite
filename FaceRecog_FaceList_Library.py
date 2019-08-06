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
#** Project: FaceRecog_FaceList_Library                              **
#** Creator: Judy Tang                                               **
#** Start Date: 2019/07/30                                           **
#** Description: library of Face List functions                      **
#**********************************************************************


# In[ ]:


#*************************
#** Content **************
#*************************
#**
#** -- FaceList --
#** FL - 1 createFaceList(str_faceListId, str_FlistName, str_userData, str_recogModel)
#**    - 2 listAllFaceList()
#**    - 3 deleteFaceList(str_faceListId)
#**    - 4 deleteFListALL()
#**    - 5 getFaceList(str_faceListId)
#**    - 6 updateFaceList(str_faceListId, str_FlistName, str_userData)
#**    - 7 addFLFace(str_faceListId, li_img)
#**    - 8 deleteFLFace(str_faceListId, str_FLfaceId)
#**    - 9 deleteFLFaceALL(str_faceListId)
#**
#*************************


# In[1]:


### Basic Setting

import requests
import json
from matplotlib.pyplot import imshow
import cognitive_face as CF
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
#import FaceRecog_PersonGroup_Library as gl
#import FaceRecog_Basic_Library as bl
#import FaceRecog_Advanced_Library as al

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
image_url1 = 'http://i.epochtimes.com/assets/uploads/2018/11/1811282149341487-600x400.jpg'#林俊傑1
image_url2 = 'https://fpscdn.yam.com/news/201702/0e/b7/58a50182c0eb7.jpg'#林俊傑3

#-- Request headers
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': KEY,
}


# In[2]:


#*************************
#** Function *************
#*************************
#** FL - 1
#** Function Name: createFaceList(str, str, str, str)
#** Description: Create an empty face list with user-specified information.[HTTP Method: PUT]
#** Parameters: 
#** -- str_faceListId: An Id for new faceList.
#** -- str_listName: A name for new faceList.
#** -- str_userData: optional. Describe this faceList.
#** -- str_recogModel: optional.Recognition model. The default value is "recognition_01".
#**
#*************************

def createFaceList(str_faceListId, str_FlistName, str_userData, str_recogModel):
    
    #-- Request body
    body = dict()
    body["name"] = str_FlistName
    body["userData"] = str_userData
    body["recognitionModel"] = str_recogModel
    body = str(body)
    
    #-- api url
    str_apiUrl_theFaceList = (BASE_URL + 'facelists/' + str_faceListId)
    
    response_createFList = requests.put(str_apiUrl_theFaceList, data=body, headers=headers)
    
    return response_createFList

#*************************


# In[3]:


#*************************
#** Function *************
#*************************
#** FL - 2
#** Function Name: listAllFaceList()
#** Description: List face lists’ information[HTTP Method: GET]
#** Parameters:
#**
#*************************

def listAllFaceList():
    
    #-- api url
    str_apiUrl_FaceList = (BASE_URL + 'facelists')

    response_listFL = requests.get(str_apiUrl_FaceList, headers=headers)

    return response_listFL

#*************************


# In[4]:


#*************************
#** Function *************
#*************************
#** FL - 3
#** Function Name: deleteFaceList(str)
#** Description: Delete a specified face list[HTTP Method: DELETE]
#** Parameters: 
#** -- str_faceListId: the faceList id want to delete.
#**
#*************************

def deleteFaceList(str_faceListId):
    
    #-- api url
    str_apiUrl_theFaceList = (BASE_URL + 'facelists/' + str_faceListId)

    response_deleteFaceList = requests.delete(str_apiUrl_theFaceList, headers=headers)

    return response_deleteFaceList

#*************************


# In[5]:


#*************************
#** Function *************
#*************************
#** FL - 4
#** Function Name: deleteFListALL()
#** Description: Delete all face list[HTTP Method: DELETE] - ALL
#** Parameters: (none)
#**
#*************************

def deleteFListALL():
    
    #-- list for storage all reponse
    li_response = list()
    
    #-- list first than do delete for every group
    getAllFList = listAllFaceList()
    json_FList = getAllFList.json()
    
    for i in range(len(json_FList)):
        FListId_del = json_FList[i]["faceListId"]

        result_delFList = deleteFaceList(FListId_del)
        
        li_response.append({'groupId': FListId_del, 
                            'responseMessege': result_delFList})
    return li_response

#*************************


# In[15]:


#*************************
#** Function *************
#*************************
#** FL - 5
#** Function Name: getFaceList(str)
#** Description: PersonGroup - Get[HTTP Method: GET]
#** Parameters: 
#** -- str_faceListId: the FaceList id want to retrieve information.
#**
#*************************

def getFaceList(str_faceListId):
    
    #-- api url
    str_apiUrl_theFaceList = (BASE_URL + 'facelists/' + str_faceListId)

    response_GetFaceList = requests.get(str_apiUrl_theFaceList, headers=headers)
    
    return response_GetFaceList
    
#*************************


# In[7]:


#*************************
#** Function *************
#*************************
#** FL - 6
#** Function Name: updateFaceList(str, str, str)
#** Description: FaceList - Update[HTTP Method: PATCH]
#** Parameters: 
#** -- str_faceListId: faceListId of the person group to be updated.
#** -- str_FlistName: Target FaceList display name.
#** -- str_userData: optional.(?) Attach userData to FaceList.
#**
#*************************

def updateFaceList(str_faceListId, str_FlistName, str_userData):
    
    #-- Request body
    body = dict()
    body["name"] = str_FlistName
    body["userData"] = str_userData
    body = str(body)
    
    #-- api url
    str_apiUrl_theFaceList = (BASE_URL + 'facelists/' + str_faceListId)
    
    #--
    response_updateFList = requests.patch(str_apiUrl_theFaceList, data=body, headers=headers)
    
    return response_updateFList

#*************************


# In[8]:


#*************************
#** Function *************
#*************************
#** FL - 7
#** Function Name: addFLFace(str, str, li)
#** Description: FaceList - Add Face[HTTP Method: POST]
#** Parameters: 
#** -- str_faceListId: Specifying the person group containing the target person.
#** -- li_img: a list include all faces want to add.
#**
#*************************

def addFLFace(str_faceListId, li_img):
    
    #-- list for storage all reponse
    li_response = []
    
    #-- Requet url
    str_apiUrl_theFLFace = (BASE_URL + 'facelists/' + str_faceListId 
                                + '/persistedFaces')

    #-- add images by for loop
    for image in li_img:
        #-- Request body
        body = dict()
        body["url"] = image
        body = str(body)
        
        #-- Request parameters
        params_detect = {
            'faceListId': str_faceListId,
            'userData': image,
        }
        
        #-- call api
        response_addFace = requests.post(str_apiUrl_theFLFace, params=params_detect, data=body, headers=headers)
        
        li_response.append({"imgUrl": image, 
                            "responseMessege": response_addFace.json()})
       
    return li_response

#*************************


# In[9]:


#*************************
#** Function *************
#*************************
#** FL - 8
#** Function Name: deleteFLFace(str, str, str)
#** Description: FaceList - Delete Face[HTTP Method: DELETE]
#** Parameters: 
#** -- str_faceListId: Specifying the FaceList that the target persisted face belong to.
#** -- str_FLfaceId: The persisted face to remove.
#**
#*************************

def deleteFLFace(str_faceListId, str_FLfaceId):
    
    #-- api url
    str_apiUrl_theFLFace = (BASE_URL + 'facelists/' + str_faceListId
                                   + '/persistedFaces/' + str_FLfaceId)
    
    response_delFace = requests.delete(str_apiUrl_theFLFace, headers=headers)
    
    return response_delFace

#*************************


# In[10]:


#*************************
#** Function *************
#*************************
#** FL - 9
#** Function Name: deleteFLFaceALL(str, str)
#** Description: FaceList - Delete Face[HTTP Method: DELETE] - ALL
#** Parameters: 
#** -- str_faceListId: the FaceList that want to clean up.
#**
#*************************

def deleteFLFaceALL(str_faceListId):
    
    #-- list for storage all reponse
    li_response = []
    
    #-- use getPerson() to get all face belongs to he/her
    getTheFList = getFaceList(str_faceListId)
    FLFacesId = getTheFList.json()["persistedFaces"]
    
    #-- do delete to every face
    for i in range(len(FLFacesId)):
        
        str_FLfaceId = FLFacesId[i]["persistedFaceId"]
        
        result_delFLFace = deleteFLFace(str_faceListId, str_FLfaceId)
        
        li_response.append({"FacesId": str_FLfaceId, 
                            "responseMessege": result_delFLFace})
    
    return li_response
    
#*************************


# In[31]:


### test create & add face
# str_faceListId = "tmepfacelistid"
# str_FlistName = "TestFaceList"
# str_userData = "list2"
# str_recogModel = "recognition_02"

# li_img = ["https://pbs.twimg.com/profile_images/578900195812900864/r1t12Hyb.jpeg",
#           "https://i.pinimg.com/736x/1c/ae/a2/1caea20e681ce50e375d2524a66808c3.jpg",
#           "http://www.newwide.com/AI/Sunny1.jpg",
#           "https://vignette.wikia.nocookie.net/friends/images/f/f5/JoeyTribbiani.jpg",
#           "http://www2.pictures.zimbio.com/mp/Cw-NvzmXZ9Wl.jpg"]

# #-- FL-1
# # result_create = createFaceList(str_faceListId, str_FlistName, str_userData, str_recogModel)
# # print(result_create)

# #-- FL-7
# #result_addFLface = addFLFace(str_faceListId, li_img)
# #print(result_addFLface)
# print(json.dumps(result_addFLface, sort_keys=True, indent=2))


# In[36]:


### test list & get

# str_faceListId = "tmepfacelistid"

# #-- FL-2
# allFLlist = listAllFaceList()

# print(json.dumps(allFLlist.json(), sort_keys=True, indent=2))

# #-- FL-5
# getFL = getFaceList(str_faceListId)

# print(json.dumps(getFL.json(), sort_keys=True, indent=2))


# In[22]:


### test deletes

# str_faceListId = "tmepfacelistid"
# #str_FLfaceId = "c368883a-e590-464d-ad3e-012f9487a8e6"

# #-- FL-3
# result_delFL = deleteFaceList(str_faceListId)
# print(result_delFL)

#-- FL-8
# result_del = deleteFLFace(str_faceListId, str_FLfaceId)

# print(result_del)

#-- FL-9
# result_delAll = deleteFLFaceALL(str_faceListId)
# print(result_delAll)


# In[34]:


### test update
# str_faceListId = "tmepfacelistid"
# str_FlistName = "TestFaceList222"
# str_userData = "list2 update"

# result_updateFL = updateFaceList(str_faceListId, str_FlistName, str_userData)

# print(result_updateFL)


# In[ ]:




