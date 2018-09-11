-- find rows with no tags key
SELECT meta FROM motion_activity WHERE NOT meta @> '{"tags": []}';

-- find rows with tag
SELECT meta FROM motion_activity WHERE meta @> '{"tags": ["default"]}';

-- test jsonb_set function
SELECT jsonb_set('{"tags": ["default"]}'::jsonb, '{tags}', '[]');

-- replace "default" tag with empty array, create missing
UPDATE motion_activity
SET meta = jsonb_set(meta, '{tags}', '[]')
WHERE meta @> '{"tags": ["default"]}';

update motion_activity
set meta = jsonb_insert(meta, '{tags}', '["default"]')
where not meta @> '{"tags": []}';

update motion_activity
set meta = meta - 'tags'
where not meta @> '{"tags": []}';