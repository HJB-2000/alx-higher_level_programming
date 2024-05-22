-- Dive into the entwined tales of shows and their genres from the rich collection of hbtn_0d_tvshows.
-- Sorted gracefully by ascending show titles and genre names, revealing the harmonious blend of narratives.
SELECT t.`title`, g.`name`
  FROM `tv_shows` AS t
       LEFT JOIN `tv_show_genres` AS s
       ON t.`id` = s.`show_id`

       LEFT JOIN `tv_genres` AS g
       ON s.`genre_id` = g.`id`
 ORDER BY t.`title`, g.`name`;
