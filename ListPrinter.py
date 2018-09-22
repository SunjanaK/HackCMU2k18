

from tkinter import *  # from tkinter import *
import time

from google.cloud import texttospeech
client = texttospeech.TextToSpeechClient()


listy = ["I", "WANT", "CAKE"]
import pygame
#
# root = Tk()
# t = Text(root)
#
i = 0
# t.pack()


def loadmp3player(file):
        # print(file)
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(0.5)
        # pygame.event.wait()

for word in listy:
    # t.insert(END, word + " ")
    synthesis_input = texttospeech.types.SynthesisInput(text="What does")

    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    with open('output1.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        # print('Audio content written to file "output1.mp3"')
        out.close()
    file = 'output1.mp3'
    loadmp3player(file)
    # pygame.init()
    # pygame.mixer.init()
    # pygame.mixer.music.load(file)
    # pygame.mixer.music.play()
    # pygame.event.wait()
    for letter in word:
        # time.sleep(0.5)
        print(letter)
        synthesis_input = texttospeech.types.SynthesisInput(text=letter)
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)
        response = client.synthesize_speech(synthesis_input, voice, audio_config)
        with open(str(i)+ ".mp3", 'wb') as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            # print('Audio content written to file "output2.mp3"')
            out.close()
        file = str(i)+ ".mp3"
        loadmp3player(file)
        i += 1

        # pygame.init()
        # pygame.mixer.init()
        # pygame.mixer.music.load(file)
        # pygame.mixer.music.play()
        # pygame.event.wait()

    synthesis_input = texttospeech.types.SynthesisInput(text="spell")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    with open('output3.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        # print('Audio content written to file "output.mp3"')
        out.close()
    file = 'output3.mp3'
    loadmp3player(file)
    # pygame.init()
    # pygame.mixer.init()
    # pygame.mixer.music.load(file)
    # pygame.mixer.music.play()
    # pygame.event.wait()


# root.mainloop()


# loadmp3player()
# print('som')

#
#
# with open('output.mp3', 'wb') as out:
#     # Write the response to the output file.
#     out.write(response.audio_content)
#     print('Audio content written to file "output.mp3"')
# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load(file)
# pygame.mixer.music.play()
# pygame.event.wait()
