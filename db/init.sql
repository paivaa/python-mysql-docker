CREATE DATABASE pessoas;
use pessoas;

CREATE TABLE cor_favorita (
  nome VARCHAR(20),
  cor VARCHAR(10)
);

INSERT INTO cor_favorita
  (nome, cor)
VALUES
  ('joao', 'vermelho'),
  ('elma', 'azul');