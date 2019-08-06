#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#**********************************************************************
#********************** Program Note Description **********************
#**********************************************************************
#
# Description: set out the rules of comments and coding
# [Name] -- camelCase_classify
# -- Program File Name: 'Suject'_'date'_'subtitle(if need)'
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
#** Project: FaceRecog_PersonGroup_Library                           **
#** Creator: Judy Tang                                               **
#** Start Date: 2019/07/23                                           **
#** Description: library of PersonGroup functions                    **
#**********************************************************************


# In[ ]:


#*************************
#** Content **************
#*************************
#**
#** -- Group --
#** G - 1 createGroup(str_groupId, str_groupName, str_userData, str_recogModel)
#**   - 2 listAllGroup(str_start, str_top, str_reRecogModel)
#**   - 3 deleteGroup(str_groupId)
#**   - 4 deleteALLGroup()
#**   - 5 getGroup(str_groupId)
#**   - 6 updateGroup(str_groupId, str_groupName, str_userData)
#**   - 7 trainGroup(str_groupId)
#** -- Person --
#** P - 1 createPerson(str_groupId, str_personName, str_userData)
#**   - 2 listPersonInGroup(str_groupId)
#**   - 3 deletePerson(str_groupId, str_personId)
#**   - 4 deleteALLPerson(str_groupId)
#**   - 5 getPerson(str_groupId, str_personId)
#**   - 6 updatePerson(str_groupId, str_personId, str_personName, str_userData)
#** -- Face --
#** F - 1 addFace(str_groupId, str_personId, li_img)
#**   - 2 getFace(str_groupId, str_personId, str_faceId)
#**   - 3 deleteFace(str_groupId, str_personId, str_faceId)
#**   - 4 deleteALLFace(str_groupId, str_personId)
#**   - 5 updateFace(str_groupId, str_personId, str_faceId, str_userData)
#**
#*************************


# In[33]:


### Basic Setting

import requests
import json
from matplotlib.pyplot import imshow
import cognitive_face as CF
from io import BytesIO #for open graphics??
from PIL import Image, ImageDraw, ImageFont

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
str_personId_Rachel = 'd662c38e-9c2e-491c-9987-5c12172874bd'
str_personId_Monica = 'd894489a-f317-414d-80ff-59cbda5d6213'
str_personId_Phoebe = '90d2f0d6-a394-48e0-90fa-88fdb2b1f915'
str_personId_Joey = '845cf846-9765-4e4c-8144-4b553dbff3ad'
str_personId_Chandler = 'bc915611-707c-4686-85b3-3190bcf157e3'
str_personId_Ross = 'c398cffc-9b8b-4ed6-9410-96eac17e1a1e'

#-- Request headers
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': KEY,
}


# In[2]:


#*************************
#** Function *************
#*************************
#** G - 1
#** Function Name: createGroup(str, str, str, str)
#** Description: PersonGroup - Create[HTTP Method: PUT]
#** Parameters: 
#** -- str_groupId: An Id for new group.
#** -- str_groupName: A name for new group.
#** -- str_userData: optional. Describe this group.
#** -- str_recogModel: optional.Recognition model. The default value is "recognition_01".
#**
#*************************

def createGroup(str_groupId, str_groupName, str_userData, str_recogModel):
    
    #-- Request body
    body = dict()
    body["name"] = str_groupName
    body["userData"] = str_userData
    body["recognitionModel"] = str_recogModel
    body = str(body)
    
    #-- api url
    str_apiUrl_theGroup = (BASE_URL + 'persongroups/' + str_groupId)
    
    response_createGroup = requests.put(str_apiUrl_theGroup, data=body, headers=headers)
    
    return response_createGroup

#*************************


# In[3]:


#*************************
#** Function *************
#*************************
#** G - 2
#** Function Name: listAllGroup(str, str, str)
#** Description: PersonGroup - List[HTTP Method: GET]
#** Parameters: 
#** -- str_start: optional. Default is empty.
#** -- str_top: optional. The number of person groups to list, ranging in [1, 1000]. Default is 1000.
#** -- str_reRecogModel: optional. Return 'recognitionModel' or not. The default value is false.
#**
#*************************

