import cv2
import csv
import face_recognition


def encoding_store(name):
    # Load the image and detect the faces
    image = cv2.imread('target.jpg')
    face_locations = face_recognition.face_locations(image)

    # Extract the face encoding values for each face
    encodings = face_recognition.face_encodings(image, face_locations)

    # Open the CSV file in append mode
    with open('face_encodings.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the titles on the first row
        if csvfile.tell()==0:
            writer.writerow(['index', 'image', 'encoding'])
        for i, encoding in enumerate(encodings):
            # Convert the encoding to a string separated by ","
            encoding_str = ",".join(str(x) for x in encoding)
            writer.writerow([i, name, encoding_str])

encoding_store("Tejas")