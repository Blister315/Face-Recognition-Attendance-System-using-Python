Project flow & explaination:


After running the project, click on the Student Details button. Then, fill in the student details so that when the system recognizes your face, it can display your information while identifying you. These details will also be stored in the database.

While filling in the details, you will see two options: Take Photo Sample and No Photo Sample. Choose the No Photo Sample option. After entering the details, click on the Save button. Your details will then appear on the blank space on the right side.

Next, click on the saved details and select the option Take Photo Sample. The system will capture a total of 100 photo samples, which will be stored in a folder named data.

After this, go back to the home screen and click on the Train Data button. A new window will open with a button labeled Train Data. Click on this button to train all 100 photo samples captured by the system.

Once the training is complete, return to the home screen and click on the Face Detector button. A new window will open where you will find a button named Face Recognition. Click on it to start the camera. The system will then identify your face and display your details, including your name, student ID, roll number, and department.

Press Enter to close the camera. Your attendance will be saved in a file named harshit.csv (you can change the file name, but remember to update it in the code as well).

Finally, go back to the home screen and click on the Attendance button. In the Attendance section, you will find an option to Import CSV. Click on it and select the harshit.csv file where the attendance data is stored. The attendance records will then be displayed on the right side of your screen.

1. System Architecture
• Programming Language: Python

• Libraries/Frameworks:
• OpenCV (for image processing)
• NumPy and Pandas (for data handling)
• Tkinter (for the user interface)

• Database: MySQL (for storing attendance records)

• Hardware Requirements:
• Webcam for face capture

3. Key Features
• Real-Time Recognition: Detects and identifies faces in real-time.
• Database Integration: Stores attendance records securely.
• Scalability: Allows adding new users to the system seamlessly.
• Report Generation: Generates detailed attendance reports in Excel
format.

5. Technical Highlights
• Face Detection: Utilizes Haar Cascade Classifier for real-time face
detection.
• Face Recognition: LBPH algorithm for identifying faces accurately.
• Real-time Updates: Attendance logs are updated live in the
database.


SCREENSHOTS

Home:
![image](https://github.com/user-attachments/assets/01f0d7d6-3ba8-49be-a707-07a5d833bfe5)

Student Details:
![image](https://github.com/user-attachments/assets/192f11f2-d823-46ba-9103-24d9a6b4bbbb)

Train Data:
![image](https://github.com/user-attachments/assets/ddaea520-a482-4fad-b8d8-17587b9fa90d)

Face Detector:
![image](https://github.com/user-attachments/assets/2cccaea8-33a9-40ca-afaf-d2bed63a27c3)

Attendance:
![image](https://github.com/user-attachments/assets/50e0190a-2919-499c-b872-5dfa58c6f2a8)

Developer:
![image](https://github.com/user-attachments/assets/53754f83-4315-496c-874d-bb29c2d3ed6f)

Help:
![image](https://github.com/user-attachments/assets/1863b517-a0c0-4ca5-aac0-ea7bbed5059c)

Photos: Clicking on this option will redirect you to the data folder, where your image samples are stored.

Exit: Clicking on this option will quit the program.









