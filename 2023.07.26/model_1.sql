CREATE DATABASE IF NOT EXISTS users_data;
USE users_data;

CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    gender VARCHAR(20)
);

insert into users (id, first_name, last_name, email, gender) values (1, 'Dame', 'Rubinsohn', 'drubinsohn0@mac.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (2, 'Carlita', 'Mayne', 'cmayne1@github.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (3, 'Libbey', 'Knapp', 'lknapp2@timesonline.co.uk', 'Female');
insert into users (id, first_name, last_name, email, gender) values (4, 'Margarette', 'Norley', 'mnorley3@last.fm', 'Female');
insert into users (id, first_name, last_name, email, gender) values (5, 'Sheela', 'Cobello', 'scobello4@aol.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (6, 'Rosette', 'Jewers', 'rjewers5@comcast.net', 'Female');
insert into users (id, first_name, last_name, email, gender) values (7, 'Ofelia', 'Southcoat', 'osouthcoat6@bloglines.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (8, 'Neda', 'Toft', 'ntoft7@list-manage.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (9, 'Umberto', 'Aireton', 'uaireton8@bloglines.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (10, 'Saba', 'Levane', 'slevane9@vkontakte.ru', 'Female');
insert into users (id, first_name, last_name, email, gender) values (11, 'Vicky', 'Aronowicz', 'varonowicza@fda.gov', 'Female');
insert into users (id, first_name, last_name, email, gender) values (12, 'Vaughan', 'Pyford', 'vpyfordb@umn.edu', 'Male');
insert into users (id, first_name, last_name, email, gender) values (13, 'Sherm', 'Willison', 'swillisonc@bbb.org', 'Male');
insert into users (id, first_name, last_name, email, gender) values (14, 'Candie', 'Pickerin', 'cpickerind@mapy.cz', 'Polygender');
insert into users (id, first_name, last_name, email, gender) values (15, 'Lilia', 'Edgley', 'ledgleye@youtu.be', 'Female');
insert into users (id, first_name, last_name, email, gender) values (16, 'Trevar', 'Lafay', 'tlafayf@ning.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (17, 'Sherill', 'Delaprelle', 'sdelaprelleg@google.de', 'Female');
insert into users (id, first_name, last_name, email, gender) values (18, 'Kirbee', 'Kun', 'kkunh@tamu.edu', 'Female');
insert into users (id, first_name, last_name, email, gender) values (19, 'Gert', 'Adanet', 'gadaneti@unc.edu', 'Female');
insert into users (id, first_name, last_name, email, gender) values (20, 'Lynelle', 'Driussi', 'ldriussij@ox.ac.uk', 'Female');
insert into users (id, first_name, last_name, email, gender) values (21, 'Bar', 'Deniset', 'bdenisetk@techcrunch.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (22, 'Kipper', 'Caldecott', 'kcaldecottl@weather.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (23, 'Ardys', 'Bythell', 'abythellm@a8.net', 'Polygender');
insert into users (id, first_name, last_name, email, gender) values (24, 'Janna', 'Heinemann', 'jheinemannn@elegantthemes.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (25, 'Ariel', 'O''Grogane', 'aogroganeo@alibaba.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (26, 'Abdul', 'Kaufman', 'akaufmanp@umn.edu', 'Male');
insert into users (id, first_name, last_name, email, gender) values (27, 'Hedda', 'Cantos', 'hcantosq@linkedin.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (28, 'Mina', 'Touzey', 'mtouzeyr@purevolume.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (29, 'Russell', 'Stanlock', 'rstanlocks@intel.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (30, 'Raviv', 'Tye', 'rtyet@apple.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (31, 'Emelia', 'Campa', 'ecampau@google.it', 'Female');
insert into users (id, first_name, last_name, email, gender) values (32, 'Alessandro', 'Haucke', 'ahauckev@oakley.com', 'Non-binary');
insert into users (id, first_name, last_name, email, gender) values (33, 'Cameron', 'Skill', 'cskillw@diigo.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (34, 'Raye', 'Gratrex', 'rgratrexx@europa.eu', 'Female');
insert into users (id, first_name, last_name, email, gender) values (35, 'Dorelle', 'Rajchert', 'drajcherty@wikipedia.org', 'Female');
insert into users (id, first_name, last_name, email, gender) values (36, 'Brandise', 'Riepel', 'briepelz@dagondesign.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (37, 'Dehlia', 'Lebbern', 'dlebbern10@reference.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (38, 'Lisetta', 'Fraanchyonok', 'lfraanchyonok11@ibm.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (39, 'Sloan', 'Wherrit', 'swherrit12@amazon.com', 'Genderqueer');
insert into users (id, first_name, last_name, email, gender) values (40, 'Durward', 'Slafford', 'dslafford13@blogspot.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (41, 'Teri', 'Rotherforth', 'trotherforth14@blogs.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (42, 'Rowen', 'Camock', 'rcamock15@nationalgeographic.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (43, 'Meredithe', 'Barszczewski', 'mbarszczewski16@artisteer.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (44, 'Dorelia', 'Chevolleau', 'dchevolleau17@nasa.gov', 'Female');
insert into users (id, first_name, last_name, email, gender) values (45, 'Allistir', 'Beavan', 'abeavan18@nytimes.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (46, 'Corissa', 'Walework', 'cwalework19@biblegateway.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (47, 'Hulda', 'McGeady', 'hmcgeady1a@moonfruit.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (48, 'Ryon', 'Labrom', 'rlabrom1b@theglobeandmail.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (49, 'Clemence', 'Blandamore', 'cblandamore1c@goo.ne.jp', 'Female');
insert into users (id, first_name, last_name, email, gender) values (50, 'Chris', 'Kinglake', 'ckinglake1d@weebly.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (51, 'Chen', 'Behn', 'cbehn1e@wunderground.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (52, 'Pacorro', 'Birds', 'pbirds1f@ucoz.ru', 'Bigender');
insert into users (id, first_name, last_name, email, gender) values (53, 'Adriaens', 'Branno', 'abranno1g@rambler.ru', 'Female');
insert into users (id, first_name, last_name, email, gender) values (54, 'Myer', 'Goody', 'mgoody1h@indiatimes.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (55, 'Noemi', 'Mahody', 'nmahody1i@smh.com.au', 'Female');
insert into users (id, first_name, last_name, email, gender) values (56, 'Roda', 'Hayler', 'rhayler1j@opera.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (57, 'Brinn', 'Fruchter', 'bfruchter1k@ox.ac.uk', 'Female');
insert into users (id, first_name, last_name, email, gender) values (58, 'Brittan', 'Govern', 'bgovern1l@freewebs.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (59, 'Pinchas', 'Von Welden', 'pvonwelden1m@ucla.edu', 'Male');
insert into users (id, first_name, last_name, email, gender) values (60, 'Robbie', 'Piesold', 'rpiesold1n@bbc.co.uk', 'Bigender');
insert into users (id, first_name, last_name, email, gender) values (61, 'Sheffield', 'Collingridge', 'scollingridge1o@state.gov', 'Male');
insert into users (id, first_name, last_name, email, gender) values (62, 'Horatius', 'Khomin', 'hkhomin1p@slideshare.net', 'Male');
insert into users (id, first_name, last_name, email, gender) values (63, 'Grove', 'Rainforth', 'grainforth1q@buzzfeed.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (64, 'Avivah', 'Clubley', 'aclubley1r@state.gov', 'Female');
insert into users (id, first_name, last_name, email, gender) values (65, 'Ade', 'Beevens', 'abeevens1s@cdbaby.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (66, 'Renate', 'Burnel', 'rburnel1t@paypal.com', 'Non-binary');
insert into users (id, first_name, last_name, email, gender) values (67, 'Julio', 'Skelhorn', 'jskelhorn1u@livejournal.com', 'Genderfluid');
insert into users (id, first_name, last_name, email, gender) values (68, 'Peg', 'Baguley', 'pbaguley1v@list-manage.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (69, 'Drusilla', 'Sinnock', 'dsinnock1w@rediff.com', 'Genderqueer');
insert into users (id, first_name, last_name, email, gender) values (70, 'Gard', 'Suero', 'gsuero1x@spiegel.de', 'Male');
insert into users (id, first_name, last_name, email, gender) values (71, 'Dominik', 'Flukes', 'dflukes1y@qq.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (72, 'Dareen', 'Doumerc', 'ddoumerc1z@spiegel.de', 'Female');
insert into users (id, first_name, last_name, email, gender) values (73, 'Perl', 'Linsay', 'plinsay20@deviantart.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (74, 'Jenda', 'Adamolli', 'jadamolli21@mapy.cz', 'Female');
insert into users (id, first_name, last_name, email, gender) values (75, 'Bridgette', 'Ericssen', 'bericssen22@eepurl.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (76, 'Weber', 'Keep', 'wkeep23@miibeian.gov.cn', 'Male');
insert into users (id, first_name, last_name, email, gender) values (77, 'Doug', 'Mahoney', 'dmahoney24@opensource.org', 'Male');
insert into users (id, first_name, last_name, email, gender) values (78, 'Archibaldo', 'Gyppes', 'agyppes25@wikia.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (79, 'Jandy', 'Diego', 'jdiego26@webs.com', 'Polygender');
insert into users (id, first_name, last_name, email, gender) values (80, 'Gael', 'Walas', 'gwalas27@goo.gl', 'Female');
insert into users (id, first_name, last_name, email, gender) values (81, 'Demott', 'Donhardt', 'ddonhardt28@example.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (82, 'Wang', 'Bodiam', 'wbodiam29@hugedomains.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (83, 'Alick', 'Fillis', 'afillis2a@printfriendly.com', 'Bigender');
insert into users (id, first_name, last_name, email, gender) values (84, 'Durand', 'Guierre', 'dguierre2b@sbwire.com', 'Male');
insert into users (id, first_name, last_name, email, gender) values (85, 'Aloin', 'Swanne', 'aswanne2c@google.co.jp', 'Male');
insert into users (id, first_name, last_name, email, gender) values (86, 'Aurthur', 'Buncom', 'abuncom2d@yandex.ru', 'Male');
insert into users (id, first_name, last_name, email, gender) values (87, 'Isabelle', 'Coventon', 'icoventon2e@youtube.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (88, 'Christin', 'Roseveare', 'croseveare2f@ftc.gov', 'Female');
insert into users (id, first_name, last_name, email, gender) values (89, 'Allin', 'Aistrop', 'aaistrop2g@purevolume.com', 'Bigender');
insert into users (id, first_name, last_name, email, gender) values (90, 'Sayre', 'Hanniger', 'shanniger2h@google.de', 'Male');
insert into users (id, first_name, last_name, email, gender) values (91, 'Wynne', 'Skelton', 'wskelton2i@surveymonkey.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (92, 'Lesya', 'McQuorkel', 'lmcquorkel2j@pcworld.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (93, 'Rudy', 'Learmont', 'rlearmont2k@geocities.jp', 'Male');
insert into users (id, first_name, last_name, email, gender) values (94, 'Helaina', 'Scimonelli', 'hscimonelli2l@cdbaby.com', 'Female');
insert into users (id, first_name, last_name, email, gender) values (95, 'Leontyne', 'Kloisner', 'lkloisner2m@nyu.edu', 'Female');
insert into users (id, first_name, last_name, email, gender) values (96, 'Frayda', 'McMurtyr', 'fmcmurtyr2n@ucsd.edu', 'Female');
insert into users (id, first_name, last_name, email, gender) values (97, 'Karoly', 'Ellcock', 'kellcock2o@ed.gov', 'Genderfluid');
insert into users (id, first_name, last_name, email, gender) values (98, 'Diahann', 'Espadater', 'despadater2p@php.net', 'Female');
insert into users (id, first_name, last_name, email, gender) values (99, 'Lianne', 'Ferry', 'lferry2q@amazon.de', 'Female');
insert into users (id, first_name, last_name, email, gender) values (100, 'Prissie', 'Corbie', 'pcorbie2r@godaddy.com', 'Female');

-- 1 --
SELECT * FROM users WHERE gender = 'Male';

-- 2 --
SELECT * FROM users WHERE (LENGTH(first_name) + LENGTH(last_name)) > 10;

-- 3 --
SELECT * FROM users WHERE email LIKE "%.com";

-- 4 --
SELECT * FROM users WHERE first_name LIKE "%a%";

-- 5 --
SELECT * FROM users WHERE gender = "Male" LIMIT 10;

-- 6 --
SELECT COUNT(gender) AS "Female" FROM users WHERE gender = "Female";