def listAllGroup(str_start, str_top, str_reRecogModel):
    
    #-- api url
    str_apiUrl_Group = (BASE_URL + 'persongroups/' + '?' + str_start + '&' + str_top + '&' + str_reRecogModel)

    response_listGroup = requests.get(str_apiUrl_Group, headers=headers)

    return response_listGroup

#*************************


# In[4]:


#*************************
#** Function *************
#*************************
#** G - 3
#** Function Name: deleteGroup(str)
#** Description: PersonGroup - Delete[HTTP Method: DELETE]
#** Parameters: 
#** -- str_groupId: the group id want to delete.
#**
#*************************

def deleteGroup(str_groupId):
    
    #-- api url
    str_apiUrl_theGroup = (BASE_URL + 'persongroups/' + str_groupId)

    response_deleteGroup = requests.delete(str_apiUrl_theGroup, headers=headers)

    return response_deleteGroup

#*************************


# In[5]:


#*************************
#** Function *************
#*************************
#** G - 4
#** Function Name: deleteALLGroup()
#** Description: PersonGroup - Delete[HTTP Method: DELETE] - ALL
#** Parameters: (none)
#**
#*************************

def deleteALLGroup():
    
    #-- list for storage all reponse
    li_response = list()
    
    #-- list first than do delete for every group
    getGroupList = listAllGroup("", "", "")
    json_GroupList = getGroupList.json()
    
    for i in range(len(json_GroupList)):
        groupId_del = json_GroupList[i]["personGroupId"]

        result_delGroup = deleteGroup(groupId_del)
        
        li_response.append({'groupId': groupId_del, 
                            'responseMessege': result_delGroup})
    return li_response

#*************************


# In[6]:


#*************************
#** Function *************
#*************************
#** G - 5
#** Function Name: getGroup(str)
#** Description: PersonGroup - Get[HTTP Method: GET]
#** Parameters: 
#** -- str_groupId: the group id want to retrieve information.
#**
#*************************

def getGroup(str_groupId):
    
    #-- api url
    str_apiUrl_theGroup = (BASE_URL + 'persongroups/' + str_groupId)

    response_GetGroup = requests.get(str_apiUrl_theGroup, headers=headers)

    #-- print the result
    #print(json.dumps(response_GetGroup.json(), sort_keys=True, indent=2))
    
    return response_GetGroup
    
#*************************


# In[7]:


#*************************
#** Function *************
#*************************
#** G - 6
#** Function Name: updateGroup(str, str, str)
#** Description: PersonGroup - Update[HTTP Method: PATCH]
#** Parameters: 
#** -- str_groupId: personGroupId of the person group to be updated.
#** -- str_groupName: Target group display name.
#** -- str_userData: optional.(?) Attach userData to person group.
#**
#*************************

def updateGroup(str_groupId, str_groupName, str_userData):
    
    #-- Request body
    body = dict()
    body["name"] = str_groupName
    body["userData"] = str_userData
    body = str(body)
    
    #-- api url
    str_apiUrl_theGroup = (BASE_URL + 'persongroups/' + str_groupId)
    
    #--
    response_updateGroup = requests.patch(str_apiUrl_theGroup, data=body, headers=headers)
    
    return response_updateGroup

#*************************


# In[8]:


#*************************
#** Function *************
#*************************
#** G - 7
#** Function Name: trainGroup(str)
#** Description: PersonGroup - Train[HTTP Method: POST]
#** Parameters: 
#** -- str_groupId: Target person group to be trained.
#**
#*************************

def trainGroup(str_groupId):
    
    #-- Request body
    body = dict()
    
    #-- api url
    str_apiUrl_trainGroup = (BASE_URL + 'persongroups/' + str_groupId + '/train')
    
    #-- 
    response_trainGroup = requests.post(str_apiUrl_trainGroup, data=body, headers=headers) 
    
    return response_trainGroup

#*************************


# In[9]:


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ GROUP ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV PERSON VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV


# In[10]:


#*************************
#** Function *************
#*************************
#** P - 1
#** Function Name: createPerson(str, str, str)
#** Description: PersonGroup Person - Create[HTTP Method: POST]
#** Parameters: 
#** -- str_groupId: the target person group to create the person.
#** -- str_personName: the name for new person.
#** -- str_userData: optional. Describe this person.
#**
#*************************

