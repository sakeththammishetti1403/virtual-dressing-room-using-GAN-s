Virtual Dressing Room using GANs
A real-time AI-based virtual dressing room that allows users to try on clothes virtually using webcam input. Built with Python, OpenCV, and MediaPipe, this project overlays selected clothing on the upper body using pose detection. Ideal for enhancing the online shopping experience and reducing return rates.

🚀 Features
1 Real-Time Webcam Feed
Capture and display live video from your webcam.

2 Pose Detection
Uses MediaPipe to detect upper body keypoints like shoulders, neck, and chest.

3 Virtual Try-On System
Aligns and overlays selected clothes over the user's upper body in real-time.

4 Dynamic Fitting
Automatically adjusts the size and orientation of clothes to match user pose.

5 Optional Flask Web Interface
A simple web UI to upload/select clothes and preview try-on.

Tech Stack
Component	Technology
Programming Language	Python
Computer Vision	OpenCV
Pose Detection	MediaPipe
Image Processing	NumPy, PIL
(Optional) Web Interface	Flask
(Future Scope)	GANs for realistic fitting

virtual-dressing-room/
├── clothes/              # Sample clothes (PNG format with transparent background)
│   ├── tshirt1.png
│   └── tshirt2.png
├── static/               # Web interface static assets (CSS, JS, images)
│   └── style.css
├── templates/            # HTML files for Flask app
│   └── index.html
├── main.py               # Main script: webcam, pose detection, cloth overlay
├── utils.py              # Helper functions
├── app.py                # Flask app to run web interface
├── requirements.txt      # Python dependencies
└── README.md             # GitHub documentation



Future Enhancements
1 Integrate GANs for realistic cloth warping and texture mapping

2 Support for lower body garments

3 Save try-on snapshots and share with friends

4 AR-based virtual trial using depth sensors (e.g., Kinect, iPhone TrueDepth)

