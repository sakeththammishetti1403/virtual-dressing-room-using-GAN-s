from flask import Flask, request, jsonify
import torch
import cv2
import numpy as np

app = Flask(__name__)

# Load TryOnGAN model (assuming it's pre-trained and available)
tryongan_model = torch.hub.load('facebookresearch/pytorch_GAN_zoo', 'DCGAN', pretrained=True)

@app.route('/tryon', methods=['POST'])
def virtual_tryon():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image'].read()
    image = np.frombuffer(image, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # Apply TryOnGAN processing (dummy processing here)
    processed_image = tryongan_model(image)  # Assuming TryOnGAN processes the image

    return jsonify({"message": "TryOnGAN Applied Successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
