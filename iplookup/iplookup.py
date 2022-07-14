import ipapi
import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def Index():
    search = flask.request.form.get('search')
    data = ipapi.location(ip=search, output='json')
    print(data)
    return flask.render_template('index.html', data=data)
    

# @app.route("/get_my_ip", methods=["GET"])
# def get_my_ip():
#     return flask.jsonify({'ip': flask.request.remote_addr}), 200


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(port=5000)
