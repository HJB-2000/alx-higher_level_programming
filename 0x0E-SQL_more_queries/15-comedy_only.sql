-- Get ready to chuckle with this list of comedy gold from the hbtn_0d_tvshows database!
-- Sorted in reverse alphabetical order by show title, because laughter loves to surprise.
SELECT t.`title`
  FROM `tv_shows` AS t
       INNER JOIN `tv_show_genres` AS s
       ON t.`id` = s.`show_id`

       INNER JOIN `tv_genres` AS g
       ON g.`id` = s.`genre_id`
       WHERE g.`name` = "Comedy"
 ORDER BY t.`title`;
