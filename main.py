# import numpy as np
# import face_recognition

# imghamza = face_recognition.load_image_file('photos/hamza.jpg')
# imghamza = cv2.cvtColor(imghamza, cv2.COLOR_BGR2RGB)
# imghamzanaveed = face_recognition.load_image_file('photos/hamzanaveed.jpg')
# imghamzanaveed= cv2.cvtColor(imghamzanaveed, cv2.COLOR_BGR2RGB)
# imgshakaib = face_recognition.load_image_file('photos/shakaib.jpg')
# imgshakaib = cv2.cvtColor(imgshakaib, cv2.COLOR_BGR2RGB)

# faceloc = face_recognition.face_locations(imghamza)[0]
# encodehamza = face_recognition.face_encodings(imghamza)[0]
# cv2.rectangle(imghamza, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (155, 0, 255), 2)

# facelochamzanaveed = face_recognition.face_locations(imghamzanaveed)[0]
# encodehamzanaveed = face_recognition.face_encodings(imghamzanaveed)[1]
# cv2.rectangle(imghamzanaveed, (facelocTest[3], facelocTest[0]), (facelocTest[1], facelocTest[2]), (155, 0, 255), 2)

# facelocshakaib = face_recognition.face_locations(imgshakaib)[0]
# encodeshakaib = face_recognition.face_encodings(imgshakaib)[0]
# cv2.rectangle(imgshakaib, (facelocshakaib[3], facelocshakaib[0]), (facelocshakaib[1], facelocshakaib[2]), (155, 0, 255), 2)

# results1 = face_recognition.compare_faces([encodehamza], encodehamzanaveed)
# faceDis1 = face_recognition.face_distance([encodehamza], encodehamzanaveed)
# print("hamza and hamzanaveed: ", results1, faceDis1)
# cv2.putText(imgTest, f'{results1} {round(faceDis1[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

# results2 = face_recognition.compare_faces([encodehamza], encodeshakaib)
# faceDis2 = face_recognition.face_distance([encodehamza], encodeshakaib)
# print("hamza and shakaib: ", results2, faceDis)



# import cv2
# import numpy as np
# import face_recognition

# # Load Images
# imghamza = face_recognition.load_image_file('photos/hamza.jpg')
# imghamza = cv2.cvtColor(imghamza, cv2.COLOR_BGR2RGB)
# imghamzanaveed = face_recognition.load_image_file('photos/hamzanaveed.jpg')
# imghamzanaveed= cv2.cvtColor(imghamzanaveed, cv2.COLOR_BGR2RGB)
# imgshakaib = face_recognition.load_image_file('photos/shakaib.jpg')
# imgshakaib = cv2.cvtColor(imgshakaib, cv2.COLOR_BGR2RGB)
# imgmuhammadsameer = face_recognition.load_image_file('photos/muhammadsameer.jpg')
# imgmuhammadsameer = cv2.cvtColor(imgmuhammadsameer, cv2.COLOR_BGR2RGB)
# imgsharoonareeb = face_recognition.load_image_file('photos/sharoonareeb.jpg')
# imgsharoonareeb = cv2.cvtColor(imgsharoonareeb, cv2.COLOR_BGR2RGB)

# #Face locations and encodings
# faceloc = face_recognition.face_locations(imghamza)[0]
# encodehamza = face_recognition.face_encodings(imghamza)[0]
# cv2.rectangle(imghamza, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (155, 0, 255), 2)

# facelochamzanaveed = face_recognition.face_locations(imghamzanaveed)[0]
# encodehamzanaveed = face_recognition.face_encodings(imghamzanaveed)[0]
# cv2.rectangle(imghamzanaveed, (facelochamzanaveed[3], facelochamzanaveed[0]), (facelochamzanaveed[1], facelochamzanaveed[2]), (155, 0, 255), 2)

# facelocshakaib = face_recognition.face_locations(imgshakaib)[0]
# encodeshakaib = face_recognition.face_encodings(imgshakaib)[0]
# cv2.rectangle(imgshakaib, (facelocshakaib[3], facelocshakaib[0]), (facelocshakaib[1], facelocshakaib[2]), (155, 0, 255), 2)

# facelocmuhammadsameer = face_recognition.face_locations(imgmuhammadsameer)[0]
# encodemuhammadsameer = face_recognition.face_encodings(imgmuhammadsameer)[0]
# cv2.rectangle(imgmuhammadsameer, (facelocmuhammadsameer[3], facelocmuhammadsameer[0]), (facelocmuhammadsameer[1], facelocmuhammadsameer[2]), (155, 0, 255), 2)

# facelocsharoonareeb = face_recognition.face_locations(imgsharoonareeb)[0]
# encodesharoonareeb = face_recognition.face_encodings(imgsharoonareeb)[0]
# cv2.rectangle(imgsharoonareeb, (facelocsharoonareeb[3], facelocsharoonareeb[0]), (facelocsharoonareeb[1], facelocsharoonareeb[2]), (155, 0, 255), 2)

# # Compare faces and get the face distance
# results1 = face_recognition.compare_faces([encodehamza], encodehamzanaveed)
# faceDis1 = face_recognition.face_distance([encodehamza], encodehamzanaveed)
# print("hamza and hamzanaveed: ", results1, faceDis1)
# cv2.putText(imghamzanaveed, f'{results1} {round(faceDis1[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

# results2 = face_recognition.compare_faces([encodehamza], encodeshakaib)
# faceDis2 = face_recognition.face_distance([encodehamza], encodeshakaib)
# print("hamza and shakaib: ", results2, faceDis2)
# cv2.putText(imgshakaib, f'{results2} {round(faceDis2[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

