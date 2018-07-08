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

# Welcome message
print("Looking for cards")

#Open sheet from google sheets
sheet = client.open('D8').sheet1
sh = client.open ('D8')

# This loop checks for chips. If one is near it will get the UID
try:

  while True:

    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()


    # If we have the UID, continue.
    if status == MIFAREReader.MI_OK :

      check_uid = str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3])
      # Print UID
      print("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))

      #Import value to google sheets
      cell = sheet.find(check_uid) #find uid number in sheet
      value = cell.value
      row_number = cell.row #store value of row
      column_number = cell.col #store value of column
      print (row_number)

      if value == check_uid:
        sheet.update_cell(row_number,4,'present')
        print('done')

      time.sleep(2)

except KeyboardInterrupt:
  GPIO.cleanup()


