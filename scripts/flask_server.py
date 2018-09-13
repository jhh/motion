from flask import Flask, request
from psycopg2 import connect
import json

app = Flask(__name__)

activity_sql = """
INSERT INTO tc_activity(name, activity_measures, data, trace_measures,  meta)
VALUES (%s, %s, %s, %s, %s)
RETURNING id
"""

data_sql = """
INSERT INTO tc_trace(activity_id, millis, data)
VALUES (%s, %s, %s)
"""

db = connect(database="jeff", user="jeff")


@app.route("/load", methods=["POST"])
def load():
    jdoc = request.json
    # print(json.dumps(jdoc))
    with db:
        with db.cursor() as csr:
            
                activity_sql,
                (
                    jdoc["name"],
                    jdoc["activityMeasures"],
                    jdoc["activityData"],
                    jdoc["traceMeasures"],
                    json.dumps(jdoc["meta"]),
                ),
            )
            activity_id = csr.fetchone()[0]

            for item in jdoc["traceData"]:
                csr.execute(data_sql, (activity_id, item.pop(0), item))

    return "OK - {:d}".format(activity_id)

