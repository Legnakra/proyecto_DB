CREATE DATABASE compositores;
CREATE USER 'mj'@'%' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON composiciones.* to 'mj'@'%';
FLUSH PRIVILEGES;
exit
USE compositores


CREATE TABLE compositores(
nombre VARCHAR (50),
anonacimiento DATE,
epoca VARCHAR (20),
CONSTRAINT PK_compositores PRIMARY KEY (nombre)
);

CREATE TABLE composiciones(
nombrecomposicion VARCHAR (70),
movimientos INT (2),
tipo VARCHAR (40),
grupo VARCHAR (40),
nombreautor VARCHAR (50),
CONSTRAINT PK_composiciones PRIMARY KEY (nombrecomposicion),
CONSTRAINT FK_nombre FOREIGN KEY (nombreautor) REFERENCES compositores (nombre)
);



INSERT INTO compositores values ('Mozart', '1756-01-27', 'Clasicismo');
INSERT INTO compositores values ('Haydn','1809-05-31','Clasicismo');
INSERT INTO compositores values ('Chopin','1849-10-17','Romanticismo');
INSERT INTO compositores values ('Bach','1685-03-31','Barroco');
INSERT INTO compositores values ('Vivaldi','1678-03-04','Barroco');
INSERT INTO compositores values ('Handel','1685-02-23','Barroco');
INSERT INTO compositores values ('Monteverdi','1567-05-09','Barroco');
INSERT INTO compositores values ('Beethoven','1770-12-26','Clasicismo');
INSERT INTO compositores values ('Wagner','1813-05-22','Romanticismo');


INSERT INTO composiciones values ('Concierto para violin n3 en Sol M','3','Orquesta sinfonica y solista','Sinfonica con solista','Mozart');
INSERT INTO composiciones values ('Sonata para teclado a cuatro manos','3','Sonata','Duo','Mozart');
INSERT INTO composiciones values ('La flauta magica','2','Opera','Orquesta sinfónica y Vocalistas','Mozart');
INSERT INTO composiciones values ('Concierto para clarinete','2','Concierto solista','Orquesta sinfonica y Vocalista','Mozart');
INSERT INTO composiciones values ('El rapto del serrallo','3','Opera','Orquesta sinfonica y Vocalista','Mozart');


INSERT INTO composiciones values ('La creacion','3','Oratorio','Orquesta sinfonica','Haydn');
INSERT INTO composiciones values ('Los adioses','4','Sinfonia','Orquesta clásica','Haydn');
INSERT INTO composiciones values ('Concierto para Cello en Do M','3','Concierto','Orquesta sinfonica y solista','Haydn');
INSERT INTO composiciones values ('Emperador','4','Cuarteto','Cuarteto de cuerda','Haydn');
INSERT INTO composiciones values ('Sonata en Re Mayor','4','Sonata','Instrumental','Haydn');


INSERT INTO composiciones values ('Nocturnos Opus 9','21','Nocturnos','Instrumental','Chopin');
INSERT INTO composiciones values ('Concierto para piano n2 en Fa M','3','Concierto','Orquesta sinfonica y solista','Chopin');
INSERT INTO composiciones values ('Sonata para Cello en Sol m Opus 65','4','Sonata','Orquesta sinfonica y solista','Chopin');
INSERT INTO composiciones values ('Vals en Reb M Opus 64','1','Vals','Instrumental','Chopin');
INSERT INTO composiciones values ('Polonesa en Lab M Opus 64','1','Instrumental','Instrumental','Chopin');
