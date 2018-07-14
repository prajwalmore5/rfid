
#import libraries and packages
import datetime
import time
import RPi.GPIO as GPIO
import sleep from time
import MFRC522
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from gpiozero import LED
from gpiozero import Buzzer

#intitializing some variables for using leds, buzzer and buttons
led = LED(17) 
Red_led = LED(27)
Green_led = LED(22)
buzzer = Buzzer(18)

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
input_state_in = GPIO.input(23)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
input_state_out = GPIO.input(24)

# Define GPIO to LCD mapping
LCD_RS = 20
LCD_E  = 5
LCD_D4 = 6
LCD_D5 = 13
LCD_D6 = 19
LCD_D7 = 26

# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

def main():
  # Main program block
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7

  # Initialise display
  lcd_init()
  return True





   

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

#assign current time as a varriable and assign todays date as anew variable
today = datetime.today()
datem = datetime(today.year, today.month, 1)
now = datetime.datetime.now()
month = 1

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


if input_state_in == False
time_in =datetime.time.now().time()

if input_state_out == False
time_out =datetime.time.now().time()
#initialize scanning
def scan():
	
	main()
	# Send some test
	lcd_string("RFID based",LCD_LINE_1)
	lcd_string("attendancesystem",LCD_LINE_2)
	if input_state_in == False OR if input_state_out == False:
		print('Button Pressed')
		# Welcome message
		print("Looking for cards")
		lcd_string("looking for cards")
		time.sleep(3) # 3 second delay
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
          return check_uid
          return time
'''
#to change dimensions of row and coloumns 
def dimensions(row,coloumn):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.row_dimensions[row].height = 20
    sheet.column_dimensions['coloumn'].width = 50
    wb.save('dimensions.xlsx')

#to merge cells
def merging(cell1,cell2):
    sheet = wb.active
    sheet.merge_cells('cell1:cell2')
    wb.save('merged.xlsx')

# to create new sheet for every month
def month():
    if  today ==datem and month!=12:
        #Open sheet from google sheets
        #sheet = client.open('D8').sheet1
        sh = client.open ('D8')
        sheet = sh.get_worksheet(month)
        month = month +1
'''
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
	try:
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



    
    
