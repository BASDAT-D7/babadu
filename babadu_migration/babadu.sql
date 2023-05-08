-- CREATE SCHEMA IF NOT EXISTS public; 
-- SET search_path to BADADU_D7;

CREATE TABLE IF NOT EXISTS MEMBER 
(
    ID UUID NOT NULL,
    Nama VARCHAR(50) NOT NULL,
    Email VARCHAR(50) NOT NULL,
    PRIMARY KEY (ID)
);

INSERT INTO MEMBER(ID, Nama, Email) VALUES
	('340d5546-a97b-49cd-8950-97f51ba6d49d', 'Engracia Minchi', 'eminchi0@elegantthemes.com'),
	('04b445f9-e7d7-47a5-84ab-3dd70e3f54b8', 'Taddeusz Dunnion', 'tdunnion1@go.com'),
	('26a00d00-541d-43b8-b2be-b88631a1a2fc', 'Vaughan Levy', 'vlevy2@amazon.co.uk'),
	('632378c6-3c3e-4bc7-9a21-1e49b0649f9c', 'Katha Willishire', 'kwillishire3@japanpost.jp'),
	('25d7d095-45c4-4296-ab23-c5a97d22aba6', 'Gabby Burnie', 'gburnie4@issuu.com'),
	('b3ad0aae-e246-4de4-af45-6f99f9b8f9d1', 'Montague Mussared', 'mmussared5@chicagotribune.com'),
	('bd486dbe-35e3-4692-8b45-01d895e815e9', 'Freddy Kerr', 'fkerr6@google.com'),
	('e9dc278b-7928-4142-88d6-9f6d8f2089bf', 'Rhodia Slimme', 'rslimme7@admin.ch'),
	('1139d87c-785f-430f-a280-d29118771295', 'Annabela Swindles', 'aswindles8@squarespace.com'),
	('0d9c4816-12c1-4e20-b9e3-09e61596f13f', 'Christoffer Antosik', 'cantosik9@baidu.com'),
	('1802242c-6f0b-4238-bfe4-c5c4b4936b4f', 'Lottie Ivushkin', 'livushkina@jalbum.net'),
	('a28e95e4-acf4-46b4-a139-bd79151be1cf', 'Innis Lesor', 'ilesorb@ovh.net'),
	('db771ea3-aba5-4a1e-a439-c12219d03d20', 'Valaree Eddies', 'veddiesc@vkontakte.ru'),
	('2f6b14d4-6202-4e47-abc1-227bc67c0935', 'Darb Makinson', 'dmakinsond@unc.edu'),
	('07a43f9f-b718-45bd-a37a-e794236f9649', 'Zaccaria Indruch', 'zindruche@usgs.gov'),
	('d7bbec6c-01f4-4cc1-89b8-2be2b0cba371', 'Jasmine Connock', 'jconnockf@printfriendly.com'),
	('4a413283-833a-417d-857f-72c957c60ed4', 'Breena Martschke', 'bmartschkeg@boston.com'),
	('6732b97e-cf4d-4cde-9372-fa1df4a103a7', 'Farris Peyro', 'fpeyroh@google.de'),
	('bdfb9e46-7b66-442a-861b-fb9c299c38b9', 'Nanice Woolfenden', 'nwoolfendeni@blog.com'),
	('75011b5f-723e-4b11-8314-80656c46c346', 'Warner Joinsey', 'wjoinseyj@blogger.com'),
	('8cc3bdc3-bc4d-46c3-81aa-b92c8f71a56c', 'Alasdair Zannuto', 'azannutok@google.com'),
	('1886f253-b84d-4d6d-8619-bebf56830ac4', 'Sena Malbon', 'smalbonl@elegantthemes.com'),
	('2e0d9f03-3158-4e4a-a928-1e0a6c838d42', 'Krishna Downey', 'kdowneym@google.com.au'),
	('35f0beb6-f2bc-4dfc-b85a-1473222a8a4f', 'Avis Boyat', 'aboyatn@wisc.edu'),
	('f2e40969-1ec7-4443-bcad-77f6d7b57e3b', 'Antonia Sadd', 'asaddo@technorati.com')
ON CONFLICT (ID) DO NOTHING;

