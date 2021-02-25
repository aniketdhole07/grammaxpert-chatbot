# GrammaXpert Chatbot
A Chatbot to Help you with Grammar Skills like Parts of Speech, Name Entities, Classification, Relations and Sentiment.

[![Click To Watch Video](https://img.youtube.com/vi/t3mKEEAZkWw/0.jpg)](https://www.youtube.com/watch?v=t3mKEEAZkWw)

## To Run Execute the Below Commands:

1. Download the code
 ```
 git clone https://github.com/aniketdhole07/grammaxpert-chatbot
 ```
2. Change to Code Directory:
```
cd grammaxpert-chatbot
```
3. Download Dependencies
```
sudo apt-get install python3-pyaudio portaudio19-dev  espeak libespeak1 alsa-utils
```
4. Install Python Packages 
```
pip3 install -r requirements.txt
```
5. Modify the API Authentication in `main.py` by your Email ID and Password of Expert.ai Account
```
os.environ["EAI_USERNAME"] = 'YOUR_EMAIL'
os.environ["EAI_PASSWORD"] = 'YOUR_PASSWORD'
```
6. Run the Program:
```
python3 main.py
```

My Environment Settings:
* Python : Python 3.8.5 (default, Aug  2 2020, 15:09:07) 
* Operating System: Kali GNU/Linux Rolling 2019.1


## Inspiration
In todays advanced world, the need of independent living is recognized in case of visually impaired students who are facing main problem of social restrictiveness. Due to lack of necessary information in the surrounding environment visually impaired people face problems and are at disadvantage since visual information is what they lack the most. With the help of my project, the visually impaired can be supported. The idea is implemented on voice assistant which is capable to assist using voice command to learn Grammar topics like Parts of Speech, Name Entities, Classification and many more. It may be the effective way blind people will learn new things.

## What it does
It takes Voice Input from User and Asks him which Operation to apply on his spoken text ,that data is analyzed using [Expert.AI's  Natural Language Processing API](https://www.expert.ai/) , which is platform to add language intelligence to our applications.
The Process works like this:
1. Initially the User is asked for Input Sentence using Speech
2. The Speech to text Algorithm converts it into text.
3. Then the user is asked to choose between Grammar Operations like Parts of Speech, Name Entities,etc.
4. The Input is converted into Text and Checked using Similarity Algorithm if it is valid operation.
5. That Operation is made active and API is called using Input Text taken initially
6. The Output of API is formatted and Converted to Speech.
7. Then Finally user is asked to Choose to Continue, Start over or Exit and this process continues.

## How we built it
This Block Diagram of Project

<a href="https://ibb.co/b7KY4T8"><img src="https://i.ibb.co/CWH4jgT/exp.png" alt="exp" border="0"></a>

#### expert.ai API:
The API is called using [Expert.ai 's Python Client](https://github.com/therealexpertai/nlapi-python). I followed the Authentication steps Documentation and it worked well. The instructions are well maintained by expert.ai community.

#### Text To Speech:
For this I have used Python's package called [pyttsx3](https://pypi.org/project/pyttsx3/) .It works according to code flow and user input.

#### Speech to Text:
I have used the python package[Speech_Recognition](https://pypi.org/project/SpeechRecognition/) ,and connected it with my laptop's Microphone. It works very well than any other STT API and is much fast.

#### Text Similarity:
As User's Speech input may not match the required operations perfectly so I have used a Text Similarity Algorithm named
add code

