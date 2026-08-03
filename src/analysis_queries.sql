SELECT COUNT(*) AS total_users
FROM users;

--Top 10 users with the most logins
SELECT
    user_id,
    COUNT(*) AS total_logins
FROM logon_events
GROUP BY user_id
ORDER BY total_logins DESC
LIMIT 10;

--Top 10 users sending the most emails
SELECT
    user_id,
    COUNT(*) AS emails_sent
FROM email_events
GROUP BY user_id
ORDER BY emails_sent DESC
LIMIT 10;

--Top users accessing the most files
SELECT
    user_id,
    COUNT(*) AS files_accessed
FROM file_events
GROUP BY user_id
ORDER BY files_accessed DESC
LIMIT 10;

--Top users visiting the most websites
SELECT
    user_id,
    COUNT(*) AS websites_visited
FROM http_events
GROUP BY user_id
ORDER BY websites_visited DESC
LIMIT 10;

--USB activity
SELECT
    user_id,
    COUNT(*) AS usb_events
FROM device_events
GROUP BY user_id
ORDER BY usb_events DESC
LIMIT 10;