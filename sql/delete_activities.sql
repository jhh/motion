delete from motion_activity_data where motion_activity_id in (select id from motion_activity where name = 'First Test Run');
delete from motion_activity where name = 'First Test Run';