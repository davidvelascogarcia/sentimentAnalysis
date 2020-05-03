'''
 * ************************************************************
 *      Program: Sentiment Analysis
 *      Type: Python
 *      Author: David Velasco Garcia @davidvelascogarcia
 * ************************************************************
 */

/*
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
from googletrans import Translator
import os
import platform
from textblob import TextBlob
import yarp


print("**************************************************************************")
print("**************************************************************************")
print("                     Program: Sentiment Analysis                          ")
print("                     Author: David Velasco Garcia                         ")
print("                             @davidvelascogarcia                          ")
print("**************************************************************************")
print("**************************************************************************")

print("")
print("Starting system...")

print("")
print("Loading Sentiment Analysis engine...")

print("")
print("")
print("**************************************************************************")
print("YARP configuration:")
print("**************************************************************************")

print("")
print("Initializing YARP network...")

# Init YARP Network
yarp.Network.init()


print("")
print("Opening data input port with name /sentimentAnalysis/data:i ...")

# Open input data port
sentimentAnalysis_inputPort = yarp.Port()
sentimentAnalysis_inputPortName = '/sentimentAnalysis/data:i'
sentimentAnalysis_inputPort.open(sentimentAnalysis_inputPortName)

# Create input data bottle
inputBottle=yarp.Bottle()

print("")
print("Opening data output port with name /sentimentAnalysis/data:o ...")

# Open output data port
sentimentAnalysis_outputPort = yarp.Port()
sentimentAnalysis_outputPortName = '/sentimentAnalysis/data:o'
sentimentAnalysis_outputPort.open(sentimentAnalysis_outputPortName)

# Create output data bottle
outputBottle=yarp.Bottle()


print("")
print("Initializing sentimentAnalysis engine...")

# Get system configuration
print("")
print("Detecting system and release version...")
systemPlatform = platform.system()
systemRelease = platform.release()
print("")
print("")
print("**************************************************************************")
print("Configuration detected:")
print("**************************************************************************")
print("Platform:")
print(systemPlatform)
print("Release:")
print(systemRelease)

print("")
print("")
print("**************************************************************************")
print("Translator configuration:")
print("**************************************************************************")

# Get languages data
print("")
print("Getting languages data ...")
languagesData = configparser.ConfigParser()
languagesData.read('../config/languages.ini')
languagesData.sections()

inputLanguage = languagesData['Languages']['language-input']
outputLanguage = languagesData['Languages']['language-output']

print("Data obtained correctly.")
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

googleTranslatorEngineClient = Translator()

print("Client configuration done.")

while True:

    # Read data text
    print("")
    print("Waiting for input text ...")

    sentimentAnalysis_inputPort.read(inputBottle)
    dataText = inputBottle.toString()

    print("Data received: "+ dataText)

    # Process data
    print("")
    print("Analyzing data text...")

    print("")
    print("")
    print("**************************************************************************")
    print("Processing:")
    print("**************************************************************************")

    try:
        try:
            # Sending request to Google Translator API
            print("")
            print("Connecting with Google Translator server ...")

            print("")
            print("Translating from "+str(inputLanguage)+ " to "+ str(outputLanguage)+" ...")

            dataTranslated = googleTranslatorEngineClient.translate(str(dataText),dest=str(outputLanguage), src=str(inputLanguage))
            dataTranslated = dataTranslated.text
            print("")
            print("Text translated.")

            print("")
            print("Server response done.")

            print("")
            print("")
            print("**************************************************************************")
            print("Results:")
            print("**************************************************************************")
            print("")
            print("Input text in "+str(inputLanguage)+" language: "+ str(dataToTranslate))
            print("")
            print("Output text in "+str(outputLanguage)+" language: "+ str(dataTranslated))

            dataAnalyzed = TextBlob(str(dataTranslated))
            dataResults=str(dataAnalyzed.sentiment)

            print("")
            print("")
            print("**************************************************************************")
            print("Sentiment analysis results:")
            print("**************************************************************************")
            print("")
            print("Results: "+ dataResults)

        except:
            dataAnalyzed = TextBlob(dataText)

            dataTranslated=str(dataAnalyzed.translate(to='en'))

            dataAnalyzed = TextBlob(dataTranslated)
            print("Data translated: "+ dataTranslated)

            dataResults=str(dataAnalyzed.sentiment)

            print("")
            print("")
            print("**************************************************************************")
            print("Sentiment analysis results:")
            print("**************************************************************************")
            print("")
            print("Results: "+ dataResults)

    except:
        print("")
        print("Sorry, i could´t resolve your request.")
        dataResults="Unknown error"

    # Send mirror coordinates
    outputBottle.clear()
    outputBottle.addString(dataResults)
    sentimentAnalysis_outputPort.write(outputBottle)


# Close YARP ports
print("Closing YARP ports...")
sentimentAnalysis_inputPort.close()
sentimentAnalysis_outputPort.close()

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
