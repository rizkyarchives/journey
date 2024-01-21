'''This Class will be in charge in processing the questions data before serving it to the user.
   Will format the questions before sending to frontend and have the functionality to create the audio file from the script.
'''

from gtts import gTTS
import random
import pronouncing
import os
from pydub import AudioSegment
from pydub.playback import play

USERCORRECTANSWER_FORMAT = ('id', 'userid', 'questionid', 'from_table', 'category')
DATA_POSITION = {key: value for (value, key) in enumerate(USERCORRECTANSWER_FORMAT)}
ACCENT = ['co.in', 'com.au', 'us']

class QuizBrain():
    def __init__(self):
        pass

    def filter_questions(self, questions: list, answered_questions: list):
        answered_ids = []
        for element in answered_questions:
            answered_ids.append(element[DATA_POSITION['questionid']])
        return [element for element in questions if element['id'] not in answered_ids]
    
    def create_audio_file(self, question: dict, category):
        if category == 'conversation':
            dialogues = question['script'].split('\n')
            combined_audio = AudioSegment.silent(duration=0)
            for (i, dialogue) in enumerate(dialogues):
                if i % 2 == 0:
                    tts = gTTS(text=dialogue, tld=ACCENT[0], lang='en')
                    tts.save('temp.mp3')
                    audio = AudioSegment.from_mp3("temp.mp3")
                elif i % 2 == 1:
                    tts = gTTS(text=dialogue, tld=ACCENT[1], lang='en')
                    tts.save('temp.mp3')
                    audio = AudioSegment.from_mp3("temp.mp3")
                combined_audio = combined_audio + audio
            combined_audio.export('answer.mp3', format='mp3')
            os.remove('temp.mp3')
        else:
            tts = gTTS(text=question['script'], tld=ACCENT[2], lang='en')
            tts.save('answer.mp3')
    
    def create_options_for_listening(self, word: str):
        result = pronouncing.rhymes(word.lower())
        try:
            distractors = random.sample(result, k = 3)
            answer_options = [word] + distractors
        except ValueError:
            answer_options = [word] + result
            i = len(answer_options)
            while(i < 4):
                answer_options.append('-')
        return answer_options
    
    def play_sound(self):
        audio = AudioSegment.from_mp3("answer.mp3")
        play(audio)
