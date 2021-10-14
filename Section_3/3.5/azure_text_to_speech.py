{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat\n",
    "from azure.cognitiveservices.speech.audio import AudioOutputConfig"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "speech_config = SpeechConfig(subscription=\"f9bee9c0e51545bab4e932a5cdf27ff4\", region=\"westus\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#audio_config = AudioOutputConfig(filename=r\"C:\\Users\\sahar\\OneDrive\\Desktop\\audios_tts\\audio0.wav\")\n",
    "audio_config = AudioOutputConfig(use_default_speaker=True)\n"
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
       "<azure.cognitiveservices.speech.ResultFuture at 0x1784ffeb7c8>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)\n",
    "synthesizer.speak_text_async(\"Hi Guys, this is Saharsh, part of the instructor team at MAKERDEMY.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)\n",
    "result = synthesizer.speak_text_async(\"Getting the response as an in-memory stream.\").get()\n",
    "stream = AudioDataStream(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat[\"Riff24Khz16BitMonoPcm\"])\n",
    "synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)\n",
    "\n",
    "result = synthesizer.speak_text_async(\"Customizing the audio output format.\").get()\n",
    "stream = AudioDataStream(result)\n",
    "stream.save_to_wav_file(r\"C:\\Users\\sahar\\OneDrive\\Desktop\\audios_tts\\audio1.wav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Single voice \n",
    "synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)\n",
    "\n",
    "ssml_string = open(\"ssml.xml\", \"r\").read()\n",
    "result = synthesizer.speak_ssml_async(ssml_string).get()\n",
    "\n",
    "stream = AudioDataStream(result)\n",
    "stream.save_to_wav_file(r\"C:\\Users\\sahar\\OneDrive\\Desktop\\audios_tts\\audio2.wav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Dual voice \n",
    "synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)\n",
    "\n",
    "ssml_string = open(\"ssml1.xml\", \"r\").read()\n",
    "result = synthesizer.speak_ssml_async(ssml_string).get()\n",
    "\n",
    "stream = AudioDataStream(result)\n",
    "stream.save_to_wav_file(r\"C:\\Users\\sahar\\OneDrive\\Desktop\\audios_tts\\audio3.wav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Adjust speaking styles \n",
    "synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)\n",
    "\n",
    "ssml_string = open(\"ssml2.xml\", \"r\").read()\n",
    "result = synthesizer.speak_ssml_async(ssml_string).get()\n",
    "\n",
    "stream = AudioDataStream(result)\n",
    "stream.save_to_wav_file(r\"C:\\Users\\sahar\\OneDrive\\Desktop\\audios_tts\\audio4.wav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Adjust speaking language \n",
    "synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)\n",
    "\n",
    "ssml_string = open(\"ssml3.xml\", \"r\").read()\n",
    "result = synthesizer.speak_ssml_async(ssml_string).get()\n",
    "\n",
    "stream = AudioDataStream(result)\n",
    "stream.save_to_wav_file(r\"C:\\Users\\sahar\\OneDrive\\Desktop\\audios_tts\\audio5.wav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Add/remove breaks \n",
    "synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)\n",
    "\n",
    "ssml_string = open(\"ssml4.xml\", \"r\").read()\n",
    "result = synthesizer.speak_ssml_async(ssml_string).get()\n",
    "\n",
    "stream = AudioDataStream(result)\n",
    "stream.save_to_wav_file(r\"C:\\Users\\sahar\\OneDrive\\Desktop\\audios_tts\\audio6.wav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Add Phonemes for better pronunciation\n",
    "synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)\n",
    "\n",
    "ssml_string = open(\"ssml5.xml\", \"r\").read()\n",
    "result = synthesizer.speak_ssml_async(ssml_string).get()\n",
    "\n",
    "stream = AudioDataStream(result)\n",
    "stream.save_to_wav_file(r\"C:\\Users\\sahar\\OneDrive\\Desktop\\audios_tts\\audio7.wav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Add Custom lexicon for better pronunciation\n",
    "synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)\n",
    "\n",
    "ssml_string = open(\"ssml6.xml\", \"r\").read()\n",
    "result = synthesizer.speak_ssml_async(ssml_string).get()\n",
    "\n",
    "stream = AudioDataStream(result)\n",
    "#stream.save_to_wav_file(r\"C:\\Users\\sahar\\OneDrive\\Desktop\\audios_tts\\yo7.wav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Use the Custom lexicon for better pronunciation in a sentence\n",
    "synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)\n",
    "\n",
    "ssml_string = open(\"ssml7.xml\", \"r\").read()\n",
    "result = synthesizer.speak_ssml_async(ssml_string).get()\n",
    "\n",
    "stream = AudioDataStream(result)\n",
    "stream.save_to_wav_file(r\"C:\\Users\\sahar\\OneDrive\\Desktop\\audios_tts\\audio8.wav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Change speaking rate\n",
    "synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)\n",
    "\n",
    "ssml_string = open(\"ssml8.xml\", \"r\").read()\n",
    "result = synthesizer.speak_ssml_async(ssml_string).get()\n",
    "\n",
    "stream = AudioDataStream(result)\n",
    "stream.save_to_wav_file(r\"C:\\Users\\sahar\\OneDrive\\Desktop\\audios_tts\\audio9.wav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Change volume\n",
    "synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)\n",
    "\n",
    "ssml_string = open(\"ssml9.xml\", \"r\").read()\n",
    "result = synthesizer.speak_ssml_async(ssml_string).get()\n",
    "\n",
    "stream = AudioDataStream(result)\n",
    "stream.save_to_wav_file(r\"C:\\Users\\sahar\\OneDrive\\Desktop\\audios_tts\\audio10.wav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Change the pitch\n",
    "synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)\n",
    "\n",
    "ssml_string = open(\"ssml10.xml\", \"r\").read()\n",
    "result = synthesizer.speak_ssml_async(ssml_string).get()\n",
    "\n",
    "stream = AudioDataStream(result)\n",
    "stream.save_to_wav_file(r\"C:\\Users\\sahar\\OneDrive\\Desktop\\audios_tts\\audio11.wav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Change the pitch contour\n",
    "synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)\n",
    "\n",
    "ssml_string = open(\"ssml11.xml\", \"r\").read()\n",
    "result = synthesizer.speak_ssml_async(ssml_string).get()\n",
    "\n",
    "stream = AudioDataStream(result)\n",
    "stream.save_to_wav_file(r\"C:\\Users\\sahar\\OneDrive\\Desktop\\audios_tts\\audio12.wav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "#say-as element\n",
    "synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)\n",
    "\n",
    "ssml_string = open(\"ssml12.xml\", \"r\").read()\n",
    "result = synthesizer.speak_ssml_async(ssml_string).get()\n",
    "\n",
    "stream = AudioDataStream(result)\n",
    "stream.save_to_wav_file(r\"C:\\Users\\sahar\\OneDrive\\Desktop\\audios_tts\\audio13.wav\")"
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
