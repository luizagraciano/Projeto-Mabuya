DROP TABLE IF EXISTS especime;
DROP TABLE IF EXISTS avistamento;

CREATE TABLE especime (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    grupo TEXT NOT NULL,
    nome_popular VARCHAR(250) NOT NULL,
    nome_cientifico VARCHAR(250) NOT NULL,
    especie VARCHAR(250) NOT NULL,
    genero VARCHAR(250) NOT NULL,
    familia VARCHAR(250) NOT NULL,
    ordem VARCHAR(250) NOT NULL,
    classe VARCHAR(250) NOT NULL,
    filo VARCHAR(250) NOT NULL,
    reino VARCHAR(250) NOT NULL,
    descricao VARCHAR(500) NOT NULL
);

CREATE TABLE avistamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome_especie VARCHAR(250) NOT NULL,
    local_avistamento TEXT NOT NULL,
    comentario TEXT NOT NULL,
    FOREIGN KEY (nome_especie) REFERENCES especime(nome_popular)
)