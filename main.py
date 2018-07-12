import datetime
import time
import RPi.GPIO as GPIO
import MFRC522
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

#assign current time as a varriable
now = datetime.datetime.now()

#assign time variables to be compared with current time
t1 = now.replace(hour = 8, minute = 10, second = 0, microsecond = 0)
t2 = now.replace(hour = 8, minute = 20, second = 0, microsecond = 0)
t3 = now.replace(hour = 9, minute = 10, second = 0, microsecond = 0)
t4 = now.replace(hour = 9, minute = 20, second = 0, microsecond = 0)
t5 = now.replace(hour = 10, minute = 10, second = 0, microsecond = 0)
t6 = now.replace(hour = 10, minute = 35, second = 0, microsecond = 0)
t7 = now.replace(hour = 11, minute = 25, second = 0, microsecond = 0)
t8 = now.replace(hour = 11, minute = 35, second = 0, microsecond = 0)
t9 = now.replace(hour = 12, minute = 25, second = 0, microsecond = 0)
t10 = now.replace(hour = 12, minute = 55, second = 0, microsecond = 0)
t11 = now.replace(hour = 13, minute = 45, second = 0, microsecond = 0)
t12 = now.replace(hour = 13, minute = 55, second = 0, microsecond = 0)
t13 = now.replace(hour = 14, minute = 45, second = 0, microsecond = 0)
t14 = now.replace(hour = 14, minute = 10, second = 0, microsecond = 0)
t15 = now.replace(hour = 16, minute = 0, second = 0, microsecond = 0)
t16 = now.replace(hour = 16, minute = 10, second = 0, microsecond = 0)

#Create variables for database
scope = ['https://spreadsheets.google.com/feeds',
	 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('rfid.json',scope)
client = gspread.authorize(creds)

#Open sheet from google sheets
#sheet = client.open('D8').sheet1
sh = client.open ('D8')
sheet = sh.get_worksheet(0)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print("Looking for cards")

# This loop checks for chips. If one is near it will get the UID
try:

  while True:

    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()


    # If we have the UID, continue
    if status == MIFAREReader.MI_OK :

      check_uid = str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3])
      # Print UID
      print("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))

      #Import cell info. from google sheets
      cell = sheet.find(check_uid) #find uid number in sheet
      value = cell.value
      row_number = cell.row #store value of row
      column_number = cell.col #store value of column
      lec = sheet.cell(2,1).value
      
      #conditions for entering attendance data according to lecture timing
      if now <= t2:
        if value == check_uid:
          sheet.update_cell(row_number,lec,'1')
          print('done')
          lec = lec+1
          sheet.update_cell(2,1,lec)
       
      elif (now >= t1) & (now <= t2):
        sheet.update_cell(row_number,lec,'1')
        print('done')
        lec = lec+1
        sheet.update_cell(2,1,lec)
          
      elif (now >= t3) & (now <= t4):
        sheet.update_cell(row_number,lec,'1')
        print('done')
        lec = lec+1
        sheet.update_cell(2,1,lec)
          
      elif (now >= t5) & (now <= t6):
        sheet.update_cell(row_number,lec,'1')
        print('done')
        lec = lec+1
        sheet.update_cell(2,1,lec)
          
      elif (now >= t7) & (now <= t8):
        sheet.update_cell(row_number,lec,'1')
        print('done')
        lec = lec+1
        sheet.update_cell(2,1,lec)
          
      elif (now >= t9) & (now <= t10):
        sheet.update_cell(row_number,lec,'1')
        print('done')
        lec = lec+1
        sheet.update_cell(2,1,lec)
          
      elif (now >= t11) & (now <= t12):
        sheet.update_cell(row_number,lec,'1')
        print('done')
        lec = lec+1
        sheet.update_cell(2,1,lec)
          
      elif (now >= t13) & (now <= t14):
        sheet.update_cell(row_number,lec,'1')
        print('done')
        lec = lec+1
        sheet.update_cell(2,1,lec)
          
      elif (now >= t15) & (now <= t16):
        sheet.update_cell(row_number,lec,'1')
        print('done')
        lec = lec+1
        sheet.update_cell(2,1,lec)
          
      else :
        print ('you are late')

      time.sleep(3)       

except KeyboardInterrupt:
  GPIO.cleanup()

