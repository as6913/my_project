"""from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
from flask import jsonify
from flask import Flask, render_template, request, redirect, session,flash
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

client = MongoClient()
db = client["mvt"]
coll = db["user"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = coll.find_one({'username': username, 'password': password})
        if user:
            session['username'] = username
            return redirect('/profile')
        else:
            return 'Invalid username or password. Please try again.'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mailid = request.form['email']
        phno = request.form['phone']
        user = coll.find_one({'username': username})
        if user:
            return 'Username already exists. Please choose a different one.'
        else:
            coll.insert_one({'username': username, 'password': password, 'mailid': mailid, 'phno': phno})
            session['username'] = username
            flash('Registration successful. Welcome!', 'success')
            return redirect('/login')
    return render_template('register.html')

from flask import render_template

@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        user = coll.find_one({'username': username})
        return render_template('profile.html', username=username, user=user)
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect('/login')

    
@app.route('/translate', methods=['POST'])
def translate_text():
    dic = {'afrikaans': 'af', 'albanian': 'sq',
       'amharic': 'am', 'arabic': 'ar',
       'armenian': 'hy', 'azerbaijani': 'az',
       'basque': 'eu', 'belarusian': 'be',
       'bengali': 'bn', 'bosnian': 'bs', 'bulgarian':
       'bg', 'catalan': 'ca', 'cebuano':
       'ceb', 'chichewa': 'ny', 'chinese (simplified)':
       'zh-cn', 'chinese (traditional)':
       'zh-tw', 'corsican': 'co', 'croatian': 'hr',
       'czech': 'cs', 'danish': 'da', 'dutch':
       'nl', 'english': 'en', 'esperanto': 'eo',
       'estonian': 'et', 'filipino': 'tl', 'finnish':
       'fi', 'french': 'fr', 'frisian': 'fy', 'galician':
       'gl', 'georgian': 'ka', 'german':
       'de', 'greek': 'el', 'gujarati': 'gu',
       'haitian creole': 'ht', 'hausa': 'ha',
       'hawaiian': 'haw', 'hebrew': 'he', 'hindi':
       'hi', 'hmong': 'hmn', 'hungarian':
       'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian':
       'id', 'irish': 'ga', 'italian':
       'it', 'japanese': 'ja', 'javanese': 'jw',
       'kannada': 'kn', 'kazakh': 'kk', 'khmer':
       'km', 'korean': 'ko', 'kurdish (kurmanji)':
       'ku', 'kyrgyz': 'ky', 'lao': 'lo',
       'latin': 'la', 'latvian': 'lv', 'lithuanian':
       'lt', 'luxembourgish': 'lb',
       'macedonian': 'mk', 'malagasy': 'mg', 'malay':
       'ms', 'malayalam': 'ml', 'maltese':
       'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian':
       'mn', 'myanmar (burmese)': 'my',
       'nepali': 'ne', 'norwegian': 'no', 'odia': 'or',
       'pashto': 'ps', 'persian': 'fa',
       'polish': 'pl', 'portuguese': 'pt', 'punjabi':
       'pa', 'romanian': 'ro', 'russian':
       'ru', 'samoan': 'sm', 'scots gaelic': 'gd',
       'serbian': 'sr', 'sesotho': 'st',
       'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si',
       'slovak': 'sk', 'slovenian': 'sl',
       'somali': 'so', 'spanish': 'es', 'sundanese':
       'su', 'swahili': 'sw', 'swedish':
       'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu':
       'te', 'thai': 'th', 'turkish':
       'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur':
       'ug', 'uzbek': 'uz',
       'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh',
       'yiddish': 'yi', 'yoruba':
       'yo', 'zulu': 'zu'}
    # Retrieve the spoken text from the POST request
    flash("listening")
    spoken_text = request.form.get('spoken_text')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"The User said {query}\n")
    except Exception as e:
        print("say that again please.....")
        return "None"
    

    # Add your speech recognition and translation logic here
    # For simplicity, I'm returning a static translated text
    translated_text = f"The User said {query}"

    # Return the translated text as JSON
    return jsonify({'translated_text': translated_text})
    

if __name__ == '__main__':
    app.run(debug=True)"""
    
from flask import Flask, jsonify, render_template, request, redirect, session
from pymongo import MongoClient
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

