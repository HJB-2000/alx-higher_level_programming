-- Unveil the urban tapestry of hbtn_0d_usa!
-- Let's journey through the cityscapes, sorted in ascending order by their IDs.
SELECT c.`id`, c.`name`, s.`name` AS `state_name`
  FROM `cities` AS c
       INNER JOIN `states` AS s
       ON c.`state_id` = s.`id`
 ORDER BY c.`id`;
