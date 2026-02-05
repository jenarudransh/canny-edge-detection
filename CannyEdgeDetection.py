import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # 2. Convert to Grayscale
    # Canny works on intensity gradients, so grayscale is necessary
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 3. Apply Gaussian Blur
    # This reduces high-frequency noise that can cause "false" edges
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 4. Perform Canny Edge Detection
    # Syntax: cv2.Canny(image, low_threshold, high_threshold)
    # Adjust 100 and 200 to change sensitivity
    edges = cv2.Canny(blurred, 100, 200)
    
    # 5. Display the results
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Edge detect', edges)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()