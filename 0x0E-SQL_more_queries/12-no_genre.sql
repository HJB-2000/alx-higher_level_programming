-- Reveal the untamed TV gems of hbtn_0d_tvshows, genre-less and bold!
-- Ascending order by the titles of TV shows, where the genre remains a mystery.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
       WHERE g.`genre_id` IS NULL
 ORDER BY s.`title`, g.`genre_id`;

