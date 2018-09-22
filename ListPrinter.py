from __future__ import division

import re
import sys
import time
import io

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import pyaudio
import wave
from six.moves import queue

from tkinter import *  # from tkinter import *
import time

from google.cloud import texttospeech
client = texttospeech.TextToSpeechClient()



listy = ["cat", "made", "cake"]
import pygame

i = 0


string = " "
def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()
    # print("read content file")

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='en-US')

    # print("config done")
    response = client.recognize(config, audio)
    # print("response found")
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.

        print(u'Transcript: {}'.format(result.alternatives[0].transcript))
        return result.alternatives[0].transcript


def record_file(time):
    language_code = 'en-US'  # a BCP-47 language tag
    words = []
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = time
    WAVE_OUTPUT_FILENAME = "voice.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)


    wf.writeframes(b''.join(frames))
    wf.close()

#
#
# def main():
#         record_file(); #need this, output voice.wav
#         spoken = transcribe_file("voice.wav") #returns a string with whatever it recognizes
#
#         print(type(spoken))
#         sentence = "the cat is on the hat"
#
#         spoken_set = set(spoken.split(' '))
#         sentence_set = set(sentence.split(' '))
#         print("Common words:")
#         print(spoken_set & sentence_set)
#         print(len(spoken_set & sentence_set))
#
#
#
#
#
#
# if __name__ == '__main__':
#     main()

def loadmp3player(file):
        # print(file)
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(0.5)


combolist = [ ]

