from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Manually list the image filenames in the desired order
    photos = ['1.png', 'WA0001.jpg', '2.png', 'WA0002.jpg', '3.png', 'WA0003.jpg', '4.png', 'WA0004.jpg', 
              '5.png', 'WA0005.jpg', '6.png', 'WA0006.jpg', '7.png', 'WA0007.jpg', '8.png', 'WA0008.jpg', 
              '9.png', 'WA0009.jpg', '10.png', 'WA0010.jpg', '11.png', 'WA0011.jpg', '12.png', 'WA0012.jpg', 
              '13.png', 'WA0013.png', 'WA0014.png', 'WA0015.png', 'WA0016.png', 'WA0017.png', 'WA0018.jpg', 
              'WA0019.jpg', 'WA0020.jpg', 'WA0021.jpg', 'WA0022.jpg', 'WA0023.jpg', 'WA0024.jpg', 'WA0025.jpg', 
              'WA0026.jpg', 'WA0027.jpg', 'WA0028.jpg', 'WA0029.jpg', 'WA0030.jpg', 'WA0031.jpg', 'WA0032.jpg', 
              'WA0033.jpg', 'WA0034.jpg', 'WA0035.jpg', 'WA0036.jpg', 'WA0037.jpg', 'WA0038.jpg', 'WA0039.jpg', 
              'WA0040.jpg', 'WA0041.jpg', 'WA0042.jpg', 'WA0043.jpg', 'WA0044.jpg', 'WA0045.jpg', 'WA0046.jpg', 
              'WA0047.jpg', 'WA0048.jpg', 'WA0049.jpg', 'WA0050.jpg', 'WA0051.jpg', 'WA0052.jpg', 'WA0053.png', 
              'WA0054.jpg', 'WA0055.jpg', 'WA0056.jpg', 'WA0057.png']
    return render_template('index.html', photos=photos)

@app.route('/photo/<filename>')
def photo(filename):
    return render_template('photo.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)