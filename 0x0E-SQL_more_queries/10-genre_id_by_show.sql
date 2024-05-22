-- Unveil the TV treasures in hbtn_0d_tvshows, adorned with genres!
-- Sorting the records by the ascending titles of TV shows and the allure of genre IDs.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       INNER JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
