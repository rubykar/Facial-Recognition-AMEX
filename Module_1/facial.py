import face_recognition

# Load images of known faces
known_image_1 = face_recognition.load_image_file("person_1.jpg")
known_image_2 = face_recognition.load_image_file("person_2.jpg")

# Extract face encodings from images
known_face_encoding_1 = face_recognition.face_encodings(known_image_1)[0]
known_face_encoding_2 = face_recognition.face_encodings(known_image_2)[0]

# Create a list of known face encodings and their names
known_face_encodings = [
    known_face_encoding_1,
    known_face_encoding_2
]
known_face_names = [
    "Person 1",
    "Person 2"
]

# Load an image to recognize
unknown_image = face_recognition.load_image_file("unknown_person.jpg")

# Extract face encodings from the unknown image
unknown_face_encodings = face_recognition.face_encodings(unknown_image)

# Loop through each face in the unknown image and compare it to the known faces
for unknown_face_encoding in unknown_face_encodings:
    # Compare the unknown face encoding to each known face encoding
    matches = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)

    # Determine the best match
    best_match_index = matches.index(True)
    name = known_face_names[best_match_index]

    print(f"Match found: {name}")
