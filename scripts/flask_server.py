from flask import Flask, request
from psycopg2 import connect
import json

app = Flask(__name__)

activity_sql = """
INSERT INTO motion_activity(name, profile_ticks, actual_ticks, actual_distance, meta)
VALUES (%s,%s, %s, %s, %s)
RETURNING id
"""

data_sql = """
INSERT INTO motion_activity_data(motion_activity_id, milliseconds,
    profile_acceleration, profile_velocity, profile_ticks,
    actual_ticks, forward, strafe, azimuth)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

db = connect(database="jeff", user="jeff")


@app.route("/load", methods=["POST"])
def load():
    jdoc = request.json
    with db:
        with db.cursor() as csr:
            csr.execute(
                activity_sql,
                (
                    jdoc["name"],
                    jdoc["profileTicks"],
                    jdoc["actualTicks"],
                    jdoc["actualDistance"],
                    json.dumps(jdoc["meta"]),
                ),
            )
            activity_id = csr.fetchone()[0]

            for item in jdoc["data"]:
                csr.execute(data_sql, (activity_id,) + tuple(item))

    return "OK - {:d}".format(activity_id)

