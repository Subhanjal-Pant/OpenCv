# Image Thresholding in OpenCV

Image thresholding is a fundamental method of image segmentation. It is the process of converting a grayscale image into a binary image (where pixels are typically either completely black or completely white) or modifying pixel values based on a predefined limit called a **threshold value**. 

In simple terms, we choose a threshold level (e.g., 70 out of 255). Every pixel in the image is then evaluated against this number and altered depending on the specific thresholding rule applied.

---

## Importance and Uses

Thresholding is a critical first step in many Computer Vision pipelines because it simplifies the image data, allowing algorithms to focus on structure rather than shading.

* **Image Segmentation:** Isolating specific objects of interest from their background (e.g., extracting text from a scanned document).
* **Noise Reduction:** Eliminating subtle gradients or background variations by forcing pixels to absolute extremes.
* **Mask Generation:** Creating binary masks used to crop, filter, or overlay specific regions of an image.
* **Pre-processing for OCR/Contour Detection:** Simplifies shape boundaries, making it significantly easier for algorithms to detect edges, find contours, or read text (Optical Character Recognition).

---

## Thresholding Types & Rules

*Note: The following examples assume a threshold value of **70**.*

### 1. `cv.THRESH_BINARY` ('binary')
* **The Rule:** If a pixel is brighter than 70, turn it completely white (255). If it is darker than 70, turn it completely black (0).
* **Result:** A stark, high-contrast black-and-white mask.

### 2. `cv.THRESH_BINARY_INV` ('binaryInv')
* **The Rule:** The exact opposite of binary. If a pixel is brighter than 70, turn it black (0). If it is darker than 70, turn it white (255).
* **Result:** Inverts the black and white areas.

### 3. `cv.THRESH_TOZERO` ('toZero')
* **The Rule:** If a pixel is brighter than 70, leave it completely alone. If it is darker than 70, destroy it by turning it black (0).
* **Result:** Dark backgrounds vanish into pure black, but the bright objects keep their original grayscale details and shading.

### 4. `cv.THRESH_TOZERO_INV` ('toZeroInv')
* **The Rule:** The inverse of toZero. If a pixel is brighter than 70, turn it black (0). If it is darker than 70, leave it completely alone.
* **Result:** Only the darker features of your image remain visible; anything bright is wiped out.

### 5. `cv.THRESH_TRUNC` ('trunc')
* **The Rule:** "Truncate" or chop off the brightness. If a pixel is brighter than 70, forcefully cap its brightness down to exactly 70. If it is darker than 70, leave it completely alone.
* **Result:** The image looks normal in dark areas, but all bright highlights are flattened out into a uniform gray tone.