def createPerson(str_groupId, str_personName, str_userData):
    
    #-- Request body
    body = dict()
    body["name"] = str_personName
    body["userData"] = str_userData
    body = str(body)
    
    #-- Requet url
    str_apiUrl_Person = (BASE_URL + 'persongroups/' + str_groupId 
                                  + '/persons')

    #--
    response_CreatePerson = requests.post(str_apiUrl_Person, data=body, headers=headers)
    
    #print(json.dumps(response_CreatePerson.json(), sort_keys=True, indent=2))
    
    return response_CreatePerson

#*************************


# In[11]:


#*************************
#** Function *************
#*************************
#** P - 2
#** Function Name: listPersonInGroup(str)
#** Description: PersonGroup Person - List[HTTP Method: GET]
#** Parameters: 
#** -- str_groupId: personGroupId of the target person group.
#**
#*************************

def listPersonInGroup(str_groupId):
    
    #-- Requet url
    str_apiUrl_Person = (BASE_URL + 'persongroups/' + str_groupId 
                                  + '/persons')

    response_listPersonInGroup = requests.get(str_apiUrl_Person, headers=headers)

    #-- print the result
    #print(json.dumps(response_listPersonInGroup.json(), sort_keys=True, indent=2))
    
    return response_listPersonInGroup
    
#*************************


# In[12]:


#*************************
#** Function *************
#*************************
#** P - 3
#** Function Name: deletePerson(str, str)
#** Description: PersonGroup Person - Delete[HTTP Method: DELETE]
#** Parameters: 
#** -- str_groupId: Specifying the person group containing the person.
#** -- str_personId: The target personId to delete.
#**
#*************************

def deletePerson(str_groupId, str_personId):
    
    #---- api url
    str_apiUrl_thePerson = (BASE_URL + 'persongroups/' + str_groupId 
                                     + '/persons/' + str_personId)
    
    response_delPerson = requests.delete(str_apiUrl_thePerson, headers=headers)
    
    return response_delPerson

#*************************


# In[13]:


#*************************
#** Function *************
#*************************
#** P - 4
#** Function Name: deleteALLPerson(str)
#** Description: PersonGroup Person - Delete[HTTP Method: DELETE] - ALL
#** Parameters: 
#** -- str_groupId: the target groupId to clean up.
#**
#*************************

def deleteALLPerson(str_groupId):
    
    #-- list for storage all reponse
    li_response = []
    
    #-- get all ids in the group first
    getPersonList = listPersonInGroup(str_groupId)
    json_personList = getPersonList.json()
    
    #-- do delete for every person
    for i in range(len(json_personList)):
        str_personId_del = json_personList[i]["personId"]

        result_delPerson = deletePerson(str_groupId, str_personId_del)
        
        li_response.append({'personId': str_personId_del, 
                            'responseMessege': result_delPerson})
        
    return li_response
    
#*************************


# In[14]:


#*************************
#** Function *************
#*************************
#** P - 5
#** Function Name: getPerson(str, str)
#** Description: PersonGroup Person - Get[HTTP Method: GET]
#** Parameters: 
#** -- str_groupId: Specifying the person group containing the target person.
#** -- str_personId: Specifying the target person.
#**
#*************************

def getPerson(str_groupId, str_personId):
    
    #-- api url
    str_apiUrl_thePerson = (BASE_URL + 'persongroups/' + str_groupId 
                                     + '/persons/' + str_personId)

    response_GetPerson = requests.get(str_apiUrl_thePerson, headers=headers)

    #-- print the result
    #print(json.dumps(response_GetPerson.json(), sort_keys=True, indent=2))
    
    return response_GetPerson
    
#*************************


# In[15]:


#*************************
#** Function *************
#*************************
#** P - 6
#** Function Name: updatePerson(str, str, str, str)
#** Description: PersonGroup Person - Update[HTTP Method: PATCH]
#** Parameters: 
#** -- str_groupId: Specifying the person group containing the target person.
#** -- str_personId: personId of the target person.
#** -- str_personName: Target person's display name.
#** -- str_userData: optional.(?) Attach userData to person.
#**
#*************************

def updatePerson(str_groupId, str_personId, str_personName, str_userData):
    
    #-- Request body
    body = dict()
    body["name"] = str_personName
    body["userData"] = str_userData
    body = str(body)
    
    #-- api url
    str_apiUrl_thePerson = (BASE_URL + 'persongroups/' + str_groupId 
                                     + '/persons/' + str_personId)
    
    #--
    response_updatePerson = requests.patch(str_apiUrl_thePerson, data=body, headers=headers)
    
    return response_updatePerson

