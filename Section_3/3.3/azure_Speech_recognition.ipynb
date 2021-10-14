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
      "Requirement already satisfied: azure-cognitiveservices-speech in d:\\anaconda\\lib\\site-packages (1.17.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install azure-cognitiveservices-speech"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import azure.cognitiveservices.speech as speechsdk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "speech_config = speechsdk.SpeechConfig(subscription=\"f9bee9c0e51545bab4e932a5cdf27ff4\", region=\"westus\")"
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
      "Hi guys, my name is Sahar and I'm an instructor at Maker Demi.\n",
      "Recognized: Hi guys, my name is Sahar and I'm an instructor at Maker Demi.\n"
     ]
    }
   ],
   "source": [
    "def speech_to_text():\n",
    "    speech_config = speechsdk.SpeechConfig(subscription=\"f9bee9c0e51545bab4e932a5cdf27ff4\", region=\"westus\")\n",
    "    audio_input = speechsdk.AudioConfig(filename=r'D:\\Intern\\audio_saharsh.wav')\n",
    "    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)\n",
    "  \n",
    "    result = speech_recognizer.recognize_once_async().get()\n",
    "    print(result.text)\n",
    "    \n",
    "    #Error Handling\n",
    "    if result.reason == speechsdk.ResultReason.RecognizedSpeech:\n",
    "        print(\"Recognized: {}\".format(result.text))\n",
    "    elif result.reason == speechsdk.ResultReason.NoMatch:\n",
    "        print(\"No speech could be recognized: {}\".format(result.no_match_details))\n",
    "    elif result.reason == speechsdk.ResultReason.Canceled:\n",
    "        cancellation_details = result.cancellation_details\n",
    "        print(\"Speech Recognition canceled: {}\".format(cancellation_details.reason))\n",
    "        \n",
    "\n",
    "speech_to_text()"
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
      "Speak into your microphone.\n",
      "Hello friends, have a nice day.\n"
     ]
    }
   ],
   "source": [
    "def from_mic():\n",
    "    speech_config = speechsdk.SpeechConfig(subscription=\"f9bee9c0e51545bab4e932a5cdf27ff4\", region=\"westus\")\n",
    "    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)\n",
    "    \n",
    "    print(\"Speak into your microphone.\")\n",
    "    result = speech_recognizer.recognize_once_async().get()\n",
    "    print(result.text)\n",
    "\n",
    "from_mic()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "audio_config = speechsdk.audio.AudioConfig(filename=r'D:\\Intern\\audio_saharsh.wav')\n",
    "speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "done = False\n",
    "\n",
    "def stop_cb(evt):\n",
    "    print('CLOSING on {}'.format(evt))\n",
    "    speech_recognizer.stop_continuous_recognition()\n",
    "    done = True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))\n",
    "speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt)))\n",
    "speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))\n",
    "speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))\n",
    "speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))\n",
    "\n",
    "speech_recognizer.session_stopped.connect(stop_cb)\n",
    "speech_recognizer.canceled.connect(stop_cb)"
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
      "SESSION STARTED: SessionEventArgs(session_id=4eee015a191a4b3f867925f799bba49f)\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'time' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-9-4b6390d201bd>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mspeech_recognizer\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstart_continuous_recognition\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mwhile\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mdone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[0mtime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m.5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'time' is not defined"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RECOGNIZING: SpeechRecognitionEventArgs(session_id=4eee015a191a4b3f867925f799bba49f, result=SpeechRecognitionResult(result_id=08fae609c0534b579828c9e3182cc2c6, text=\"hi\", reason=ResultReason.RecognizingSpeech))\n",
      "RECOGNIZING: SpeechRecognitionEventArgs(session_id=4eee015a191a4b3f867925f799bba49f, result=SpeechRecognitionResult(result_id=b2c188ddcbab4020999abf404c140d9c, text=\"hi guys\", reason=ResultReason.RecognizingSpeech))\n",
      "RECOGNIZING: SpeechRecognitionEventArgs(session_id=4eee015a191a4b3f867925f799bba49f, result=SpeechRecognitionResult(result_id=3658ce3ea0554e65be8132598ec0964a, text=\"hi guys my name is\", reason=ResultReason.RecognizingSpeech))\n",
      "RECOGNIZING: SpeechRecognitionEventArgs(session_id=4eee015a191a4b3f867925f799bba49f, result=SpeechRecognitionResult(result_id=45584a0c4b6e440f819dd92fe0a8513d, text=\"hi guys my name is sahar\", reason=ResultReason.RecognizingSpeech))\n",
      "RECOGNIZING: SpeechRecognitionEventArgs(session_id=4eee015a191a4b3f867925f799bba49f, result=SpeechRecognitionResult(result_id=4821280a89ae4304af550f3161771c70, text=\"hi guys my name is sahar and\", reason=ResultReason.RecognizingSpeech))\n",
      "RECOGNIZING: SpeechRecognitionEventArgs(session_id=4eee015a191a4b3f867925f799bba49f, result=SpeechRecognitionResult(result_id=8f2a4cf4f7e448d8a62945ec8cce9948, text=\"hi guys my name is sahar and diamond\", reason=ResultReason.RecognizingSpeech))\n",
      "RECOGNIZING: SpeechRecognitionEventArgs(session_id=4eee015a191a4b3f867925f799bba49f, result=SpeechRecognitionResult(result_id=19e0650321724da39ae2322e6af04802, text=\"hi guys my name is sahar and i'm an\", reason=ResultReason.RecognizingSpeech))\n",
      "RECOGNIZING: SpeechRecognitionEventArgs(session_id=4eee015a191a4b3f867925f799bba49f, result=SpeechRecognitionResult(result_id=7def9c103d9f4d2095493cea272627f1, text=\"hi guys my name is sahar and i'm an instructor\", reason=ResultReason.RecognizingSpeech))\n",
      "RECOGNIZING: SpeechRecognitionEventArgs(session_id=4eee015a191a4b3f867925f799bba49f, result=SpeechRecognitionResult(result_id=fa5912ffbaea4bb0937135c7104191ee, text=\"hi guys my name is sahar and i'm an instructor at\", reason=ResultReason.RecognizingSpeech))\n",
      "RECOGNIZING: SpeechRecognitionEventArgs(session_id=4eee015a191a4b3f867925f799bba49f, result=SpeechRecognitionResult(result_id=5ad4c418b76b473793d59f601382bf67, text=\"hi guys my name is sahar and i'm an instructor at maker\", reason=ResultReason.RecognizingSpeech))\n",
      "RECOGNIZING: SpeechRecognitionEventArgs(session_id=4eee015a191a4b3f867925f799bba49f, result=SpeechRecognitionResult(result_id=702face7a34644c69de3a7890deb32d6, text=\"hi guys my name is sahar and i'm an instructor at maker demi\", reason=ResultReason.RecognizingSpeech))\n",
      "RECOGNIZED: SpeechRecognitionEventArgs(session_id=4eee015a191a4b3f867925f799bba49f, result=SpeechRecognitionResult(result_id=53daf7d39761464c8c4e761b72466334, text=\"Hi guys, my name is Sahar and I'm an instructor at maker Dummy.\", reason=ResultReason.RecognizedSpeech))\n",
      "RECOGNIZED: SpeechRecognitionEventArgs(session_id=4eee015a191a4b3f867925f799bba49f, result=SpeechRecognitionResult(result_id=003f9729b20c4785bbe0f4c98ca2ae59, text=\"\", reason=ResultReason.RecognizedSpeech))\n",
      "CANCELED SpeechRecognitionCanceledEventArgs(session_id=4eee015a191a4b3f867925f799bba49f, result=SpeechRecognitionResult(result_id=28daadc00e2b46f0bb110f752246dbd8, text=\"\", reason=ResultReason.Canceled))\n",
      "CLOSING on SpeechRecognitionCanceledEventArgs(session_id=4eee015a191a4b3f867925f799bba49f, result=SpeechRecognitionResult(result_id=28daadc00e2b46f0bb110f752246dbd8, text=\"\", reason=ResultReason.Canceled))\n",
      "SESSION STOPPED SessionEventArgs(session_id=4eee015a191a4b3f867925f799bba49f)\n",
      "CLOSING on SessionEventArgs(session_id=4eee015a191a4b3f867925f799bba49f)\n"
     ]
    }
   ],
   "source": [
    "speech_recognizer.start_continuous_recognition()\n",
    "while not done:\n",
    "    time.sleep(.5)"
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
      "Hi guys my name is Saharsh and I'm an instructor at Makerdemy.\n"
     ]
    }
   ],
   "source": [
    "def speech_to_text_grammar():\n",
    "    speech_config = speechsdk.SpeechConfig(subscription=\"f9bee9c0e51545bab4e932a5cdf27ff4\", region=\"westus\")\n",
    "    audio_input = speechsdk.AudioConfig(filename=r'D:\\Intern\\audio_saharsh.wav')\n",
    "    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)\n",
    "    phrase_list_grammar = speechsdk.PhraseListGrammar.from_recognizer(speech_recognizer)\n",
    "    phrase_list_grammar.addPhrase(\"Saharsh\")\n",
    "    phrase_list_grammar.addPhrase(\"Makerdemy\")\n",
    "    \n",
    "    result = speech_recognizer.recognize_once_async().get()\n",
    "    print(result.text)\n",
    "    \n",
    "\n",
    "speech_to_text_grammar()"
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
      "What are you doing?\n"
     ]
    }
   ],
   "source": [
    "def speech_to_text():\n",
    "    speech_config = speechsdk.SpeechConfig(subscription=\"f9bee9c0e51545bab4e932a5cdf27ff4\", region=\"westus\")    \n",
    "    speech_config.enable_dictation()\n",
    "    audio_input = speechsdk.AudioConfig(filename=r'D:\\Intern\\audio_punctuation.wav')\n",
    "    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)\n",
    "    \n",
    "    result = speech_recognizer.recognize_once_async().get()\n",
    "    print(result.text)\n",
    "    \n",
    "\n",
    "speech_to_text()"
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
      "Hi Guys, Mein Name ist der Hirsch alemannenstraße.\n"
     ]
    }
   ],
   "source": [
    "def speech_to_text():\n",
    "    speech_config = speechsdk.SpeechConfig(subscription=\"f9bee9c0e51545bab4e932a5cdf27ff4\", region=\"westus\")\n",
    "    speech_config.speech_recognition_language=\"de-DE\"\n",
    "    audio_input = speechsdk.AudioConfig(filename=r'D:\\Intern\\audio_saharsh.wav')\n",
    "    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)\n",
    "  \n",
    "    result = speech_recognizer.recognize_once_async().get()\n",
    "    print(result.text)\n",
    "       \n",
    "\n",
    "speech_to_text()"
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
