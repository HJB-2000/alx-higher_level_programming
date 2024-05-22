-- Explore the diverse genres absent from the world of Dexter in hbtn_0d_tvshows.
-- Ordered in ascending order by genre name, revealing the unique narratives untouched by Dexter's influence.
SELECT DISTINCT g.`name`
  FROM `tv_genres` AS g
       LEFT JOIN `tv_show_genres` AS s
       ON g.`id` = s.`genre_id`

       LEFT JOIN `tv_shows` AS t
       ON s.`show_id` = t.`id`
       WHERE t.`title` != "Dexter" OR t.`title` IS NULL
 ORDER BY g.`name`;
