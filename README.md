CREATE DATABASE myapp;

USE myapp;

CREATE TABLE IF NOT EXISTS `accounts` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
);

INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES (1, 'a', 'a', 'a@a.com');


# Inserts into accounts and lets the PK auto-generate
INSERT INTO accounts VALUES (NULL, 'aa', 'a', 'a');