# results3 = face_recognition.compare_faces([encodehamza], encodemuhammadsameer)
# faceDis3 = face_recognition.face_distance([encodehamza], encodemuhammadsameer)
# print("hamza and muhammadsameer: ", results3, faceDis3)
# cv2.putText(imgmuhammadsameer, f'{results3} {round(faceDis3[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

# results4 = face_recognition.compare_faces([encodehamza], encodesharoonareeb)
# faceDis4 = face_recognition.face_distance([encodehamza], encodesharoonareeb)
# print("hamza and sharoonareeb: ", results4, faceDis4)
# cv2.putText(imgsharoonareeb, f'{results4} {round(faceDis4[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)



# imgtest = face_recognition.load_image_file('photos/test.jpg')
# imgtest = cv2.cvtColor(imgtest, cv2.COLOR_BGR2RGB)

# # Get face location and encoding for test image
# faceloctest = face_recognition.face_locations(imgtest)[0]
# encodetest = face_recognition.face_encodings(imgtest)[0]
# cv2.rectangle(imgtest, (faceloctest[3], faceloctest[0]), (faceloctest[1], faceloctest[2]), (155, 0, 255), 2)

# # Compare test image against known images
# results2 = face_recognition.compare_faces([encodehamza], encodetest)
# faceDis2 = face_recognition.face_distance([encodehamza], encodetest)
# print("hamza and test image: ", results2, faceDis2)
# cv2.putText(imgtest, f'{results2}...{round(faceDis2[0], 2)}', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# results3 = face_recognition.compare_faces([encodeshakaib], encodetest)
# faceDis3 = face_recognition.face_distance([encodeshakaib], encodetest)
# print("shakaib and test image: ", results3, faceDis3)
# cv2.putText(imgtest, f'{results3}...{round(faceDis3[0], 2)}', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# results4 = face_recognition.compare_faces([encodemuhammadsameer], encodetest)
# faceDis4 = face_recognition.face_distance([encodemuhammadsameer], encodetest)
# print("muhammadsameer and test image: ", results4, faceDis4)
# cv2.putText(imgtest, f'{results4}...{round(faceDis4[0], 2)}', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# results5 = face_recognition.compare_faces([encodesharoonareeb], encodetest)
# faceDis5 = face_recognition.face_distance([encodesharoonareeb], encodetest)
# print("sharoonareeb and test image: ", results5, faceDis5)
# cv2.putText(imgtest, f'{results5}...{round(faceDis5[0], 2)}', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# Display the final images
# cv2.imshow('Hamza', imghamza)
# cv2.imshow('HamzaNaveed', imghamzanaveed)
# cv2.imshow('Shakaib', imgshakaib)
# cv2.imshow('MuhammadSameer',imgmuhammadsameer)
# cv2.imshow('sharoonareeb',imgsharoonareeb)




# import numpy as np
# import face_recognition

# imghamza = face_recognition.load_image_file('photos/hamza.jpg')
# imghamza = cv2.cvtColor(imghamza, cv2.COLOR_BGR2RGB)
# imghamzanaveed = face_recognition.load_image_file('photos/hamzanaveed.jpg')
# imghamzanaveed= cv2.cvtColor(imghamzanaveed, cv2.COLOR_BGR2RGB)
# imghassan = face_recognition.load_image_file('photos/Hassan.jpg')
# imghassan = cv2.cvtColor(imghassan, cv2.COLOR_BGR2RGB)

# faceloc = face_recognition.face_locations(imghamza)[0]
# encodehamza = face_recognition.face_encodings(imghamza)[0]
# cv2.rectangle(imghamza, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (155, 0, 255), 2)

# facelochamzanaveed = face_recognition.face_locations(imghamzanaveed)[0]
# encodehamzanaveed = face_recognition.face_encodings(imghamzanaveed)[1]
# cv2.rectangle(imghamzanaveed, (facelocTest[3], facelocTest[0]), (facelocTest[1], facelocTest[2]), (155, 0, 255), 2)

# facelochassan = face_recognition.face_locations(imghassan)[0]
# encodehassan = face_recognition.face_encodings(imghassan)[0]
# cv2.rectangle(imghassan, (facelochassan[3], facelochassan[0]), (facelochassan[1], facelochassan[2]), (155, 0, 255), 2)

# results1 = face_recognition.compare_faces([encodehamza], encodehamzanaveed)
# faceDis1 = face_recognition.face_distance([encodehamza], encodehamzanaveed)
# print("hamza and hamzanaveed: ", results1, faceDis1)
# cv2.putText(imgTest, f'{results1} {round(faceDis1[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

# results2 = face_recognition.compare_faces([encodehamza], encodehassan)
# faceDis2 = face_recognition.face_distance([encodehamza], encodehassan)
# print("hamza and hassan: ", results2, faceDis)




import face_recognition

# Load all the known images of faces
known_faces = []
known_faces_names = []
for name in os.listdir("photos/"):
    image = face_recognition.load_image_file("photos/" + name)
    encoding = face_recognition.face_encodings(image)[0]
    known_faces.append(encoding)
    known_faces_names.append(name)

# Load an unknown image
unknown_image = face_recognition.load_image_file("unknown.jpg")

# Find all the faces in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Compare the unknown faces to all known faces
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_faces, face_encoding)
    name = "Unknown"

    # If a match was found in known_faces, just use the first one.
    if True in matches:
        first_match_index = matches.index(True)
        name = known_faces_names[first_match_index]

    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

    # Remove the drawing library from memory as per the Pillow docs
    del draw
