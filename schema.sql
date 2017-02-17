CREATE TABLE users
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    age INT
);
CREATE UNIQUE INDEX users_id_uindex ON users (id);

INSERT INTO users ( name, age) VALUES ( 'Tom', 13);
INSERT INTO users ( name, age) VALUES ( 'Mary', 12);
INSERT INTO users ( name, age) VALUES ( 'John', 11);
INSERT INTO users ( name, age) VALUES ( 'Ally', 13);