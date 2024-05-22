-- Unveil the array of TV shows from the vaults of hbtn_0d_tvshows.
-- Revel in the diversity, even as some remain untethered from genres.
-- Sorted gracefully by the ascending titles of TV shows and the mystical genre IDs.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
