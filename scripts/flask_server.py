from flask import Flask, request
from psycopg2 import connect
from psycopg2.extras import register_hstore
import json

app = Flask(__name__)

activity_sql = """
INSERT INTO motion_activity(name, profile_ticks, actual_ticks, actual_distance, meta)
VALUES (%(name)s,%(profileTicks)s, %(actualTicks)s, %(actualDistance)s, %(meta)s)
RETURNING id
"""

data_sql = """
INSERT INTO motion_activity_data(motion_activity_id, milliseconds,
    profile_acceleration, profile_velocity, profile_ticks,
    actual_ticks, forward, strafe, azimuth)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

db = connect(database="jeff", user="jeff")
register_hstore(db)


@app.route("/load", methods=["POST"])
def load():
    jdoc = request.json
    with db:
        with db.cursor() as csr:
            csr.execute(activity_sql, jdoc)
            activity_id = csr.fetchone()[0]

            for item in jdoc["data"]:
                csr.execute(data_sql, (activity_id,) + tuple(item))

    return "OK - {:d}".format(activity_id)

