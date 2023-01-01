# Face Recognition

Face Recognition is implemented using the face-recognition package in python. This is using the deep learning model provided in the package which generates encodings for the faces which is stored in a CSV file and then later on used for face recognition in live camera systems.

Currently the folder  **Celebrity Images** holds all the images which are used to show face recognition. It holds about 30 images.

To set up your environment install the packages required using the following command

    pip install -r requirements.txt
The **requirements.txt** file is provided in the repository.

# Files
The **Generate Data.py** file reads all the images in the **Celebrity Images** folder and generates the encodings and stores them in a CSV file using pandas along with the name of the person.

The **LiveCamera.py** file then reads the CSV file when run to compare the encoding values of the face in the frame to the existing encoding values. The threshold for matching is kept as 0.6 i.e. if the difference between the encoding values of the faces in the CSV files and the face in the frame is greater than 0.6 then the name is returned as un-identified. 

The **LiveCam-Adding Data.py** allows the un-identified user to give their name which is then added to the CSV file and stored, after which the users' name is returned and not displayed as un-identified person.
# Usage
To use the code just add your image with title as your name and run the **Generate Data.py** script which will generate the CSV using the images in the Celebrity Images folder.
Now connect your webcam if needed and the run the **LiveCamera.py** script and see the results.
