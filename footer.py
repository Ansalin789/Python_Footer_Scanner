# import sys
# import cv2
# import numpy as np
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
# from PyQt5.QtGui import QImage, QPixmap
# from PyQt5.QtCore import Qt, QTimer

# class FootSizeScannerApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.reference_length_pixels = None
#         self.reference_length_inches = None

#     def initUI(self):
#         self.setWindowTitle("Foot Size Scanner")
#         self.setGeometry(100, 100, 800, 600)

#         self.video_label = QLabel(self)
#         self.video_label.setAlignment(Qt.AlignCenter)

#         self.start_btn = QPushButton("Start Scanning", self)
#         self.start_btn.clicked.connect(self.start_scanning)

#         self.result_label = QLabel(self)
#         self.result_label.setAlignment(Qt.AlignCenter)

#         layout = QVBoxLayout()
#         layout.addWidget(self.video_label)
#         layout.addWidget(self.start_btn)
#         layout.addWidget(self.result_label)

#         central_widget = QWidget(self)
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         self.video_capture = cv2.VideoCapture(0)
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.is_scanning = False

#     def start_scanning(self):
#         if not self.is_scanning:
#             self.is_scanning = True
#             self.start_btn.setText("Stop Scanning")
#             self.timer.start(33)  # 30 FPS (33ms per frame)
#         else:
#             self.is_scanning = False
#             self.start_btn.setText("Start Scanning")
#             self.timer.stop()

#     def update_frame(self):
#         ret, frame = self.video_capture.read()
#         if ret:
#             # Convert the frame to grayscale
#             gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#             # Apply edge detection to find contours
#             edges = cv2.Canny(gray_frame, 50, 150)

#             # Find contours in the edge-detected image
#             contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#             # Find the largest contour (assuming it's the foot)
#             if len(contours) > 0:
#                 foot_contour = max(contours, key=cv2.contourArea)

#                 # Calculate the length of the foot contour in pixels
#                 foot_length_pixels = cv2.arcLength(foot_contour, True)

#                 # If reference length (inches) is known, calculate the foot length in inches and centimeters
#                 if self.reference_length_inches:
#                     pixels_per_inch = foot_length_pixels / self.reference_length_inches
#                     foot_length_inches = foot_length_pixels / pixels_per_inch
#                     foot_length_cm = foot_length_inches * 2.54  # Convert inches to centimeters

#                     # Display the foot length in the result label
#                     self.result_label.setText(f"Foot Length: {foot_length_inches:.2f} inches ({foot_length_cm:.2f} cm)")

#                 else:
#                     # Display a message to prompt the user to calibrate
#                     self.result_label.setText("Please calibrate the system using a reference object.")

#             # Convert OpenCV image to QImage
#             height, width, channel = frame.shape
#             bytes_per_line = 3 * width
#             q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

#             # Display the frame in the QLabel
#             self.video_label.setPixmap(QPixmap.fromImage(q_image))

#     def closeEvent(self, event):
#         self.video_capture.release()
#         super().closeEvent(event)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = FootSizeScannerApp()
#     window.show()
#     sys.exit(app.exec_())


# import cv2
# import numpy as np

# # Real length (in cm or inches) of the reference object
# reference_object_length_cm = (
#     20  # Replace this with the actual length of your reference object in cm
# )
# reference_object_length_inches = (
#     8  # Replace this with the actual length of your reference object in inches
# )

# # Load the image
# image_path = "fot.jpg"
# image = cv2.imread(image_path)

# # Preprocess the image
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# # Detect edges
# edges = cv2.Canny(blurred_image, 50, 150)

# # Find contours
# contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Find the rectangle with the maximum area
# max_area = 0
# max_contour = None
# for contour in contours:
#     area = cv2.contourArea(contour)
#     if area > max_area:
#         max_area = area
#         max_contour = contour

# if max_contour is None:
#     print("No foot size detected.")
#     exit()

# # Draw the rectangle around the detected foot size
# rect = cv2.minAreaRect(max_contour)
# box = cv2.boxPoints(rect)
# box = np.int0(box)
# cv2.drawContours(image, [box], 0, (0, 255, 0), 2)

# # Calculate the foot size length (in cm) based on the reference object
# foot_length_cm = max(rect[1][0], rect[1][1]) / max(rect[1]) * reference_object_length_cm
# print(f"Estimated foot size length in centimeters: {foot_length_cm:.2f} cm")

# # Convert the foot length to inches
# foot_length_inches = foot_length_cm / 2.54
# print(f"Estimated foot size length in inches: {foot_length_inches:.2f} inches")

# # Calculate the foot size width (in cm) based on the reference object
# foot_width_cm = min(rect[1][0], rect[1][1]) / max(rect[1]) * reference_object_length_cm
# print(f"Estimated foot size width in centimeters: {foot_width_cm:.2f} cm")

