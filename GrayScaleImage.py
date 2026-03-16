import cv2
import matplotlib.pyplot as plt
import os

# Load the image in grayscale
img = cv2.imread("C:\\Users\\Rudransh\\Downloads\\wallpaper.jpg", 0)

# Plot the histogram
plt.hist(img.ravel(), 256, [0, 256])
plt.xlabel("Gray scale pixels")
plt.ylabel("Number of pixels")
plt.title("Histogram of an image")

# Save the plot to the Downloads folder
download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
plt.savefig(os.path.join(download_folder, "grayscale_histogram.png"))

# Display the plot
plt.show()