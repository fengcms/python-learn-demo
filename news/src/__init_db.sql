CREATE TABLE article (
    id integer primary key autoincrement,
    title varchar(255),
    channel_id integer,
    author varchar(255),
    origin varchar(255),
    content text,
    img varchar(255),
    time timestamp default current_timestamp
)
