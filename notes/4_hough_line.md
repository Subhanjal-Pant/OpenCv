# Hough Line Transform

The Hough Line Transform is a powerful feature extraction technique used in computer vision to detect straight lines within an image, even if those lines are broken, noisy, or slightly interrupted.

---

## 1. What It Is
* **Definition:** A mathematical technique that maps pixels from the standard Image Space (Cartesian coordinates) into a Parameter Space (Hough Space) to detect geometric shapes, most commonly, straight lines.
* **The Core Concept:** It operates on a voting system. Every edge pixel in an image "votes" for all possible lines that could pass through it. The lines that receive the most votes are identified as the actual lines present in the image.
* **Prerequisite:** It does not work on raw images. It requires a binary edge map as an input (typically the output of a **Canny Edge Detector**).

---

## 2. Why Use It
* **Handles Imperfections:** It can successfully identify lines that are faint, fragmented, or partially obscured by noise, making it highly robust compared to simple pixel-tracking methods.
* **Global View:** Instead of looking at local pixel connections, it analyzes the image globally to find structural alignments.
* **Key Applications:**
  * **Autonomous Driving:** Lane detection (identifying the painted lines on a road).
  * **Document Processing:** Deskewing (straightening scanned documents by detecting text lines).
  * **Robotics:** Structural mapping (detecting walls, doors, and building corridors).

---

## 3. How It Works (The Math and the Mapping)

To understand how it works, you have to look at how a line is represented mathematically.

### Step 1: Switching from $y = mx + c$ to Polar Coordinates
* **The Problem:** In the standard slope-intercept form ($y = mx + c$), a vertical line has an infinite slope ($m = \infty$). Computers cannot easily calculate or store infinity.
* **The Solution:** The Hough