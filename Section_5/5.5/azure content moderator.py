{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install --upgrade azure-cognitiveservices-vision-contentmoderator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os.path\n",
    "from pprint import pprint\n",
    "import time\n",
    "from io import BytesIO\n",
    "from random import random\n",
    "import uuid\n",
    "\n",
    "from azure.cognitiveservices.vision.contentmoderator import ContentModeratorClient\n",
    "import azure.cognitiveservices.vision.contentmoderator.models\n",
    "from msrest.authentication import CognitiveServicesCredentials"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "CONTENT_MODERATOR_ENDPOINT = \"https://my-cog-services-1.cognitiveservices.azure.com/\"\n",
    "subscription_key = \"81d80fb56b7e461e9ee8d919578d7276\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "client = ContentModeratorClient(endpoint=CONTENT_MODERATOR_ENDPOINT,\n",
    "    credentials=CognitiveServicesCredentials(subscription_key)\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "TEXT_FOLDER = os.path.join(os.path.dirname(os.path.realpath(\"text_moderation.txt\")), \"text_files\")"
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
      "{'auto_corrected_text': 'Is this a garbage email abcdef@abcd.com, phone: '\n",
      "                        '4255550111, IP: 255.255.255.255, 1234 Main Boulevard, '\n",
      "                        'Pentapolis WA 96555.\\r\\n'\n",
      "                        'Crap is the profanity here. Is this information PII? '\n",
      "                        'phone 2065550111',\n",
      " 'language': 'eng',\n",
      " 'normalized_text': '   grabage email abcdef@abcd.com, phone: 4255550111, IP: '\n",
      "                    '255.255.255.255, 1234 Main Boulevard, Panapolis WA '\n",
      "                    '96555.\\r\\n'\n",
      "                    'Crap   profanity .   information PII? phone 2065550111',\n",
      " 'original_text': 'Is this a grabage email abcdef@abcd.com, phone: 4255550111, '\n",
      "                  'IP: 255.255.255.255, 1234 Main Boulevard, Panapolis WA '\n",
      "                  '96555.\\r\\n'\n",
      "                  'Crap is the profanity here. Is this information PII? phone '\n",
      "                  '2065550111',\n",
      " 'pii': {'address': [{'index': 81,\n",
      "                      'text': '1234 Main Boulevard, Panapolis WA 96555'}],\n",
      "         'email': [{'detected': 'abcdef@abcd.com',\n",
      "                    'index': 24,\n",
      "                    'sub_type': 'Regular',\n",
      "                    'text': 'abcdef@abcd.com'}],\n",
      "         'ipa': [{'index': 64, 'sub_type': 'IPV4', 'text': '255.255.255.255'}],\n",
      "         'phone': [{'country_code': 'US', 'index': 48, 'text': '4255550111'},\n",
      "                   {'country_code': 'US', 'index': 182, 'text': '2065550111'}],\n",
      "         'ssn': []},\n",
      " 'status': {'code': 3000, 'description': 'OK'},\n",
      " 'terms': [{'index': 116, 'list_id': 0, 'original_index': 123, 'term': 'crap'}],\n",
      " 'tracking_id': '27f0fa03-ea0d-4b10-a657-5d939be66b81'}\n"
     ]
    }
   ],
   "source": [
    "# Screen the input text: check for profanity, autocorrect text, and check for personally identifying information (PII)\n",
    "with open(os.path.join(TEXT_FOLDER, 'text_moderation.txt'), \"rb\") as text_fd:\n",
    "    screen = client.text_moderation.screen_text(text_content_type=\"text/plain\",text_content=text_fd,language=\"eng\",\n",
    "        autocorrect=True,\n",
    "        pii=True\n",
    "    )\n",
    "    pprint(screen.as_dict())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "TEXT_FOLDER = os.path.join(os.path.dirname(os.path.realpath(\"custom_term_list.txt\")), \"text_files\")"
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
      "\n",
      "Creating list\n",
      "List created:\n",
      "{'description': 'Term list description', 'id': 832, 'name': 'Term list name'}\n"
     ]
    }
   ],
   "source": [
    "# Create list\n",
    "print(\"\\nCreating list\")\n",
    "custom_list = client.list_management_term_lists.create(content_type=\"application/json\",\n",
    "    body={\n",
    "        \"name\": \"Term list name\",\n",
    "        \"description\": \"Term list description\",\n",
    "    }\n",
    ")\n",
    "print(\"List created:\")\n",
    "pprint(custom_list.as_dict())\n",
    "list_id = custom_list.id"
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
      "\n",
      "Updating details for list 832\n",
      "{'description': 'New list description', 'id': 832, 'name': 'New Term list name'}\n"
     ]
    }
   ],
   "source": [
    "# Update list details\n",
    "print(\"\\nUpdating details for list {}\".format(list_id))\n",
    "updated_list = client.list_management_term_lists.update(\n",
    "    list_id=list_id,\n",
    "    content_type=\"application/json\",\n",
    "    body={\n",
    "        \"name\": \"New Term list name\",\n",
    "        \"description\": \"New list description\"\n",
    "    }\n",
    ")\n",
    "pprint(updated_list.as_dict())"
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
      "\n",
      "Adding terms to list 832\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{'ContentId': '182966',\n",
       " 'AdditionalInfo': [{'Key': 'Source', 'Value': '832'}],\n",
       " 'Status': {'Code': 3000, 'Description': 'OK', 'Exception': None},\n",
       " 'TrackingId': 'b0f9cc7e-215b-44c8-ae19-c2661b98dd15'}"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Add terms\n",
    "print(\"\\nAdding terms to list {}\".format(list_id))\n",
    "client.list_management_term.add_term(\n",
    "    list_id=list_id,\n",
    "    term=\"term1\",\n",
    "    language=\"eng\"\n",
    ")\n",
    "client.list_management_term.add_term(\n",
    "    list_id=list_id,\n",
    "    term=\"term2\",\n",
    "    language=\"eng\"\n",
    ")"
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
      "\n",
      "Getting all term IDs for list 832\n",
      "{'language': 'eng',\n",
      " 'status': {'code': 3000, 'description': 'OK'},\n",
      " 'terms': [{'term': 'term1'}, {'term': 'term2'}],\n",
      " 'tracking_id': 'b4d45862-acfd-40ac-b89a-591d1548236d'}\n"
     ]
    }
   ],
   "source": [
    "# Get all terms ids\n",
    "print(\"\\nGetting all term IDs for list {}\".format(list_id))\n",
    "terms = client.list_management_term.get_all_terms(list_id=list_id, language=\"eng\")\n",
    "terms_data = terms.data\n",
    "pprint(terms_data.as_dict())"
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
      "\n",
      "Refreshing the search index for list 832\n",
      "{'advanced_info': [],\n",
      " 'content_source_id': '832',\n",
      " 'is_update_success': True,\n",
      " 'status': {'code': 3000, 'description': 'OK'},\n",
      " 'tracking_id': 'be94a6dd-bbb7-4f76-845d-0cb246fcb7df'}\n"
     ]
    }
   ],
   "source": [
    "# Refresh the index\n",
    "print(\"\\nRefreshing the search index for list {}\".format(list_id))\n",
    "refresh_index = client.list_management_term_lists.refresh_index_method(list_id=list_id, language=\"eng\")\n",
    "\n",
    "pprint(refresh_index.as_dict())"
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
      "{'language': 'eng',\n",
      " 'normalized_text': ' text contains  terms \"term1\"  \"term2\".',\n",
      " 'original_text': 'This text contains the terms \"term1\" and \"term2\".',\n",
      " 'status': {'code': 3000, 'description': 'OK'},\n",
      " 'terms': [{'index': 23, 'list_id': 832, 'original_index': 30, 'term': 'term1'},\n",
      "           {'index': 32,\n",
      "            'list_id': 832,\n",
      "            'original_index': 42,\n",
      "            'term': 'term2'}],\n",
      " 'tracking_id': 'ba05033c-35ec-435b-905e-3c3e572753d3'}\n"
     ]
    }
   ],
   "source": [
    "# Screen text\n",
    "with open(os.path.join(TEXT_FOLDER, 'custom_term_list.txt'), \"rb\") as text_fd:\n",
    "    screen = client.text_moderation.screen_text(\n",
    "        text_content_type=\"text/plain\",\n",
    "        text_content=text_fd,\n",
    "        language=\"eng\",\n",
    "        autocorrect=False,\n",
    "        pii=False,\n",
    "        list_id=list_id\n",
    "    )\n",
    "    \n",
    "    pprint(screen.as_dict())"
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
      "\n",
      "Remove term term1 from list 832\n"
     ]
    }
   ],
   "source": [
    "# Remove terms\n",
    "term_to_remove = \"term1\"\n",
    "print(\"\\nRemove term {} from list {}\".format(term_to_remove, list_id))\n",
    "client.list_management_term.delete_term(\n",
    "    list_id=list_id,\n",
    "    term=term_to_remove,\n",
    "    language=\"eng\"\n",
    ")"
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
      "Delete all terms in the image list 832\n"
     ]
    }
   ],
   "source": [
    "# Delete all terms\n",
    "print(\"\\nDelete all terms in the image list {}\".format(list_id))\n",
    "client.list_management_term.delete_all_terms(list_id=list_id, language=\"eng\")"
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
      "\n",
      "Delete the term list 832\n"
     ]
    }
   ],
   "source": [
    "# Delete list\n",
    "print(\"\\nDelete the term list {}\".format(list_id))\n",
    "client.list_management_term_lists.delete(list_id=list_id)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "IMAGE_LIST = [\n",
    "    \"https://moderatorsampleimages.blob.core.windows.net/samples/sample2.jpg\",\n",
    "    \"https://moderatorsampleimages.blob.core.windows.net/samples/sample5.png\"\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Evaluate image https://moderatorsampleimages.blob.core.windows.net/samples/sample2.jpg\n",
      "\n",
      "Evaluate image https://moderatorsampleimages.blob.core.windows.net/samples/sample5.png\n"
     ]
    }
   ],
   "source": [
    "for image_url in IMAGE_LIST:\n",
    "    print(\"\\nEvaluate image {}\".format(image_url))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Evaluate for adult and racy content.\n",
      "{'adult_classification_score': 0.001438833656720817,\n",
      " 'advanced_info': [{'key': 'ImageDownloadTimeInMs', 'value': '297'},\n",
      "                   {'key': 'ImageSizeInBytes', 'value': '2278902'}],\n",
      " 'cache_id': 'd1727060-7fb0-47b5-8390-5efab73df232_637668530553834032',\n",
      " 'is_image_adult_classified': False,\n",
      " 'is_image_racy_classified': False,\n",
      " 'racy_classification_score': 0.004629917559213936,\n",
      " 'result': False,\n",
      " 'status': {'code': 3000, 'description': 'OK'},\n",
      " 'tracking_id': '6842c02f-4ba0-43f9-a6fa-72cc9bb29ae8'}\n"
     ]
    }
   ],
   "source": [
    "#Adult or Racy content detection\n",
    "print(\"\\nEvaluate for adult and racy content.\")\n",
    "evaluation = client.image_moderation.evaluate_url_input(\n",
    "    content_type=\"application/json\",\n",
    "    cache_image=True,\n",
    "    data_representation=\"URL\",\n",
    "    value=IMAGE_LIST[1]\n",
    ")\n",
    "\n",
    "pprint(evaluation.as_dict())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Detect and extract text.\n",
      "{'candidates': [],\n",
      " 'language': 'eng',\n",
      " 'metadata': [{'key': 'ImageDownloadTimeInMs', 'value': '172'},\n",
      "              {'key': 'ImageSizeInBytes', 'value': '273405'}],\n",
      " 'status': {'code': 3000, 'description': 'OK'},\n",
      " 'text': 'IF WE DID \\n'\n",
      "         'ALL \\n'\n",
      "         'THE THINGS \\n'\n",
      "         'WE ARE \\n'\n",
      "         'CAPABLE \\n'\n",
      "         'OF DOING, \\n'\n",
      "         'WE WOULD \\n'\n",
      "         'LITERALLY \\n'\n",
      "         'ASTOUND \\n'\n",
      "         'OURSELVES. \\n',\n",
      " 'tracking_id': '91c88ae4-4a11-414d-b510-b0b1ba3dd6e8'}\n"
     ]
    }
   ],
   "source": [
    "#OCR\n",
    "print(\"\\nDetect and extract text.\")\n",
    "evaluation = client.image_moderation.ocr_url_input(\n",
    "    language=\"eng\",\n",
    "    content_type=\"application/json\",\n",
    "    data_representation=\"URL\",\n",
    "    value=IMAGE_LIST[0],\n",
    "    cache_image=True,\n",
    ")\n",
    "\n",
    "pprint(evaluation.as_dict())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Detect faces.\n",
      "{'advanced_info': [{'key': 'ImageDownloadTimeInMs', 'value': '232'},\n",
      "                   {'key': 'ImageSizeInBytes', 'value': '2278902'}],\n",
      " 'count': 6,\n",
      " 'faces': [{'bottom': 633, 'left': 297, 'right': 531, 'top': 399},\n",
      "           {'bottom': 503, 'left': 1228, 'right': 1453, 'top': 278},\n",
      "           {'bottom': 595, 'left': 47, 'right': 257, 'top': 385},\n",
      "           {'bottom': 619, 'left': 966, 'right': 1168, 'top': 417},\n",
      "           {'bottom': 590, 'left': 589, 'right': 781, 'top': 398},\n",
      "           {'bottom': 578, 'left': 807, 'right': 978, 'top': 407}],\n",
      " 'result': True,\n",
      " 'status': {'code': 3000, 'description': 'OK'},\n",
      " 'tracking_id': '5d52b719-0b6b-417a-8781-80da100644be'}\n"
     ]
    }
   ],
   "source": [
    "#Face detection\n",
    "print(\"\\nDetect faces.\")\n",
    "evaluation = client.image_moderation.find_faces_url_input(\n",
    "    content_type=\"application/json\",\n",
    "    cache_image=True,\n",
    "    data_representation=\"URL\",\n",
    "    value=IMAGE_LIST[1]\n",
    ")\n",
    "\n",
    "pprint(evaluation.as_dict())"
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
