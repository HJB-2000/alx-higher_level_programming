-- Behold the TV treasures of hbtn_0d_tvshows_rate, ranked by their ratings!
-- Ordered in descending order of their collective ratings, offering a glimpse into the highest peaks of television excellence.
SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS t
       INNER JOIN `tv_show_ratings` AS r
       ON t.`id` = r.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
