from flask import Flask, request, jsonify , render_template
from chatbot import generate_response
#from loginHuella import decode_and_verify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

#Cambiar la URL a la que estás accediendo para que coincida con una ruta definida en tu aplicación Flask.
@app.route('/app')
def app_page():
    return 'http://127.0.0.1:5000/app'

# Configura la ruta de los archivos estáticos
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')


@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        input_text = request.json['input']
        response = generate_response(input_text)
        return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)


"""
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part in the request'}), 400

    image_file = request.files['image']

    # If the user does not select a file, the browser submits an empty file without a filename
    if image_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400


    user = decode_and_verify(image_file)

    response = {}

    if user:
        response = {
            'authenticated': True,
            'user': user
        }
    else:
        response = {
            'authenticated': False,
            'user': 'none'
        }

    return jsonify(response), 200"""