#!/usr/bin/env python

import json
import psycopg2

activity_measures = ["profile_ticks", "actual_ticks", "actual_distance"]
trace_measures = [
    "profile_acc",
    "profile_vel",
    "profile_ticks",
    "actual_vel",
    "actual_ticks",
    "foward",
    "strafe",
    "azimuth",
]

conn = psycopg2.connect(database="jeff", user="jeff")

select_activity_sql = """
SELECT name, timestamp, profile_ticks, actual_ticks, actual_distance, meta, id
FROM motion_activity
WHERE name IN ('Colson on Skippy', 'Magic on Jif')
"""

insert_activity_sql = """
INSERT INTO tc_activity(name, timestamp, activity_measures, data, trace_measures,  meta)
VALUES (%s, %s, %s, %s, %s, %s)
RETURNING id
"""

select_trace_sql = """
SELECT milliseconds, profile_acceleration, profile_velocity, profile_ticks,
       actual_velocity, actual_ticks, forward, strafe, azimuth
FROM motion_activity_data
WHERE motion_activity_id = %s
"""

insert_trace_sql = """
INSERT INTO tc_trace(activity_id, millis, data)
VALUES (%s, %s, %s)
"""

with conn:
    with conn.cursor() as csr:
        csr.execute(select_activity_sql)
        activity_rows = csr.fetchall()

    for a_row in activity_rows:
        activity_id = a_row[6]
        a_data = []
        a_data.append(a_row[2])
        a_data.append(a_row[3])
        a_data.append(a_row[4])

        with conn.cursor() as csr:
            csr.execute(
                insert_activity_sql,
                (
                    a_row[0],
                    a_row[1],
                    activity_measures,
                    a_data,
                    trace_measures,
                    json.dumps(a_row[5]),
                ),
            )
            activity_id = csr.fetchone()[0]

        with conn.cursor() as csr:
            csr.execute(select_trace_sql, (activity_id,))
            trace_rows = csr.fetchall()

        for t_row in trace_rows:
            t_data = list(t_row)
            millis = t_data.pop(0)
            
            with conn.cursor() as csr:
                csr.execute(insert_trace_sql, (activity_id, millis, t_data))

conn.close()
