CREATE TABLE compositores(
nombre VARCHAR (50),
anonacimiento DATE (4),
epoca VARCHAR (20),
CONSTRAINT PK_compositores PRIMARY KEY (nombre)
);

CREATE TABLE composiciones(
nombrecomposicion VARCHAR (70),
movimientos INT (2),
tipo VARCHAR (20),
grupo VARCHAR (30),
nombreautor VARCHAR (50),
CONSTRAINT PK_composiciones PRIMARY KEY (nombrecomposicion),
CONSTRAINT FK_nombre FOREIGN KEY (nombreautor) REFERENCES compositores (nombre)
);