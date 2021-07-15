from flask import Flask, request, jsonify
from model.summarizer import summarize
app = Flask(__name__)

@app.route('/', methods=['POST'])
def summarize():
    if (request.method=='POST'):
        print(request.json["selected"])
        summary=summarize(request.json["selected"])
        #print(data)
        return jsonify({"summary": summary})
    else:
        return "Wrong HTTP method", 405

if (__name__=="__main__"):
    app.run(debug=True)