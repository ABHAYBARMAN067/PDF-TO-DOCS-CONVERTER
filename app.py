from flask import Flask, request, send_from_directory, render_template, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename
from pdf2docx import Converter

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Define absolute paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
CONVERTED_FOLDER = os.path.join(BASE_DIR, 'converted')
ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create directories if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))
    
    if file and allowed_file(file.filename):
        try:
            filename = secure_filename(file.filename)
            pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(pdf_path)
            
            docx_filename = filename.rsplit('.', 1)[0] + '.docx'
            docx_path = os.path.join(app.config['CONVERTED_FOLDER'], docx_filename)
            
            # Convert PDF to DOCX
            cv = Converter(pdf_path)
            cv.convert(docx_path)
            cv.close()
            
            # Clean up the uploaded PDF
            os.remove(pdf_path)
            
            return send_from_directory(
                app.config['CONVERTED_FOLDER'],
                docx_filename,
                as_attachment=True
            )
        
        except Exception as e:
            flash(f'Error during conversion: {str(e)}')
            return redirect(url_for('index'))
    
    flash('Invalid file type. Please upload a PDF file.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)