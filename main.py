import cv2
import numpy as np
from google.colab.patches import cv2_imshow
image_path = "/content/drive/MyDrive/IMG_1940.jpeg" 
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

_, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

contours, _ = cv2.findContours(clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

coin_info = []

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 2000:
        continue
    perimeter = cv2.arcLength(cnt, True)
    circularity = 4 * np.pi * area / (perimeter ** 2)
    if circularity > 0.8:
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        coin_info.append((x, y, radius, cnt))

ref_coin = max(coin_info, key=lambda c: c[0])  
ref_diameter_px = 2 * ref_coin[2]
ref_diameter_mm = 24.75
pixels_per_mm = ref_diameter_px / ref_diameter_mm

for x, y, radius, cnt in coin_info:
    diameter_px = 2 * radius
    diameter_mm = diameter_px / pixels_per_mm
    center = (int(x), int(y))

    cv2.circle(image, center, int(radius), (0, 255, 0), 3)
    cv2.circle(image, center, 3, (0, 0, 255), -1)
    cv2.putText(image, f"{diameter_mm:.2f} mm", (int(x - radius), int(y + radius + 20)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

cv2.circle(image, (int(ref_coin[0]), int(ref_coin[1])), int(ref_coin[2]), (0, 0, 255), 3)

cv2_imshow(image)
output_path = "/content/drive/My Drive/coin_output_rightmost_ref.jpg"
cv2.imwrite(output_path, image)
print(f"✅ Final image saved to: {output_path}")
