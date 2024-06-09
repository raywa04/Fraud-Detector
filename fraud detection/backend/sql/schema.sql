-- Create users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(60) NOT NULL
);

-- Create tweets table
CREATE TABLE tweets (
    id SERIAL PRIMARY KEY,
    user VARCHAR(50) NOT NULL,
    text TEXT NOT NULL,
    sentiment FLOAT NOT NULL
);
