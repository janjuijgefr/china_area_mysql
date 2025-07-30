-- sample-data.enhanced.sql
-- Auto-generated Sen 20 Okt 2025 03:04:22 WIB

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
