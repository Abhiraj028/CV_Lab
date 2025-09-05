# Import libraries
import cv2

# File paths
haar_cascade = 'cars.xml'
video = 'Car_Video_Generation.mp4'

# Initialize video capture and cascade classifier
cap = cv2.VideoCapture(video)
car_cascade = cv2.CascadeClassifier(haar_cascade)

# Main loop for processing video frames
while True:
    # Read frames from video
    ret, frames = cap.read()

    # Break loop if video ends
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    # Detect cars of different sizes in the frame
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # Draw rectangle around each detected car
    for (x, y, w, h) in cars:
        cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display frame in window
    cv2.imshow('video', frames)

    # Wait for Esc key to stop (27 is ASCII for Esc)
    if cv2.waitKey(33) == 27:
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()