#*************************


# In[16]:


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ PERSON ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV FACE VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV


# In[17]:


#*************************
#** Function *************
#*************************
#** F - 1
#** Function Name: addFace(str, str, li)
#** Description: PersonGroup Person - Add Face[HTTP Method: POST]
#** Parameters: 
#** -- str_groupId: Specifying the person group containing the target person.
#** -- str_personId: Target person that the face is added to.
#** -- li_img: a list include all faces want to add.
#**
#*************************

def addFace(str_groupId, str_personId, li_img):
    
    #-- list for storage all reponse
    li_response = []
    
    #-- Requet url
    str_apiUrl_Face = (BASE_URL + 'persongroups/' + str_groupId 
                                   + '/persons/' + str_personId 
                                   + '/persistedFaces')

    #-- add images by for loop
    for image in li_img:
        body = dict()
        body["url"] = image
        body = str(body)

        #-- call api
        response_addFace = requests.post(str_apiUrl_Face, data=body, headers=headers)
        
#         return_body = dict()
#         return_body["imgUrl"] = image
#         return_body["responseMessege"] = response_addFace.json()
        
        li_response.append({"imgUrl": image, 
                            "responseMessege": response_addFace.json()})
#         li_response.append(return_body)
        
    return li_response

#*************************


# In[18]:


#*************************
#** Function *************
#*************************
#** F - 2
#** Function Name: getFace(str, str, str)
#** Description: PersonGroup Person - Get Face[HTTP Method: GET]
#** Parameters: 
#** -- str_groupId: Specifying the person group containing the target person.
#** -- str_personId: Specifying the target person that the face belongs to.
#** -- str_faceId: The persistedFaceId of the target persisted face of the person.
#**
#*************************

def getFace(str_groupId, str_personId, str_faceId):
    
    #-- api url
    str_apiUrl_theFace = (BASE_URL + 'persongroups/' + str_groupId 
                                   + '/persons/' + str_personId 
                                   + '/persistedFaces/' + str_faceId)

    response_GetFace = requests.get(str_apiUrl_theFace, headers=headers)
    
    return response_GetFace
    
#*************************


# In[19]:


#*************************
#** Function *************
#*************************
#** F - 3
#** Function Name: deleteFace(str, str, str)
#** Description: PersonGroup Person - Delete Face[HTTP Method: DELETE]
#** Parameters: 
#** -- str_groupId: Specifying the person group containing the target person.
#** -- str_personId: Specifying the person that the target persisted face belong to.
#** -- str_faceId: The persisted face to remove.
#**
#*************************

def deleteFace(str_groupId, str_personId, str_faceId):
    
    #-- api url
    str_apiUrl_theFace = (BASE_URL + 'persongroups/' + str_groupId 
                                   + '/persons/' + str_personId 
                                   + '/persistedFaces/' + str_faceId)
    
    response_delFace = requests.delete(str_apiUrl_theFace, headers=headers)
    
    return response_delFace

#*************************


# In[20]:


#*************************
#** Function *************
#*************************
#** F - 4
#** Function Name: deleteALLFace(str, str)
#** Description: PersonGroup Person - Delete Face[HTTP Method: DELETE] - ALL
#** Parameters: 
#** -- str_groupId: Specifying the person group containing the target person.
#** -- str_personId: the person that want to clean up.
#**
#*************************

def deleteALLFace(str_groupId, str_personId):
    
    #-- list for storage all reponse
    #li_response = list()
    li_response = []
    
    #-- use getPerson() to get all face belongs to he/her
    getThePerson = getPerson(str_groupId, str_personId)
    personFacesId = getThePerson.json()["persistedFaceIds"]
    
    #-- do delete to every face
    for i in range(len(personFacesId)):
        
        str_faceId = personFacesId[i]
        
        result_delFace = deleteFace(str_groupId, str_personId, str_faceId)
        
        li_response.append({"FacesId": str_faceId, 
                            "responseMessege": result_delFace})
    
    return li_response
    
#*************************


# In[21]:


