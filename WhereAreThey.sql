CREATE TABLE crew
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    x FLOAT,
    y FLOAT,
    info VARCHAR
);
CREATE UNIQUE INDEX crew_id_uindex ON crew (id);

INSERT INTO crew (name, x, y, info) VALUES ('Tom', 121.123, 23.46, "Hello");
INSERT INTO crew (name, x, y, info) VALUES ('Mary', 121.125, 23.43, "Hi");
INSERT INTO crew (name, x, y, info) VALUES ('John', 121.124, 23.47, "ZZZ...");
INSERT INTO crew (name, x, y, info) VALUES ('Ally', 121.122, 23.46, "I am ....");
