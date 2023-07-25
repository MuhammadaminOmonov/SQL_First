CREATE DATABASE IF NOT EXISTS airports_data;
USE airports_data;

CREATE TABLE IF NOT EXISTS airports(
    id SERIAL,
    airport_name VARCHAR(255) NOT NULL,
    built_date DATE,
    plane_count INTEGER NOT NULL
);

insert into airports (airport_name, built_date, plane_count) values ('Salamanca Airport', '2010-10-13', 80);
insert into airports (airport_name, built_date, plane_count) values ('Cluff Lake Airport', '1956-04-06', 53);
insert into airports (airport_name, built_date, plane_count) values ('Pensacola Regional Airport', '1989-08-02', 77);
insert into airports (airport_name, built_date, plane_count) values ('Interlaken Air Base', '2004-09-29', 55);
insert into airports (airport_name, built_date, plane_count) values ('Westerly State Airport', '1983-06-19', 93);
insert into airports (airport_name, built_date, plane_count) values ('Pdte. Carlos Ibañez del Campo Airport', '2005-11-25', 70);
insert into airports (airport_name, built_date, plane_count) values ('Sandstone Airport', '1961-03-30', 74);
insert into airports (airport_name, built_date, plane_count) values ('Markovo Airport', '1982-01-10', 51);
insert into airports (airport_name, built_date, plane_count) values ('Moshi Airport', '1983-08-08', 55);
insert into airports (airport_name, built_date, plane_count) values ('Athens Ben Epps Airport', '1983-08-20', 46);
insert into airports (airport_name, built_date, plane_count) values ('Hat Yai International Airport', '2010-09-01', 91);
insert into airports (airport_name, built_date, plane_count) values ('Tydeo Larre Borges Airport', '1992-03-05', 99);
insert into airports (airport_name, built_date, plane_count) values ('Goondiwindi Airport', '1960-10-28', 88);
insert into airports (airport_name, built_date, plane_count) values ('Cattle Creek Airport', '1971-02-07', 91);
insert into airports (airport_name, built_date, plane_count) values ('Los Alamos Airport', '1956-08-18', 23);
insert into airports (airport_name, built_date, plane_count) values ('Meekatharra Airport', '2002-06-01', 62);
insert into airports (airport_name, built_date, plane_count) values ('Chernivtsi International Airport', '1984-01-01', 90);
insert into airports (airport_name, built_date, plane_count) values ('Yas Island Seaplane Base', '1983-08-07', 29);
insert into airports (airport_name, built_date, plane_count) values ('RAF Kinloss', '1963-09-29', 65);
insert into airports (airport_name, built_date, plane_count) values ('Atlas Brasil Cantanhede Airport', '1991-03-09', 20);
insert into airports (airport_name, built_date, plane_count) values ('Qeshm International Airport', '1979-10-18', 65);
insert into airports (airport_name, built_date, plane_count) values ('Karimui Airport', '1993-06-16', 70);
insert into airports (airport_name, built_date, plane_count) values ('Lingling Airport', '1988-08-17', 21);
insert into airports (airport_name, built_date, plane_count) values ('Igaliku Heliport', '1964-03-27', 24);
insert into airports (airport_name, built_date, plane_count) values ('Salinas Municipal Airport', '1996-04-21', 41);
insert into airports (airport_name, built_date, plane_count) values ('Sumter Airport', '1980-05-02', 27);
insert into airports (airport_name, built_date, plane_count) values ('Santa Barbara Municipal Airport', '2002-09-11', 81);
insert into airports (airport_name, built_date, plane_count) values ('Salina Municipal Airport', '1987-10-07', 49);
insert into airports (airport_name, built_date, plane_count) values ('Botucatu - Tancredo de Almeida Neves Airport', '1971-03-21', 89);
insert into airports (airport_name, built_date, plane_count) values ('Uriman Airport', '1993-10-01', 36);
insert into airports (airport_name, built_date, plane_count) values ('Vichadero Airport', '2001-09-20', 34);
insert into airports (airport_name, built_date, plane_count) values ('Wake Island Airfield', '1988-04-03', 47);
insert into airports (airport_name, built_date, plane_count) values ('Leshukonskoye Airport', '1996-05-02', 35);
insert into airports (airport_name, built_date, plane_count) values ('Jérémie Airport', '1977-01-31', 53);
insert into airports (airport_name, built_date, plane_count) values ('Kenieba Airport', '1974-12-30', 74);
insert into airports (airport_name, built_date, plane_count) values ('Tweed New Haven Airport', '1971-03-28', 28);
insert into airports (airport_name, built_date, plane_count) values ('Chernivtsi International Airport', '2001-03-07', 53);
insert into airports (airport_name, built_date, plane_count) values ('Hiroshimanishi Airport', '2009-04-07', 90);
insert into airports (airport_name, built_date, plane_count) values ('Sawan Airport', '1973-08-31', 49);
insert into airports (airport_name, built_date, plane_count) values ('Gambell Airport', '1981-04-23', 78);
insert into airports (airport_name, built_date, plane_count) values ('Juanda International Airport', '2001-04-04', 25);
insert into airports (airport_name, built_date, plane_count) values ('Cairns AAF (Fort Rucker) Air Field', '1987-09-01', 58);
insert into airports (airport_name, built_date, plane_count) values ('Sable Island Landing Strip', '1971-06-04', 66);
insert into airports (airport_name, built_date, plane_count) values ('Nesson Airport', '2008-04-17', 25);
insert into airports (airport_name, built_date, plane_count) values ('Rendani Airport', '1998-09-12', 83);
insert into airports (airport_name, built_date, plane_count) values ('Tabuk Airport', '1979-02-07', 58);
insert into airports (airport_name, built_date, plane_count) values ('Nyurba Airport', '1991-05-25', 66);
insert into airports (airport_name, built_date, plane_count) values ('Roben Hood Airport', '2004-01-07', 37);
insert into airports (airport_name, built_date, plane_count) values ('Debre Tabor Airport', '2006-07-31', 76);
insert into airports (airport_name, built_date, plane_count) values ('Hanimaadhoo Airport', '2008-09-20', 63);
insert into airports (airport_name, built_date, plane_count) values ('Cataratas International Airport', '1959-09-02', 87);
insert into airports (airport_name, built_date, plane_count) values ('Glasgow Prestwick Airport', '2004-06-03', 71);
insert into airports (airport_name, built_date, plane_count) values ('Homer Airport', '1980-01-25', 56);
insert into airports (airport_name, built_date, plane_count) values ('Košice Airport', '1960-06-16', 30);
insert into airports (airport_name, built_date, plane_count) values ('Ormara Airport', '1989-09-21', 30);
insert into airports (airport_name, built_date, plane_count) values ('Vila Real Airport', '2001-09-29', 59);
insert into airports (airport_name, built_date, plane_count) values ('Yola Airport', '1992-12-28', 40);
insert into airports (airport_name, built_date, plane_count) values ('Zabreh Ostrava Airport', '1989-11-10', 99);
insert into airports (airport_name, built_date, plane_count) values ('Fazenda Cataco Airport', '1985-08-06', 98);
insert into airports (airport_name, built_date, plane_count) values ('Sidney Municipal Airport', '1989-01-04', 66);
insert into airports (airport_name, built_date, plane_count) values ('Goundam Airport', '1968-06-10', 42);
insert into airports (airport_name, built_date, plane_count) values ('Chennai International Airport', '1988-04-17', 74);
insert into airports (airport_name, built_date, plane_count) values ('Oxnard Airport', '1963-05-14', 67);
insert into airports (airport_name, built_date, plane_count) values ('Diyawanna Oya Seaplane Base', '1986-10-23', 65);
insert into airports (airport_name, built_date, plane_count) values ('Arrabury Airport', '1993-01-26', 49);
insert into airports (airport_name, built_date, plane_count) values ('Menorca Airport', '1965-02-11', 43);
insert into airports (airport_name, built_date, plane_count) values ('Dr Juan Plate Airport', '1978-02-07', 59);
insert into airports (airport_name, built_date, plane_count) values ('New Ishigaki Airport', '1994-04-04', 54);
insert into airports (airport_name, built_date, plane_count) values ('Stroudsburg Pocono Airport', '1972-11-06', 51);
insert into airports (airport_name, built_date, plane_count) values ('Amman-Marka International Airport', '1970-11-21', 40);
insert into airports (airport_name, built_date, plane_count) values ('Taliabu Island Airport', '1992-07-05', 27);
insert into airports (airport_name, built_date, plane_count) values ('Hana Airport', '1966-09-27', 51);
insert into airports (airport_name, built_date, plane_count) values ('La Cumbre Airport', '1984-03-06', 38);
insert into airports (airport_name, built_date, plane_count) values ('General Manuel Carlos Piar International Airport', '1983-09-26', 24);
insert into airports (airport_name, built_date, plane_count) values ('Paradise River Airport', '1968-01-06', 21);
insert into airports (airport_name, built_date, plane_count) values ('Aratika Nord Airport', '1974-11-06', 48);
insert into airports (airport_name, built_date, plane_count) values ('Komatsu Airport', '1965-04-22', 39);
insert into airports (airport_name, built_date, plane_count) values ('Balmaceda Airport', '2005-09-21', 24);
insert into airports (airport_name, built_date, plane_count) values ('El Nido Airport', '2001-05-13', 71);
insert into airports (airport_name, built_date, plane_count) values ('Albert Whitted Airport', '1968-06-03', 20);
insert into airports (airport_name, built_date, plane_count) values ('Allegheny County Airport', '1963-05-26', 64);
insert into airports (airport_name, built_date, plane_count) values ('Silvio Pettirossi International Airport', '1972-07-11', 93);
insert into airports (airport_name, built_date, plane_count) values ('Creech Air Force Base', '2007-05-29', 100);
insert into airports (airport_name, built_date, plane_count) values ('Port St Johns Airport', '1990-01-11', 96);
insert into airports (airport_name, built_date, plane_count) values ('Cataratas Del Iguazú International Airport', '1967-08-29', 53);
insert into airports (airport_name, built_date, plane_count) values ('Igloolik Airport', '1990-09-16', 90);
insert into airports (airport_name, built_date, plane_count) values ('Puerto La Victoria Airport', '1996-02-18', 67);
insert into airports (airport_name, built_date, plane_count) values ('Ewo Airport', '1972-03-09', 51);
insert into airports (airport_name, built_date, plane_count) values ('Wana Airport', '2007-06-28', 87);
insert into airports (airport_name, built_date, plane_count) values ('Nieuw Nickerie Airport', '1978-06-16', 48);
insert into airports (airport_name, built_date, plane_count) values ('Havadarya Airport', '1970-02-23', 66);
insert into airports (airport_name, built_date, plane_count) values ('Tweed New Haven Airport', '1979-12-15', 27);
insert into airports (airport_name, built_date, plane_count) values ('Lifou Airport', '2006-01-09', 66);
insert into airports (airport_name, built_date, plane_count) values ('Atauro Airport', '2002-12-25', 32);
insert into airports (airport_name, built_date, plane_count) values ('Webster City Municipal Airport', '1969-05-13', 61);
insert into airports (airport_name, built_date, plane_count) values ('Bahir Dar Airport', '1956-10-29', 88);
insert into airports (airport_name, built_date, plane_count) values ('Chetwynd Airport', '1964-02-07', 76);
insert into airports (airport_name, built_date, plane_count) values ('Josephstaal Airport', '1966-04-17', 94);
insert into airports (airport_name, built_date, plane_count) values ('Aratika Nord Airport', '2006-08-24', 40);
insert into airports (airport_name, built_date, plane_count) values ('Saidu Sharif Airport', '1956-03-15', 26);

-- 1 --
SELECT * FROM airports WHERE airport_name LIKE "a%";

-- 2 --
SELECT * FROM airports WHERE built_date < '2003-07-25';

-- 3 --
SELECT COUNT(plane_count) AS "Planes" FROM airports WHERE plane_count < 50;

-- 4 --
SELECT airport_name FROM airports ORDER BY built_date ASC LIMIT 1;

-- 5 --
SELECT airport_name FROM airports ORDER BY built_date DESC LIMIT 1;

-- 6 --
SELECT * FROM airports ORDER BY plane_count DESC LIMIT 1;

DROP DATABASE IF EXISTS airports;

\! cls
