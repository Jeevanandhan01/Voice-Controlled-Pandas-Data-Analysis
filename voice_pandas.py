import pandas as pd
import pyttsx3
import speech_recognition as sr
df = pd.read_csv('iris.csv')
eng = pyttsx3.init()
sent = "Hello Boss , Welcome to Pandas functions , You can see column names , null values , shape ,and head ,say exit to stop"
eng.setProperty("rate",190)
eng.say(sent)
eng.runAndWait()
reco = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print(".....CALIBRATING.....")
        print(".....LISTENING.....")
        ad = reco.listen(source)
        print(".....RECORDED..SUCCESSFULLY.....")
        sp = reco.recognize_google(ad)
        sp = sp.lower()
        print("Your voice input is",sp)
        if(sp == "column names"):
            print("Column Names : ",df.columns.values.tolist())
            print(" ")
        elif(sp =="null values"):
            print("Null values : ",df.isnull().sum())
            print(" ")
        elif(sp =="shape"):
            print("Shape : ",df.shape)
            print(" ")
        elif(sp =="head"):
            print("Glance : ",df.head())
            print(" ")
        elif(sp =="exit"):
            print("Bye !")
            break
        else:
            print("Please give the proper voice input")
