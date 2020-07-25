'''
 * ************************************************************
 *      Program: Sentiment Analysis
 *      Type: Python
 *      Author: David Velasco Garcia @davidvelascogarcia
 * ************************************************************
 *
 * | INPUT PORT                           | CONTENT                                                 |
 * |--------------------------------------|---------------------------------------------------------|
 * | /sentimentAnalysis/data:i            | Input data text                                         |
 *
 * | OUTPUT PORT                          | CONTENT                                                 |
 * |--------------------------------------|---------------------------------------------------------|
 * | /sentimentAnalysis/data:o            | Output analysis results                                 |
 *
'''

# Libraries
import datetime
import configparser
from googletrans import Translator
import os
import platform
from textblob import TextBlob
import time
import yarp


print("**************************************************************************")
print("**************************************************************************")
print("                     Program: Sentiment Analysis                          ")
print("                     Author: David Velasco Garcia                         ")
print("                             @davidvelascogarcia                          ")
print("**************************************************************************")
print("**************************************************************************")

print("")
print("Starting system ...")
print("")

print("")
print("Loading Sentiment Analysis engine ...")
print("")

print("")
print("Initializing sentimentAnalysis engine ...")
print("")

# Get system configuration
print("")
print("Detecting system and release version ...")
print("")

systemPlatform = platform.system()
systemRelease = platform.release()

print("")
print("**************************************************************************")
print("Configuration detected:")
print("**************************************************************************")
print("")
print("Platform:")
print(systemPlatform)
print("Release:")
print(systemRelease)

print("")
print("**************************************************************************")
print("Translator configuration:")
print("**************************************************************************")
print("")

loopControlIniExist = 0

while int(loopControlIniExist)==0:

    try:
        # Get languages data
        print("")
        print("[INFO] Getting languages data ...")
        print("")

        languagesData = configparser.ConfigParser()
        languagesData.read('../config/languages.ini')
        languagesData.sections()

        inputLanguage = languagesData['Languages']['language-input']
        outputLanguage = languagesData['Languages']['language-output']
        loopControlIniExist = 1

    except:
        print("")
        print("**************************************************************************")
        print("Error file not founded:")
        print("**************************************************************************")
        print("")
        print("[ERROR] Error, languages.ini not founded, i will check again in 4 seconds ...")
        print("")
        time.sleep(4)

print("")
print("[INFO] Data obtained correctly.")
print("")
print("Input language: "+ str(inputLanguage))
print("Output language: "+ str(outputLanguage))
print("")

print("")
print("**************************************************************************")
print("Google Translator client:")
print("**************************************************************************")
print("")
print("Configuring Google Translator client ...")
print("")

googleTranslatorEngineClient = Translator()

print("")
print("[INFO] Client configuration done at " + str(datetime.datetime.now()) + ".")
print("")


print("")
print("**************************************************************************")
print("YARP configuration:")
print("**************************************************************************")
print("")
print("Initializing YARP network ...")
print("")

# Init YARP Network
yarp.Network.init()

print("")
print("[INFO] Opening data input port with name /sentimentAnalysis/data:i ...")
print("")

# Open sentimentAnalysis input data port
sentimentAnalysis_inputPort = yarp.Port()
sentimentAnalysis_inputPortName = '/sentimentAnalysis/data:i'
sentimentAnalysis_inputPort.open(sentimentAnalysis_inputPortName)

# Create sentimentAnalysis input data bottle
sentimentAnalysisInputBottle = yarp.Bottle()

print("")
print("[INFO] Opening data output port with name /sentimentAnalysis/data:o ...")
print("")

# Open sentimentAnalysis output data port
sentimentAnalysis_outputPort = yarp.Port()
sentimentAnalysis_outputPortName = '/sentimentAnalysis/data:o'
sentimentAnalysis_outputPort.open(sentimentAnalysis_outputPortName)

# Create sentimentAnalysis output data bottle
sentimentAnalysisOutputBottle = yarp.Bottle()

print("")
print("[INFO] YARP network configured correctly.")
print("")

# Variable loopControlRequest
loopControlRequest = 0

while int(loopControlRequest) == 0:

    print("")
    print("**************************************************************************")
    print("Waiting for input request text:")
    print("**************************************************************************")
    print("")
    print("[INFO] Waiting for input request text ...")
    print("")

    sentimentAnalysis_inputPort.read(sentimentAnalysisInputBottle)
    dataText = sentimentAnalysisInputBottle.toString()

    print("")
    print("[RESULTS] Data received: "+ dataText + "at " + str(datetime.datetime.now()) + ".")
    print("")

    print("")
    print("**************************************************************************")
    print("Analyzing data text:")
    print("**************************************************************************")
    print("")
    print("[INFO] Analyzing data text ...")
    print("")

    try:
        try:
            # Sending request to Google Translator API
            print("")
            print("[INFO] Connecting with Google Translator server ...")
            print("")

            print("")
            print("[INFO] Translating from " + str(inputLanguage) + " to " + str(outputLanguage) + " ...")
            print("")

            dataTranslated = googleTranslatorEngineClient.translate(str(dataText),dest=str(outputLanguage), src=str(inputLanguage))
            dataTranslated = dataTranslated.text

            print("")
            print("[INFO] Text translated at " + str(datetime.datetime.now()) + ".")
            print("")

            print("")
            print("[INFO] Server response done.")
            print("")

            print("")
            print("**************************************************************************")
            print("Results:")
            print("**************************************************************************")
            print("")
            print("[RESULTS] Input text in " + str(inputLanguage) + " language: " + str(dataToTranslate))
            print("")
            print("[RESULTS] Output text in " + str(outputLanguage) + " language: " + str(dataTranslated))
            print("")

            dataAnalyzed = TextBlob(str(dataTranslated))
            dataResults = str(dataAnalyzed.sentiment)

            print("")
            print("**************************************************************************")
            print("Sentiment analysis results:")
            print("**************************************************************************")
            print("")
            print("[RESULTS] Request results: " + dataResults + "at " + str(datetime.datetime.now()) + ".")
            print("")

        except:
            # Enter input text and translate with internal textblob translator
            dataAnalyzed = TextBlob(dataText)
            dataTranslated = str(dataAnalyzed.translate(to='en'))

            # Translated text to analysis
            dataAnalyzed = TextBlob(dataTranslated)

            print("")
            print("[INFO] Data translated: " + dataTranslated + "at " + str(datetime.datetime.now()) + ".")
            print("")

            dataResults=str(dataAnalyzed.sentiment)

            print("")
            print("")
            print("**************************************************************************")
            print("Sentiment analysis results:")
            print("**************************************************************************")
            print("")
            print("[RESULTS] Request results: " + dataResults  + "at " + str(datetime.datetime.now()) + ".")
            print("")

    except:
        print("")
        print("[ERROR] Sorry, i could´t resolve your request.")
        print("")

        dataResults = "Unknown error"

    # Publish sentimentAnalysis results
    sentimentAnalysisOutputBottle.clear()
    sentimentAnalysisOutputBottle.addString("RESULTS:")
    sentimentAnalysisOutputBottle.addString(dataResults)
    sentimentAnalysisOutputBottle.addString("DATE:")
    sentimentAnalysisOutputBottle.addString(str(datetime.datetime.now()))
    sentimentAnalysis_outputPort.write(sentimentAnalysisOutputBottle)

# Close YARP ports
print("[INFO] Closing YARP ports...")
sentimentAnalysis_inputPort.close()
sentimentAnalysis_outputPort.close()

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
print("")
print("sentimentAnalysis program finished correctly.")
print("")