#*************************
#** Function *************
#*************************
#** F - 5
#** Function Name: updateFace(str, str, str, str)
#** Description: PersonGroup Person - Update Face[HTTP Method: PATCH]
#** Parameters: 
#** -- str_groupId: Specifying the person group containing the target person.
#** -- str_personId: personId of the target person.
#** -- str_faceId: persistedFaceId of target face, which is persisted and will not expire.
#** -- str_userData: optional. Attach userData to person's persisted face.
#**
#*************************

def updateFace(str_groupId, str_personId, str_faceId, str_userData):
    
    #-- Request body
    body = dict()
    body["userData"] = str_userData
    body = str(body)
    
    #-- api url
    str_apiUrl_theFace = (BASE_URL + 'persongroups/' + str_groupId 
                                   + '/persons/' + str_personId 
                                   + '/persistedFaces/' + str_faceId)
    
    #--
    response_updateFace = requests.patch(str_apiUrl_theFace, data=body, headers=headers)
    
    return response_updateFace

#*************************


# In[ ]:


### Example - [Group Stucture]

#-- FRIENDS -- Rachel Green:{"https://pixel.nymag.com/imgs/daily/vulture/2014/12/17/17-rachel-green-jewish.w700.h700.jpg",
#--                          "https://pbs.twimg.com/profile_images/578900195812900864/r1t12Hyb.jpeg",
#--                          "https://i.pinimg.com/originals/ac/de/c9/acdec92f459960f821e659dadc0c6de2.jpg"}
#--         -- Monica Geller:{"https://upload.wikimedia.org/wikipedia/en/thumb/d/d0/Courteney_Cox_as_Monica_Geller.jpg/220px-Courteney_Cox_as_Monica_Geller.jpg",
#--                           "https://thespinoff.co.nz/wp-content/uploads/2016/05/f4asdasdasd-850x510.jpg",
#--                           "https://friendv.files.wordpress.com/2013/08/monica-geller.jpg",
#--                           "http://images6.fanpop.com/image/photos/39500000/Monica-Geller-friends-39567785-500-735.jpg",
#--                           "http://www2.pictures.zimbio.com/mp/Cw-NvzmXZ9Wl.jpg"}
#--         -- Phoebe Buffay:{"https://static-22.sinclairstoryline.com/resources/media/55b260ef-2382-40bc-b96d-6b17f10eec64-smallScale_wenn2710740.jpg"}
#--         -- Joey Tribbiani:{"https://upload.wikimedia.org/wikipedia/en/thumb/d/da/Matt_LeBlanc_as_Joey_Tribbiani.jpg/220px-Matt_LeBlanc_as_Joey_Tribbiani.jpg",
#--                            "https://vignette.wikia.nocookie.net/friends/images/f/f5/JoeyTribbiani.jpg",
#--                            "https://imgix.bustle.com/uploads/image/2017/8/22/4dbabff7-c8bd-4817-abff-a413fd946e49-joey-tribbiani-pineapple.jpg"}
#--         -- Chandler Bing:{"https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/Matthew_Perry_as_Chandler_Bing.jpg/220px-Matthew_Perry_as_Chandler_Bing.jpg",
#--                           "https://static2.srcdn.com/wordpress/wp-content/uploads/2019/03/Chandler-Bing-Friends-1.jpg",
#--                           "https://i.pinimg.com/736x/1c/ae/a2/1caea20e681ce50e375d2524a66808c3.jpg",
#--                           "https://pbs.twimg.com/profile_images/378800000040987447/4464131179ce9435f81942cd7fbaa8cf_400x400.jpeg",
#--                           "https://img.buzzfeed.com/buzzfeed-static/static/2014-05/campaign_images/webdr02/12/11/the-33-best-chandler-bing-one-liners-1-24600-1399910198-37_big.jpg"}
#--         -- Ross Geller:{"https://www.thesun.co.uk/wp-content/uploads/2017/08/nintchdbpict000003441959.jpg"}


# In[ ]:


#*************************
#** Example **************
#*************************
#-- Example for create a person group, create person and add feces


# In[22]:


# ### G - 1 createGroup()

# #-- parameters
# str_groupId = "groupid_test02"
# str_groupName = "FRIENDS"
# str_userData = "All friends cast"
# str_recogModel = "recognition_02"

# #--
# result_createGroup = createGroup(str_groupId, str_groupName, str_userData, str_recogModel)

# print(result_createGroup)


