-- Behold the tapestry of TV genres from the vast realm of hbtn_0d_tvshows, each adorned with the count of shows it rules!
-- Genres are showcased only if they reign over at least one show, ascending by the number of shows they command.
SELECT g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS t
       ON g.`id` = t.`genre_id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;
