{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install azure-cognitiveservices-personalizer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from azure.cognitiveservices.personalizer import PersonalizerClient\n",
    "from azure.cognitiveservices.personalizer.models import RankableAction, RewardRequest, RankRequest\n",
    "from msrest.authentication import CognitiveServicesCredentials\n",
    "\n",
    "import datetime, json, os, time, uuid\n",
    "\n",
    "key = \"8aa5a928f0a14d6f83642a598f88e396\"\n",
    "endpoint = \"https://mypersonalizer1.cognitiveservices.azure.com/\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Instantiate a Personalizer client\n",
    "client = PersonalizerClient(endpoint, CognitiveServicesCredentials(key))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_actions():\n",
    "    action1 = RankableAction(id='pasta', features=[{\"taste\":\"salty\", \"spice_level\":\"medium\"},{\"nutrition_level\":5,\"cuisine\":\"italian\"}])\n",
    "    action2 = RankableAction(id='ice cream', features=[{\"taste\":\"sweet\", \"spice_level\":\"none\"}, { \"nutritional_level\": 2 }])\n",
    "    action3 = RankableAction(id='juice', features=[{\"taste\":\"sweet\", 'spice_level':'none'}, {'nutritional_level': 5}, {'drink':True}])\n",
    "    action4 = RankableAction(id='salad', features=[{'taste':'salty', 'spice_level':'none'},{'nutritional_level': 2}])\n",
    "    return [action1, action2, action3, action4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_user_timeofday():\n",
    "    res={}\n",
    "    time_features = [\"morning\", \"afternoon\", \"evening\", \"night\"]\n",
    "    time = input(\"What time of day is it (enter number)? 1. morning 2. afternoon 3. evening 4. night\\n\")\n",
    "    try:\n",
    "        ptime = int(time)\n",
    "        if(ptime<=0 or ptime>len(time_features)):\n",
    "            raise IndexError\n",
    "        res['time_of_day'] = time_features[ptime-1]\n",
    "    except (ValueError, IndexError):\n",
    "        print(\"Entered value is invalid. Setting feature value to\", time_features[0] + \".\")\n",
    "        res['time_of_day'] = time_features[0]\n",
    "    return res"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_user_preference():\n",
    "    res = {}\n",
    "    taste_features = ['salty','sweet']\n",
    "    pref = input(\"What type of food would you prefer? Enter number 1.salty 2.sweet\\n\")\n",
    "    \n",
    "    try:\n",
    "        ppref = int(pref)\n",
    "        if(ppref<=0 or ppref>len(taste_features)):\n",
    "            raise IndexError\n",
    "        res['taste_preference'] = taste_features[ppref-1]\n",
    "    except (ValueError, IndexError):\n",
    "        print(\"Entered value is invalid. Setting feature value to\", taste_features[0]+ \".\")\n",
    "        res['taste_preference'] = taste_features[0]\n",
    "    return res"
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
      "What type of food would you prefer? Enter number 1.salty 2.sweet\n",
      "2\n",
      "What time of day is it (enter number)? 1. morning 2. afternoon 3. evening 4. night\n",
      "4\n",
      "Personalizer service ranked the actions with the probabilities listed below:\n",
      "salad : 0.8666667\n",
      "ice cream : 0.06666667\n",
      "juice : 0.0\n",
      "pasta : 0.06666667\n",
      "Personalizer thinks you would like to have salad.\n",
      "Is this correct?(y/n)\n",
      "n\n",
      "Press Q to exit, any other key to continue: q\n"
     ]
    }
   ],
   "source": [
    "keep_going = True\n",
    "while keep_going:\n",
    "\n",
    "    eventid = str(uuid.uuid4())\n",
    "\n",
    "    context = [get_user_preference(), get_user_timeofday()]\n",
    "    actions = get_actions()\n",
    "\n",
    "    rank_request = RankRequest( actions=actions, context_features=context, excluded_actions=['juice'], event_id=eventid)\n",
    "    response = client.rank(rank_request=rank_request)\n",
    "    \n",
    "    print(\"Personalizer service ranked the actions with the probabilities listed below:\")\n",
    "    \n",
    "    rankedList = response.ranking\n",
    "    for ranked in rankedList:\n",
    "        print(ranked.id, ':',ranked.probability)\n",
    "\n",
    "    print(\"Personalizer thinks you would like to have\", response.reward_action_id+\".\")\n",
    "    answer = input(\"Is this correct?(y/n)\\n\")[0]\n",
    "\n",
    "    reward_val = \"0.0\"\n",
    "    \n",
    "    if(answer.lower()=='y'):\n",
    "        reward_val = \"1.0\"\n",
    "    elif(answer.lower()=='n'):\n",
    "        reward_val = \"0.0\"\n",
    "    else:\n",
    "        print(\"Entered choice is invalid. Service assumes that you didn't like the recommended food choice.\")\n",
    "\n",
    "    client.events.reward(event_id=eventid, value=reward_val)\n",
    "\n",
    "    br = input(\"Press Q to exit, any other key to continue: \")\n",
    "    if(br.lower()=='q'):\n",
    "        keep_going = False"
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
