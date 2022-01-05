#!/usr/env python3
# -*- encode: utf-8 -*-

# IMPORT MODULES
    # Ghoib
from math import e
#from re import S, split
from subprocess import ABOVE_NORMAL_PRIORITY_CLASS
from urllib.parse import _ResultMixinBytes
#from wikipedia.wikipedia import search
    # Manual
try:
    print("\n[*] Importing modules ...")
    import datetime, time, os, sys, platform, random, re, subprocess, ctypes, shutil
    import speech_recognition as sr
    import pyttsx3, webbrowser, wikipedia, requests, googletrans
    from telegram.ext import Updater, CommandHandler
    print("[+] Successfully importing modules!")
except ImportError:
    "[!] Failed to import one or more modules, please make sure you've installed the required modules!"
    exit()

# VARIABLE GLOBAL
sistem_operasi = platform.system()
kecepatan_bicara = 210
durasi_input = 4
youtube_loc = '"C:\\Program Files\\Chromium\\chrome_proxy.exe"  --app-id=agimnkijcaahngcdmfeangaknmldooml'
whatsapp_loc = "C:\\Users\\Human\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
telegram_loc = "C:\\Users\\Human\\SomeApps\\Telegram Desktop\\Telegram.exe"
photoshop_loc = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
illustrator_loc = "C:\\Program Files\\Adobe\\Adobe Illustrator 2021\\Support Files\\Contents\\Windows\\illustrator.exe"
word_loc = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
excel_loc = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
powerpoint_loc = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
notepad_loc = "C:\\Windows\\System32\\notepad.exe"
sublimetext_loc = "C:\\Program Files\\Sublime Text\\sublime_text.exe"
vscode_loc = "C:\\Users\\Human\\SomeApps\\Microsoft VS Code\\Code.exe"
firefox_loc = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
chrome_loc = '"C:\\Program Files\\Chromium\\chrome.exe"'
vmware_loc = "C:\\Program Files\\VMware\\VMware Workstation\\vmware.exe"
vm_loc = 'D:\\VIRTUAL MACHINE\\VW\\Kali Linux x64 by Offensive Security\\kali-linux-2021.1-vmware-amd64.vmx'
music_playlist = "Your Playlist Here"

# PERSIAPAN PROGRAM
try:
    # Inisialisasi
    print("[*] Initializing PyTTSx3 library ...")
    speak_engine = pyttsx3.init('sapi5')
    # Seleksi Suara
    print("[*] Using voices number 2")
    voices_list = speak_engine.getProperty("voices")
    speak_engine.setProperty("voices", voices_list[1])
    # Mengatur Kecepatan Suara
    speak_engine.setProperty("rate", kecepatan_bicara)
    # Recognizer Suara
    recognizer = sr.Recognizer()
    '''recognizer.energy_threshold = 300'''
    # List Microphone
    list_mic = sr.Microphone()
    '''print("\n[+] All available microphone on this devices :")
    counter = 0
    for nama_mic in mic_list:
        print(f" |--[{counter}] {nama_mic}")
        counter += 1
    mic_index = int(input("[?] Choose your input device > "))'''
except:
    print("[!] Error when initializing PyTTSx3 library, quitting ...")
    exit()

# FUNGSI OPERASI
def openBrowser(url):
    webbrowser.open(url, new=1)

# FUNGSI WIKIPEDIA
def searchWikipedia(phrase, sentence_num):
    search_result = wikipedia.summary(phrase, sentences=sentence_num)
    print("[Leffy]\t" + search_result)
    doSpeak(search_result)
    #openBrowser("https://wikipedia.org/wiki/{0}".format(phrase))

# FUNGSI TRANSLATE
def translatePhrase(phrase, src='unknown', dst='en'):
    print()

# FUNGSI BICARA
def doSpeak(text):
    speak_engine.say(text)
    speak_engine.runAndWait()

