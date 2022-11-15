CREATE DATABASE myapp;

USE myapp;

CREATE TABLE users (
    uname varchar(255) NOT NULL PRIMARY KEY,
    nickname varchar(255)
);

INSERT INTO users (uname, nickname) VALUES ('test', 'test');

