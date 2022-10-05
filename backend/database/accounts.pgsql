CREATE TABLE accounts (
    user_id serial PRIMARY KEY,
    email VARCHAR(50) UNIQUE NOT NULL,
    user_pwd bytea UNIQUE NOT NULL,
    salt bytea UNIQUE NOT NULL,
    created_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP,
    login_attempts INTEGER
)

drop table accounts

select * from accounts;