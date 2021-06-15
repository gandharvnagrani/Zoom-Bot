# Zoom-Bot
<li>Using the PyAutoGUI, Pandas, and subprocess modules available in Python, I created a Zoom bot that automates the process of joining Zoom meetings for you. The details of the meeting are entered in a .csv file. </li>
<li> The login function forms the base of this python script which takes in two parameters: the Zoom meeting ID and the Zoom meeting password. </li>
<li> The subprocess module allows us to open the Zoom application. </li>
<li> The time.sleep command is placed logically at places where a time delay is observed. </li>
<li> The PyAutoGUI module allows us to automate tasks like moving cursors, filling out text fields, and more importantly, identifying the location on the screen to be clicked. </li>
<li> Since my setup involves a Retina display MBP, the screenshots taken on my machine are double the true resolution of my display. To account for this, the x-y coordinates were divided by 2 at respective places in the code. </li>
<li> For non-retina displays, the code is available as a comment in the same line. </li>
<li> Finally, a csv file is used that stores all details of the meeting. </li>
<li> When the time on your machine matches the time outlined in the csv file, the pandas library helps us assign the respective meeting ID and passcode to the appropriate variables. </li>
<li> The function is then run with the mentioned inputs. </li>
<li> Never be late for a meeting again! </li>
