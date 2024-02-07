import os
import datetime
from flask import Flask, render_template, request, session, send_from_directory
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
app.secret_key = os.urandom(24)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = 'uploaded-images'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_DIR)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def classify_image(model, img_path):
    interpreter = tf.lite.Interpreter(model_path=model)
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    img = image.load_img(img_path, target_size=(300, 300))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])

    interpreter.set_tensor(input_details[0]['index'], images)
    interpreter.invoke()
    classes = interpreter.get_tensor(output_details[0]['index'])

    return classes[0]


@app.route('/')
def upload_file():
    return render_template('index.html', uploaded_image='default-image.png', classification="unclassified")


@app.route('/uploader', methods=['POST'])
def image_upload():
    current_dt = datetime.datetime.now()
    if request.method == 'POST':
        f = request.files['file']
        if f and allowed_file(f.filename):
            session['logged_in'] = True
            filename = f'uploaded_{current_dt.strftime("%Y-%m-%d")}_{current_dt.strftime("%H-%M-%S-%f")}.jpg'
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            f.save(path)
            session['path'] = filename
            return render_template('index.html', uploaded_image=filename, classification="unclassified")
        else:
            return 'Unsupported file type. Try [png, jpg or jpeg] <a href="/">Go back?</a>'


@app.route('/classify', methods=['POST'])
def image_classify():
    if request.method == 'POST':
        from_path = session.get('path')
        if not from_path:
            return 'Invalid request'

        model_path = "model/image-model.tflite"
        classification_threshold = 0.5

        result = classify_image(model_path, os.path.join(app.config['UPLOAD_FOLDER'], from_path))

        if result > classification_threshold:
            return render_template('index.html', uploaded_image=from_path,
                                   classification="uploaded image is of a human")
        else:
            return render_template('index.html', uploaded_image=from_path,
                                   classification="uploaded image is of a horse")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    # Run the Flask application
    app.run(port=5000, debug=True)
