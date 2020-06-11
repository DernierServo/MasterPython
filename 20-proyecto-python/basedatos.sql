CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE usuarios(
    id              INT(25) auto_increment NOT NULL,
    nombre          VARCHAR(100),
    apellidos       VARCHAR(255),
    email           VARCHAR(255) NOT NULL,
    `password`      VARCHAR(255) NOT NULL,
    fecha           DATE NOT NULL,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
) ENGINE=InnoDb;

CREATE TABLE notas(
    id              INT(25) auto_increment NOT NULL,
    usuario_id      INT(25) NOT NULL,
    titulo          VARCHAR(255) NOT NULL,
    descripcion     VARCHAR(255) NOT NULL,
    fecha           DATE NOT NULL,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
) ENGINE=InnoDb;

