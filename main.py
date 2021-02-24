import speech_recognition as SRG 
import time
import pyttsx3
from difflib import SequenceMatcher
from expertai.nlapi.cloud.client import ExpertAiClient
import os
import sys
os.environ["EAI_USERNAME"] = #Your Expert.AI Email
os.environ["EAI_PASSWORD"] = #Your Expert.AI Password

client  = ExpertAiClient()
language= 'en'

engine = pyttsx3.init()
store = SRG.Recognizer()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[2].id)


def findsim(a_list,b):
    mx=0
    op=""
    for i in a_list:
        score=SequenceMatcher(None, i, b).ratio()
        if(score>mx):
            mx=score
            op=i
    return op


is_continue=True
is_exit=True
task_list=["parts of speech","name entities","key elements", "sentiment", "classify text"]
pos_list=["noun","verb","adjectives","pronouns"]
decision_list=["continue", "start over","exit"]
entity_values = {
    "ADR": "Street address","ANM": "Animals","BLD": "Building","COM": "Businesses / companies","DAT": "Date","DEV": "Device","DOC": "RequestDocument","EVN": "Event","FDD": "Food/beverage","GEA": "Physical geographic features","GEO": "Administrative geographic areas","GEX": "Extended geography","HOU": "Hours","LEN": "Legal entities","MAI": "Email address","MEA": "Measure","MMD": "Mass media","MON": "Money","NPH": "Humans","ORG": "Organizations","PCT": "Percentage","PHO": "Phone number","PPH": "Physical phenomena","PRD": "Product","VCL": "Vehicle","WEB": "Web address","WRK": "Work of human intelligence","NPR": "Proper noun",
}

while is_exit:
    is_continue=True
    with SRG.Microphone() as s:
        engine.setProperty('rate', 100)
        engine.say("Hello Please Say Something")
        engine.runAndWait()
        audio_input = store.record(s, duration=10)
        print("Done Reading")
        
        try:
            print("Done")
            text_output = store.recognize_google(audio_input)
            engine.setProperty('rate', 100)
            print("Done Reading",text_output)
            while is_continue:
                
                engine.say("What Do You What To do,  Parts Of Speech , Find Name Entities, Find Key Elements, Find Sentiment  or Classify The Text")
                engine.runAndWait()
                with SRG.Microphone() as s:
                    task_input = store.record(s, duration=5)
                    print("Starting Reading")
                    try:
                        task_output = store.recognize_google(task_input)
                        task=findsim(task_list,task_output)
                        print(task,task_output,text_output)
                        if(task=="parts of speech"):
                            text = text_output 
                            language= 'en'
                            document = client.specific_resource_analysis(
                                body={"document": {"text": text}}, 
                                params={'language': language, 'resource': 'disambiguation'
                            })
                            print (f'{"TOKEN":{20}} {"LEMMA":{8}}')

                            engine.say("In Parts of Speech what do you want to find , noun, verb , pronoun or adjectives")
                            engine.runAndWait()
                            with SRG.Microphone() as s:
                                pos_input = store.record(s, duration=5)
                                print("Starting Reading POS")
                                try:
                                    pos_output = store.recognize_google(pos_input)
                                    op_pos_output=findsim(pos_list,pos_output)
                                    print(op_pos_output,pos_output)
                                    if(op_pos_output=="noun"):
                                        engine.say("The Nouns Are ")
                                        engine.runAndWait()
                                        for token in document.tokens:
                                            if(token.pos=="NOUN"):
                                                engine.say(text[token.start:token.end])
                                                engine.runAndWait()
                                    elif(op_pos_output=="verb"):
                                        engine.say("The Verbs Are ")
                                        engine.runAndWait()
                                        for token in document.tokens:
                                            if(token.pos=="VERB"):
                                                engine.say(text[token.start:token.end])
                                                engine.runAndWait()
                                    elif(op_pos_output=="adjectives"):
                                        engine.say("The Adjectives Are ")
                                        engine.runAndWait()
                                        for token in document.tokens:
                                            if(token.pos=="ADJ"):
                                                engine.say(text[token.start:token.end])
                                                engine.runAndWait()
                                    elif(op_pos_output=="pronouns"):
                                        engine.say("The Pronouns Are ")
                                        engine.runAndWait()
                                        for token in document.tokens:
                                            if(token.pos=="PRON"):
                                                engine.say(text[token.start:token.end])
                                                engine.runAndWait()
                                    
                                except:
                                    print("Couldn't process the audio input.")
                        elif(task=="name entities"):
                            document = client.specific_resource_analysis(
                                    body={"document": {"text": text_output}}, 
                                    params={'language': language, 'resource': 'entities'})
                            print (f'{"ENTITY":{40}} {"TYPE":{10}}')
                            engine.say("Name Entities are as Follows: ")
                            engine.runAndWait()
                            for entity in document.entities:
                                entity_speech=entity.lemma+" has Entity : "+entity_values[entity.type_]
                                engine.say(entity_speech)
                                engine.runAndWait()
                                print (f'{entity.lemma:{40}} {entity.type_:{10}}')

                        elif(task=="key elements"):
                            document = client.specific_resource_analysis(
                                    body={"document": {"text": text_output}}, 
                                    params={'language': language, 'resource': 'relevants'})
                            print (f'{"LEMMA":{20}} {"SCORE":{5}} ')
                            engine.say("Key Elements are : ")
                            engine.runAndWait()
                            for mainlemma in document.main_lemmas:
                                engine.say(mainlemma.value)
                                engine.runAndWait()
                                print (f'{mainlemma.value:{20}} {mainlemma.score:{5}}')

                        elif(task=="sentiment"):
                            document = client.specific_resource_analysis(
                                    body={"document": {"text": text_output}}, 
                                    params={'language': language, 'resource': 'sentiment'})
                            print("sentiment:", document.sentiment.overall)
                            engine.say("Sentiment of Text is "+ str(document.sentiment.overall) + " Percentage")
                            engine.runAndWait()

                        else:
                            taxonomy='iptc'
                            document = client.classification(body={"document": {"text": text_output}}, params={'taxonomy': taxonomy,'language': language})
                            categories = []
                            scores = []
                            engine.say("Main Categories are ")
                            engine.runAndWait()
                            for category in document.categories:
                                engine.say(category.label)
                                engine.runAndWait()
                                print (f'{category.label:{27}} {category.id_:{10}}{category.frequency:{8}}')
                    except:
                        print("Couldn't process the audio input.")
                
                engine.say("What Do You What To do,Continue , Start Over , Exit")
                engine.runAndWait()
                with SRG.Microphone() as s:
                    decision_input = store.record(s, duration=5)
                    print("Starting Reading")
                    
                    decision_output = store.recognize_google(decision_input)
                    print("OP Decision",decision_output)
                    op_decision_output=findsim(decision_list,decision_output)
                    print(op_decision_output,decision_output)
                    if(op_decision_output=="start over"):
                        is_continue=False
                    elif(op_decision_output=="exit"):
                        engine.say("Thank You For Using GrammoXpert, Please Visit Again")
                        engine.runAndWait()
                        is_exit=False
                        is_continue=False
                        sys.exit()
            print("Taken Input")
        except:
            print("Couldn't process the audio input.")
