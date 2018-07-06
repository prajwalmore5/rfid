import time
import RPi.GPIO as GPIO
import MFRC522
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

#Create variables for database
scope = ['https://spreadsheets.google.com/feeds',
	 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('rfid.json',scope)
client = gspread.authorize(creds)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Ask user for name
name = eval(input("Enter your name."))

# Welcome message
print("Looking for cards")
print("Press Ctrl-C to stop.")

#Open sheet from google sheets
sheet = client.open('RFID attendance system').sheet1

# This loop checks for chips. If one is near it will get the UID
try:

  while True:

    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    #assign uid to varible
    uid_new = ("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

      # Print UID
      print("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))

      #Import value to google sheets
      row = ["name","uid_new","1"]
      index = 4
      sheet.insert_row (row,index)
      time.sleep(2)

except KeyboardInterrupt:
  GPIO.cleanup()