# FUNGSI EKSEKUSI KALIMAT
def doCommand(text):
    text = text.lower()
    splitted_text = text.split(" ")
    ############## WAKTU ##############
    if splitted_text[:2] == ['what','time'] or text == "what time is it" or text == "what time it is" or text == "tell me the time":
        print("[Rizky]\t" + text)
        time_now = datetime.datetime.now()
        time_h = time_now.hour
        time_m = time_now.minute
        if time_h >= 0 and time_h <= 12:
            am_pm = "AM"
        else:
            am_pm = "PM"
        print("[Leffy]\tRight now is {0} and {1} {2} sir!\n".format(time_h, time_m, am_pm))
        doSpeak("Right now is {0} and {1} {2} sir!".format(time_h, time_m, am_pm))
    elif splitted_text[:2] == ['what','day'] or text == "what day is it" or text == "what day it is" or text == "today is":
        print("[Rizky]\t" + text)
        time_now = datetime.datetime.now()
        day_name = time_now.strftime("%A")
        print("[Leffy]\tToday is {0} sir!\n".format(day_name))
        doSpeak("Today is {0} sir!".format(day_name))
    ############## SEARCHING/INFO ##############
    # WikiPedia
    elif splitted_text[:2] == ['what', 'is'] and len(splitted_text) > 2:
        print("[Rizky]\t" + text)
        keyword_raw = text.split("what is")
        if keyword_raw[-1][0] == " ":
            keyword = keyword_raw[-1][1::]
        else:
            keyword = keyword_raw[-1]
        try:
            searchWikipedia(keyword, 3)
        except wikipedia.exceptions.PageError:
            pass
        except wikipedia.exceptions.DisambiguationError:
            pass
        print("\n")
    # Searching Custom Platform
    elif splitted_text[0] == "search" and "on" in text and len(splitted_text) > 3:
        print("[Rizky]\t" + text)
        keyword_raw = re.split("search|on",text)
        if keyword_raw[1][0] == " ":
            keyword = keyword_raw[1][1::]
        else:
            keyword = keyword_raw[1]
        if keyword_raw[2][0] == " ":
            search_engine = keyword_raw[2][1::]
        else:
            search_engine = keyword_raw[2]
        if search_engine == "google":
            print("[Leffy]\tSearching '{0}' on Google\n".format(keyword))
            openBrowser("https://www.google.com/search?q={0}".format(keyword))
        elif search_engine == "bing":
            print("[Leffy]\tSearching '{0}' on Bing\n".format(keyword))
            openBrowser("https://www.bing.com/search?q={0}".format(keyword))
        elif search_engine == "duckduckgo" or search_engine == "duck duck go" or search_engine == "duckduck go":
            print("[Leffy]\tSearching '{0}' on DuckDuckGo\n".format(keyword))
            openBrowser("https://duckduckgo.com/?q={0}".format(keyword))
        elif search_engine == "youtube":
            print("[Leffy]\tSearching '{0}' on YouTube\n".format(keyword))
            openBrowser("https://www.youtube.com/results?search_query={0}".format(keyword))
        elif search_engine == "stackoverflow" or search_engine == "stack over flow" or search_engine == "stack overflow":
            print("[Leffy]\tSearching '{0}' on StackOverflow\n".format(keyword))
            openBrowser("https://stackoverflow.com/search?q={0}".format(keyword))
        elif search_engine == "wikipedia" or search_engine == "wiki pedia":
            print("[Leffy]\tSearching '{0}' on WikiPedia\n".format(keyword))
            openBrowser("https://wikipedia.org/wiki/{0}".format(keyword))
        else:
            print("[Leffy]\tSearching '{0}' on {1}\n".format(keyword, search_engine))
            openBrowser("https://www.google.com/search?q={0}".format(keyword))
            #print("[Leffy]\t" + search_engine + " is not available as search engine")
            #doSpeak(search_engine + " is not available as search engine")
    # Searching Google
    elif splitted_text[0] == "search" and len(splitted_text) > 1:
        print("[Rizky]\t" + text)
        keyword_raw = text.split("search")
        if keyword_raw[-1][0] == " ":
            keyword = keyword_raw[-1][1::]
        else:
            keyword = keyword_raw[-1]
        print("[Leffy]\tSearching {0} on Google\n".format(keyword))
        doSpeak("Searching {0} on Google\n".format(keyword))
        openBrowser("https://www.google.com/search?q={0}".format(keyword))
    # Cari Lokasi di Google Maps
    elif splitted_text[:2] == ['where','is'] and len(splitted_text) > 2:
        print("[Rizky]\t" + text)
        keyword_raw = text.split("where is")
        if keyword_raw[-1][0] == " ":
            keyword = keyword_raw[-1][1::]
        else:
            keyword = keyword_raw[1]
        print("[Leffy]\tLooking for {0} on Google Maps\n".format(keyword))
        doSpeak("Looking for {0} on Google Maps\n".format(keyword))
        openBrowser("https://www.google.com/maps/place/{0}/".format(keyword))
    ############## BUKA/TUTUP APLIKASI ##############
    # Buka YouTube
    elif text == "open youtube":
        print("[Rizky]\t" + text)
        print("[Leffy]\tOpening YouTube\n")
        #openBrowser("https://www.youtube.com")
        doSpeak("Okay, opening YouTube")
        subprocess.Popen(youtube_loc)
    # Buka/Tutup WhatsApp
    elif (text == "open whatsapp" or text == "open whats up") and (whatsapp_loc != ''):
        print("[Rizky]\t" + text)
        print("[Leffy]\tOpening WhatsApp\n")
        doSpeak("Okay, opening WhatsApp")
        subprocess.Popen(whatsapp_loc)
    elif text == "close whatsapp" or text == "close whats up":
        print("[Rizky]\t" + text)
        print("[Leffy]\tClosing WhatsApp and it's child process\n")
        doSpeak("Closing WhatsApp and it's child process")
        subprocess.Popen("taskkill /IM whatsapp.exe /T")
    # Buka/Tutup Telegram
    elif (text == "open telegram" or text == "open tele gram") and (telegram_loc != ''):
        print("[Rizky]\t" + text)
        print("[Leffy]\tOpening Telegram\n")
        doSpeak("Okay, opening Telegram")
        subprocess.Popen(telegram_loc)
    elif text == "close telegram" or text == "close tele gram":
        print("[Rizky]\t" + text)
        print("[Leffy]\tClosing Telegram and it's child process\n")
        doSpeak("Closing Telegram and it's child process")
        subprocess.Popen("taskkill /IM telegram.exe /T")
    # Buka/Tutup Adobe Photoshop
    elif (text == "open adobe photoshop" or text == "open photoshop" or text == "open photo shop") and (photoshop_loc != ''):
        print("[Rizky]\t" + text)
        print("[Leffy]\tOpening Adobe Photoshop\n")
        doSpeak("Okay, opening Adobe Photoshop")
        subprocess.Popen(photoshop_loc)
    elif text == "close adobe photoshop" or text == "close photoshop" or text == "close photo shop":
        print("[Rizky]\t" + text)
        print("[Leffy]\tClosing Adobe Photoshop and it's child process\n")
        doSpeak("Closing Photoshop and it's child process")
        subprocess.Popen("taskkill /IM photoshop.exe /T")
    # Buka Adobe Illustrator
    elif (text == "open adobe illustrator" or text == "open illustrator") and (illustrator_loc != ''):
        print("[Rizky]\t" + text)
        print("[Leffy]\tOpening Adobe Illustrator\n")
        doSpeak("Okay, opening Adobe Illustrator")
        subprocess.Popen(illustrator_loc)
    elif text == "close adobe illustrator" or text == "close illustrator":
        print("[Rizky]\t" + text)
        print("[Leffy]\tClosing Adobe Illustrator and it's child process\n")
        doSpeak("Closing Illustrator and it's child process")
        subprocess.Popen("taskkill /IM illustrator.exe /T")
    # Buka/Tutup Office Word
    elif (text == "open office word" or text == "open word" or text == "open war") and (word_loc != ''):
        print("[Rizky]\t" + text)
        print("[Leffy]\tOpening Microsoft Office Word\n")
        doSpeak("Okay, opening Office Word")
        subprocess.Popen(word_loc)
    elif text == "close office word" or text == "close word" or text == "close war":
        print("[Rizky]\t" + text)
        print("[Leffy]\tClosing Microsoft Office Word and it's child process\n")
        doSpeak("Closing Office Word and it's child process")
        subprocess.Popen("taskkill /IM winword.exe /T")
    # Buka/Tutup Office Excel
    elif (text == "open office excel" or text == "open excel" or text == "axel" or text == "axle") and (excel_loc != ''):
        print("[Rizky]\t" + text)
        print("[Leffy]\tOpening Microsoft Office Excel\n")
        doSpeak("Okay, opening Office Excel")
        subprocess.Popen(excel_loc)
    elif text == "close office excel" or text == "close excel" or text == "close axel" or text == "close axle":
        print("[Rizky]\t" + text)
        print("[Leffy]\tClosing Microsoft Office Excel and it's child process\n")
        doSpeak("Closing Office Excel and it's child process")
        subprocess.Popen("taskkill /IM excel.exe /T")
    # Buka/Tutup Office PowerPoint
    elif (text == "open office powerpoint" or text == "open powerpoint" or text == "open power point") and (powerpoint_loc != ''):
        print("[Rizky]\t" + text)
        print("[Leffy]\tOpening Microsoft Office PowerPoint\n")
        doSpeak("Okay, opening Office PowerPoint")
        subprocess.Popen(powerpoint_loc)
    elif text == "close office powerpoint" or text == "close powerpoint" or text == "close power point":
        print("[Rizky]\t" + text)
        print("[Leffy]\tClosing Microsoft Office PowerPoint and it's child process\n")
        doSpeak("Closing Office PowerPoint and it's child process")
        subprocess.Popen("taskkill /IM powerpnt.exe /T")
    # Buka/Tutup Notepad
    elif (text == "open notepad" or text == "open notpad" or text == "open note pad") and (notepad_loc != ''):
        print("[Rizky]\t" + text)
        print("[Leffy]\tOpening Notepad\n")
        doSpeak("Okay, opening Notepad")
        subprocess.Popen(notepad_loc)
    elif text == "close notepad" or text == "close notpad" or text == "close note pad":
        print("[Rizky]\t" + text)
        print("[Leffy]\tClosing Notepad and it's child process\n")
        doSpeak("Closing Notepad and it's child process")
        subprocess.Popen("taskkill /IM notepad.exe /T")
    # Buka/Tutup Sublime Text
    elif (text == "open sublime" or text == "open sub lime") and (sublimetext_loc != ''):
        print("[Rizky]\t" + text)
        print("[Leffy]\tOpening Sublime Text\n")
        doSpeak("Okay, opening Sublime Text")
        subprocess.Popen(sublimetext_loc)
    elif text == "close sublime" or text == "close sub lime":
        print("[Rizky]\t" + text)
        print("[Leffy]\tClosing Sublime Text and it's child process\n")
        doSpeak("Closing Sublime Text and it's child process")
        subprocess.Popen("taskkill /IM sublime_text.exe /T")
    # Buka/Tutup Visual Studio Code
    elif (text == "open vscode" or text == "open vs code" or text == "open studio code") and (vscode_loc != ''):
        print("[Rizky]\t" + text)
        print("[Leffy]\tOpening Visual Studio Code\n")
        doSpeak("Okay, opening Visual Studio Code")
        subprocess.Popen(vscode_loc)
    elif text == "close vscode" or text == "close vs code" or text == "close studio code":
        print("[Rizky]\t" + text)
        print("[Leffy]\tClosing Visual Studio Code and it's child process\n")
        doSpeak("Closing Visual Studio Code and it's child process")
        subprocess.Popen("taskkill /IM code.exe /T")
    # Buka/Tutup Firefox
    elif (text == "open firefox" or text == "open fire fox") and (firefox_loc != ''):
        print("[Rizky]\t" + text)
        print("[Leffy]\tOpening Mozilla Firefox\n")
        doSpeak("Okay, opening Mozilla Firefox")
        subprocess.Popen(firefox_loc)
    elif text == "close firefox" or text == "close fire fox":
        print("[Rizky]\t" + text)
        print("[Leffy]\tClosing Mozilla Firefox and it's child process\n")
        doSpeak("Closing Mozilla Firefox and it's child process")
        subprocess.Popen("taskkill /IM firefox.exe /T")
    # Buka/Tutup Chromium
    elif (text == "open chromium" or text == "open chrome" or text == "open google chrome") and (chrome_loc != ''):
        print("[Rizky]\t" + text)
        print("[Leffy]\tOpening Chromium\n")
        doSpeak("Okay, opening Chromium")
        subprocess.Popen(chrome_loc)
    elif text == "close chromium" or text == "close chrome" or text == "close google chrome":
        print("[Rizky]\t" + text)
        print("[Leffy]\tClosing Chromium and it's child process\n")
        doSpeak("Closing Chromium and it's child process")
        subprocess.Popen("taskkill /IM chrome.exe /T")
    ############## UTILITY ##############
    # Buka VMware Kali Linux
    elif (text == "pentesting mode" or text == "pentesting space" or text == "mr. robot" or text == "fsociety") and (vmware_loc != '' and sublimetext_loc != '' and telegram_loc != ''):
        print("[Rizky]\t" + text)
        print("[Leffy]\tOpening Kali Linux virtual machine and other Pentesting tools\n")
        doSpeak("Entering the hacking space, opening Kali Linux virtual machine and other Pentesting tools")
        subprocess.Popen(f'"{vmware_loc}" -X "{vm_loc}"')
        subprocess.Popen('{0} 0day-note'.format(sublimetext_loc))
        subprocess.Popen('"C:\\Tools\\Cmder\\Cmder.exe" /start "D:\\CYBER SECURITY" /icon "D:\\EDITING-DESIGNING\\PERSONAL\\Logo PentaByte\\Logo-2.ico"')
        subprocess.Popen(telegram_loc)
        #subprocess.Popen('"C:\\Program Files\\Mozilla Firefox\\firefox.exe"')
    # Matikan/Hidupkan Windows Update
    elif text == "stop windows update" or text == "cancel windows update":
        print("[Rizky]\t" + text)
        print("[Leffy]\tStopping Windows Update service\n")
        doSpeak("Stopping Windows Update service")
        os.system('net stop wuauserv')
        os.system('net stop bits')
        os.system('net stop dosvc')
    elif text == "start windows update" or text == "run windows update" or text == "continue windows update":
        print("[Rizky]\t" + text)
        print("[Leffy]\tStarting Windows Update service\n")
        doSpeak("Starting Windows Update service")
        os.system('net start wuauserv')
        os.system('net start bits')
        os.system('net start dosvc')
    # Bersihkan Sampah Temporary
    elif text == "start clean maid" or text == "start clean utility" or text == "start clean protocol":
        print("[Rizky]\t" + text)
        print("[Leffy]\tCleaning trash on temporary files folder\n")
        doSpeak("Cleaning trash on temporary files folder")
        #os.system('del %temp%\*.* /S /Q >nul')
        os.system('cleanmgr /sagerun:1337') # Using sageset preset 1337
    ############## RANDOM THINGS ##############
    # Mainkan Playlist di YouTube
    elif text == "play music" or text == "open music" or "put some music" in text:
        print("[Rizky]\t" + text)
        print("[Leffy]\tPlaying music playlist on YouTube\n")
        doSpeak("Playing music playlist on YouTube")
        openBrowser(music_playlist)
    # Who Are You
    elif text == "who are you" or text == "what are you" or text == "program info":
        print("[Rizky]\t" + text)
        print("[Leffy]\tHi! My name is Leffy. I'm a voice assistant coded by Muhammad Rizky for managing simple daily task\n")
        doSpeak("Hi! My name is Leffy. I'm a voice assistant coded by Muhammad Rizky for managing simple daily task")
    # Thank You
    elif text == "thanks" or text == "thank you" or text == "okay thank you":
        print("[Rizky]\t" + text)
        randnum = random.randint(1,4)
        if randnum in [1,3]:
            print("[Leffy]\tMy pleasure sir\n")
            doSpeak("My pleasure sir")
        else:
            print("[Leffy]\tYour welcome sir\n")
            doSpeak("Your welcome sir")
    # Hi
    elif text == "hi" or text == "hey" or text == "hai" or text == "hello" or text == "can you hear me":
        print("[Rizky]\t" + text)
        randnum = random.randint(1,3)
        if randnum == 1:
            print("[Leffy]\tYes sir?\n")
            doSpeak("Yes sir?") 
        elif randnum == 2:
            print("[Leffy]\tI'm here sir!\n")
            doSpeak("I'm here sir!")
        elif randnum == 3:
            print("[Leffy]\tI'm listening sir\n")
            doSpeak("I'm listening sir")    
    # Unrecognized
    else:
        print("[Rizky]\t" + text)
        #doSpeak("You said" + text)

