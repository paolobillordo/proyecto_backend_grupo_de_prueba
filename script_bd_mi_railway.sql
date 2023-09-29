
CREATE DATABASE IF NOT EXISTS railway;
USE railway;
CREATE TABLE IF NOT EXISTS users(
id_user INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
first_name VARCHAR (50) NOT NULL,
last_name VARCHAR (50) NOT NULL,
nick_name  VARCHAR (50) NOT NULL UNIQUE,
email	   VARCHAR (50) NOT NULL UNIQUE,
birth_date DATE,
password   VARCHAR (50) NOT NULL,
image      VARCHAR (50)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS servers(
id_server   INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
name_server VARCHAR (50) NOT NULL UNIQUE,
description VARCHAR (200) NOT NULL,
id_user     INT NOT NULL,
icono       VARCHAR (100)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS use_ser(
id_use_ser INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
id_user INT NOT NULL,
id_server   INT NOT NULL,

CONSTRAINT user_fk FOREIGN KEY (id_user)
REFERENCES users (id_user), -- ON DELETE CASCADE

CONSTRAINT server_fk FOREIGN KEY (id_server)
REFERENCES Servers (id_server) -- ON DELETE CASCADE
)ENGINE=InnoDB;


CREATE TABLE IF NOT EXISTS channels(
id_channel   INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
name_channel VARCHAR (50) NOT NULL ,
description VARCHAR (50) NOT NULL,
id_server   INT NOT NULL,
id_user     INT NOT NULL,
create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
UNIQUE KEY unique_name_server (name_channel, id_server),

CONSTRAINT serverc_fk FOREIGN KEY (id_server)
REFERENCES servers (id_server) -- ON DELETE CASCADE

)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS messages(
id_message   INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
message      TEXT,
id_user		 INT NOT NULL,
id_channel   INT NOT NULL,
create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

CONSTRAINT message_fk FOREIGN KEY (id_user)
REFERENCES users (id_user) -- ON DELETE CASCADE

)ENGINE=InnoDB;

