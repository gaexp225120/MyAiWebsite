import requests
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches
from io import BytesIO
import os


subscription_key = "cfb82ad9df704e27a3f5aa64a249188f" #DSFace API
face_api_url = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/detect'

image_path = os.path.join('C:/Users/user/Desktop/Faceapi/images.jpg')
image_data = open(image_path, "rb")

def config():
    print("Call Config")
    return subscription_key, face_api_url
subscription_key, face_api_url = config();

headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion'
}

response = requests.post(face_api_url, params=params, headers=headers, data=image_data)
response.raise_for_status()
faces = response.json()


#Display the image
def im():
    image_orig = open(image_path, "rb").read()
    image = Image.open(BytesIO(image_orig))
    plt.figure(figsize=(12, 12))
    ax = plt.imshow(image, alpha=1)
    for face in faces:
        fr = face["faceRectangle"]
        fa = face["faceAttributes"]
        origin = (fr["left"], fr["top"])
        p = patches.Rectangle(
            origin, fr["width"], fr["height"], fill=False, linewidth=2, color='r')
        plt.text(origin[0], origin[1], "%s, %d " % (fa["gender"], fa["age"]),
                 fontsize=30, color='r', weight="bold", va="bottom")
        ax.axes.add_patch(p)
    plt.show()
    plt.savefig("img1.png")
print(im())
