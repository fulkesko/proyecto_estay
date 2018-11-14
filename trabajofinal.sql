DROP DATABASE IF EXISTS hospital;
CREATE DATABASE hospital;
USE hospital;

CREATE TABLE cargo(
	id INT AUTO_INCREMENT,
	nombre VARCHAR(30),
	
	PRIMARY KEY(id)
);

INSERT INTO cargo VALUES(NULL, 'Doctor/a');
INSERT INTO cargo VALUES(NULL, 'Enfermera/o');
INSERT INTO cargo VALUES(NULL, 'Psicologo/a');
INSERT INTO cargo VALUES(NULL, 'Pediatra');
INSERT INTO cargo VALUES(NULL, 'Psiquiatra');
INSERT INTO cargo VALUES(NULL, 'Ginecologo/a');

CREATE TABLE prevision(
	id INT AUTO_INCREMENT,
	nombre VARCHAR(40),
	
	PRIMARY KEY(id)
);

INSERT INTO prevision VALUES(NULL, 'Fonasa');
INSERT INTO prevision VALUES(NULL, 'Isapre');

CREATE TABLE trabajador(
	id INT AUTO_INCREMENT,
	nombre VARCHAR(60),
	pass VARCHAR(64),
	telefono VARCHAR(12),
	cargo_id_fk INT,
	
	PRIMARY KEY(id),
	FOREIGN KEY(cargo_id_fk) REFERENCES cargo(id)
);

INSERT INTO trabajador VALUES(NULL, 'Ana', SHA2('hola',0), '12345789', 5);
INSERT INTO trabajador VALUES(NULL, 'Cordero', SHA2('holo',0), '98854712',2);



CREATE TABLE paciente(
	id INT AUTO_INCREMENT,
	nombre VARCHAR(30),
	apellido VARCHAR(30),
	telefono VARCHAR(12),
	prevision_id_fk INT,
	
	PRIMARY KEY(id),
	FOREIGN KEY (prevision_id_fk) REFERENCES prevision(id)
);

INSERT INTO paciente VALUES(NULL,'Flavio','Toro','213546',2);


CREATE TABLE consulta(
	id INT AUTO_INCREMENT,
	paciente_id_fk INT,
	trabajador_id_fk INT,
	observacion TEXT,

	PRIMARY KEY (id),
	FOREIGN KEY (paciente_id_fk) REFERENCES paciente(id),
	FOREIGN KEY (trabajador_id_fk) REFERENCES trabajador(id)

);

INSERT INTO consulta VALUES(NULL,1,2,'Paciente con una grave contuciòn anal ya que lo penetraron salvajemente');

/*consulta para revisar si existe el trabajador*/
--"SELECT COUNT(*) FROM trabajador WHERE nombre = '" +nombre+ "' AND pass = SHA2('" +clave+ "',0)"
