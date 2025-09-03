🪙 Coin Measurement and Detection Using OpenCV

This project detects coins in an image, calculates their diameters in millimeters, and visualizes them using OpenCV. The algorithm uses a reference coin for accurate size estimation.

✨ Features

Automatic coin detection using contour detection.

Diameter measurement in millimeters using a reference coin.

Visual annotation: circles for coins, center points, and diameter labels.

Flexible thresholding with Gaussian blur and Otsu's method.

Morphological cleaning to remove noise.

🛠️ How It Works

Load Image
The input image is read from your Google Drive.

Preprocessing

Convert to grayscale

Apply Gaussian blur

Threshold using Otsu’s method

Morphological opening to remove noise

Contour Detection

Find contours of all potential coins

Filter based on area and circularity to isolate actual coins

Reference Coin Selection

The rightmost coin is considered the reference

Real-world diameter is used to calculate pixels-per-mm ratio

Diameter Calculation

For each coin, calculate diameter in pixels

Convert pixels to millimeters using the reference coin

Visualization

Draw circles around detected coins

Mark centers

Annotate each coin with diameter

Save Output
The final annotated image is saved back to Google Drive.

📦 Requirements
pip install opencv-python-headless numpy google-colab

🔧 Usage
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Load and process the image
image_path = "/content/drive/MyDrive/IMG_1940.jpeg"
# Your coin detection and measurement code here


Input your coin image path

Run the script in Google Colab

Check the output image with measured diameters

🖼️ Output

The final image shows:

Green circles around each coin

Red dots marking centers

Blue text showing the diameter in millimeters

Reference coin highlighted in red

✅ Example

Reference Coin: Rightmost coin, 24.75 mm
Other Coins: Measured relative to reference

🔗 Notes

Ensure all coins are fully visible and non-overlapping for accurate measurement.

Adjust area and circularity thresholds depending on coin sizes.

Works best on clear, well-lit images.
