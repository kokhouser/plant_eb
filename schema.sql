drop table if exists plants;
drop table if exists admin;

create table plants(
	id integer primary key autoincrement,
	genus varchar,
	commonName varchar,
	latinName varchar,
	longitude real,
	latitude real
);

create table admin(
	id integer primary key autoincrement,
	firstName varchar,
	lastName varchar,
	email varchar,
	password varchar
);