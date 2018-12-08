SELECT meta->'direction' AS direction, count(*)
FROM tc_activity
WHERE timestamp::date = date '2018-09-25' AND data[3] <> 0
GROUP BY meta->'direction';