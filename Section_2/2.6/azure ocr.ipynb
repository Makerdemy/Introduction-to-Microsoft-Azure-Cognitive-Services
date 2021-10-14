{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already up-to-date: azure-cognitiveservices-vision-computervision in d:\\anaconda\\lib\\site-packages (0.9.0)\n",
      "Requirement already satisfied, skipping upgrade: azure-common~=1.1 in d:\\anaconda\\lib\\site-packages (from azure-cognitiveservices-vision-computervision) (1.1.27)\n",
      "Requirement already satisfied, skipping upgrade: msrest>=0.5.0 in d:\\anaconda\\lib\\site-packages (from azure-cognitiveservices-vision-computervision) (0.6.21)\n",
      "Requirement already satisfied, skipping upgrade: requests-oauthlib>=0.5.0 in d:\\anaconda\\lib\\site-packages (from msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (1.3.0)\n",
      "Requirement already satisfied, skipping upgrade: isodate>=0.6.0 in d:\\anaconda\\lib\\site-packages (from msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (0.6.0)\n",
      "Requirement already satisfied, skipping upgrade: requests~=2.16 in d:\\anaconda\\lib\\site-packages (from msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (2.22.0)\n",
      "Requirement already satisfied, skipping upgrade: certifi>=2017.4.17 in d:\\anaconda\\lib\\site-packages (from msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (2019.11.28)\n",
      "Requirement already satisfied, skipping upgrade: oauthlib>=3.0.0 in d:\\anaconda\\lib\\site-packages (from requests-oauthlib>=0.5.0->msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (3.1.1)\n",
      "Requirement already satisfied, skipping upgrade: six in d:\\anaconda\\lib\\site-packages (from isodate>=0.6.0->msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (1.14.0)\n",
      "Requirement already satisfied, skipping upgrade: idna<2.9,>=2.5 in d:\\anaconda\\lib\\site-packages (from requests~=2.16->msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (2.8)\n",
      "Requirement already satisfied, skipping upgrade: chardet<3.1.0,>=3.0.2 in d:\\anaconda\\lib\\site-packages (from requests~=2.16->msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (3.0.4)\n",
      "Requirement already satisfied, skipping upgrade: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in d:\\anaconda\\lib\\site-packages (from requests~=2.16->msrest>=0.5.0->azure-cognitiveservices-vision-computervision) (1.25.8)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install --upgrade azure-cognitiveservices-vision-computervision"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pillow in d:\\anaconda\\lib\\site-packages (7.0.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pillow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from azure.cognitiveservices.vision.computervision import ComputerVisionClient\n",
    "from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes\n",
    "from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes\n",
    "from msrest.authentication import CognitiveServicesCredentials\n",
    "\n",
    "from array import array\n",
    "import os\n",
    "from PIL import Image\n",
    "import sys\n",
    "import time\n",
    "\n",
    "'''\n",
    "Authenticate\n",
    "Authenticates your credentials and creates a client.\n",
    "'''\n",
    "subscription_key = \"f9bee9c0e51545bab4e932a5cdf27ff4\"\n",
    "endpoint = \"https://mycogser1.cognitiveservices.azure.com/\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===== Read File - remote =====\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "OCR: Read File using the Read API, extract text - remote\n",
    "This example will extract text in an image, then print results, line by line.\n",
    "This API call can also extract handwriting style text (not shown).\n",
    "'''\n",
    "print(\"===== Read File - remote =====\")\n",
    "# Get an image with text\n",
    "read_image_url = \"https://i.postimg.cc/k4SRqry6/use-this-text-1.jpg\"\n",
    "\n",
    "# Call API with URL and raw response (allows you to get the operation location)\n",
    "read_response = computervision_client.read(read_image_url,  raw=True)"
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
      "My name is Saharsh & I love to\n",
      "work on\n",
      "Azwie Cognitive Services.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Get the operation location (URL with an ID at the end) from the response\n",
    "read_operation_location = read_response.headers[\"Operation-Location\"]\n",
    "# Grab the ID from the URL\n",
    "operation_id = read_operation_location.split(\"/\")[-1]\n",
    "\n",
    "# Call the \"GET\" API and wait for it to retrieve the results \n",
    "while True:\n",
    "    read_result = computervision_client.get_read_result(operation_id)\n",
    "    if read_result.status not in ['notStarted', 'running']:\n",
    "        break\n",
    "    time.sleep(1)\n",
    "\n",
    "# Print the detected text, line by line\n",
    "if read_result.status == OperationStatusCodes.succeeded:\n",
    "    for text_result in read_result.analyze_result.read_results:\n",
    "        for line in text_result.lines:\n",
    "            print(line.text)\n",
    "            #print(line.bounding_box)\n",
    "print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
