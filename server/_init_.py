from flask import Flask

app = Flask(__name__)

UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
# SUBSCRIPTION = "2cacc70852ff4ad08d839c35d309670e"
SUBSCRIPTION = "015975ded8144a4c9e3f92cc9996458a"
# ENDPOINT_AZURE = "https://vytecnastudenstkapomuckaocr.cognitiveservices.azure.com/"
ENDPOINT_AZURE = "https://cloudproject-ocr.cognitiveservices.azure.com/"
# ENDPOINT_SUMMARIZE = "http://localhost:7071/api/summarizeEn/"
ENDPOINT_SUMMARIZE = "https://exampleflaskfunction.azurewebsites.net/api/summarizeEn"
# ENDPOINT_TRANSLATE = "http://localhost:7071/api/translateEnSk/"
ENDPOINT_TRANSLATE = "https://exampleflaskfunction.azurewebsites.net/api/translateEnSk"

@app.route("/docs")
def index():
  return render_template("index.html")

@app.route("/docs/<int:doc_id>")
def index():
  return render_template("index.html")

# @app.route("/translate_nav")
# def translate_nav():
#   return render_template("land_translate.html")  

# @app.route("/summarize_nav")
# def summarize_nav():
#   return render_template("land_summarize.html")

# @app.route("/text_from_image_nav")
# def text_from_image_nav():
#   return render_template("land_image_to_text.html")

# @app.route('/translate', methods = ['GET', 'POST'])
# def translate():
#   en_text = request.args.get('text')
#   print(f'[+] Text {en_text}')
#   response = requests.get(f'{ENDPOINT_TRANSLATE}?text={en_text}')
#   sk_text = response.json()['translations']
#   return render_template("translate.html", translate_text=sk_text, original_text=en_text)

# @app.route('/summarize', methods = ['GET', 'POST'])
# def summarize():
#   en_text = request.args.get('text')
#   print(f'[+] Text {en_text}')
#   response = requests.get(f'{ENDPOINT_SUMMARIZE}?text={en_text}')
#   sk_text = response.json()['output']
#   return render_template("summarize.html", summarize_text=sk_text, original_text=en_text)

# @app.route('/text_from_image', methods = ['GET', 'POST'])
# def ocr():
#   if request.method == 'POST':
#     f = request.files['file']

#     filename = secure_filename(f.filename)
#     filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     f.save(filepath)
    
#     computervision_client = ComputerVisionClient(ENDPOINT_AZURE, CognitiveServicesCredentials(SUBSCRIPTION))

#     with open(filepath, "rb") as local_image_printed_text:
#         response = computervision_client.read_in_stream(local_image_printed_text, raw=True)
        
#     read_operation_location = response.headers["Operation-Location"]
#     operation_id = read_operation_location.split("/")[-1]

#     while True:
#         read_result = computervision_client.get_read_result(operation_id)
#         if read_result.status not in ['notStarted', 'running']:
#             break
#         time.sleep(1)

#     text = ''
#     if read_result.status == OperationStatusCodes.succeeded:
#         for text_result in read_result.analyze_result.read_results:
#             for line in text_result.lines:
#                 text += line.text + '\n'

#     return render_template("image_to_text.html", displaytext=text, fname=filename)


if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0', port=666)
  # app.run()