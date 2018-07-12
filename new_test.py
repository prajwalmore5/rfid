
#import libraries and packages
import datetime
import time
import RPi.GPIO as GPIO
import MFRC522
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

#Create variables for online database
scope = ['https://spreadsheets.google.com/feeds',
	 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('rfid.json',scope)
client = gspread.authorize(creds)

#Open sheet from google sheets
#sheet = client.open('D8').sheet1
sh = client.open ('D8')
sheet = sh.get_worksheet(0)

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







#initialize scanning
def scan():
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
          
          time=datetime.time.now().time()
          check_uid = str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3])
          # Print UID
          print("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
          return check_uid
          return time
        
#online data
def gsheet():

      scan()
      #Import cell info. from google sheets
      cell = sheet.find(check_uid)        #find uid number in sheet
      value = cell.value
      row_number = cell.row               #store value of row
      column_number = cell.col            #store value of column
      lec = sheet.cell(2,1).value

      #conditions for entering attendance data according to lecture timing
      if value == check_uid:
          
          if (now <= t2) or ((now >= t1) and (now <= t2)):
              lec=lec+1
              sheet.update_cell(row_number,lec,'1')
              print('done')
              lec = lec-1

          elif (now >= t3) and (now <= t4):
              lec=lec+2
              sheet.update_cell(row_number,lec,'1')
              print('done')
              lec = lec-2
              
          elif (now >= t5) and (now <= t6):
              lec=lec+3
              sheet.update_cell(row_number,lec,'1')
              print('done')
              lec = lec-3
              
          elif (now >= t7) and (now <= t8):
              lec=lec+4
              sheet.update_cell(row_number,lec,'1')
              print('done')
              lec = lec-4
              
          elif (now >= t9) and (now <= t10):
              lec=lec+5
              sheet.update_cell(row_number,lec,'1')
              print('done')
              lec = lec-5
              
          elif (now >= t11) and (now <= t12):
              lec=lec+6
              sheet.update_cell(row_number,lec,'1')
              print('done')
              lec = lec-6
             
          else:
              print('you are late')
    
      else:
          print('invalid entry')
      lec=lec+6
      sheet.update_cell(2,1,lect)
      
          
time.sleep(3)

except KeyboardInterrupt:
    GPIO.cleanup()
      

    
    
