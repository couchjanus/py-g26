create table project(
    name text PRIMARY KEY,
    description text,
    deadline date
);

create table task(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    priority integer default 1,
    detail text,
    status text,
    completed_at date,
    project text not null REFERENCES project(name)
);