import cv2
import numpy as np
from tkinter import Tk, filedialog

try:
    print("Canny Edge Detection - Image File Mode")
    print("=" * 50)
    
    # Get screen dimensions
    root = Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    
    # Set max display dimensions (leaving some margin)
    max_width = screen_width - 100
    max_height = screen_height - 150
    
    print(f"Screen dimensions: {screen_width}x{screen_height}")
    
    while True:
        # Create a Tkinter root window (hidden)
        root = Tk()
        root.withdraw()
        
        # Open file dialog
        file_path = filedialog.askopenfilename(
            title="Select an image file",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff"), ("All files", "*.*")]
        )
        
        # If user cancels, exit
        if not file_path:
            print("No image selected. Exiting...")
            break
        
        root.destroy()
        
        # Load the image
        img = cv2.imread(file_path)
        
        if img is None:
            print(f"Error: Could not load image from {file_path}")
            continue
        
        print(f"\nImage loaded: {file_path}")
        print(f"Original image size: {img.shape[1]}x{img.shape[0]}")
        
        # Resize image to fit screen
        height, width = img.shape[:2]
        scale = min(max_width / width, max_height / height, 1.0)
        new_width = int(width * scale)
        new_height = int(height * scale)
        
        img_resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
        
        # 2. Convert to Grayscale
        # Canny works on intensity gradients, so grayscale is necessary
        gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
        
        # 3. Apply Gaussian Blur
        # This reduces high-frequency noise that can cause "false" edges
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # 4. Perform Canny Edge Detection
        # Syntax: cv2.Canny(image, low_threshold, high_threshold)
        # Adjust 100 and 200 to change sensitivity
        edges = cv2.Canny(blurred, 100, 200)
        
        # 5. Display the results
        cv2.imshow('Original Image', img_resized)
        cv2.imshow('Edge Detected Image', edges)
        
        print(f"Resized to: {new_width}x{new_height}")
        print("Press any key to select another image, or close windows to exit")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        print("\nSelect another image or close the dialog to exit...")
        
except Exception as e:
    print(f"Error: {e}")
    exit()