from flask import Flask, send_file,request,render_template
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html') #postをtasks.htmlに渡す
    
@app.route("/download", methods=["GET"])
def download_api():
    filepath = "./輸入車部品_問合せ手順.pdf"
    return send_file(filepath, as_attachment=True,
                     )
if __name__ == "__main__":
    app.run(debug=True)