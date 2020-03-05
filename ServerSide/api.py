import flask
from flask import request, jsonify
import json
from subprocess import call

app = flask.Flask(__name__)
app.config["DEBUG"] = True
# Create an empty list for our results
results = []
@app.route('/api/image', methods=['GET'])
def api_id():
    #extract arguments from url by get (?id=1)
    #if 'source' in request.args:
     #   img['img-name']=request.args[0]
    pippo=request.args.getlist('source')
    img1=jsonify(request.args)
    s=pippo[0]
    print("------------")
    test=s
    print(test)
    call("python ne.py "+test,shell=True)
    print("--------------")
    return json.load(open("api.json","r"))
app.run()

