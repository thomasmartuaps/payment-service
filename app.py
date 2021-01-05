from flask import Flask

from flask import (
    json, request, Response
)

app = Flask(__name__)

@app.route('/')
def landing():
    response = Response(
        response=json.dumps({
            "message": "this is the landing page."
        }),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/cart', methods=('GET', 'POST', 'PUT', 'DELETE'))
def cart():
    if request.method == 'GET':
        return Response(
            response=json.dumps({
                "cart": "here"
            }),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'POST':
        usertoken = request.form['usertoken']
        itemid = request.form['itemid']
        itemname = request.form['itemname']
        
        return Response(
            response=json.dumps({
                "message": "added to cart"
                "user": usertoken,
                "item_name": itemname,
                "item_id": itemid
            }),
            status=200,
            mimetype='application/json'
        )
    else:
        return Response(
            response=json.dumps({
                "message": "method not yet supported"
            }),
            status=404,
            mimetype='application/json'
        )