CREATE TABLE IF NOT EXISTS UMPIRE
(
    ID UUID NOT NULL,
    Negara VARCHAR(50) NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (ID) REFERENCES MEMBER(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO UMPIRE(ID, Negara) VALUES ('340d5546-a97b-49cd-8950-97f51ba6d49d', 'China'),
	('04b445f9-e7d7-47a5-84ab-3dd70e3f54b8', 'Germany'),
	('26a00d00-541d-43b8-b2be-b88631a1a2fc', 'Brazil'),
	('632378c6-3c3e-4bc7-9a21-1e49b0649f9c', 'Thailand'),
	('25d7d095-45c4-4296-ab23-c5a97d22aba6', 'Indonesia')
ON CONFLICT (ID) DO NOTHING;

CREATE TABLE IF NOT EXISTS PELATIH
(
    ID UUID NOT NULL,
    Tanggal_Mulai DATE NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (ID) REFERENCES MEMBER(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO PELATIH(ID, Tanggal_Mulai) VALUES ('b3ad0aae-e246-4de4-af45-6f99f9b8f9d1', '2020-06-05 02:01:51'),
	('bd486dbe-35e3-4692-8b45-01d895e815e9', '2021-02-04 01:19:00'),
	('e9dc278b-7928-4142-88d6-9f6d8f2089bf', '2020-05-15 03:41:01'),
	('1139d87c-785f-430f-a280-d29118771295', '2020-09-08 07:25:26'),
	('0d9c4816-12c1-4e20-b9e3-09e61596f13f', '2023-05-01 21:37:19')
ON CONFLICT (ID) DO NOTHING;

CREATE TABLE IF NOT EXISTS SPESIALISASI
(
    ID UUID NOT NULL,
    Spesialisasi VARCHAR(20) NOT NULL,
    PRIMARY KEY (ID)
);

INSERT INTO SPESIALISASI(ID, Spesialisasi) VALUES ('0942c677-74ae-414b-b513-86a04362b937', 'Tunggal Putra '),
	('02306471-40c2-4ab0-99ad-76d84f5fb1b8', 'Tunggal Putri '),
	('76e23523-d198-4415-b6ce-a0501c071b1d', 'Ganda Putra '),
	('b8d63b0f-6836-4e41-a4df-373f0876819b', 'Ganda Putri '),
	('ed38b0ca-1179-4d66-abc9-5ce830d66e5a', 'Ganda Campuran')
ON CONFLICT (ID) DO NOTHING;

CREATE TABLE IF NOT EXISTS ATLET
(
    ID UUID NOT NULL,
    Tgl_Lahir DATE NOT NULL,
    Negara_Asal VARCHAR(50) NOT NULL,
    Play_Right BOOLEAN NOT NULL,
    Height INT NOT NULL,
    World_Rank INT,
    Jenis_Kelamin BOOLEAN NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (ID) REFERENCES MEMBER(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO ATLET (ID, Tgl_Lahir, Negara_Asal, Play_Right, Height, World_Rank, Jenis_Kelamin) VALUES ('1802242c-6f0b-4238-bfe4-c5c4b4936b4f', '1997-09-04 05:57:45', 'Germany', TRUE, 163, 3, TRUE),
	('a28e95e4-acf4-46b4-a139-bd79151be1cf', '1998-03-22 11:05:09', 'Japan', TRUE, 165, 5, TRUE),
	('db771ea3-aba5-4a1e-a439-c12219d03d20', '1995-02-01 22:43:59', 'Indonesia', TRUE, 159, 6, FALSE),
	('2f6b14d4-6202-4e47-abc1-227bc67c0935', '1999-01-24 11:24:43', 'Ghana', FALSE, 150, 1, TRUE),
	('07a43f9f-b718-45bd-a37a-e794236f9649', '1996-11-25 12:03:31', 'Indonesia', TRUE, 172, 4, TRUE),
	('d7bbec6c-01f4-4cc1-89b8-2be2b0cba371', '1999-04-20 15:35:17', 'Poland', FALSE, 169, 7, FALSE),
	('4a413283-833a-417d-857f-72c957c60ed4', '1991-10-04 11:56:18', 'Portugal', TRUE, 164, 2, TRUE),
	('6732b97e-cf4d-4cde-9372-fa1df4a103a7', '1994-04-07 15:17:58', 'Indonesia', FALSE, 150, 8, FALSE),
	('bdfb9e46-7b66-442a-861b-fb9c299c38b9', '1991-02-23 19:25:54', 'Syria', TRUE, 155, null, TRUE),
	('75011b5f-723e-4b11-8314-80656c46c346', '1994-04-24 00:56:00', 'Philippines', TRUE, 175, null, FALSE),
	('8cc3bdc3-bc4d-46c3-81aa-b92c8f71a56c', '1994-01-13 23:16:19', 'France', TRUE, 153, null, TRUE),
	('1886f253-b84d-4d6d-8619-bebf56830ac4', '1997-09-27 22:17:32', 'Ireland', FALSE, 154, null, FALSE),
	('2e0d9f03-3158-4e4a-a928-1e0a6c838d42', '1992-01-31 05:12:14', 'Indonesia', TRUE, 173, null, TRUE),
	('35f0beb6-f2bc-4dfc-b85a-1473222a8a4f', '1996-08-14 05:10:21', 'Indonesia', TRUE, 153, null, FALSE),
	('f2e40969-1ec7-4443-bcad-77f6d7b57e3b', '1998-07-04 08:34:22', 'China', TRUE, 179, null, FALSE)
ON CONFLICT (ID) DO NOTHING;