from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['POST'])
def summarize():
    if (request.method=='POST'):
        print(request.json)
        #print(data)
        return jsonify(request.json)
    else:
        return "Wrong HTTP method", 405

if (__name__=="__main__"):
    # "0.0.0.0:8080"
    app.run(debug=True)