import subprocess
import pandas as pd
import pyautogui
import time
from datetime import datetime

def login(m_id, m_pswd):
    #open zoom
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])
    
    #avoid delay at start
    time.sleep(5)
    
    #locates and clicks the join button for a meeting
    join_button = pyautogui.locateCenterOnScreen('Join.png')
    pyautogui.moveTo(join_button.x/2, join_button.y/2)
    pyautogui.click() #coordiantes are divided by 2 because macOS takes a screenshot that is double the deafult resolution
    
    time.sleep(1)
    
    #entering meeting id
    meeting_button = pyautogui.locateCenterOnScreen('id1.png')
    pyautogui.moveTo(meeting_button.x/2, meeting_button.y/2)
    pyautogui.click()
    pyautogui.write(m_id)
    
    time.sleep(1)
    #turn off audio and video - optional
    A_button = pyautogui.locateCenterOnScreen('auv.png')
    pyautogui.click(A_button.x/2,A_button.y/2)
    V_button = pyautogui.locateCenterOnScreen('auv.png')
    pyautogui.click(V_button.x/2,V_button.y/2)
    
    #Join meeting
    join_2 = pyautogui.locateCenterOnScreen('Join_2.png')
    pyautogui.click(join_2.x/2, join_2.y/2)
    
    time.sleep(1)
    #Enter Passcode
    pswd = pyautogui.locateCenterOnScreen('pswd.png')
    pyautogui.click(pswd.x/2, pswd.y/2)
    pyautogui.write(m_pswd)
    pyautogui.press('enter')
    
#use Pandas to read the csv file

df = pd.read_csv("Meeting_times.csv")

#infinite while loop to check when the scheduled time comes
while True:
    now = datetime.now().strftime("%H:%M")
    if now in str(df['Time']):
        row = df.loc[df['Time']==now]
        m_id = str(row.iloc[0,1])
        m_pswd = str(row.iloc[0,2])
        
        login(m_id, m_pswd)
        time.sleep(30)
        print("Successfully joined meeting with ID:" + m_id)
