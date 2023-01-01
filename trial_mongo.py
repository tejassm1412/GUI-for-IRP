# Import necessary libraries
import face_recognition
import pymongo
import cv2

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb+srv://irp:irp2022@irpmongodb.26cuy7l.mongodb.net/")
db = client["face_recognition"]
collection = db["encodings"]

# Function to extract face encoding from image
def get_face_encoding(image):
    try:
        # Use the face_recognition library to extract face encoding from image
        face_encoding = face_recognition.face_encodings(image)[0]
        return face_encoding
    except:
        return "False"
        

# Function to store face encoding in MongoDB collection
def store_face_encoding(name, image):
    # Extract face encoding from image
    face_encoding = get_face_encoding(image)
    # Store face encoding in MongoDB collection along with name
    result = collection.insert_one({ "name": name, "encoding": face_encoding.tolist() })
    print("Face encoding stored in MongoDB with ID:", result.inserted_id)

# Function to recognize person in real time
def recognize_person():
    # Capture video frames from webcam
    video_capture = cv2.VideoCapture(0)

    # Continuously capture and process video frames
    while True:
        # Capture frame
        ret, frame = video_capture.read()

        # Extract face encoding from frame
        face_encoding = get_face_encoding(frame)

        if face_encoding!= "False":

            # Compare face encoding with stored face encodings
            for doc in collection.find({}):
                # Calculate cosine similarity between face encoding and stored encoding
                similarity = face_recognition.face_distance([doc["encoding"]], face_encoding)
                if similarity < 0.5:
                    # If similarity is below threshold, recognize person
                    print("Person recognized:", doc["name"])
                    break
                elif similarity>=0.5:
                    print("Person not recognized")
                    break
            break

        else:
            print("No Person")

image = cv2.imread("/home/tejas/Desktop/MySTuff/20-11-2022/target.jpg")

# Store face encoding in MongoDB collection
store_face_encoding("John", image)

# Recognize person in real time
recognize_person()
