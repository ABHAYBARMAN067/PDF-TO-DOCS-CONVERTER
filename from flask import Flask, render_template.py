from flask import Flask, render_template, request, send_file, flash
from pdf2docx import Converter
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

# Configure upload settings
UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
ALLOWED_EXTENSIONS = {'pdf'}

# Create directories if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        flash('No file selected')
        return render_template('index.html')
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No file selected')
        return render_template('index.html')
    
    if file and allowed_file(file.filename):
        # Secure the filename
        filename = secure_filename(file.filename)
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        docx_path = os.path.join(app.config['CONVERTED_FOLDER'], 
                                os.path.splitext(filename)[0] + '.docx')
        
        # Save the uploaded PDF
        file.save(pdf_path)
        
        try:
            # Convert PDF to DOCX
            cv = Converter(pdf_path)
            cv.convert(docx_path)
            cv.close()
            
            # Clean up PDF file
            os.remove(pdf_path)
            
            # Send the converted file
            return send_file(docx_path, as_attachment=True)
            
        except Exception as e:
            flash(f'Error during conversion: {str(e)}')
            return render_template('index.html')
    else:
        flash('Only PDF files are allowed')
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)