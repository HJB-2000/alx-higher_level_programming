-- Crafting the hbtn_0d_2 realm and enlisting user_0d_2
-- Bestowing upon user_0d_2 the power to gaze upon the treasures of hbtn_0d_2 with the key 'user_0d_2_pwd'
CREATE DATABASE
    IF NOT EXISTS `hbtn_0d_2`;
CREATE USER
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
   ON `hbtn_0d_2`.*
   TO 'user_0d_2'@'localhost'
   IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;
