from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    images = os.listdir('static/images')  # list all files in the static/images directory
    photos = [img for img in images if img.endswith(('.jpg', '.jpeg', '.png'))]  # filter out non-image files
    return render_template('index.html', photos=photos)


@app.route('/photo/<filename>')
def photo(filename):
    return render_template('photo.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)