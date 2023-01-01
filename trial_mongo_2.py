import face_recognition
import pymongo
import cv2

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb+srv://irp:irp2022@irpmongodb.26cuy7l.mongodb.net/")
db = client["facial_recognition"]

# Set up the video capture
capture = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = capture.read()

    # Convert the frame to RGB
    rgb_frame = frame[:, :, ::-1]

    # Detect faces in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Iterate over the detected faces
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Prompt the user for a name
        name = input("Enter the name of the person: ")

        # Store the encoding and name in the database
        db.recognition_data.insert_one({
            "facial_features": face_encoding,
            "name": name
        })

    # Break out of the loop if the user presses "q"
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture
capture.release()

# Destroy all windows
cv2.destroyAllWindows()
