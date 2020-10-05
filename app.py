from flask import Flask, render_template, request
import ED

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', version=ED.__version__)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/encrypt', methods=['POST'])
def encrypt():
    """
    Encrypt the given input using encryptor
    """
    return render_template('response.html', version=ED.__version__, input=request.form['input'], message="Encrypted",
                           response=ED.encrypt(request.form['input'], False))


@app.route('/decrypt', methods=['POST'])
def decrypt():
    """
    Decrypt the Given cypher using encryptor
    """
    try:
        return render_template('response.html', version=ED.__version__, input=request.form['input'], message="Decrypted",
                               response=ED.decrypt(request.form['input'], False))
    except SyntaxError:
        return render_template('response.html', version=ED.__version__, input=request.form['input'], message="Error",
                               response="Decryption failed, please make sure the encrypted text is correct.")


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
