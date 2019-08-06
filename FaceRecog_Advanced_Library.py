import requests
import json
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
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


imgSavePath = 'C:/Users/user/Desktop/Faceapi/Flask/test/Pictures/imgno'
tempFileName = 1
def DetectFace(str_targetImg, detectMode):
    global tempFileName
    filename=imgSavePath+str(tempFileName)+'.jpg'
    #-- 1. detect
    result_detect = bl.Detect(str_targetImg)
    j_faces = result_detect.json()
    
    #-- 2. deal with different mode
    if detectMode == 0:
        result_img =  bl.drawRect(str_targetImg, j_faces)
    
    #result_img.savefig('test.jpg')
    #plt.savefig('test.jpg')
    plt.imshow(result_img)
    plt.axis('off')
    #plt.show()
    plt.savefig(filename)#儲存圖片
    tempFileName=tempFileName+1
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





