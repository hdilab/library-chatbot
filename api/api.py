import flask
from flask import request
from flask_cors import CORS
import psycopg2

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def home():
    return "ok"


@app.route('/feedback', methods=['POST'])
def submit_feedback():
    print(request.json)
    conn = None
    try:
        data = request.json
        conn = psycopg2.connect(host="localhost", database="library", user="postgres", password="postgres")
        cursor = conn.cursor()
        sql_parameterized_query = "insert into feedback (session_id ,smiley, questions) values(%s, %s, %s ) "
        input_values = (data.get("session_id"), data.get("smiley"), data.get("questions"))
        cursor.execute(sql_parameterized_query, input_values)
        conn.commit()
    except Exception as ex:
        print("Exception Occurred", ex)
    finally:
        if conn is not None:
            conn.close()

    return "True"


app.run(host='0.0.0.0')

