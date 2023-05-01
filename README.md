# face-recognition-attendance
# face-recognition-attendance
<br>
Main steps for the Face Recognistion system<br>
a.	Web Cam setting.<br>
b.	Graphics.<br>
c.	Encoding Generator.<br>
d.	Face Recognition.<br>
e.	Database setup.<br>
f.	Adding data to database.<br>
g.	Adding Images to Database.<br>
h.	Realtime database update.<br>
i.	Limits no.of attendence per day<br>

<br>
Face Recognistion System Using Python <br>

⦁	Created a project using Pycharm.<br>
⦁	Created 2 new folders named Resources & Images.<br>
⦁	Insert 2 Photos to Image folder.<br>
⦁	Renamed the file name to ID number, Because the name may be similar but the ID should be different.<br>
⦁	Add some mode/images to the Resource folder.<br>
⦁	We need C++ complier, Because it is easy to use.<br>
⦁	Then File > Settings > Project name > Python Intrepreter<br>
⦁	Install Libraries <br>
⦁	cmake, dlib, face-recognition, cvzone, opencv-python (downgrade to version 4.5.4.60), Because it is more stable than new one (Python 3.7.6) Install those packages.<br>
⦁	Create a new python file (main.py).<br>
⦁	Code for webcam.<br>
⦁	Create file named EncodeGenerator.py.<br>
⦁	While coding there need to change the default system BGR to RGB, otherwise it will not work.<br>
⦁	Open-Cv mainly using BGR method and the Face-Recognition system uses RGB method.<br>
⦁	In this case while saving we need 2 things ID's & Encoding.<br>
⦁	Generate a pickle file.<br>
⦁	We are using cvzone for making the rectangle for the image recognition.<br>
⦁	Moving to Data base.<br>
⦁	Here mainly using the Firebase as Database. you can scale as you can go through the firebase.<br>
⦁	Steps for creating Database.<br>
	Chrome > Firebase > Console > New project > Project name > 	Build > Realtime Database > Create > Testmode > Copy link<br>
⦁	We need one file that upload all the data to server and then file helps to download the code.<br>
⦁	Ones you downloaded the file you can use those.<br>
⦁	The data will be in Json format.<br>
⦁	Next need a storage, for that.<br>
⦁	Storage > Testmode > next.<br>
⦁	Settings > Project settings > Service accoount > Python > Generate new private key.<br>
⦁	Copy and paste that private key to the Project.<br>
⦁	To add the data to Database.<br>
⦁	Create a new python file named AddDataToDatabase.py > Paste the Copied code.<br>
⦁	Install firebase_admin package.<br>
⦁	Create reference.<br>
⦁	Upload data.<br>


Overview

The Face Recognition Attendance System utilizes manual input of student images. When the webcam matches a student's image, the system displays their attendance, study status, and department. Attendance can be added again after 30 seconds, otherwise, it will show as already marked. The database is updated with attendance information and any changes made