for word in listy:

    synthesis_input = texttospeech.types.SynthesisInput(text="Spell")

    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    with open('output1.mp3', 'wb') as out:

        out.write(response.audio_content)

        out.close()
    file = 'output1.mp3'
    loadmp3player(file)

    for letter in word:

        string += letter
        print(string)
        synthesis_input = texttospeech.types.SynthesisInput(text=letter)
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)
        response = client.synthesize_speech(synthesis_input, voice, audio_config)
        with open(str(i)+ ".mp3", 'wb') as out:

            out.write(response.audio_content)

            out.close()
        file = str(i)+ ".mp3"
        loadmp3player(file)
        i += 1

    correct = False
    correctness = 0
    while not correct:
        print(correctness)
        record_file(3)
        spoken = transcribe_file("voice.wav") #returns a string with whatever it recognizes
        statement = ""

        if spoken != None:
            if word in spoken or spoken in word:
                correct = True
                combolist += [word + " "]
                statement += word
                synthesis_input = texttospeech.types.SynthesisInput(text="Good Job!")
                voice = texttospeech.types.VoiceSelectionParams(
                language_code='en-US',
                ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
                audio_config = texttospeech.types.AudioConfig(
                audio_encoding=texttospeech.enums.AudioEncoding.MP3)
                response = client.synthesize_speech(synthesis_input, voice, audio_config)
                with open("praise.mp3", 'wb') as out:

                    out.write(response.audio_content)

                    out.close()
                    file = "praise.mp3"
                    loadmp3player(file)

        if correct == False:
            correctness += 1
            synthesis_input = texttospeech.types.SynthesisInput(text="Try Again!")
            voice = texttospeech.types.VoiceSelectionParams(
                language_code='en-US',
                ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
            audio_config = texttospeech.types.AudioConfig(
                audio_encoding=texttospeech.enums.AudioEncoding.MP3)
            response = client.synthesize_speech(synthesis_input, voice, audio_config)
            with open("retry.mp3", 'wb') as out:

                out.write(response.audio_content)

                out.close()
            file = "retry.mp3"
            loadmp3player(file)
            correct = False
            synthesis_input = texttospeech.types.SynthesisInput(text="Spell")

            voice = texttospeech.types.VoiceSelectionParams(
                language_code='en-US',
                ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
            audio_config = texttospeech.types.AudioConfig(
                audio_encoding=texttospeech.enums.AudioEncoding.MP3)
            response = client.synthesize_speech(synthesis_input, voice, audio_config)

            with open('output1.mp3', 'wb') as out:

                out.write(response.audio_content)

                out.close()
            file = 'output1.mp3'
            loadmp3player(file)
            for letter in word:
                correct = False

                statement += letter
                print(statement)
                synthesis_input = texttospeech.types.SynthesisInput(text=letter)
                voice = texttospeech.types.VoiceSelectionParams(
                    language_code='en-US',
                    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
                audio_config = texttospeech.types.AudioConfig(
                    audio_encoding=texttospeech.enums.AudioEncoding.MP3)
                response = client.synthesize_speech(synthesis_input, voice, audio_config)
                with open(str(i)+ ".mp3", 'wb') as out:

                    out.write(response.audio_content)

                    out.close()
                file = str(i)+ ".mp3"
                loadmp3player(file)
                i += 1

    print("while loop over")
    string += " "

    if len(combolist) > 1:
        combination = ' '.join(combolist)
        print(combination)
        synthesis_input = texttospeech.types.SynthesisInput(text="Now put the words together")

        voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)
        response = client.synthesize_speech(synthesis_input, voice, audio_config)
        with open("together.mp3", 'wb') as out:

            out.write(response.audio_content)

            out.close()
        file = "together.mp3"
        loadmp3player(file)
        record_file(5)
        spoken = transcribe_file("voice.wav") #returns a string with whatever it recognizes

        spoken_set = set(spoken.split(' '))



        if spoken_set != None:
            sentence_set = set(combination.split(' '))
            # print(sentence_set)
            # print("Common words:")
            # print(spoken_set & sentence_set)
            # print(len(spoken_set & sentence_set))
            if len(spoken_set & sentence_set) >= 2:
                synthesis_input = texttospeech.types.SynthesisInput(text="Good Job!")
                voice = texttospeech.types.VoiceSelectionParams(
                    language_code='en-US',
                    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
                audio_config = texttospeech.types.AudioConfig(
                    audio_encoding=texttospeech.enums.AudioEncoding.MP3)
                response = client.synthesize_speech(synthesis_input, voice, audio_config)
                with open("praise.mp3", 'wb') as out:

                    out.write(response.audio_content)

                    out.close()
                file = "praise.mp3"
                loadmp3player(file)



statement = ' '.join(listy)
synthesis_input = texttospeech.types.SynthesisInput(text="Now say the sentence")
print(statement)
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)
response = client.synthesize_speech(synthesis_input, voice, audio_config)
with open(str(i)+ ".mp3", 'wb') as out:

    out.write(response.audio_content)

    out.close()
file = str(i)+ ".mp3"
loadmp3player(file)
record_file(5)
spoken = transcribe_file("voice.wav") #returns a string with whatever it recognizes

spoken_set = set(spoken.split(' '))



if spoken_set != None:
    sentence_set = set(statement.split(' '))
    # print(sentence_set)
    # print("Common words:")
    # print(spoken_set & sentence_set)
    # print(len(spoken_set & sentence_set))
    if len(spoken_set & sentence_set) >= 2:
        synthesis_input = texttospeech.types.SynthesisInput(text="Good Job!")
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)
        response = client.synthesize_speech(synthesis_input, voice, audio_config)
        with open("praise.mp3", 'wb') as out:

            out.write(response.audio_content)

            out.close()
        file = "praise.mp3"
        loadmp3player(file)
    # synthesis_input = texttospeech.types.SynthesisInput(text="spell")
    # voice = texttospeech.types.VoiceSelectionParams(
    #     language_code='en-US',
    #     ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
    # audio_config = texttospeech.types.AudioConfig(
    #     audio_encoding=texttospeech.enums.AudioEncoding.MP3)
    # response = client.synthesize_speech(synthesis_input, voice, audio_config)
    # with open('output3.mp3', 'wb') as out:
    #     # Write the response to the output file.
    #     out.write(response.audio_content)
    #     # print('Audio content written to file "output.mp3"')
    #     out.close()
    # file = 'output3.mp3'
    # loadmp3player(file)