app = Flask(__name__)
app.secret_key = 'b_5#y2L"F4Q8z\n\xec]/'
dic = {'afrikaans': 'af', 'albanian': 'sq',
       'amharic': 'am', 'arabic': 'ar',
       'armenian': 'hy', 'azerbaijani': 'az',
       'basque': 'eu', 'belarusian': 'be',
       'bengali': 'bn', 'bosnian': 'bs', 'bulgarian':
       'bg', 'catalan': 'ca', 'cebuano':
       'ceb', 'chichewa': 'ny', 'chinese (simplified)':
       'zh-cn', 'chinese (traditional)':
       'zh-tw', 'corsican': 'co', 'croatian': 'hr',
       'czech': 'cs', 'danish': 'da', 'dutch':
       'nl', 'english': 'en', 'esperanto': 'eo',
       'estonian': 'et', 'filipino': 'tl', 'finnish':
       'fi', 'french': 'fr', 'frisian': 'fy', 'galician':
       'gl', 'georgian': 'ka', 'german':
       'de', 'greek': 'el', 'gujarati': 'gu',
       'haitian creole': 'ht', 'hausa': 'ha',
       'hawaiian': 'haw', 'hebrew': 'he', 'hindi':
       'hi', 'hmong': 'hmn', 'hungarian':
       'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian':
       'id', 'irish': 'ga', 'italian':
       'it', 'japanese': 'ja', 'javanese': 'jw',
       'kannada': 'kn', 'kazakh': 'kk', 'khmer':
       'km', 'korean': 'ko', 'kurdish (kurmanji)':
       'ku', 'kyrgyz': 'ky', 'lao': 'lo',
       'latin': 'la', 'latvian': 'lv', 'lithuanian':
       'lt', 'luxembourgish': 'lb',
       'macedonian': 'mk', 'malagasy': 'mg', 'malay':
       'ms', 'malayalam': 'ml', 'maltese':
       'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian':
       'mn', 'myanmar (burmese)': 'my',
       'nepali': 'ne', 'norwegian': 'no', 'odia': 'or',
       'pashto': 'ps', 'persian': 'fa',
       'polish': 'pl', 'portuguese': 'pt', 'punjabi':
       'pa', 'romanian': 'ro', 'russian':
       'ru', 'samoan': 'sm', 'scots gaelic': 'gd',
       'serbian': 'sr', 'sesotho': 'st',
       'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si',
       'slovak': 'sk', 'slovenian': 'sl',
       'somali': 'so', 'spanish': 'es', 'sundanese':
       'su', 'swahili': 'sw', 'swedish':
       'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu':
       'te', 'thai': 'th', 'turkish':
       'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur':
       'ug', 'uzbek': 'uz',
       'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh',
       'yiddish': 'yi', 'yoruba':
       'yo', 'zulu': 'zu'}


client = MongoClient()
db = client["mvt"]
coll = db["user"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = coll.find_one({'username': username, 'password': password})
        if user:
            session['username'] = username
            return redirect('/profile')
        else:
            return 'Invalid username or password. Please try again.'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mailid = request.form['email']
        phno = request.form['phone']
        user = coll.find_one({'username': username})
        if user:
            return 'Username already exists. Please choose a different one.'
        else:
            coll.insert_one({'username': username, 'password': password, 'mailid': mailid, 'phno': phno})
            session['username'] = username
            return redirect('/profile')
    return render_template('register.html')

from flask import render_template

@app.route('/profile', methods=['GET'])
def profile():
    if 'username' in session:
        username = session['username']
        user = coll.find_one({'username': username})
        return render_template('profile.html', username=username, user=user)
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')


@app.route('/translate_voice', methods=['GET'])
def translate_voice():
    def destination_language():
        print("Enter the language in which you want to convert: Ex. Hindi, English, etc.")
        print()

        while True:
            to_lang = input("Enter destination language: ").strip().lower()
            if to_lang in dic:
                return to_lang
            else:
                print("Language not supported. Please enter a valid language.")

    try:
        spoken_text = request.args.get('language')
        to_lang = request.args.get('to_lang')
        print(to_lang)
        destination_language(to_lang)

        translator = Translator()
        text_to_translate = translator.translate(spoken_text, dest=to_lang)
        translated_text = text_to_translate.text
        print(translated_text)

        speak = gTTS(text=translated_text, lang=to_lang, slow=False)
        speak.save("static/captured_voice.mp3")
        print(speak)

        return jsonify({"status": "success", "audio_url": "/static/captured_voice.mp3"})
    except Exception as e:
        print(e)
        return jsonify({"status": "error"}), 500



if __name__ == '__main__':
    app.run(debug=True)
