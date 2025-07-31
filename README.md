### **Virtual Shirt Try-On Application**

**Description:**  
This application provides a virtual experience where users can try on different shirts using real-time video captured from a webcam. It detects the user’s pose and hands, overlays shirt images onto the user's body based on shoulder positions, and allows for interaction through hand gestures.

**Key Features:**
- Real-time pose and hand detection using MediaPipe.
- Overlay of shirt images on the user's body.
- Gesture-based controls to switch shirts using virtual buttons.
- Immediate visual feedback through real-time video processing.

**Technologies Used:**
- **OpenCV**: For video capture and image processing.
- **MediaPipe**: For detecting body landmarks and hand gestures.
- **NumPy**: For numerical operations and image processing.
- **OS Module**: To load shirt images and interact with the file system.

**Installation Procedure:**
1. Install required libraries:
   ```bash
   pip install opencv-python mediapipe numpy
   ```
2. Place the script, shirt images, and button images in the same directory.
3. Modify the paths in the script if necessary.

**How to Use:**
1. Run the script with `python main.py`.
2. Stand in front of the webcam, ensuring your upper body is visible.
3. Use hand gestures to press virtual buttons to switch between shirts.
4. Press `Esc` to exit.

**Future Enhancements:**
- Add more clothing items like pants and jackets.
- Improve gesture recognition and add new gesture-based controls.
- Develop a user-friendly GUI and integrate mobile compatibility.
- Connect with e-commerce platforms for a direct try-and-buy experience.

### **Advantages of Virtual Try-On for Online Shopping:**
- **Enhanced Experience**: Allows customers to see how clothes look on them, increasing engagement and satisfaction.
- **Increased Confidence and Reduced Returns**: Better visualization leads to informed purchasing decisions, reducing return rates.
- **Convenience**: Try on clothes from anywhere, anytime, without the need for physical stores.
- **Personalization**: AI can recommend clothes based on body shape and past preferences.
- **Safety and Hygiene**: Eliminates physical contact with garments, ensuring a safer shopping environment.

### **Advantages Over Offline Shopping:**
- **Greater Accessibility**: Shop and try on clothes from any location.
- **Broader Selection**: Access to a wider range of styles and sizes than typically available in physical stores.
- **No Waiting**: Immediate try-on experience without fitting room queues.
- **Social Sharing**: Easily share looks with friends for feedback through social media.

Implementing this virtual try-on application can significantly enhance the online shopping experience, making it more interactive, personalized, and user-friendly compared to traditional offline shopping.
