import os

def setup_workspace():
    # Define the project structure
    directories = [
        'uploads',
        'converted',
        'static',
        'templates'
    ]
    
    files = [
        'uploads/.gitkeep',
        'converted/.gitkeep',
        '.gitignore',
        'requirements.txt',
        'app.py',
        'static/style.css',
        'templates/index.html'
    ]
    
    # Create directories
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    # Create files
    for file in files:
        if not os.path.exists(file):
            with open(file, 'w') as f:
                pass  # Create an empty file

if __name__ == "__main__":
    setup_workspace()