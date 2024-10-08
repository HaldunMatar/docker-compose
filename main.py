
from flask import Flask, Response,request
from flask import Flask, jsonify,send_file
import  databaseMA.connection as conne
import setting
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Flask is running on 172.18.0.3:5005!"


if __name__ == '__main__':
    host_name= setting.get_host_name()
    setting.get_ip_by_name(host_name)

    conne.get_connection()
    app.run(host='0.0.0.0', port=5005)