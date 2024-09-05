DROP TABLE IF EXISTS especime;

CREATE TABLE especime (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    grupo ENUM ('Fauna', 'Flora') NOT NULL,
    nome_popular VARCHAR(250) NOT NULL,
    nome_cientifico VARCHAR(250) NOT NULL,
    especie VARCHAR(250) NOT NULL,
    genero VARCHAR(250) NOT NULL,
    familia VARCHAR(250) NOT NULL,
    ordem VARCHAR(250) NOT NULL,
    classe VARCHAR(250) NOT NULL,
    filo VARCHAR(250) NOT NULL,
    reino VARCHAR(250) NOT NULL
)