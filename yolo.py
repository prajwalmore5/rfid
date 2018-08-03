#first we'll install & import libraries and packages.
import RPi.GPIO as GPIO
import MFRC522
import gspread
from datetime import datetime
import time
import pprint
from time import sleep
from oauth2client.service_account import ServiceAccountCredentials

GPIO.setmode(GPIO.BOARD)   # Use Physical Pin Numbering Scheme
button1=16
button2=18
LED1=15
LED2=13
GPIO.setwarnings(False)
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button1 an input, Activate Pull UP Resistor
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 2 an input, Activate Pull Up Resistor
GPIO.setup(LED1,GPIO.OUT,) # Make LED 1 an Output
GPIO.setup(LED2,GPIO.OUT)  # Make LED 2 an Output
BS1=False                  # Set Flag BS1 to indicate LED is initially off
BS2=False                  # Set Flag BS2 to indicate LED is initially off

#subject uid
sub_uid=[0,"6714816839","224254182212","48193190212","48217182212","11222237112","208149134212"]

#Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()
#print('chaltay mc.. tuza net hagtay')
#Create variables for online database
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('rfid.json',scope)
client = gspread.authorize(creds)

#Open sheet from google sheets
sh = client.open ('D8')    #sheet = client.open('D8').sheet1

#sheet = sh.get_worksheet(0)


#assign current time as a varriable and assign todays date as anew variable
now = datetime.now()
date = datetime.now().day
month = datetime.now().month
year = datetime.now().year
day1 = 1

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

def scan():
    # Welcome message
    #print("Looking for cards")
    
    # This loop checks for chips. If one is near it will get the UID
    try:
        while True:
            # Scan for cards
            (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
            
            # Get the UID of the card
            (status,uid) = MIFAREReader.MFRC522_Anticoll()
            
            # If we have the UID, continue
            if status == MIFAREReader.MI_OK :
                
                uid = str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3])
                
                # Print UID
                #print("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
                return(uid)
                #time.sleep(5)
                
    except KeyboardInterrupt:
        GPIO.cleanup()

def teacher():
    teacher_uid = scan()
    return(teacher_uid)

def student():
    student_uid = scan()
    return(student_uid)


  
#main loop
print("press button 1 for teacher")
#print("press button 2 for student")
try:
    while True:
        if GPIO.input(button1)==0:              # checks if button 1 is pressed
            print ("scan subject card")
            if BS1==False:
                GPIO.output(LED1,True)  # turn it on
                global tuid
                tuid = teacher()
                print(tuid)
                index = sub_uid.index(tuid)
                print(index)
                global sheet
                sheet = sh.get_worksheet(index)
                GPIO.output(LED1,False)
                print("press button 2 to start attendance.")
                break
            break
        
        #if GPIO.input(button2)==0:
            #print('wrong button pressed')
        
    '''       
    global count
    count = sheet.cell(1,1).value
    '''
    while True:     
        if GPIO.input(button2)==0:  # checks if button 1 is pressed
            print ("scan student card")
            if BS2==False:
                GPIO.output(LED2,True)  # turn it on
                global suid
                suid = student()
                
                #Import value to google sheets
                cell = sheet.find(suid) #find uid number in sheet
                value = cell.value
                row_number = cell.row #store value of row
                column_number = cell.col #store value of column
                print (row_number)
                count = sheet.cell(1,1).value
                count = int(count)
                
                
                if value == suid:
                    sheet.update_cell(row_number,count,'1')
                    print('done')
                    count = count + 1
                    sheet.update_cell(1,1,count)
                    print('next')

                else:
                    print('Invalid Card. Press button again and scan the card.')
                
     
    print(tuid)

except KeyboardInterrupt:
    GPIO.cleanup()

    
    
                        
'''
#main loop
    
if GPIO.input(button1)==0:              # checks if button 1 is pressed
        print ("scan subject card")
        if BS1==False:                  # If the LED is off
                GPIO.output(LED1,True)  # turn it on
                global teacher_uid
                tuid = teacher()
                print(tuid)
                index = sub_uid.index(tuid)
                print(index)
                        
                sleep(1)
                GPIO.output(LED1,False)
'''                               
                    
                    
                                         
        
    

       


