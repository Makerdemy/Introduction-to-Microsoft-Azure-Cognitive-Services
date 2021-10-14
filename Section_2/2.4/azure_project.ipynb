{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pathlib import Path\n",
    "from urllib.parse import urlparse\n",
    "import requests\n",
    "import json\n",
    "from PIL import Image\n",
    "from io import BytesIO\n",
    "from matplotlib import patches\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "subscription_key = 'f9bee9c0e51545bab4e932a5cdf27ff4'\n",
    "face_api_url = 'https://mycogser1.cognitiveservices.azure.com/face/v1.0/detect'\n",
    "face_api_url_verify = 'https://mycogser1.cognitiveservices.azure.com/face/v1.0/verify'\n",
    "\n",
    "def annotate_image(image_url, subscription_key, api_url, show_face_id=False):\n",
    "\n",
    "    # The default header must include the sunbscription key\n",
    "    headers = {'Ocp-Apim-Subscription-Key': subscription_key}\n",
    "\n",
    "    params = {\n",
    "        'returnFaceId': 'true',\n",
    "        'returnFaceLandmarks': 'false',\n",
    "        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',\n",
    "    }\n",
    "\n",
    "    # Figure out if this is a local file or url\n",
    "    parsed_url = urlparse(image_url)\n",
    "    if parsed_url.scheme == 'file':\n",
    "        image_data = open(parsed_url.path, \"rb\").read()\n",
    "\n",
    "        # When making the request, we need to add a Content-Type Header\n",
    "        # and pass data instead of a url\n",
    "        headers['Content-Type']='application/octet-stream'\n",
    "        response = requests.post(api_url, params=params, headers=headers, data=image_data)\n",
    "\n",
    "        # Open up the image for plotting\n",
    "        image = Image.open(parsed_url.path)\n",
    "    else:\n",
    "        # Pass in the URL to the API\n",
    "        response = requests.post(api_url, params=params, headers=headers, json={\"url\": image_url})\n",
    "        image_file = BytesIO(requests.get(image_url).content)\n",
    "        image = Image.open(image_file)\n",
    "\n",
    "    faces = response.json()\n",
    "\n",
    "    fig, ax = plt.subplots(figsize=(10,10))\n",
    "\n",
    "    ax.imshow(image, alpha=0.6)\n",
    "    for face in faces:\n",
    "        fr = face[\"faceRectangle\"]\n",
    "        fa = face[\"faceAttributes\"]\n",
    "        origin = (fr[\"left\"], fr[\"top\"])\n",
    "        p = patches.Rectangle(origin, fr[\"width\"],\n",
    "                            fr[\"height\"], fill=False, linewidth=2, color='b')\n",
    "        ax.axes.add_patch(p)\n",
    "        ax.text(origin[0], origin[1], \"%s, %d\"%(fa[\"gender\"].capitalize(), fa[\"age\"]),\n",
    "                fontsize=16, weight=\"bold\", va=\"bottom\")\n",
    "\n",
    "        if show_face_id:\n",
    "            ax.text(origin[0], origin[1]+fr[\"height\"], \"%s\"%(face[\"faceId\"][:5]),\n",
    "            fontsize=12, va=\"bottom\")\n",
    "    ax.axis(\"off\")\n",
    "\n",
    "    # Explicitly closing image so it does not show in the notebook\n",
    "    plt.close()\n",
    "    return fig, faces\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'annotate_image' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-b0c6113f16c4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     15\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mjson\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     16\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 17\u001b[1;33m cousins_image, cousins = annotate_image('https://i.postimg.cc/vBQTs1XH/cousins-image.jpg',\n\u001b[0m\u001b[0;32m     18\u001b[0m                                             \u001b[0msubscription_key\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     19\u001b[0m                                             \u001b[0mface_api_url\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'annotate_image' is not defined"
     ]
    }
   ],
   "source": [
    "def face_compare(id_1, id_2, api_url):\n",
    "    \n",
    "    headers = {\n",
    "        'Content-Type': 'application/json',\n",
    "        'Ocp-Apim-Subscription-Key': subscription_key\n",
    "    }\n",
    "\n",
    "    body = {\"faceId1\": id_1, \"faceId2\": id_2}\n",
    "\n",
    "    params = {}\n",
    "    response = requests.post(api_url,\n",
    "                            params=params,\n",
    "                            headers=headers,\n",
    "                            json=body)\n",
    "    return response.json()\n",
    "\n",
    "cousins_image, cousins = annotate_image('https://i.postimg.cc/vBQTs1XH/cousins-image.jpg',\n",
    "                                            subscription_key,\n",
    "                                            face_api_url,\n",
    "                                            show_face_id=True)\n",
    "\n",
    "my_solo_image, me = annotate_image('https://i.postimg.cc/d0Ft27bm/my-solo-image.jpg',\n",
    "                                           subscription_key,\n",
    "                                           face_api_url,\n",
    "                                           show_face_id=True)\n",
    "\n",
    "cousins_image \n",
    "\n",
    "my_solo_image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "FaceIDs and corresponding ages of the Faces in the cousins image\n",
      "faceid0=  e4908769-db9b-449a-aa2c-0cf7a6d83928 AGE=  25.0\n",
      "faceid1=  9b47b03e-6a14-4549-8748-bcbd2a2f1edf AGE=  14.0\n",
      "faceid2=  2cccdf9f-bbdd-4d6e-bd77-aa3c9c5e1c18 AGE=  29.0\n",
      "faceid3=  5e874513-66fa-4bf5-b852-a7c5552cd1a3 AGE=  20.0\n",
      "faceid4=  cd8a1a81-f63e-425e-a95d-a563eba055d1 AGE=  16.0\n",
      "\n",
      "FaceID and corresponding age of the Face in my solo image\n",
      "faceid_myface=  8f80465a-34eb-4656-9d11-7704f83a54af AGE=  21.0\n"
     ]
    }
   ],
   "source": [
    "print(\"FaceIDs and corresponding ages of the Faces in the cousins image\")\n",
    "print(\"faceid0= \",cousins[0]['faceId'],\"AGE= \",cousins[0]['faceAttributes']['age'])\n",
    "print(\"faceid1= \",cousins[1]['faceId'],\"AGE= \",cousins[1]['faceAttributes']['age'])\n",
    "print(\"faceid2= \",cousins[2]['faceId'],\"AGE= \",cousins[2]['faceAttributes']['age'])\n",
    "print(\"faceid3= \",cousins[3]['faceId'],\"AGE= \",cousins[3]['faceAttributes']['age'])\n",
    "print(\"faceid4= \",cousins[4]['faceId'],\"AGE= \",cousins[4]['faceAttributes']['age'])\n",
    "print(\"\")\n",
    "print(\"FaceID and corresponding age of the Face in my solo image\")\n",
    "print(\"faceid_myface= \",me[0]['faceId'],\"AGE= \",me[0]['faceAttributes']['age'])\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Comparing faceid 0  with my face: \n",
      "{'isIdentical': False, 'confidence': 0.30385}\n",
      "Comparing faceid 1  with my face: \n",
      "{'isIdentical': False, 'confidence': 0.09449}\n",
      "Comparing faceid 2  with my face: \n",
      "{'isIdentical': True, 'confidence': 0.69045}\n",
      "Comparing faceid 3  with my face: \n",
      "{'isIdentical': False, 'confidence': 0.16735}\n",
      "Comparing faceid 4  with my face: \n",
      "{'isIdentical': False, 'confidence': 0.28128}\n"
     ]
    }
   ],
   "source": [
    "for i in range(5):\n",
    "    print(\"Comparing faceid\",i,\" with my face: \")\n",
    "    print(face_compare(me[0]['faceId'], cousins[i]['faceId'], face_api_url_verify))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
