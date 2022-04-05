# SenSave

<u><b>Stack used:</b></u>
Python

<u><b>Python/libraries setup:</b></u>
1) Install the latest python version.
2) Install Anaconda.
3) Navigate to the directory where you cloned the database at.
4) Open terminal and type "pip install -r requirements.txt" to install all the dependencies required.
5) Do note that Cmake and Dlib might be difficult to install for macbook M1 and windows machine. So creating a virtual environment for this project is highly recommended. For windows user, please follow the guide in this URL to install dlib: https://medium.com/analytics-vidhya/how-to-install-dlib-library-for-python-in-windows-10-57348ba1117f

<u><b>Apps to launch: </b></u><br>
There are certain python files needed to be launched at different terminals for it to receive information. <br>
1) iot_bot_code.py (to initate telegram bot) <br>
2) main.py (to launch microbits) <br>

<b>Extra notes:</b><br>
1) For telegram bot, please use BotFather to generate unique token and chat ID for the telegram bot. Follow the guide in this URL to generate the data https://sendpulse.com/knowledge-base/chatbot/create-telegram-chatbot <br>
2) Insert the generated token and chat ID into iot_bot_code.py and main.py file, replace the values with <TOKEN_ID> and <CHAT_ID> found in the source code. <br>
3) Create a group chat and invite your bot into the group chat to start receiving notifications and interact with it. <br>

<b>Telegram bot commands:</b><br>
1) /profile (Retrieve elderly profile information)
2) /unique (Retrieve the number of unique visitors that visit the elderly premise)
3) /where (Retrieve the current location of the elderly and how long she was at that location for)


<u><b>App used: </b></u>

<b>Facial recognition</b>: final_face_detection_v3.py

Description: This file uses the python library opencv, to snap a picture using the laptop cam, followed by comparing the captured image and the stored image to see if the photos matched with the database (Using facial_recognition library). Lastly, it will trigger a push notification to our telegram bot to inform the user if the elderly is entering the premises or unknown personel is nearby the premises. Furthermore, if no faces are detected in the snapshot, no action will be taken, to reduce redunctant notification pushed and to save spaces too.
