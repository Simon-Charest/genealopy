SELECT p.*
FROM persons AS p
WHERE 0 = 0
AND p.last_name IN ('TREMBLAY', 'CHAREST')
AND p.first_name IN  ('DELPHIS', 'RITA', 'CLEMENT')
LIMIT 10000
;
