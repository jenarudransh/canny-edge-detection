import cv2
import matplotlib.pyplot as plt
import os

img = cv2.imread("C:\\Users\\Rudransh\\Downloads\\wallpaper.jpg")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  

colors = ('b', 'g', 'r')

for channel, color in enumerate(colors):
    histogram = cv2.calcHist([img_rgb], [channel], None, [256], [0, 256])
    plt.plot(histogram, color=color)

plt.title('Histogram for each RGB channel')
plt.xlabel('Gray Level')
plt.ylabel('Number of Pixels')

save_plot_path = os.path.join(os.path.expanduser('~'), 'Downloads')
plt.savefig(os.path.join(save_plot_path, "histogram_plot.png"))

print(f"Histogram saved to {os.path.join(save_plot_path, 'histogram_plot.png')}")