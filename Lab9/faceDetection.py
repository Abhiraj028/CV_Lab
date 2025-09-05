import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video = 'Separate_Video_Cuts_for_Computer_Vision.mp4'  # Change to your video file
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the input image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw a rectangle around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the output image with detected faces
    cv2.imshow('Face Detection', frame)

    # Wait for user input to exit or continue processing
    if cv2.waitKey(1) == ord('q'):
        break

# Release the resources and close the windows
cap.release()
cv2.destroyAllWindows()