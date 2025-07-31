-- creates the table unique_id
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE,
    name VARCHAR(256) NOT NULL
);