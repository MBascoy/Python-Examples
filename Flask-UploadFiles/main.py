from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uploads.db'
db = SQLAlchemy(app)

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    filename = db.Column(db.String(100))

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    name = request.form.get('name', '')

    if file:
        filename = os.path.join('uploads', file.filename)
        file.save(filename)

        new_upload = Upload(name=name, filename=filename)
        db.session.add(new_upload)
        db.session.commit()

        return jsonify({'message': 'File uploaded successfully'}), 200

@app.route('/uploads/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory('uploads', filename)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    with app.app_context():
        db.create_all()

    app.run(debug=True)
