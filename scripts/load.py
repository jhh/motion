#!/usr/bin/env python

import json
import sys
import psycopg2

with open(sys.argv[1], "r") as src:
    j = json.load(src)

conn = psycopg2.connect(database="jeff", user="jeff")
cursor = conn.cursor()

activity_sql = """
INSERT INTO motion_activity(name, profile_velocity, profile_distance, actual_distance)
VALUES (%s, %s, %s, %s)
RETURNING id
"""

cursor.execute(
    activity_sql,
    (j["name"], j["profileVelocity"], j["profileDistance"], j["actualDistance"]),
)

activity_id = cursor.fetchone()[0]

data_sql = """
INSERT INTO motion_activity_data(motion_activity_id, milliseconds, profile_position,
    profile_velocity, profile_acceleration, actual_position)
VALUES (%s, %s, %s, %s, %s, %s)
"""

for item in j["data"]:
    cursor.execute(data_sql, (activity_id,) + tuple(item))

conn.commit()
conn.close()
