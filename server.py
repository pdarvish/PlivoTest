from flask import Flask, request, make_response
import plivo, plivoxml

app = Flask(__name__)

@app.route('/dial/', methods=['GET','POST'])
def dial_id():
    clid = request.values.get('CLID')
    to_number = "2222222222"
    # Set the caller ID using Dial XML
    params = {
        'callerId': clid
    }

    r = plivoxml.Response()
    d = r.addDial(**params)
    d.addNumber(to_number)
    print r.to_xml()
    return Response(str(r), mimetype='text/xml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
