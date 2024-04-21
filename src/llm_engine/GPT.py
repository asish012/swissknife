import os
import sys
import streamlit as st
sys.path.append('..')
from decouple import config
from openai import OpenAI


def get_openai_api_key():
    api_key = config('OPENAI_API_KEY')
    if not api_key:
        api_key = st.secrets["OPENAI_API_KEY"]
    if not api_key:
        api_key = os.environ["OPENAI_API_KEY"]
    return api_key

class GPTQuery:
    CLIENT = OpenAI(api_key=get_openai_api_key())

    def __init__(self, system_prompt, tokens=3000, temperature=0.75):
        self._system_prompt = system_prompt
        self._result = None
        self._max_tokens = tokens
        self._temperature = temperature

    def translations(self, query):
        try:
            print(">>>GPT System", self._system_prompt)
            print(">>>GPT Query", query)
            transcription = self.CLIENT.audio.translations.create(model="whisper-1", file=audio_file)
            # return transcription['text']
            completion = self.CLIENT.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self._system_prompt},
                    {"role": "user", "content": query},
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