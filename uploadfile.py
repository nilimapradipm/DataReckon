from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return """
        <h1>File Upload</h1>
        <form method="POST" action="" enctype="multipart/form-data">
          <p><input type="file" name="file"></p>
          <p><input type="submit" value="Submit"></p>
        </form>
    """

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))

if __name__ == "__main__":
             app.run(host="127.0.0.1", port=8086, debug=True)