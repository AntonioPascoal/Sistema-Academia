CREATE TABLE public.tb_instrutores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    sobrenome VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    endereco TEXT,
    telefone VARCHAR(255) NOT NULL
);

CREATE TABLE public.tb_planos (
    id SERIAL PRIMARY KEY,
    plano VARCHAR(255) NOT NULL
);

CREATE TABLE public.tb_membros (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    sobrenome VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    endereco TEXT,
    telefone VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    tipo_plano INTEGER REFERENCES TB_PLANOS(id),
    data_inicio DATE NOT NULL,
    ativo BOOLEAN NOT NULL
);

CREATE TABLE public.tb_atividades (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    instrutor INTEGER REFERENCES TB_INSTRUTORES(id) ON DELETE CASCADE,
    data TIMESTAMP NOT NULL,
    duracao INT NOT NULL,
    capacidade INT NOT NULL,
    tipo_plano INT REFERENCES TB_PLANOS(id),
    ativo BOOLEAN NOT NULL
);

CREATE TABLE public.tb_agendamentos (
    id SERIAL PRIMARY KEY,
    atividade INTEGER REFERENCES TB_ATIVIDADES(id) ON DELETE CASCADE,
    membro INTEGER REFERENCES TB_MEMBROS(id) ON DELETE CASCADE
);