# In[23]:


# ### G - 2 listAllGroup()

# #-- parameters
# str_start = ""
# str_top = ""
# str_reRecogModel = ""

# #--
# result_listGroup = listAllGroup(str_start, str_top, str_reRecogModel)

# #print(result_listGroup)
# print(json.dumps(result_listGroup.json(), sort_keys=True, indent=2))


# In[ ]:


### G - 3 deleteGroup()

# #-- parameters
# str_groupId = ""

# #--
# result_delGroup = deleteGroup(str_groupId)

# print(result_delGroup)


# In[ ]:


### G - 4 deleteALLGroup()
#-- NEVER TRY!!!

#--
#result_delALLGroup = deleteALLGroup()

#print(result_delALLGroup)


# In[24]:


# ### G - 5 getGroup()

# #-- parameters
# str_groupId = str_personGroupId_test02

# #--
# result_Group = getGroup(str_groupId)

# print(json.dumps(result_Group.json(), sort_keys=True, indent=2))


# In[26]:


# ### G - 6 updateGroup()

# #-- parameters
# str_groupId = str_personGroupId_test02
# str_groupName = "FRIENDS"
# str_userData = "update user data test. All friends cast"

# #--
# result_updateGroup = updateGroup(str_groupId, str_groupName, str_userData)

# print(result_updateGroup)


# In[47]:


# ### G - 7 trainGroup()

# #-- parameters
# str_groupId = str_personGroupId_test02

# #--
# result_trainGroup = trainGroup(str_groupId)

# print(result_trainGroup)
# print("RESPONSE:" + str(result_trainGroup.status_code))


# In[32]:


# ### P - 1 createPerson()

# #-- parameters
# str_groupId = str_personGroupId_test02
# # str_personName = "Rachel Green"
# # str_userData = "Jennifer Aniston"

# # str_personName = "Monica Geller"
# # str_userData = "Courteney Cox"

# # str_personName = "Phoebe Buffay"
# # str_userData = "Lisa Kudrow"

# # str_personName = "Joey Tribbiani"
# # str_userData = "Matthew LeBlanc"

# # str_personName = "Chandler Bing"
# # str_userData = "Matthew Perry"

# str_personName = "Ross Geller"
# str_userData = "David Schwimmer"

# #--
# result_createPerson = createPerson(str_groupId, str_personName, str_userData)

# #print(result_createGroup)
# print(json.dumps(result_createPerson.json(), sort_keys=True, indent=2))


# In[45]:


# ### P - 2 listPersonInGroup()

# #-- parameters
# str_groupId = str_personGroupId_test02

# #--
# result_listPerson = listPersonInGroup(str_groupId)

# print(json.dumps(result_listPerson.json(), sort_keys=True, indent=2))


# In[ ]:


# ### P - 3 deletePerson()

# #-- parameters
# #str_groupId = str_personGroupId_test02
# str_personId = str_personId_Phoebe

# #--
# result_delPerson = deletePerson(str_groupId, str_personId)

# print(result_delPerson)


# In[ ]:


# ### P - 4 deleteALLPerson()

# #-- parameters
# #str_groupId = str_personGroupId_test02

# #--
# result_delALLPerson = deleteALLPerson(str_groupId)

# print(result_delALLPerson)


# In[37]:


# ### P - 5 getPerson()

# #-- parameters
# str_groupId = str_personGroupId_test02
# str_personId = str_personId_Phoebe

# #--
# result_Person = getPerson(str_groupId, str_personId)

# print(json.dumps(result_Person.json(), sort_keys=True, indent=2))


# In[36]:


# ### P - 6 updatePerson()

# #-- parameters
# str_groupId = str_personGroupId_test02
# str_personId = str_personId_Phoebe
# str_personName = "Phoebe Buffay"
# str_userData = "Lisa Valerie Kudrow"

# #--
# result_updatePerson = updatePerson(str_groupId, str_personId, str_personName, str_userData)

# print(result_updatePerson)


# In[43]:


# ### F - 1 addFace()

# #-- parameters
# str_groupId = str_personGroupId_test02
# str_personId = str_personId_Ross

