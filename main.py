"""
Main file for the Irancell's Operator project

this is only a Dummy preview from what will happen in main project

"""
from recorder import speech_to_text
import json
import asyncio
import pygame
from io import BytesIO
import requests
import base64
import soundfile as sf
import sounddevice as sd
import time

import numpy as np
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiN2Q0NWI2OGItODQyZi00OTgzLTg3ZmMtYTVmMmEzOTEzZDBkIiwidHlwZSI6ImFwaV90b2tlbiJ9.L93GDqn-KvgdtUho4emsiXhp3u8vCvUKgv6-NiCwAQo"}
async def save_audio(audio_bytes, filename):
    with open(filename, 'wb') as f:
        f.write(audio_bytes)
    await play_wav_file(filename)

async def play_wav_file(filename):
    wave_data, fs = sf.read(filename, dtype='float32')
    sd.play(wave_data, fs)
    sd.wait()


async def speech2text():
    url = "https://api.edenai.run/v2/audio/speech_to_text_async"
    data = {
        "providers": "openai",
        "language": "fa-IR",
    }
    files = {'file': open("/Users/codedpro/Desktop/Irancell/IRANCELL AGENT/audio/recording.wav", 'rb')}
    response = requests.post(url, data=data, files=files, headers=headers)
    result = json.loads(response.text)
    return result['results']['openai']['text']

async def textGen(text: str):
    url = "https://api.edenai.run/v2/text/chat"
    payload = {
        "providers": "openai",
        "text": text,
        "chatbot_global_action": "You are Irancell's Agent bot that assist user's in real time and fix their issues and report their issues to the Operators, also You Only response In persian language, and you should response to user like you are their personal Customer service agent and also if user had problem with their simcart you must ask for their problem and give some answers and then say you will report it to the Admins",
        "previous_history": [],
        "temperature": 0.0,
        "max_tokens": 1500,
        "fallback_providers": ""
    }
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    return result
async def voiceGen(text: str):
    url = "https://api.edenai.run/v2/audio/text_to_speech"
    payload = {
        "providers": "microsoft",
        "language": "fa-IR",
        "option": "MALE",
        "text": text,
        "fallback_providers": ""
    }
    response = requests.post(url, json=payload, headers=headers)

    result = response.json()
    audio_bytes = base64.b64decode(result['microsoft']['audio'])
    return audio_bytes

async def main():
    while True:
        print("go ahead im listening")
        speech_to_text() # TODO: get voice as input from Call Center
        print("Done listening")
        start_time = time.time()
        # TODO: Implement Speech enhancement and noise cancellation
        # TODO: Implement language and accent detection
        # TODO: Implement Users emotion and mood (optional)
        text = await speech2text()  # TODO: Use our own API for Speech To Text with supporting all languages and accents used in Iran
        #with also validating the texts using language model
        print("User: " + text)
        system = await textGen(text) # TODO: Use our own custom API for Language Model supporting all languages used in Iran, 
        # leveraging data from previous customer interactions including audios, chats,
        # and website analysis of Irancell along with user history.
        print("System: " + system['openai']['generated_text'])
        # TODO: Language Selection based on System's response language
        voice_bytes = await voiceGen(system['openai']['generated_text']) # TODO: Use our own custom API for Language Model supporting all languages used in Iran,
        # With Customized Voice and with realistic Voices, real time
        wav_filename = "/Users/codedpro/Desktop/Irancell/IRANCELL AGENT/audio/system_voice.wav"
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed timce: {elapsed_time} seconds")
        await save_audio(voice_bytes, wav_filename)# TODO: #return the audio to the Call center With Maximom 3s response time
        time.sleep(30)
if __name__ == "__main__":
    asyncio.run(main())
