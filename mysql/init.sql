CREATE DATABASE IF NOT EXISTS myapp;

use myapp;

CREATE TABLE IF NOT EXISTS `accounts` (
    id int(11) NOT NULL AUTO_INCREMENT,
    username varchar(50) NOT NULL unique,
    password varchar(255) NULL,
    email varchar(100) NULL,
    chips INT NOT NULL,
    PRIMARY KEY (id)
);

-- CREATE TABLE IF NOT EXISTS 'roulette_spins' (
--     spin_counter int NOT NULL AUTO_INCREMENT,
--     winning_space int NOT NULL,
--     PRIMARY KEY (spin_counter)
-- );