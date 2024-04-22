import os
import sys
import streamlit as st
from decouple import config
from openai import OpenAI
sys.path.append('..')


def get_openai_api_key():
    api_key = config('OPENAI_API_KEY')
    if not api_key:
        api_key = st.secrets["OPENAI_API_KEY"]
    if not api_key:
        api_key = os.environ["OPENAI_API_KEY"]
    return api_key


CLIENT = OpenAI(api_key=get_openai_api_key())


class Translator:
    def __init__(self):
        pass

    def translate_audio(self, audio_file):
        try:
            transcription = CLIENT.audio.translations.create(model="whisper-1", file=audio_file)
            if not transcription:
                raise Exception("Empty result !!!")
            return transcription.text
        except Exception as e:
            raise Exception("Failed to translate the audio file.")


class FinancialAdvisor:
    def __init__(self, tokens=2000, temperature=1):
        self._system_prompt = """
        Act as an English Grammar expert. 
        Rewrite the text fixing grammatical issues.
        """
        self._max_tokens = tokens
        self._temperature = temperature
        self._result = None

    def describe(self, text):
        try:
            print(">>>GPT System", self._system_prompt)
            print(">>>GPT Query", text)
            completion = CLIENT.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self._system_prompt},
                    {"role": "user", "content": text},
                ],
                max_tokens=self._max_tokens,
                temperature=self._temperature
            )
            self._result = completion.choices[0].message.content
            print(">>>GPT Response", self._result)
            return self._result
        except Exception as e:
            raise Exception(f'GPTQuery Error: {str(e)}')

    def get_result(self):
        return self._result