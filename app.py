from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def upload_form():
    return '''
    <!doctype html>
    <title>Upload File</title>
    <h1>Upload a File</h1>
    <form method="POST" enctype="multipart/form-data" action="/upload">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part in the request"
    
    file = request.files['file']
    if file.filename == '':
        return "No file selected"
    
    # Save the file locally
    file.save(file.filename)
    
    # Check the contents of the file
    with open(file.filename, 'r') as f:
        content = f.read()
    
    return f"File uploaded successfully! Contents:\n{content}"

if __name__ == '__main__':
    app.run(debug=True)