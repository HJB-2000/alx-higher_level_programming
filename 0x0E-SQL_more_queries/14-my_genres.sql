-- Delve into the diverse palette of Dexter's TV world within the hbtn_0d_tvshows database.
-- Sorting the genres alphabetically, revealing the myriad facets of Dexter's narrative.
SELECT g.`name`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS s
       ON g.`id` = s.`genre_id`

       INNER JOIN `tv_shows` AS t
       ON t.`id` = s.`show_id`
       WHERE t.`title` = "Dexter"
 ORDER BY g.`name`;