"""
Project overview:
    This Tool will get Human Voice in Persian, Azerbaijani, Kurdish, Arabic, Gilaki, Luri, Mazandarani, Balochi, Turkmen, English and etc ...
    Do Some Enchantments like improving voice with noise cancellation and Do some analyzes like detecting emotions and language of User.
    create Texts based on User's Voice with using advanced Language Model that can Support all languages mentioned to Improve it.
    Use That Texts with Our Text Generator Model to write response for our user based on All Informations gathered from Irancell's Customer's history 
    and live datas on my irancell and irancell.ir including latest Trends, News, Prices, Current User's History and etc ...
    We Will use response of Text Generator and make a realistic voice based on user's prefered language and responsed text and 
    return generated Voice to the User.

Models and Tools:
    At The end of the Day we Won't Have Only 1 Tool, we will have multiple Tools and APIs That We can reuse Multiple Times in Many Projects, including:
    ▪︎ Speech-To-Text powered by Ai which will Support Multiple languages and accents which some of are extremly rare and we are first ones in world sing that languages to train a model, and also we would have best models in them.
    ▪︎ Speech-Enchantment powered by Ai to increase quality of user's voice.
    ▪︎ Language-Model we will have a Language model powered by Ai in multiple languages used in Iran with vast information in Telecom and Customer Service and etc ...
    ▪︎ Text-To-Speech powered by Ai and using Voice Actors of Irancell in multiple languages used in iran with realistic Voices Trained on Vast amount of Datas.
    ▪︎ Speech-Emotion-Recognizer to recognizer Emotion of the speaker and optimize response based on that and also Do actions needed based on Emotion of the user in call
    ▪︎ Speech-Language-Recognizer to detect what language user is speaking in and write response based on that.
    ▪︎ Speech-Identification which will detect if multiple Persons are in Call and we be able to Idenify that which speech is blong to what person ( its a tool for collecting Data from History Of Voices To Detect Operators texts and Users texts seprately)
    All of These Great Tools will be usable For any future needs of MTN Irancell and they will be easy to understand for any Developer to use the APIs.

benefits:
    Cost Reduction
        ▶︎ Operational Efficiency: Automation of customer service through AI can reduce the need for a large support staff, leading to substantial cost savings over time 
        and reducing the need for extensive human recruitment
    Revenue Increase
        ▶︎ Enhanced Customer Experience: The project's ability to provide personalized and efficient customer service can lead to increased customer satisfaction and loyalty
        ▶︎ New Revenue: The development of multiple tools and APIs as part of the project opens up opportunities for MTN Irancell to license these technologies 
        to other businesses or to create new services for customers, generating additional revenue streams !
    Competitive Advantage
        ▶︎ Market Differentiation: By being the first to train models in extremely rare languages and accents, MTN Irancell can set itself apart from competitors, 
          offering unique services that cater to a diverse customer base.
        ▶︎ Innovation Leadership: The project positions MTN Irancell as a leader in innovation within the telecom sector,
          potentially attracting more customers and partnerships.
    Efficiency and Productivity
        ▶︎ Quality Assurance: Automated quality assurance and audits through speech analytics ensure high standards of customer service, 
        reducing the likelihood of errors and improving customer trust
    these are only a few of benefits that we offer.

Requirements:
    Data: 
        Irancell's Customer audios which where recorded in Call Center.
        Customer Live Chats from irancell.ir and etc.
        all Contents availble inside Irancell.ir, my irancell and etc (anything that Ai Should answer them)
        Audio contents from internet, TV and radio shows, etc .... ( we need a lot of data)
    Resources:
        Server with High GPU ( higher == better )
        Server must be in same network as call center so we can transfer data in real time and fast
        Studio for Recording audios and related things
        Development essentials
    Team: 
        Developer:
            i ll Do all Developments related to, Data analyze, API Development, Machine Learning Model Training, Neural Network Development and etc
        Annotators:
            We need couple of Human Resources to annotate and label datas for large amount of datas we will have (about 1M hours of audio data)
            (we can use automation for *Some* Datas but not for all accents and languages used in iran and to have high quality datas)
        Voice Actors:
            we need Couple of Voice Actors for Recording Their Voices in Studios and use their voices for Speeches.
""" 