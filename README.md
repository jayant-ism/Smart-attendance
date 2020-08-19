A system is developed wherein as a student enters the class in the first period, his/her face will be recognised by the CCTV camera and the student will be registered as present in the class. The name of the student will be displayed on the LCD screen(placed above the blackboard), so that he/she can know that their attendance has been recorded. Immediately, their parents will also receive a message that their wards have reached the school, and thus students won’t be able to bunk the school and also will ensure parents that they have safely reached the school premises. Once the attendance has been marked in the first period, it will be notified (saved), so that it can help other teachers for verification. The number of students currently present in the class will continuously be displayed on the display board (LCD). For marking the presence of the wards in the class at proper time it is required that they get their attendance marked before the entry of the teacher(teacher may provide them 10 minutes relaxation). The face of the teacher will also be recognised and once the teacher enters the class, the camera will be closed and none of the student will get attendance after that. The total student tally, will vary depending on the current number of students present inside the classroom. The student’s entry and exit will be monitored and tracked to keep updating the number of students present in the class at the moment. Each day’s information regarding the total number of students present and absent will be stored and maintained in a database(firestore database). If a particular student is falling short of attendance for example less than 75 percent then, a message will be conveyed regarding it to their parents. The class teacher will be given Admin Access to the portal (wherein attendance is being uploaded), in case of any query or issue related to attendance one can directly contact their respective class teacher.

This project was deployed within 36 hours, as a part of SIH internal Hackathon, held at IIT(ISM) Dhanbad, where it was declared winner in the hardware category. The creators of the project were: Anukriti Rawat Neha Modak Jayant Anand Sayantani Bhattacharya Neelansh Maheshwari Ashutosh Saxena





Software Used:
postgresql
Python 3.6
Python IDLE

Python libraries.
Dlib
Tensorflow
Django
OpenCv

##################################### *

Hardware:

Node MCU
LCD module
Web Camera
Raspberry Pi

##################################### *
#################################### *

How to use it ?

Install all the software required for a raspberry cam to work. (at the moment the installation files are not provided.)

Make sure the Py Cam is working before proceeding.

Download all the files and folders and extract the folders.

Install all the packages required for the python (preferably create a new environment)

Using the raspberry bash open the python 3.5 environment.
First call "django runserver"  from commandprompt
Go to the link which will be provided in the cmd.
Submit your details. (It will be regestration time)
After it click on save then  class time .
Attendance will be directly uploaded on teachers portal , Which can be viewed by clicking "ok" on the same regestration page.
##################################### *


Add the timestamps and data to a database

Provide analytics on the data.
