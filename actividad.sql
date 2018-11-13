CREATE DATABASE blog2;
USE blog2;

CREATE TABLE usuario(
    id int AUTO_INCREMENT,
    nickname VARCHAR(20),
    email VARCHAR(20),
    passwd VARCHAR(100),

    PRIMARY KEY (id),
    UNIQUE (nickname),
    UNIQUE (email)
);
INSERT INTO usuario VALUES(NULL, 'fulvio','correo@correo.cl',SHA2('hola',0));
INSERT INTO usuario VALUES(NULL, 'owo','gmail.com',SHA2('holo',0));

SELECT nickname, email from usuario;
CREATE TABLE comentario(
    id int AUTO_INCREMENT,
    usuario_id_fk int,
    fecha DATE,
    texto TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (usuario_id_fk) REFERENCES usuario(id)
);


INSERT INTO comentario VALUES (NULL, 1, NOW(), 'paso paso paso paso paso');
INSERT INTO comentario VALUES (NULL, 2, NOW(), 'ejemeorkwermwek');



SELECT usuario.nickname, comentario.fecha, comentario.texto, usuario.id
FROM comentario
INNER JOIN usuario ON comentario.usuario_id_fk = usuario.id
WHERE usuario.id = 1
;