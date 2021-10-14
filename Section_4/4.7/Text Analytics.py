{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "key = \"81d80fb56b7e461e9ee8d919578d7276\"\n",
    "endpoint = \"https://my-cog-services-1.cognitiveservices.azure.com/\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install azure-ai-textanalytics==5.1.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from azure.ai.textanalytics import TextAnalyticsClient\n",
    "from azure.core.credentials import AzureKeyCredential\n",
    "\n",
    "def authenticate_client():\n",
    "    ta_credential = AzureKeyCredential(key)\n",
    "    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=ta_credential)\n",
    "    return text_analytics_client\n",
    "\n",
    "client = authenticate_client()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Document Sentiment: mixed\n",
      "Overall scores: positive=0.41; neutral=0.00; negative=0.59 \n",
      "\n",
      "Sentence: I didn't write my exam well.\n",
      "Sentence 1 sentiment: negative\n",
      "Sentence score:\n",
      "Positive=0.23\n",
      "Neutral=0.00\n",
      "Negative=0.77\n",
      "\n",
      "Sentence: It feels very bad at the moment.\n",
      "Sentence 2 sentiment: negative\n",
      "Sentence score:\n",
      "Positive=0.00\n",
      "Neutral=0.00\n",
      "Negative=1.00\n",
      "\n",
      "Sentence: But I'll work hard next time and pass out with flying colours.\n",
      "Sentence 3 sentiment: neutral\n",
      "Sentence score:\n",
      "Positive=0.01\n",
      "Neutral=0.99\n",
      "Negative=0.00\n",
      "\n",
      "Sentence: That'll be one of the best moments of my life.\n",
      "Sentence 4 sentiment: positive\n",
      "Sentence score:\n",
      "Positive=1.00\n",
      "Neutral=0.00\n",
      "Negative=0.00\n",
      "\n"
     ]
    }
   ],
   "source": [
    "def sentiment_analysis_example(client):\n",
    "\n",
    "    documents = [\"I didn't write my exam well. It feels very bad at the moment. But I'll work hard next time and pass out with flying colours. That'll be one of the best moments of my life.\"]\n",
    "    response = client.analyze_sentiment(documents=documents)[0]\n",
    "    print(\"Document Sentiment: {}\".format(response.sentiment))\n",
    "    print(\"Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \\n\".format(\n",
    "        response.confidence_scores.positive,\n",
    "        response.confidence_scores.neutral,\n",
    "        response.confidence_scores.negative,\n",
    "    ))\n",
    "    for idx, sentence in enumerate(response.sentences):\n",
    "        print(\"Sentence: {}\".format(sentence.text))\n",
    "        print(\"Sentence {} sentiment: {}\".format(idx+1, sentence.sentiment))\n",
    "        print(\"Sentence score:\\nPositive={0:.2f}\\nNeutral={1:.2f}\\nNegative={2:.2f}\\n\".format(\n",
    "            sentence.confidence_scores.positive,\n",
    "            sentence.confidence_scores.neutral,\n",
    "            sentence.confidence_scores.negative,\n",
    "        ))\n",
    "          \n",
    "sentiment_analysis_example(client)"
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
      "Language:  Spanish\n"
     ]
    }
   ],
   "source": [
    "def language_detection_example(client):\n",
    "    try:\n",
    "        documents = [\"Hola amigos que tengan un buen dia\"]\n",
    "        response = client.detect_language(documents = documents, country_hint = 'us')[0]\n",
    "        print(\"Language: \", response.primary_language.name)\n",
    "\n",
    "    except Exception as err:\n",
    "        print(\"Encountered exception. {}\".format(err))\n",
    "language_detection_example(client)"
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
      "Named Entities:\n",
      "\n",
      "\tText: \t Lionel Messi \tCategory: \t Person \tSubCategory: \t None \n",
      "\tConfidence Score: \t 1.0 \n",
      "\n",
      "\tText: \t one \tCategory: \t Quantity \tSubCategory: \t Number \n",
      "\tConfidence Score: \t 0.8 \n",
      "\n",
      "\tText: \t football \tCategory: \t Skill \tSubCategory: \t None \n",
      "\tConfidence Score: \t 0.53 \n",
      "\n",
      "\tText: \t football players \tCategory: \t PersonType \tSubCategory: \t None \n",
      "\tConfidence Score: \t 0.82 \n",
      "\n",
      "\tText: \t 2012 \tCategory: \t DateTime \tSubCategory: \t DateRange \n",
      "\tConfidence Score: \t 0.8 \n",
      "\n"
     ]
    }
   ],
   "source": [
    "def entity_recognition_example(client):\n",
    "\n",
    "    try:\n",
    "        documents = [\"Lionel Messi is one of the best football players of all time but he was a beast during the 2012 season.\"]\n",
    "        result = client.recognize_entities(documents = documents)[0]\n",
    "\n",
    "        print(\"Named Entities:\\n\")\n",
    "        for entity in result.entities:\n",
    "            print(\"\\tText: \\t\", entity.text, \"\\tCategory: \\t\", entity.category, \"\\tSubCategory: \\t\", entity.subcategory,\n",
    "                    \"\\n\\tConfidence Score: \\t\", round(entity.confidence_score, 2),  \"\\n\")\n",
    "\n",
    "    except Exception as err:\n",
    "        print(\"Encountered exception. {}\".format(err))\n",
    "entity_recognition_example(client)"
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
      "\tKey Phrases:\n",
      "\t\t dad\n",
      "\t\t check\n",
      "\t\t hospital\n"
     ]
    }
   ],
   "source": [
    "def key_phrase_extraction_example(client):\n",
    "\n",
    "    try:\n",
    "        documents = [\"My dad needs to go for a check up to the hospital.\"]\n",
    "\n",
    "        response = client.extract_key_phrases(documents = documents)[0]\n",
    "\n",
    "        if not response.is_error:\n",
    "            print(\"\\tKey Phrases:\")\n",
    "            for phrase in response.key_phrases:\n",
    "                print(\"\\t\\t\", phrase)\n",
    "        else:\n",
    "            print(response.id, response.error)\n",
    "\n",
    "    except Exception as err:\n",
    "        print(\"Encountered exception. {}\".format(err))\n",
    "        \n",
    "key_phrase_extraction_example(client)"
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
