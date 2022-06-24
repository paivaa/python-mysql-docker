use db;

CREATE TABLE estudantes(
    ID int not null AUTO_INCREMENT,
    Nome varchar(100) NOT NULL,
    Profissao varchar(100) NOT NULL,
    PRIMARY KEY (ID)
);

INSERT INTO estudantes(Nome, Profissao)
VALUES("João Paiva","Programador"), ("Ana Luiza","Assistente");