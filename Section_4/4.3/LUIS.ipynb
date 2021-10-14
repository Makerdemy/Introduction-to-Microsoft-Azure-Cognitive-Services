{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from azure.cognitiveservices.language.luis.authoring import LUISAuthoringClient\n",
    "from azure.cognitiveservices.language.luis.authoring.models import ApplicationCreateObject\n",
    "from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient\n",
    "from msrest.authentication import CognitiveServicesCredentials\n",
    "from functools import reduce\n",
    "\n",
    "import json, time, uuid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "authoringKey = 'c0f1c358dc2643e38af788ad567f0a49'\n",
    "authoringEndpoint = 'https://westus.api.cognitive.microsoft.com/'\n",
    "predictionKey = 'c0f1c358dc2643e38af788ad567f0a49'\n",
    "predictionEndpoint = 'https://westus.api.cognitive.microsoft.com/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# We use a UUID to avoid name collisions.\n",
    "appName = \"My Pizza Company \" + str(uuid.uuid4())\n",
    "versionId = \"0.2\"\n",
    "intentName = \"OrderPizzaIntent\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "client = LUISAuthoringClient(authoringEndpoint, CognitiveServicesCredentials(authoringKey))"
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
      "Created LUIS app with ID e47e411e-a693-444a-80c0-a6d4fd47ed7b\n"
     ]
    }
   ],
   "source": [
    "# define app basics\n",
    "appDefinition = ApplicationCreateObject(name=appName, initial_version_id=versionId, culture='en-us')\n",
    "\n",
    "# create app\n",
    "app_id = client.apps.add(appDefinition)\n",
    "\n",
    "# get app id - necessary for all other changes\n",
    "print(\"Created LUIS app with ID {}\".format(app_id))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'91eff93c-4653-4d90-895a-606c0a8cdabf'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Adding intent\n",
    "client.model.add_intent(app_id, versionId, intentName)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_grandchild_id(model, childName, grandChildName):\n",
    "    \n",
    "    theseChildren = next(filter((lambda child: child.name == childName), model.children))\n",
    "    theseGrandchildren = next(filter((lambda child: child.name == grandChildName), theseChildren.children))\n",
    "    \n",
    "    grandChildId = theseGrandchildren.id\n",
    "    \n",
    "    return grandChildId"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<azure.cognitiveservices.language.luis.authoring.models._models_py3.PrebuiltEntityExtractor at 0x20cac71cd08>]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Add Prebuilt entity\n",
    "client.model.add_prebuilt(app_id, versionId, prebuilt_extractor_names=[\"number\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<azure.cognitiveservices.language.luis.authoring.models._models_py3.OperationStatus at 0x20cac71ea08>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# define machine-learned entity\n",
    "mlEntityDefinition = [\n",
    "{\n",
    "    \"name\": \"Pizza\",\n",
    "    \"children\": [\n",
    "        { \"name\": \"Quantity\" },\n",
    "        { \"name\": \"Type\" },\n",
    "        { \"name\": \"Size\" }\n",
    "    ]\n",
    "},\n",
    "{\n",
    "    \"name\": \"Toppings\",\n",
    "    \"children\": [\n",
    "        { \"name\": \"Type\" },\n",
    "        { \"name\": \"Quantity\" }\n",
    "    ]\n",
    "}]\n",
    "\n",
    "# add entity to app\n",
    "modelId = client.model.add_entity(app_id, versionId, name=\"Pizza order\", children=mlEntityDefinition)\n",
    "\n",
    "# define phraselist - add phrases as significant vocabulary to app\n",
    "phraseList = {\n",
    "    \"enabledForAllModels\": False,\n",
    "    \"isExchangeable\": True,\n",
    "    \"name\": \"QuantityPhraselist\",\n",
    "    \"phrases\": \"few,more,extra\"\n",
    "}\n",
    "\n",
    "# add phrase list to app\n",
    "phraseListId = client.features.add_phrase_list(app_id, versionId, phraseList)\n",
    "\n",
    "# Get entity and subentities\n",
    "modelObject = client.model.get_entity(app_id, versionId, modelId)\n",
    "toppingQuantityId = get_grandchild_id(modelObject, \"Toppings\", \"Quantity\")\n",
    "pizzaQuantityId = get_grandchild_id(modelObject, \"Pizza\", \"Quantity\")\n",
    "\n",
    "# add model as feature to subentity model\n",
    "prebuiltFeatureRequiredDefinition = { \"model_name\": \"number\", \"is_required\": True }\n",
    "client.features.add_entity_feature(app_id, versionId, pizzaQuantityId, prebuiltFeatureRequiredDefinition)\n",
    "\n",
    "# add model as feature to subentity model\n",
    "prebuiltFeatureNotRequiredDefinition = { \"model_name\": \"number\" }\n",
    "client.features.add_entity_feature(app_id, versionId, toppingQuantityId, prebuiltFeatureNotRequiredDefinition)\n",
    "\n",
    "# add phrase list as feature to subentity model\n",
    "phraseListFeatureDefinition = { \"feature_name\": \"QuantityPhraselist\", \"model_name\": None }\n",
    "client.features.add_entity_feature(app_id, versionId, toppingQuantityId, phraseListFeatureDefinition)"
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
      "Labeled Example Utterance: {'text': 'I want two small seafood pizzas with extra cheese.', 'intentName': 'OrderPizzaIntent', 'entityLabels': [{'startCharIndex': 7, 'endCharIndex': 48, 'entityName': 'Pizza order', 'children': [{'startCharIndex': 7, 'endCharIndex': 30, 'entityName': 'Pizza', 'children': [{'startCharIndex': 7, 'endCharIndex': 9, 'entityName': 'Quantity'}, {'startCharIndex': 11, 'endCharIndex': 15, 'entityName': 'Size'}, {'startCharIndex': 17, 'endCharIndex': 23, 'entityName': 'Type'}]}, {'startCharIndex': 37, 'endCharIndex': 48, 'entityName': 'Toppings', 'children': [{'startCharIndex': 37, 'endCharIndex': 41, 'entityName': 'Quantity'}, {'startCharIndex': 43, 'endCharIndex': 48, 'entityName': 'Type'}]}]}]}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<azure.cognitiveservices.language.luis.authoring.models._models_py3.LabelExampleResponse at 0x20cac728148>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Define labeled example\n",
    "labeledExampleUtteranceWithMLEntity = {\n",
    "    \"text\": \"I want two small seafood pizzas with extra cheese.\",\n",
    "    \"intentName\": intentName,\n",
    "    \"entityLabels\": [\n",
    "        {\n",
    "            \"startCharIndex\": 7,\n",
    "            \"endCharIndex\": 48,\n",
    "            \"entityName\": \"Pizza order\",\n",
    "            \"children\": [\n",
    "                {\n",
    "                    \"startCharIndex\": 7,\n",
    "                    \"endCharIndex\": 30,\n",
    "                    \"entityName\": \"Pizza\",\n",
    "                    \"children\": [\n",
    "                        {\n",
    "                            \"startCharIndex\": 7,\n",
    "                            \"endCharIndex\": 9,\n",
    "                            \"entityName\": \"Quantity\"\n",
    "                        },\n",
    "                        {\n",
    "                            \"startCharIndex\": 11,\n",
    "                            \"endCharIndex\": 15,\n",
    "                            \"entityName\": \"Size\"\n",
    "                        },\n",
    "                        {\n",
    "                            \"startCharIndex\": 17,\n",
    "                            \"endCharIndex\": 23,\n",
    "                            \"entityName\": \"Type\"\n",
    "                        }]\n",
    "                },\n",
    "                {\n",
    "                    \"startCharIndex\": 37,\n",
    "                    \"endCharIndex\": 48,\n",
    "                    \"entityName\": \"Toppings\",\n",
    "                    \"children\": [\n",
    "                        {\n",
    "                            \"startCharIndex\": 37,\n",
    "                            \"endCharIndex\": 41,\n",
    "                            \"entityName\": \"Quantity\"\n",
    "                        },\n",
    "                        {\n",
    "                            \"startCharIndex\": 43,\n",
    "                            \"endCharIndex\": 48,\n",
    "                            \"entityName\": \"Type\"\n",
    "                        }]\n",
    "                }\n",
    "            ]\n",
    "        }\n",
    "    ]\n",
    "}\n",
    "\n",
    "print(\"Labeled Example Utterance:\", labeledExampleUtteranceWithMLEntity)\n",
    "\n",
    "# Add an example for the entity.\n",
    "# Enable nested children to allow using multiple models with the same name.\n",
    "# The quantity subentity and the phraselist could have the same exact name if this is set to True\n",
    "client.examples.add(app_id, versionId, labeledExampleUtteranceWithMLEntity, { \"enableNestedChildren\": True })"
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