# #-- Rachel
# # li_img = ["https://pixel.nymag.com/imgs/daily/vulture/2014/12/17/17-rachel-green-jewish.w700.h700.jpg",
# #           "https://pbs.twimg.com/profile_images/578900195812900864/r1t12Hyb.jpeg",
# #           "https://i.pinimg.com/originals/ac/de/c9/acdec92f459960f821e659dadc0c6de2.jpg"]

# #-- Monica
# # li_img = ["https://upload.wikimedia.org/wikipedia/en/thumb/d/d0/Courteney_Cox_as_Monica_Geller.jpg/220px-Courteney_Cox_as_Monica_Geller.jpg",
# #           "https://thespinoff.co.nz/wp-content/uploads/2016/05/f4asdasdasd-850x510.jpg",
# #           "https://friendv.files.wordpress.com/2013/08/monica-geller.jpg",
# #           "http://images6.fanpop.com/image/photos/39500000/Monica-Geller-friends-39567785-500-735.jpg",
# #           "http://www2.pictures.zimbio.com/mp/Cw-NvzmXZ9Wl.jpg"]

# #-- Phoebe
# # li_img = ["https://static-22.sinclairstoryline.com/resources/media/55b260ef-2382-40bc-b96d-6b17f10eec64-smallScale_wenn2710740.jpg"]

# #-- Joey
# # li_img = ["https://upload.wikimedia.org/wikipedia/en/thumb/d/da/Matt_LeBlanc_as_Joey_Tribbiani.jpg/220px-Matt_LeBlanc_as_Joey_Tribbiani.jpg",
# #         "https://vignette.wikia.nocookie.net/friends/images/f/f5/JoeyTribbiani.jpg",
# #         "https://imgix.bustle.com/uploads/image/2017/8/22/4dbabff7-c8bd-4817-abff-a413fd946e49-joey-tribbiani-pineapple.jpg"]

# #-- Chandler
# # li_img = ["https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/Matthew_Perry_as_Chandler_Bing.jpg/220px-Matthew_Perry_as_Chandler_Bing.jpg",
# #           "https://static2.srcdn.com/wordpress/wp-content/uploads/2019/03/Chandler-Bing-Friends-1.jpg",
# #           "https://i.pinimg.com/736x/1c/ae/a2/1caea20e681ce50e375d2524a66808c3.jpg",
# #           "https://pbs.twimg.com/profile_images/378800000040987447/4464131179ce9435f81942cd7fbaa8cf_400x400.jpeg",
# #           "https://img.buzzfeed.com/buzzfeed-static/static/2014-05/campaign_images/webdr02/12/11/the-33-best-chandler-bing-one-liners-1-24600-1399910198-37_big.jpg"]

# #-- Ross
# li_img = ["https://www.thesun.co.uk/wp-content/uploads/2017/08/nintchdbpict000003441959.jpg"]

# #--
# li_result_addFace = addFace(str_groupId, str_personId, li_img)

# print(json.dumps(li_result_addFace, sort_keys=True, indent=2))


# In[44]:


# ### F - 2 getFace()

# #-- parameters
# str_groupId = str_personGroupId_test02
# str_personId = str_personId_Ross
# str_faceId = "d575ff4c-75df-431b-8559-edd5d9e50545"

# #--
# result_Face = getFace(str_groupId, str_personId, str_faceId)

# print(json.dumps(result_Face.json(), sort_keys=True, indent=2))


# In[ ]:


# ### F - 3 deleteFace()

# #-- parameters
# #str_groupId = str_personGroupId_test02
# str_personId = str_personId_Rachel
# str_faceId = "2f54afde-0c4b-4340-ba5c-4ba409af4022"

# #--
# #result_delFace = deleteFace(str_groupId, str_personId, str_faceId)

# print(result_delFace)


# In[ ]:


# ### F - 4 deleteALLFace()

# #-- parameters
# #str_groupId = str_personGroupId_test02
# str_personId = str_personId_Rachel

# #--
# result_delAllFace = deleteALLFace(str_groupId, str_personId)

# print(result_delAllFace)


# In[46]:


# ### F - 5 updateFace()

# #-- parameters
# str_groupId = str_personGroupId_test02
# str_personId = str_personId_Ross
# str_faceId = "d575ff4c-75df-431b-8559-edd5d9e50545"
# str_userData = "test change user data"

# #--
# result_updateFace = updateFace(str_groupId, str_personId, str_faceId, str_userData)

# print(result_updateFace)


# In[ ]:




