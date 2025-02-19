"" 
from flask import Flask, request, jsonify
import torch
import cv2
import numpy as np
from tryongan import TryOnGAN  # Ensure TryOnGAN is implemented

app = Flask(__name__)

# Load TryOnGAN model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
gan_model = TryOnGAN().to(device)

@app.route('/tryon', methods=['POST'])
def virtual_tryon():
    user_image = request.files['user_image']
    outfit_image = request.files['outfit_image']

    # Read images
    user_img = cv2.imdecode(np.frombuffer(user_image.read(), np.uint8), cv2.IMREAD_COLOR)
    outfit_img = cv2.imdecode(np.frombuffer(outfit_image.read(), np.uint8), cv2.IMREAD_COLOR)

    # Generate Try-On Output
    tryon_img = gan_model.generate(user_img, outfit_img)

    # Save & return result
    result_path = "static/output.jpg"
    cv2.imwrite(result_path, tryon_img)

    return jsonify({"status": "success", "output_url": result_path})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
