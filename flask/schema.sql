CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin BOOLEAN
);

CREATE TABLE spas(
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,  
    spa_id INTEGER REFERENCES spas,
    stars INTEGER,
    comment TEXT
);

CREATE TABLE locations (
  id SERIAL PRIMARY KEY,
  spa_id INTEGER REFERENCES spas,
  address TEXT,
  city TEXT
);

CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  name TEXT,
  spa_id INTEGER REFERENCES spas
);
