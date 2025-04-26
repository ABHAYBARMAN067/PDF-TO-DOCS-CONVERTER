# PDF to DOCX Converter

A simple web application that converts PDF files to DOCX format using Python Flask and pdf2docx library.

## Features

- Upload PDF files through drag & drop or file selection
- Convert PDF files to DOCX format
- Automatic download of converted files
- User-friendly interface with real-time feedback
- Support for files up to 16MB

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pdf-to-doc-converter.git
cd pdf-to-doc-converter
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Upload a PDF file by either:
   - Clicking the upload area and selecting a file
   - Dragging and dropping a file onto the upload area

4. The converted DOCX file will download automatically after conversion

## Project Structure

```
pdf_to_doc_converter/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── uploads/
├── converted/
├── app.py
└── requirements.txt
```

## Dependencies

- Flask==2.0.1
- pdf2docx==0.5.6
- Werkzeug==2.0.1

## Requirements

- Python 3.7 or higher
- Sufficient disk space for temporary file storage
- Modern web browser

## Limitations

- Maximum file size: 16MB
- Only supports PDF to DOCX conversion
- Single file conversion at a time

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request