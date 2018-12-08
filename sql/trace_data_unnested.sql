SELECT t.millis, u.*
FROM tc_activity a, tc_trace t, unnest(a.trace_measures, t.data) AS u(measure, value)
WHERE a.id = t.activity_id AND a.timestamp = (SELECT max(timestamp) FROM tc_activity);