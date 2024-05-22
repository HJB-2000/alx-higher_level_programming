-- Discover all cities in the sunny state of California!
-- Arranging the cities by their IDs in ascending order.
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;

