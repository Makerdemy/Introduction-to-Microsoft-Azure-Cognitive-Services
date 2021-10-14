{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
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
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "subscription_key = \"f9bee9c0e51545bab4e932a5cdf27ff4\"\n",
    "endpoint = \"https://mycogser1.cognitiveservices.azure.com/\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "remote_image_url = \"https://miro.medium.com/max/1200/1*56MtNM2fh_mdG3iGnD7_ZQ.jpeg\""
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
      "===== Describe an image - remote =====\n",
      "Description of remote image: \n",
      "'a couple of men playing cricket' with confidence 57.33%\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Describe an Image - remote\n",
    "This example describes the contents of an image with the confidence score.\n",
    "'''\n",
    "print(\"===== Describe an image - remote =====\")\n",
    "# Call API\n",
    "description_results = computervision_client.describe_image(remote_image_url )\n",
    "\n",
    "# Get the captions (descriptions) from the response, with confidence level\n",
    "print(\"Description of remote image: \")\n",
    "if (len(description_results.captions) == 0):\n",
    "    print(\"No description detected.\")\n",
    "else:\n",
    "    for caption in description_results.captions:\n",
    "        print(\"'{}' with confidence {:.2f}%\".format(caption.text, caption.confidence * 100))"
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
      "===== Categorize an image - remote =====\n",
      "Categories from remote image: \n",
      "'outdoor_' with confidence 0.39%\n",
      "'trans_bicycle' with confidence 89.06%\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Categorize an Image - remote\n",
    "This example extracts (general) categories from a remote image with a confidence score.\n",
    "'''\n",
    "print(\"===== Categorize an image - remote =====\")\n",
    "# Select the visual feature(s) you want.\n",
    "remote_image_features = [\"categories\"]\n",
    "# Call API with URL and features\n",
    "categorize_results_remote = computervision_client.analyze_image(remote_image_url , remote_image_features)\n",
    "\n",
    "# Print results with confidence score\n",
    "print(\"Categories from remote image: \")\n",
    "if (len(categorize_results_remote.categories) == 0):\n",
    "    print(\"No categories detected.\")\n",
    "else:\n",
    "    for category in categorize_results_remote.categories:\n",
    "        print(\"'{}' with confidence {:.2f}%\".format(category.name, category.score * 100))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===== Tag an image - remote =====\n",
      "Tags in the remote image: \n",
      "'grass' with confidence 99.53%\n",
      "'person' with confidence 99.35%\n",
      "'sports equipment' with confidence 98.32%\n",
      "'outdoor' with confidence 97.45%\n",
      "'player' with confidence 97.10%\n",
      "'sport venue' with confidence 96.37%\n",
      "'ball game' with confidence 96.23%\n",
      "'cricketer' with confidence 95.22%\n",
      "'bat-and-ball games' with confidence 94.76%\n",
      "'wicket' with confidence 93.16%\n",
      "'sports uniform' with confidence 92.58%\n",
      "'cricket bat' with confidence 91.86%\n",
      "'limited overs cricket' with confidence 91.69%\n",
      "'sports' with confidence 91.32%\n",
      "'test cricket' with confidence 90.94%\n",
      "'man' with confidence 90.33%\n",
      "'one day international' with confidence 90.13%\n",
      "'ball' with confidence 88.15%\n",
      "'twenty20' with confidence 84.62%\n",
      "'glove' with confidence 84.29%\n",
      "'cricket' with confidence 81.03%\n",
      "'game' with confidence 80.21%\n",
      "'field' with confidence 63.11%\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Tag an Image - remote\n",
    "This example returns a tag (key word) for each thing in the image.\n",
    "'''\n",
    "print(\"===== Tag an image - remote =====\")\n",
    "# Call API with remote image\n",
    "tags_result_remote = computervision_client.tag_image(remote_image_url )\n",
    "\n",
    "# Print results with confidence score\n",
    "print(\"Tags in the remote image: \")\n",
    "if (len(tags_result_remote.tags) == 0):\n",
    "    print(\"No tags detected.\")\n",
    "else:\n",
    "    for tag in tags_result_remote.tags:\n",
    "        print(\"'{}' with confidence {:.2f}%\".format(tag.name, tag.confidence * 100))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===== Detect Objects - remote =====\n",
      "Detecting objects in remote image:\n",
      "object at location 213, 365, 85, 208\n",
      "object at location 218, 402, 179, 384\n",
      "object at location 238, 417, 298, 416\n",
      "object at location 116, 419, 60, 386\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Detect Objects - remote\n",
    "This example detects different kinds of objects with bounding boxes in a remote image.\n",
    "'''\n",
    "print(\"===== Detect Objects - remote =====\")\n",
    "# Get URL image with different objects\n",
    "remote_image_url_objects = \"https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/objects.jpg\"\n",
    "# Call API with URL\n",
    "detect_objects_results_remote = computervision_client.detect_objects(remote_image_url_objects)\n",
    "\n",
    "# Print detected objects results with bounding boxes\n",
    "print(\"Detecting objects in remote image:\")\n",
    "if len(detect_objects_results_remote.objects) == 0:\n",
    "    print(\"No objects detected.\")\n",
    "else:\n",
    "    for object in detect_objects_results_remote.objects:\n",
    "        print(\"object at location {}, {}, {}, {}\".format( \\\n",
    "        object.rectangle.x, object.rectangle.x + object.rectangle.w, \\\n",
    "        object.rectangle.y, object.rectangle.y + object.rectangle.h))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===== Detect Brands - remote =====\n",
      "Detecting brands in remote image: \n",
      "'Nike' brand detected with confidence 69.5% at location 96, 202, 615, 737\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Detect Brands - remote\n",
    "This example detects common brands like logos and puts a bounding box around them.\n",
    "'''\n",
    "print(\"===== Detect Brands - remote =====\")\n",
    "# Get a URL with a brand logo\n",
    "remote_image_url = \"https://n3.sdlcdn.com/imgs/h/6/j/Airmax_Black_1-35bb6.jpg\"\n",
    "# Select the visual feature(s) you want\n",
    "remote_image_features = [\"brands\"]\n",
    "# Call API with URL and features\n",
    "detect_brands_results_remote = computervision_client.analyze_image(remote_image_url, remote_image_features)\n",
    "\n",
    "print(\"Detecting brands in remote image: \")\n",
    "if len(detect_brands_results_remote.brands) == 0:\n",
    "    print(\"No brands detected.\")\n",
    "else:\n",
    "    for brand in detect_brands_results_remote.brands:\n",
    "        print(\"'{}' brand detected with confidence {:.1f}% at location {}, {}, {}, {}\".format( \\\n",
    "        brand.name, brand.confidence * 100, brand.rectangle.x, brand.rectangle.x + brand.rectangle.w, \\\n",
    "        brand.rectangle.y, brand.rectangle.y + brand.rectangle.h))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===== Detect Faces - remote =====\n",
      "Faces in the remote image: \n",
      "'Male' of age 39 at location 118, 159, 212, 253\n",
      "'Male' of age 54 at location 492, 111, 582, 201\n",
      "'Female' of age 55 at location 18, 153, 102, 237\n",
      "'Female' of age 33 at location 386, 166, 467, 247\n",
      "'Female' of age 18 at location 235, 158, 311, 234\n",
      "'Female' of age 8 at location 323, 163, 391, 231\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Detect Faces - remote\n",
    "This example detects faces in a remote image, gets their gender and age, \n",
    "and marks them with a bounding box.\n",
    "'''\n",
    "print(\"===== Detect Faces - remote =====\")\n",
    "# Get an image with faces\n",
    "remote_image_url_faces = \"https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/faces.jpg\"\n",
    "# Select the visual feature(s) you want.\n",
    "remote_image_features = [\"faces\"]\n",
    "# Call the API with remote URL and features\n",
    "detect_faces_results_remote = computervision_client.analyze_image(remote_image_url_faces, remote_image_features)\n",
    "\n",
    "# Print the results with gender, age, and bounding box\n",
    "print(\"Faces in the remote image: \")\n",
    "if (len(detect_faces_results_remote.faces) == 0):\n",
    "    print(\"No faces detected.\")\n",
    "else:\n",
    "    for face in detect_faces_results_remote.faces:\n",
    "        print(\"'{}' of age {} at location {}, {}, {}, {}\".format(face.gender, face.age, \\\n",
    "        face.face_rectangle.left, face.face_rectangle.top, \\\n",
    "        face.face_rectangle.left + face.face_rectangle.width, \\\n",
    "        face.face_rectangle.top + face.face_rectangle.height))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===== Detect Adult or Racy Content - remote =====\n",
      "Analyzing remote image for adult or racy content ... \n",
      "Is adult content: False with confidence 0.10\n",
      "Has racy content: False with confidence 0.16\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Detect Adult or Racy Content - remote\n",
    "This example detects adult or racy content in a remote image, then prints the adult/racy score.\n",
    "The score is ranged 0.0 - 1.0 with smaller numbers indicating negative results.\n",
    "'''\n",
    "print(\"===== Detect Adult or Racy Content - remote =====\")\n",
    "# Select the visual feature(s) you want\n",
    "remote_image_features = [\"adult\"]\n",
    "# Call API with URL and features\n",
    "detect_adult_results_remote = computervision_client.analyze_image(remote_image_url, remote_image_features)\n",
    "\n",
    "# Print results with adult/racy score\n",
    "print(\"Analyzing remote image for adult or racy content ... \")\n",
    "print(\"Is adult content: {} with confidence {:.2f}\".format(detect_adult_results_remote.adult.is_adult_content, detect_adult_results_remote.adult.adult_score * 100))\n",
    "print(\"Has racy content: {} with confidence {:.2f}\".format(detect_adult_results_remote.adult.is_racy_content, detect_adult_results_remote.adult.racy_score * 100))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===== Detect Color - remote =====\n",
      "Getting color scheme of the remote image: \n",
      "Is black and white: False\n",
      "Accent color: 8D593E\n",
      "Dominant background color: White\n",
      "Dominant foreground color: Black\n",
      "Dominant colors: ['White', 'Black', 'Grey']\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Detect Color - remote\n",
    "This example detects the different aspects of its color scheme in a remote image.\n",
    "'''\n",
    "print(\"===== Detect Color - remote =====\")\n",
    "# Select the feature(s) you want\n",
    "remote_image_features = [\"color\"]\n",
    "# Call API with URL and features\n",
    "detect_color_results_remote = computervision_client.analyze_image(remote_image_url, remote_image_features)\n",
    "\n",
    "# Print results of color scheme\n",
    "print(\"Getting color scheme of the remote image: \")\n",
    "print(\"Is black and white: {}\".format(detect_color_results_remote.color.is_bw_img))\n",
    "print(\"Accent color: {}\".format(detect_color_results_remote.color.accent_color))\n",
    "print(\"Dominant background color: {}\".format(detect_color_results_remote.color.dominant_color_background))\n",
    "print(\"Dominant foreground color: {}\".format(detect_color_results_remote.color.dominant_color_foreground))\n",
    "print(\"Dominant colors: {}\".format(detect_color_results_remote.color.dominant_colors))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===== Detect Domain-specific Content - remote =====\n",
      "Celebrities in the remote image:\n",
      "Shah Rukh Khan\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Detect Domain-specific Content - remote\n",
    "This example detects celebrites and landmarks in remote images.\n",
    "'''\n",
    "print(\"===== Detect Domain-specific Content - remote =====\")\n",
    "# URL of one or more celebrities\n",
    "remote_image_url_celebs = \"https://m.media-amazon.com/images/M/MV5BZDk1ZmU0NGYtMzQ2Yi00N2NjLTkyNWEtZWE2NTU4NTJiZGUzXkEyXkFqcGdeQXVyMTExNDQ2MTI@._V1_UY1200_CR107,0,630,1200_AL_.jpg\"\n",
    "# Call API with content type (celebrities) and URL\n",
    "detect_domain_results_celebs_remote = computervision_client.analyze_image_by_domain(\"celebrities\", remote_image_url_celebs)\n",
    "\n",
    "# Print detection results with name\n",
    "print(\"Celebrities in the remote image:\")\n",
    "if len(detect_domain_results_celebs_remote.result[\"celebrities\"]) == 0:\n",
    "    print(\"No celebrities detected.\")\n",
    "else:\n",
    "    for celeb in detect_domain_results_celebs_remote.result[\"celebrities\"]:\n",
    "        print(celeb[\"name\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Landmarks in the remote image:\n",
      "Taj Mahal\n"
     ]
    }
   ],
   "source": [
    "# Call API with content type (landmarks) and URL\n",
    "remote_image_landmark_url = \"https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Taj_Mahal_in_India_-_Kristian_Bertel.jpg/1200px-Taj_Mahal_in_India_-_Kristian_Bertel.jpg\"\n",
    "detect_domain_results_landmarks = computervision_client.analyze_image_by_domain(\"landmarks\", remote_image_landmark_url)\n",
    "print()\n",
    "\n",
    "print(\"Landmarks in the remote image:\")\n",
    "if len(detect_domain_results_landmarks.result[\"landmarks\"]) == 0:\n",
    "    print(\"No landmarks detected.\")\n",
    "else:\n",
    "    for landmark in detect_domain_results_landmarks.result[\"landmarks\"]:\n",
    "        print(landmark[\"name\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===== Detect Image Types - remote =====\n",
      "Type of remote image:\n",
      "Image is good clip art.\n",
      "Image is not a line drawing.\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Detect Image Types - remote\n",
    "This example detects an image's type (clip art/line drawing).\n",
    "'''\n",
    "print(\"===== Detect Image Types - remote =====\")\n",
    "# Get URL of an image with a type\n",
    "remote_image_url_type = \"https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/type-image.jpg\"\n",
    "# Select visual feature(s) you want\n",
    "remote_image_features = [VisualFeatureTypes.image_type]\n",
    "# Call API with URL and features\n",
    "detect_type_results_remote = computervision_client.analyze_image(remote_image_url_type, remote_image_features)\n",
    "\n",
    "# Prints type results with degree of accuracy\n",
    "print(\"Type of remote image:\")\n",
    "if detect_type_results_remote.image_type.clip_art_type == 0:\n",
    "    print(\"Image is not clip art.\")\n",
    "elif detect_type_results_remote.image_type.line_drawing_type == 1:\n",
    "    print(\"Image is ambiguously clip art.\")\n",
    "elif detect_type_results_remote.image_type.line_drawing_type == 2:\n",
    "    print(\"Image is normal clip art.\")\n",
    "else:\n",
    "    print(\"Image is good clip art.\")\n",
    "\n",
    "if detect_type_results_remote.image_type.line_drawing_type == 0:\n",
    "    print(\"Image is not a line drawing.\")\n",
    "else:\n",
    "    print(\"Image is a line drawing\")"
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
