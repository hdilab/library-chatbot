CREATE TABLE feedback(
   insert_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   id SERIAL PRIMARY KEY,
   session_id VARCHAR (50),
   smiley VARCHAR (50) NOT NULL,
   questions VARCHAR (50)
);