def doListen():
    mode = "standby"
    loop = 0
    print("[Leffy]\tI'm activated sir!\n")
    doSpeak("I'm activated sir!")
    
    while mode == "standby":
        loop += 1
        # Mengusir Kegaringan
        if loop >= 15:
            randnum = random.randint(1,10)
            if randnum in [1,2]:
                doSpeak("You know sir? I'm something of a scientist myself")
            elif randnum in [3,4]:
                doSpeak("Don't forget to breath sir!")
            elif randnum in [5,6]:
                doSpeak("I'm wondering what you gonna do next sir?")
            elif randnum in [7,8]:
                doSpeak("Want some music sir?")
            elif randnum in [9,10]:
                doSpeak("Such a nice weather today, isn't it sir?")
            loop = 0
        with sr.Microphone(device_index=1) as source:
            # if sistem_operasi == "Windows":
            #     ctypes.windll.kernel32.SetConsoleTitleW("Listening...")
            print("Listening...", end="\r")
            try:
                detected_audio = recognizer.listen(source, phrase_time_limit=durasi_input)
                try:
                    # if sistem_operasi == "Windows":
                    #     ctypes.windll.kernel32.SetConsoleTitleW("Recognizing...")
                    print("Recognizing...", end="\r")
                    recognized_sound = recognizer.recognize_google(detected_audio)
                    # Exit Program
                    if recognized_sound == "exit program" or recognized_sound == "exit the program" or recognized_sound == "stop program" or recognized_sound == "stop the program" or recognized_sound == "shut up":
                        print("[Rizky]\t" + recognized_sound)
                        print("[Leffy]\tStopping the program. Goodbye sir!")
                        doSpeak("Stopping the program. Goodbye sir!")
                        mode = "stop"
                    elif recognized_sound == "shutdown system":
                        if sistem_operasi == "Windows":
                            print("[Rizky]\t" + recognized_sound)
                            print("[Leffy]\tStopping the program and shutdown system under 30 seconds. Goodbye sir!")
                            doSpeak("Stopping the program and shutdown system under 30 seconds. Goodbye sir!")
                            subprocess.Popen("shutdown /s /t 30")
                            mode = "stop"
                        elif sistem_operasi == "Linux":
                            print("[Rizky]\t" + recognized_sound)
                            print("[Leffy]\tStopping the program and shutdown system under 1 minute. Goodbye sir!")
                            doSpeak("Stopping the program and shutdown system under 1 minute. Goodbye sir!")
                            subprocess.Popen("sudo shutdown +1")
                            mode = "stop"
                        elif sistem_operasi == "Darwin":
                            print("[Rizky]\t" + recognized_sound)
                            print("[Leffy]\tStopping the program and shutdown system under 1 minute. Goodbye sir!")
                            doSpeak("Stopping the program and shutdown system under 1 minute. Goodbye sir!")
                            subprocess.Popen("sudo shutdown -P +1")
                            mode = "stop"
                        else:
                            print("[Rizky]\t" + recognized_sound)
                            print("[Leffy]\tUnknown operating system : " + sistem_operasi + "\n")
                            doSpeak("Unknown operating system : " + sistem_operasi)
                    else:
                        doCommand(recognized_sound)
                    loop = 0
                except sr.UnknownValueError:
                    pass
                except sr.RequestError as e:
                    pass
                except KeyboardInterrupt:
                    print("[Leffy]\tKeyboard interrupt detected")
                    doSpeak("Keyboard interrupt detected")
                    mode = "stop"
                    break
            except KeyboardInterrupt:
                print("[Leffy]\tKeyboard interrupt detected")
                doSpeak("Keyboard interrupt detected")
                mode = "stop"
                break

    print("\n[###]==={ LEFFY v1.0 // My Personal Voice Assistant }===[###]\n")
    exit()

def main():
    if sistem_operasi == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    
    print("\n[###]==={ LEFFY v1.0 // My Personal Voice Assistant }===[###]\n")
    time_now = datetime.datetime.now()
    time_h = time_now.hour
    time_m = time_now.minute
    if time_h >= 0 and time_h <= 12:
        doSpeak("Good morning sir!")
    elif time_h >= 13 and time_h <= 18:
        doSpeak("Good afternoon sir")
    else:
        doSpeak("Good night sir!")
    doListen()

if __name__ == '__main__':
    main()