# # Convert the foot width to inches
# foot_width_inches = foot_width_cm / 2.54
# print(f"Estimated foot size width in inches: {foot_width_inches:.2f} inches")

# # Display the output image
# cv2.imshow("Foot Size Detection", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import sys
# import cv2
# import numpy as np
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
# from PyQt5.QtGui import QImage, QPixmap
# from PyQt5.QtCore import Qt, QTimer

# class FootSizeScannerApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.reference_length_pixels = None
#         self.reference_length_inches = None

#     def initUI(self):
#         self.setWindowTitle("Foot Size Scanner")
#         self.setGeometry(100, 100, 800, 600)

#         self.video_label = QLabel(self)
#         self.video_label.setAlignment(Qt.AlignCenter)

#         self.start_btn = QPushButton("Start Scanning", self)
#         self.start_btn.clicked.connect(self.start_scanning)

#         self.result_label = QLabel(self)
#         self.result_label.setAlignment(Qt.AlignCenter)

#         layout = QVBoxLayout()
#         layout.addWidget(self.video_label)
#         layout.addWidget(self.start_btn)
#         layout.addWidget(self.result_label)

#         central_widget = QWidget(self)
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         self.video_capture = cv2.VideoCapture(0)
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.is_scanning = False

#     def start_scanning(self):
#         if not self.is_scanning:
#             self.is_scanning = True
#             self.start_btn.setText("Stop Scanning")
#             self.timer.start(33)  # 30 FPS (33ms per frame)
#         else:
#             self.is_scanning = False
#             self.start_btn.setText("Start Scanning")
#             self.timer.stop()

#     def update_frame(self):
#         ret, frame = self.video_capture.read()
#         if ret:
#             # Convert the frame to grayscale
#             gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#             # Apply edge detection to find contours
#             edges = cv2.Canny(gray_frame, 50, 150)

#             # Find contours in the edge-detected image
#             contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#             # Find the largest contour (assuming it's the foot)
#             if len(contours) > 0:
#                 foot_contour = max(contours, key=cv2.contourArea)

#                 # Calculate the length of the foot contour in pixels
#                 foot_length_pixels = cv2.arcLength(foot_contour, True)

#                 # If reference length (inches) is known, calculate the foot length in inches and centimeters
#                 if self.reference_length_inches:
#                     pixels_per_inch = foot_length_pixels / self.reference_length_inches
#                     foot_length_inches = foot_length_pixels / pixels_per_inch
#                     foot_length_cm = foot_length_inches * 2.54  # Convert inches to centimeters

#                     # Display the foot length in the result label
#                     self.result_label.setText(f"Foot Length: {foot_length_inches:.2f} inches ({foot_length_cm:.2f} cm)")

#                 else:
#                     # Display a message to prompt the user to calibrate
#                     self.result_label.setText("Please calibrate the system using a reference object.")

#             # Convert OpenCV image to QImage
#             height, width, channel = frame.shape
#             bytes_per_line = 3 * width
#             q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

#             # Display the frame in the QLabel
#             self.video_label.setPixmap(QPixmap.fromImage(q_image))

#     def closeEvent(self, event):
#         self.video_capture.release()
#         super().closeEvent(event)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = FootSizeScannerApp()
#     window.show()
#     sys.exit(app.exec_())


# import sys
# import cv2
# import numpy as np
# from PyQt5.QtWidgets import (
#     QApplication,
#     QMainWindow,
#     QLabel,
#     QPushButton,
#     QVBoxLayout,
#     QWidget,
# )
# from PyQt5.QtGui import QImage, QPixmap
# from PyQt5.QtCore import Qt, QTimer


# class FootSizeScannerApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.reference_length_pixels = None
#         self.reference_length_inches = None

#     def initUI(self):
#         self.setWindowTitle("Foot Size Scanner")
#         self.setGeometry(100, 100, 800, 600)

#         self.video_label = QLabel(self)
#         self.video_label.setAlignment(Qt.AlignCenter)

#         self.start_btn = QPushButton("Start Scanning", self)
#         self.start_btn.clicked.connect(self.start_scanning)

#         self.result_label = QLabel(self)
#         self.result_label.setAlignment(Qt.AlignCenter)

#         layout = QVBoxLayout()
#         layout.addWidget(self.video_label)
#         layout.addWidget(self.start_btn)
#         layout.addWidget(self.result_label)

#         central_widget = QWidget(self)
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         self.video_capture = cv2.VideoCapture(0)
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.is_scanning = False

#     def start_scanning(self):
#         if not self.is_scanning:
#             self.is_scanning = True
#             self.start_btn.setText("Stop Scanning")
#             self.timer.start(33)  # 30 FPS (33ms per frame)
#         else:
#             self.is_scanning = False
#             self.start_btn.setText("Start Scanning")
#             self.timer.stop()

#     def update_frame(self):
#         ret, frame = self.video_capture.read()
#         if ret:
#             # Convert the frame to grayscale
#             gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#             # Apply edge detection to find contours
#             edges = cv2.Canny(gray_frame, 50, 150)

