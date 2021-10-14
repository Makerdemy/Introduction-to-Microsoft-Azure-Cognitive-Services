{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import azure.cognitiveservices.speech as speechsdk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "speech_key, service_region = \"f9bee9c0e51545bab4e932a5cdf27ff4\", \"westus\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from_language, to_language = 'en-US', 'de'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def translate_speech_to_text():\n",
    "    translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=speech_key, region=service_region)\n",
    "\n",
    "    translation_config.speech_recognition_language = from_language\n",
    "    \n",
    "    translation_config.add_target_language(to_language)\n",
    "\n",
    "    recognizer = speechsdk.translation.TranslationRecognizer(\n",
    "            translation_config=translation_config)\n",
    "    \n",
    "    print('Say something...')\n",
    "    result = recognizer.recognize_once()\n",
    "    print(error_handling(reason=result.reason, result=result))"
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
      "Say something...\n",
      "RECOGNIZED \"en-US\": Hello friends, how are you guys doing?\n",
      "TRANSLATED into \"de\"\": Hallo Freunde, wie geht es euch?\n"
     ]
    }
   ],
   "source": [
    "def error_handling(reason, result):\n",
    "    reason_format = {\n",
    "        speechsdk.ResultReason.TranslatedSpeech:\n",
    "            f'RECOGNIZED \"{from_language}\": {result.text}\\n' +\n",
    "            f'TRANSLATED into \"{to_language}\"\": {result.translations[to_language]}',\n",
    "        speechsdk.ResultReason.RecognizedSpeech: f'Recognized: \"{result.text}\"',\n",
    "        speechsdk.ResultReason.NoMatch: f'No speech could be recognized: {result.no_match_details}',\n",
    "        speechsdk.ResultReason.Canceled: f'Speech Recognition canceled: {result.cancellation_details}'\n",
    "    }\n",
    "    return reason_format.get(reason, 'Unable to recognize speech')\n",
    "\n",
    "translate_speech_to_text()"
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
      "Say something...\n",
      "Recognized: \"Hello friends, how are you guys doing?\"\n",
      "Translated into \"de\": Hallo Freunde, wie geht es euch?\n",
      "Translated into \"en\": Hello friends, how are you guys doing?\n",
      "Translated into \"it\": Ciao amici, come state?\n",
      "Translated into \"pt\": Olá amigos, como vocês estão?\n",
      "Translated into \"zh-Hans\": 朋友们，你们好吗？\n"
     ]
    }
   ],
   "source": [
    "from_language, to_languages = 'en-US', [ 'de', 'en', 'it', 'pt', 'zh-Hans' ]\n",
    "\n",
    "def translate_speech_to_text():\n",
    "    translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=speech_key, region=service_region)\n",
    "\n",
    "    translation_config.speech_recognition_language = from_language\n",
    "    for lang in to_languages:\n",
    "        translation_config.add_target_language(lang)\n",
    "\n",
    "    recognizer = speechsdk.translation.TranslationRecognizer(\n",
    "            translation_config=translation_config)\n",
    "    \n",
    "    print('Say something...')\n",
    "    result = recognizer.recognize_once()\n",
    "    synthesize_translations(result=result)\n",
    "\n",
    "def synthesize_translations(result):\n",
    "    language_to_voice_map = {\n",
    "        \"de\": \"de-DE-KatjaNeural\",\n",
    "        \"en\": \"en-US-AriaNeural\",\n",
    "        \"it\": \"it-IT-ElsaNeural\",\n",
    "        \"pt\": \"pt-BR-FranciscaNeural\",\n",
    "        \"zh-Hans\": \"zh-CN-XiaoxiaoNeural\"\n",
    "    }\n",
    "    print(f'Recognized: \"{result.text}\"')\n",
    "\n",
    "    for language in result.translations:\n",
    "        translation = result.translations[language]\n",
    "        print(f'Translated into \"{language}\": {translation}')\n",
    "\n",
    "        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)\n",
    "        speech_config.speech_synthesis_voice_name = language_to_voice_map.get(language)\n",
    "        \n",
    "        audio_config = speechsdk.audio.AudioOutputConfig(filename=f'{language}-translation.wav')\n",
    "        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)\n",
    "        speech_synthesizer.speak_text_async(translation).get()\n",
    "\n",
    "translate_speech_to_text()"
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
