from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated storage for files
files = []

@app.route('/')
def index():
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    filename = request.form.get('filename')
    if filename:
        files.append(filename)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
    new_filename = request.form.get('new_filename')
    if 0 <= index < len(files) and new_filename:
        files[index] = new_filename
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(files):
        files.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)