#             # Find contours in the edge-detected image
#             contours, _ = cv2.findContours(
#                 edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
#             )

#             # Find the largest contour (assuming it's the foot)
#             if len(contours) > 0:
#                 foot_contour = max(contours, key=cv2.contourArea)

#                 # Calculate the length of the foot contour in pixels
#                 foot_length_pixels = cv2.arcLength(foot_contour, True)

#                 # If reference length (inches) is known, calculate the foot length in inches and centimeters
#                 if self.reference_length_inches:
#                     pixels_per_inch = foot_length_pixels / self.reference_length_inches
#                     foot_length_inches = foot_length_pixels / pixels_per_inch
#                     foot_length_cm = (
#                         foot_length_inches * 2.54
#                     )  # Convert inches to centimeters

#                     # Display the foot length in the result label
#                     self.result_label.setText(
#                         f"Foot Length: {foot_length_inches:.2f} inches ({foot_length_cm:.2f} cm)"
#                     )

#                 else:
#                     # Display a message to prompt the user to calibrate
#                     self.result_label.setText(
#                         "Please calibrate the system using a reference object."
#                     )

#             # Convert OpenCV image to QImage
#             height, width, channel = frame.shape
#             bytes_per_line = 3 * width
#             q_image = QImage(
#                 frame.data, width, height, bytes_per_line, QImage.Format_RGB888
#             ).rgbSwapped()

#             # Display the frame in the QLabel
#             self.video_label.setPixmap(QPixmap.fromImage(q_image))

#     def closeEvent(self, event):
#         self.video_capture.release()
#         super().closeEvent(event)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = FootSizeScannerApp()
#     window.show()
#     sys.exit(app.exec_())


import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer


class FootSizeScannerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.reference_length_pixels = None
        self.reference_length_inches = None

    def initUI(self):
        self.setWindowTitle("Foot Size Scanner")
        self.setGeometry(100, 100, 800, 600)

        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignCenter)

        self.start_btn = QPushButton("Start Scanning", self)
        self.start_btn.clicked.connect(self.start_scanning)

        self.result_label = QLabel(self)
        self.result_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addWidget(self.start_btn)
        layout.addWidget(self.result_label)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.video_capture = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.is_scanning = False

    def start_scanning(self):
        if not self.is_scanning:
            self.is_scanning = True
            self.start_btn.setText("Stop Scanning")
            self.timer.start(33)  # 30 FPS (33ms per frame)
        else:
            self.is_scanning = False
            self.start_btn.setText("Start Scanning")
            self.timer.stop()

    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            # Convert the frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Apply edge detection to find contours
            edges = cv2.Canny(gray_frame, 50, 150)

            # Find contours in the edge-detected image
            contours, _ = cv2.findContours(
                edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )

            # Filter contours based on area to find the foot contour
            min_area = 2000  # Adjust this threshold based on your camera resolution and foot size
            foot_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

            # Find the largest contour (assuming it's the foot)
            if len(foot_contours) > 0:
                foot_contour = max(foot_contours, key=cv2.contourArea)

                # Calculate the length of the foot contour in pixels
                foot_length_pixels = cv2.arcLength(foot_contour, True)

                # Calculate the bounding rectangle for the contour
                x, y, w, h = cv2.boundingRect(foot_contour)

                # Calculate the width of the foot bounding rectangle in pixels
                foot_width_pixels = w

                # If reference length (inches) is known, calculate the foot length and width in inches and centimeters
                if self.reference_length_inches:
                    pixels_per_inch = foot_length_pixels / self.reference_length_inches
                    foot_length_inches = foot_length_pixels / pixels_per_inch
                    foot_length_cm = (
                        foot_length_inches * 2.54
                    )  # Convert inches to centimeters

                    pixels_per_inch_width = (
                        foot_width_pixels / self.reference_length_inches
                    )
                    foot_width_inches = foot_width_pixels / pixels_per_inch_width
                    foot_width_cm = (
                        foot_width_inches * 2.54
                    )  # Convert inches to centimeters

                    # Display the foot length and width in the result label
                    self.result_label.setText(
                        f"Foot Length: {foot_length_inches:.2f} inches ({foot_length_cm:.2f} cm)\n"
                        f"Foot Width: {foot_width_inches:.2f} inches ({foot_width_cm:.2f} cm)"
                    )

                else:
                    # Display a message to prompt the user to calibrate
                    self.result_label.setText(
                        "Please calibrate the system using a reference object."
                    )

            # Convert OpenCV image to QImage
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_image = QImage(
                frame.data, width, height, bytes_per_line, QImage.Format_RGB888
            ).rgbSwapped()

            # Display the frame in the QLabel
            self.video_label.setPixmap(QPixmap.fromImage(q_image))

    def closeEvent(self, event):
        self.video_capture.release()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FootSizeScannerApp()
    window.show()
    sys.exit(app.exec_())
