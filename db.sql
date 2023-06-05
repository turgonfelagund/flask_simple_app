CREATE DATABASE test;

USE test;

CREATE TABLE `usuario` ( `id` INT NOT NULL AUTO_INCREMENT , `nombre` VARCHAR(45) NOT NULL , `edad` INT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB; 

INSERT INTO `usuario` (`id`, `nombre`, `edad`) VALUES (NULL, 'Marcos', '30'), (NULL, 'Ana', '29');