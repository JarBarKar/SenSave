# SenSave

<u><b>Stack used:</b></u>
Python

<u><b>Python/libraries setup:</b></u>
1) Install the latest python version.
2) Install Anaconda.
3) Navigate to the directory where you cloned the database at.
4) Open terminal and type "pip install -r requirements.txt" to install all the dependencies required.
5) Do note that Cmake and Dlib might be difficult to install for macbook M1 and windows machine. So creating a virtual environment for this project is highly recommended. For windows user, please follow the guide in this URL to install dlib: https://medium.com/analytics-vidhya/how-to-install-dlib-library-for-python-in-windows-10-57348ba1117f

<u><b>Serial port setup:</b></u>
1) Open Device Manager on the computer (press window + s to search)
2) Under Ports (COM &LPT), take note the current port used.
3) Plug in the mircobit used as a reciever into an USB port.
4) Under Ports (COM &LPT), check the new port used.
5) Change the port number at main.py, line 97 to the port identified in step 4

<u><b>Apps to launch: </b></u><br>
There are certain python files needed to be launched at different terminals for it to receive information. <br>
1) iot_bot_code.py (to initate telegram bot) <br>
2) main.py (to initiate data collection from microbits, and coordinate other functions) <br>

<b>Generate telegram bot:</b><br>
1) For telegram bot, please use BotFather to generate unique token and chat ID for the telegram bot. Follow the guide in this URL to generate the data https://sendpulse.com/knowledge-base/chatbot/create-telegram-chatbot <br>
2) Insert the generated token and chat ID into iot_bot_code.py, tele_notification.py and main.py file, replace the values with <TOKEN_ID> and <CHAT_ID> found in the source code. <br>
3) Create a group chat and invite your bot into the group chat to start receiving notifications and interact with it. <br>

<b>Telegram bot commands:</b><br>
1) /profile (Retrieve elderly profile information)
2) /unique (Retrieve the number of unique visitors that visit the elderly premise)
3) /where (Retrieve the current location of the elderly and how long she was at that location for)

<br>
<b>Updating elderly face for facial recognition:</b><br>
1)For the facial recognition, if you want to change to a new elderly face for the face_recognition software to use as a basis of comparison for visitors and elderly. Navigate to known_faces directory and replace elderly.jpg with the new photo.
2) *NOTE* that the file must be named <b>elderly.jpg</b> for the software to recognize.
<br><br>
<u><b>App used: </b></u><br><br>

<b>Facial recognition</b>: final_face_detection_v3.py

Description: This file uses the python library opencv, to snap a picture using the laptop cam, followed by comparing the captured image and the stored image to see if the photos matched with the database (Using facial_recognition library). Lastly, it will trigger a push notification to our telegram bot to inform the user if the elderly is entering the premises or unknown personel is nearby the premises. Furthermore, if no faces are detected in the snapshot, no action will be taken, to reduce redunctant notification pushed and to save spaces too.

<b>Telegram Bot</b>: <br>
tele_notification.py <br>

Description: This file sends push notification to the telegram bot to broadcast the elderly status. <br>

iot_bot_code.py <br>

Description: This file responds to telegram commands when user input it in the group chat that the bot is in it. <br><br>

<u><b>Data storage: </b></u>

<b>Machine learning data</b>: elderlyHabits.csv

Description: This file stores parameter needed to train the sense making machine learning model. Stored parameters [year, month, day, hour, minutes, second, weekday, location, duration]. First 6 parameter is to store time. [weekday] refers to the day of the week (e.g. 0: monday, 1: Tuesday). [location] is refers to where the elderly is. [duration] refers to how long the elderly is in that location, in hours.

<b>Movement tracking</b>: lastMovement.csv

Description: This file stores time stamp and motion detected by PIR sensors in different room. Stored parameters [year, month, day, hour, minutes, second, location]. First 6 parameter is to store time. [location] is refers to where the sensor is placed. This data is used to approximate elderly's movement.

<b>Person tracking</b>: ownerVisitor.csv

Description: This file stores how many people is in the elderly's house. Stored parameters [year, month, day, hour, minutes, second, personCount, elderly]. First 6 parameter is to store time. [personCount] is refers to number of visitors in the house. [elderly] is a boolean parameter that refers to if the elderly is at home.

<u><b>Microbit files: </b></u>

<b>Receiver</b>: microbit-Receiver.hex

Description: This file is to be downloaded to the microbit connected to the laptop to serve as a receiver for other microbits.

<b>Directional movement tracking(1)</b>: microbit-first.hex

Description: This file is to be downloaded to the microbit located nearer to the door to track entrance and exit.

<b>Directional movement tracking(2)</b>: microbit-second.hex

Description: This file is to be downloaded to the microbit located further to the door to track entrance and exit.

<b>Bedroom sensor</b>: microbit-Sensorbedroom.hex

Description: This file is to be downloaded to the microbit placed at the bedroom.

<b>Kitchen sensor</b>: microbit-Sensorkitchen.hex

Description: This file is to be downloaded to the microbit placed at the kitchen.

<b>Living room sensor</b>: microbit-sensorliving-room.hex

Description: This file is to be downloaded to the microbit placed at the living room.

<b>Toilet sensor</b>: microbit-Sensortoilet.hex

Description: This file is to be downloaded to the microbit placed at the toilet.
