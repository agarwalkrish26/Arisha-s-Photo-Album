from flask import Flask, render_template
import os
import re

app = Flask(__name__)

def sort_key(filename):
    # Extract numeric part of the filename and convert to integer
    numbers = re.findall(r'\d+', filename)
    return int(numbers[0]) if numbers else 0

@app.route('/')
def index():
    image_dir = 'static/images'
    image_files = os.listdir(image_dir)
    # Filter out non-image files and sort using the custom sort key
    photos = sorted(
        [file for file in image_files if file.lower().endswith(('.png', '.jpg', '.jpeg'))],
        key=sort_key
    )
    return render_template('index.html', photos=photos)

@app.route('/photo/<filename>')
def photo(filename):
    return render_template('photo.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
