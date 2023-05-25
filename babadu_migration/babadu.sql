-- CREATE SCHEMA IF NOT EXISTS public; 
-- SET search_path to BADADU_D7;

-- Table MEMBER

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

-- Table UMPIRE

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

-- Table PELATIH

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

-- Table SPESIALISASI

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

-- Table PELATIH_SPESIALISASI

CREATE TABLE IF NOT EXISTS PELATIH_SPESIALISASI
(
    ID_Pelatih UUID NOT NULL,
    ID_Spesialisasi UUID NOT NULL,
    PRIMARY KEY (ID_Pelatih, ID_Spesialisasi),
    FOREIGN KEY (ID_Pelatih) REFERENCES PELATIH(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ID_Spesialisasi) REFERENCES SPESIALISASI(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO PELATIH_SPESIALISASI (ID_Pelatih , ID_Spesialisasi) VALUES ('b3ad0aae-e246-4de4-af45-6f99f9b8f9d1', '0942c677-74ae-414b-b513-86a04362b937'),
	('bd486dbe-35e3-4692-8b45-01d895e815e9', '02306471-40c2-4ab0-99ad-76d84f5fb1b8'),
	('b3ad0aae-e246-4de4-af45-6f99f9b8f9d1', '02306471-40c2-4ab0-99ad-76d84f5fb1b8'),
	('e9dc278b-7928-4142-88d6-9f6d8f2089bf', '76e23523-d198-4415-b6ce-a0501c071b1d'),
	('0d9c4816-12c1-4e20-b9e3-09e61596f13f', 'ed38b0ca-1179-4d66-abc9-5ce830d66e5a'),
	('1139d87c-785f-430f-a280-d29118771295', 'b8d63b0f-6836-4e41-a4df-373f0876819b'),
	('bd486dbe-35e3-4692-8b45-01d895e815e9', 'b8d63b0f-6836-4e41-a4df-373f0876819b'),
	('0d9c4816-12c1-4e20-b9e3-09e61596f13f', '76e23523-d198-4415-b6ce-a0501c071b1d'),
	('b3ad0aae-e246-4de4-af45-6f99f9b8f9d1', 'ed38b0ca-1179-4d66-abc9-5ce830d66e5a'),
	('e9dc278b-7928-4142-88d6-9f6d8f2089bf', '0942c677-74ae-414b-b513-86a04362b937')
ON CONFLICT (ID) DO NOTHING;

-- Table ATLET

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

-- Table ATLET_PELATIH

CREATE TABLE IF NOT EXISTS ATLET_PELATIH
(
	ID_Pelatih UUID NOT NULL,
	ID_Atlet UUID NOT NULL,
	PRIMARY KEY (ID_Pelatih, ID_Atlet),

	FOREIGN KEY (ID_Atlet) REFERENCES ATLET(ID) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_Pelatih) REFERENCES PELATIH(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO ATLET_PELATIH VALUES ('b3ad0aae-e246-4de4-af45-6f99f9b8f9d1', 'a28e95e4-acf4-46b4-a139-bd79151be1cf'),
	('e9dc278b-7928-4142-88d6-9f6d8f2089bf', '1802242c-6f0b-4238-bfe4-c5c4b4936b4f'),
	('b3ad0aae-e246-4de4-af45-6f99f9b8f9d1', '8cc3bdc3-bc4d-46c3-81aa-b92c8f71a56c'),
	('1139d87c-785f-430f-a280-d29118771295', 'db771ea3-aba5-4a1e-a439-c12219d03d20'),
	('0d9c4816-12c1-4e20-b9e3-09e61596f13f', 'a28e95e4-acf4-46b4-a139-bd79151be1cf'),
	('0d9c4816-12c1-4e20-b9e3-09e61596f13f', '2f6b14d4-6202-4e47-abc1-227bc67c0935'),
	('bd486dbe-35e3-4692-8b45-01d895e815e9', '07a43f9f-b718-45bd-a37a-e794236f9649'),
	('1139d87c-785f-430f-a280-d29118771295', 'd7bbec6c-01f4-4cc1-89b8-2be2b0cba371'),
	('0d9c4816-12c1-4e20-b9e3-09e61596f13f', '4a413283-833a-417d-857f-72c957c60ed4'),
	('bd486dbe-35e3-4692-8b45-01d895e815e9', 'bdfb9e46-7b66-442a-861b-fb9c299c38b9'),
	('1139d87c-785f-430f-a280-d29118771295', '6732b97e-cf4d-4cde-9372-fa1df4a103a7'),
	('0d9c4816-12c1-4e20-b9e3-09e61596f13f', '07a43f9f-b718-45bd-a37a-e794236f9649'),
	('b3ad0aae-e246-4de4-af45-6f99f9b8f9d1', '75011b5f-723e-4b11-8314-80656c46c346'),
	('1139d87c-785f-430f-a280-d29118771295', '35f0beb6-f2bc-4dfc-b85a-1473222a8a4f'),
	('e9dc278b-7928-4142-88d6-9f6d8f2089bf', '8cc3bdc3-bc4d-46c3-81aa-b92c8f71a56c'),
	('0d9c4816-12c1-4e20-b9e3-09e61596f13f', '1886f253-b84d-4d6d-8619-bebf56830ac4'),
	('bd486dbe-35e3-4692-8b45-01d895e815e9', '6732b97e-cf4d-4cde-9372-fa1df4a103a7'),
	('e9dc278b-7928-4142-88d6-9f6d8f2089bf', '2e0d9f03-3158-4e4a-a928-1e0a6c838d42'),
	('e9dc278b-7928-4142-88d6-9f6d8f2089bf', '35f0beb6-f2bc-4dfc-b85a-1473222a8a4f'),
	('b3ad0aae-e246-4de4-af45-6f99f9b8f9d1', 'f2e40969-1ec7-4443-bcad-77f6d7b57e3b')
ON CONFLICT (ID) DO NOTHING;

-- Table SPONSOR

CREATE TABLE IF NOT EXISTS SPONSOR
(
	ID UUID NOT NULL,
	Nama_Brand VARCHAR(50) NOT NULL,
	Website VARCHAR(50),
	CP_Name VARCHAR(50) NOT NULL,
	CP_Email VARCHAR(50) NOT NULL,
	PRIMARY KEY (ID)
);

INSERT INTO SPONSOR ("id", "nama_brand", "website", "cp_name", "cp_email") VALUES ('3a01e612-25c5-4911-99b3-58dcd74186cd', 'Yonex', 'www.yonex.com', 'Syd Delicate', 'sdelicatee@howstuffworks.com'),
	('2e51b0ce-80fa-4853-8bf8-d88957684fdb', 'Victor', 'id.victorsport.com', 'Tucker Walne', 'twalnef@desdev.cn'),
	('e90118c4-7b09-439e-a98a-78fc45f9ca8e', 'Li-nings', 'www.shopnings.com', 'Enoch Fleet', 'efleetg@indiegogo.com'),
	('a343638c-c332-44df-9548-05287f8d3250', 'Djarum', 'www.djarum.com/', 'Abbie Ravenhills', 'aravenhillsh@yelp.com'),
	('cbb4b1bd-9000-4e3a-b450-87c02a4543d1', 'Daihatsu', 'daihatsu.co.id', 'Sile Gorghetto', 'sgorghettoi@people.com.cn')
ON CONFLICT (ID) DO NOTHING;

-- Table ATLET_SPONSOR

CREATE TABLE IF NOT EXISTS ATLET_SPONSOR
(
	ID_Atlet UUID NOT NULL,
	ID_Sponsor UUID NOT NULL,
	Tgl_Mulai DATE NOT NULL,
	Tgl_Selesai  DATE,
	PRIMARY KEY (ID_Atlet, ID_Sponsor),
	FOREIGN KEY (ID_Atlet) REFERENCES ATLET(ID) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (ID_Sponsor) REFERENCES SPONSOR(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO ATLET_SPONSOR ("id_atlet", "id_sponsor", "tgl_mulai", "tgl_selesai") VALUES ('1802242c-6f0b-4238-bfe4-c5c4b4936b4f', '3a01e612-25c5-4911-99b3-58dcd74186cd', '2022-12-16', '2024-09-10'),
	('a28e95e4-acf4-46b4-a139-bd79151be1cf', '2e51b0ce-80fa-4853-8bf8-d88957684fdb', '2023-02-01', '2023-11-11'),
	('db771ea3-aba5-4a1e-a439-c12219d03d20', 'e90118c4-7b09-439e-a98a-78fc45f9ca8e', '2022-07-30', '2023-04-23'),
	('2f6b14d4-6202-4e47-abc1-227bc67c0935', 'a343638c-c332-44df-9548-05287f8d3250', '2022-07-31', '2024-08-18'),
	('07a43f9f-b718-45bd-a37a-e794236f9649', 'cbb4b1bd-9000-4e3a-b450-87c02a4543d1', '2022-10-12', '2024-08-12'),
	('d7bbec6c-01f4-4cc1-89b8-2be2b0cba371', 'e90118c4-7b09-439e-a98a-78fc45f9ca8e', '2022-08-15', '2024-11-01'),
	('4a413283-833a-417d-857f-72c957c60ed4', '2e51b0ce-80fa-4853-8bf8-d88957684fdb', '2023-03-22', '2024-05-18'),
	('6732b97e-cf4d-4cde-9372-fa1df4a103a7', 'cbb4b1bd-9000-4e3a-b450-87c02a4543d1', '2023-01-20', '2023-10-22'),
	('bdfb9e46-7b66-442a-861b-fb9c299c38b9', '2e51b0ce-80fa-4853-8bf8-d88957684fdb', '2022-07-07', '2024-05-07'),
	('75011b5f-723e-4b11-8314-80656c46c346', '3a01e612-25c5-4911-99b3-58dcd74186cd', '2023-01-30', '2024-01-16'),
	('8cc3bdc3-bc4d-46c3-81aa-b92c8f71a56c', '2e51b0ce-80fa-4853-8bf8-d88957684fdb', '2022-08-23', '2023-05-24'),
	('1886f253-b84d-4d6d-8619-bebf56830ac4', 'e90118c4-7b09-439e-a98a-78fc45f9ca8e', '2022-07-02', '2024-01-25'),
	('2e0d9f03-3158-4e4a-a928-1e0a6c838d42', 'a343638c-c332-44df-9548-05287f8d3250', '2023-01-23', '2024-02-17'),
	('35f0beb6-f2bc-4dfc-b85a-1473222a8a4f', 'cbb4b1bd-9000-4e3a-b450-87c02a4543d1', '2022-10-26', '2024-01-13'),
	('f2e40969-1ec7-4443-bcad-77f6d7b57e3b', 'a343638c-c332-44df-9548-05287f8d3250', '2022-11-23', '2023-09-13')
ON CONFLICT (ID) DO NOTHING;

-- Table ATLET_KUALIFIKASI

CREATE TABLE IF NOT EXISTS ATLET_KUALIFIKASI
(
    ID_Atlet UUID NOT NULL,
    World_Rank INT,
    World_Tour_Rank INT NOT NULL,
    PRIMARY KEY (ID_Atlet),
    FOREIGN KEY (ID_Atlet) REFERENCES ATLET(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO ATLET_KUALIFIKASI (ID_Atlet, World_Rank, World_Tour_Rank) VALUES ('1802242c-6f0b-4238-bfe4-c5c4b4936b4f', 3, 3),
	('a28e95e4-acf4-46b4-a139-bd79151be1cf', 5, 5),
	('db771ea3-aba5-4a1e-a439-c12219d03d20', 6, 6),
	('2f6b14d4-6202-4e47-abc1-227bc67c0935', 1, 1),
	('07a43f9f-b718-45bd-a37a-e794236f9649', 4, 4),
	('d7bbec6c-01f4-4cc1-89b8-2be2b0cba371', 7, 7),
	('4a413283-833a-417d-857f-72c957c60ed4', 2, 2),
	('6732b97e-cf4d-4cde-9372-fa1df4a103a7', 8, 8)
ON CONFLICT (ID) DO NOTHING;

-- Table ATLET_NON_KUALIFIKASI

CREATE TABLE IF NOT EXISTS ATLET_NON_KUALIFIKASI
(
    ID_Atlet UUID NOT NULL,
    PRIMARY KEY (ID_Atlet),
    FOREIGN KEY (ID_Atlet) REFERENCES ATLET(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO ATLET_NON_KUALIFIKASI(ID_Atlet) VALUES ('bdfb9e46-7b66-442a-861b-fb9c299c38b9'),
	('75011b5f-723e-4b11-8314-80656c46c346'),
	('8cc3bdc3-bc4d-46c3-81aa-b92c8f71a56c'),
	('1886f253-b84d-4d6d-8619-bebf56830ac4'),
	('2e0d9f03-3158-4e4a-a928-1e0a6c838d42'),
	('35f0beb6-f2bc-4dfc-b85a-1473222a8a4f'),
	('f2e40969-1ec7-4443-bcad-77f6d7b57e3b')
ON CONFLICT (ID) DO NOTHING;

-- Table UJIAN_KUALIFIKASI

CREATE TABLE IF NOT EXISTS UJIAN_KUALIFIKASI
(
    Tahun INT,
    Batch INT,
    Tempat VARCHAR(50),
    Tanggal  DATE,
    PRIMARY KEY (Tahun, Batch, Tempat, Tanggal)
);

INSERT INTO UJIAN_KUALIFIKASI(Tahun, Batch, Tempat, Tanggal) VALUES('2023', '1', 'Jakarta', '2023-02-26'),
	('2022', '1', 'Bandung', '2022-08-12'),
	('2022', '2', 'Bogor', '2022-06-10')
ON CONFLICT (ID) DO NOTHING;

-- Table ATLET_NONKUALIFIKASI_UJIAN_KUALIFIKASI

CREATE TABLE IF NOT EXISTS ATLET_NONKUALIFIKASI_UJIAN_KUALIFIKASI
(
    ID_Atlet UUID NOT NULL,
    Tahun INT,
    Batch INT,
    Tempat VARCHAR(50),
    Tanggal DATE,
    Hasil_Lulus BOOLEAN,
    PRIMARY KEY (ID_Atlet, Tahun, Batch, Tempat, Tanggal, Hasil_Lulus),
    FOREIGN KEY (ID_Atlet) REFERENCES ATLET(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Tahun, Batch, Tempat, Tanggal) REFERENCES UJIAN_KUALIFIKASI(Tahun, Batch, Tempat, Tanggal) ON UPDATE CASCADE ON DELETE CASCADE
)

INSERT INTO ATLET_NONKUALIFIKASI_UJIAN_KUALIFIKASI ("id_atlet", "tahun", "batch", "tempat", "tanggal", "hasil_lulus") VALUES ('bdfb9e46-7b66-442a-861b-fb9c299c38b9', '2023', '1', 'Jakarta', '2023-02-26', '1'),
	('75011b5f-723e-4b11-8314-80656c46c346', '2022', '1', 'Bandung', '2022-08-12', '0'),
	('8cc3bdc3-bc4d-46c3-81aa-b92c8f71a56c', '2022', '2', 'Bogor', '2022-06-10', '1'),
	('1886f253-b84d-4d6d-8619-bebf56830ac4', '2022', '2', 'Bogor', '2022-06-10', '0'),
	('2e0d9f03-3158-4e4a-a928-1e0a6c838d42', '2022', '1', 'Bandung', '2022-08-12', '0'),
	('35f0beb6-f2bc-4dfc-b85a-1473222a8a4f', '2022', '2', 'Bogor', '2022-06-10', '1'),
	('f2e40969-1ec7-4443-bcad-77f6d7b57e3b', '2022', '1', 'Bandung', '2022-08-12', '0'),
	('75011b5f-723e-4b11-8314-80656c46c346', '2023', '1', 'Jakarta', '2023-02-26', '0'),
	('1886f253-b84d-4d6d-8619-bebf56830ac4', '2022', '1', 'Bandung', '2022-08-12', '1'),
	('2e0d9f03-3158-4e4a-a928-1e0a6c838d42', '2023', '1', 'Jakarta', '2023-02-26', '1')
ON CONFLICT (ID) DO NOTHING;

-- Table ATLET_GANDA

CREATE TABLE IF NOT EXISTS ATLET_GANDA
(
    ID_Atlet_Ganda UUID NOT NULL,
    ID_Atlet_Kualifikasi UUID NOT NULL,
    ID_Atlet_Kualifikasi_2 UUID NOT NULL,
    PRIMARY KEY (ID_Atlet_Ganda),
    FOREIGN KEY (ID_Atlet_Kualifikasi) REFERENCES ATLET_KUALIFIKASI(ID_Atlet) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ID_Atlet_Kualifikasi_2) REFERENCES ATLET_KUALIFIKASI(ID_Atlet) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO ATLET_GANDA ("id_atlet_ganda", "id_atlet_kualifikasi", "id_atlet_kualifikasi_2") VALUES ('d5901864-105f-4e38-9f21-42443ca8bd63', '1802242c-6f0b-4238-bfe4-c5c4b4936b4f', 'a28e95e4-acf4-46b4-a139-bd79151be1cf'),
	('1e0eaca1-9d12-494c-89fa-f20329da402e', 'db771ea3-aba5-4a1e-a439-c12219d03d20', '2f6b14d4-6202-4e47-abc1-227bc67c0935'),
	('1f956038-b934-415f-a69a-1b2ffd25e19b', '07a43f9f-b718-45bd-a37a-e794236f9649', 'd7bbec6c-01f4-4cc1-89b8-2be2b0cba371'),
	('1dd9d25a-ff3b-445a-82f8-d9f6d81a5efb', '4a413283-833a-417d-857f-72c957c60ed4', '6732b97e-cf4d-4cde-9372-fa1df4a103a7'),
	('1d113bc2-204d-413f-a56b-6369a07e5772', 'db771ea3-aba5-4a1e-a439-c12219d03d20', '1802242c-6f0b-4238-bfe4-c5c4b4936b4f'),
	('d093586d-63bf-4397-84f9-9386754ba309', '6732b97e-cf4d-4cde-9372-fa1df4a103a7', '2f6b14d4-6202-4e47-abc1-227bc67c0935'),
	('29f513cb-16e3-41b3-8808-3c8c1b624f19', 'd7bbec6c-01f4-4cc1-89b8-2be2b0cba371', 'a28e95e4-acf4-46b4-a139-bd79151be1cf'),
	('1823b8ae-58af-4236-82bf-35d8dd3afb7d', '07a43f9f-b718-45bd-a37a-e794236f9649', '4a413283-833a-417d-857f-72c957c60ed4'),
	('db7c3dbe-eecd-416b-ad26-0f3972ca5d58', 'd7bbec6c-01f4-4cc1-89b8-2be2b0cba371', 'db771ea3-aba5-4a1e-a439-c12219d03d20'),
	('b6265eaf-b11c-47ef-85a5-db097ed5df51', 'a28e95e4-acf4-46b4-a139-bd79151be1cf', '6732b97e-cf4d-4cde-9372-fa1df4a103a7')
ON CONFLICT (ID) DO NOTHING;

-- Table PESERTA_KOMPETISI

CREATE TABLE IF NOT EXISTS PESERTA_KOMPETISI
(
    Nomor_Peserta INT NOT NULL,
    ID_Atlet_Ganda UUID,
    ID_Atlet_Kualifikasi UUID,
    World_Rank INT,
    World_Tour_Rank INT NOT NULL,
    PRIMARY KEY (Nomor_Peserta),  
    FOREIGN KEY (ID_Atlet_Ganda) REFERENCES ATLET_GANDA(ID_Atlet_Ganda) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ID_Atlet_Kualifikasi) REFERENCES ATLET_KUALIFIKASI(ID_Atlet) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO PESERTA_KOMPETISI ("nomor_peserta", "id_atlet_ganda", "id_atlet_kualifikasi", "world_rank", "world_tour_rank") VALUES ('1', 'd5901864-105f-4e38-9f21-42443ca8bd63', '1802242c-6f0b-4238-bfe4-c5c4b4936b4f', '4', '4'),
	('2', '1e0eaca1-9d12-494c-89fa-f20329da402e', 'db771ea3-aba5-4a1e-a439-c12219d03d20', '2', '2'),
	('3', '1f956038-b934-415f-a69a-1b2ffd25e19b', '07a43f9f-b718-45bd-a37a-e794236f9649', '7', '7'),
	('4', '1dd9d25a-ff3b-445a-82f8-d9f6d81a5efb', '4a413283-833a-417d-857f-72c957c60ed4', '5', '5'),
	('5', '1d113bc2-204d-413f-a56b-6369a07e5772', 'db771ea3-aba5-4a1e-a439-c12219d03d20', '8', '8'),
	('6', 'd093586d-63bf-4397-84f9-9386754ba309', '6732b97e-cf4d-4cde-9372-fa1df4a103a7', '1', '1'),
	('7', '29f513cb-16e3-41b3-8808-3c8c1b624f19', 'd7bbec6c-01f4-4cc1-89b8-2be2b0cba371', '6', '6'),
	('8', '1823b8ae-58af-4236-82bf-35d8dd3afb7d', '07a43f9f-b718-45bd-a37a-e794236f9649', '3', '3'),
	('9', 'db7c3dbe-eecd-416b-ad26-0f3972ca5d58', 'd7bbec6c-01f4-4cc1-89b8-2be2b0cba371', '9', '9'),
	('10', 'b6265eaf-b11c-47ef-85a5-db097ed5df51', 'a28e95e4-acf4-46b4-a139-bd79151be1cf', '10', '10'),
    ('11', 'd5901864-105f-4e38-9f21-42443ca8bd63', 'a28e95e4-acf4-46b4-a139-bd79151be1cf', '4', '4'),
    ('12', 'db7c3dbe-eecd-416b-ad26-0f3972ca5d58', 'db771ea3-aba5-4a1e-a439-c12219d03d20', '9', '9'),
    ('13', '1e0eaca1-9d12-494c-89fa-f20329da402e', '2f6b14d4-6202-4e47-abc1-227bc67c0935', '2', '2')
ON CONFLICT (ID) DO NOTHING;

-- Table STADIUM

CREATE TABLE IF NOT EXISTS STADIUM
(
	Nama VARCHAR(50) NOT NULL,
	Alamat VARCHAR(50) NOT NULL,
	Kapasitas INT NOT NULL,
	Negara VARCHAR(50) NOT NULL,
	PRIMARY KEY (Nama)
);

INSERT INTO STADIUM (Nama, Alamat, Kapasitas, Negara) VALUES ('Istora Senayan', 'Jakarta', '8', 'Indonesia'),
	('Axiata Arena', 'Kuala Lumpur', '16', 'Malaysia'),
	('Haixia', 'Fuzhou', '10', 'China'),
	('Maruzen', 'Osaka', '32', 'Japan'),
	('BICC', 'Bali', '8', 'Indonesia')
ON CONFLICT (ID) DO NOTHING;

-- Table EVENT

CREATE TABLE IF NOT EXISTS EVENT
(
	Nama_Event VARCHAR(50) NOT NULL,
	Tahun INT NOT NULL,
	Nama_Stadium VARCHAR(50) NOT NULL,
	Negara VARCHAR(50) NOT NULL,
	Tgl_Mulai DATE NOT NULL,
	Tgl_Selesai DATE NOT NULL,
	Kategori_Superseries VARCHAR(5) NOT NULL,
	Total_Hadiah BIGINT NOT NULL,
	PRIMARY KEY (Nama_Event, Tahun),
	FOREIGN KEY (Nama_Stadium) REFERENCES STADIUM(Nama) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO EVENT (Nama_Event, Tahun, Nama_Stadium, Negara, Tgl_Mulai, Tgl_Selesai, Kategori_Superseries, Total_Hadiah) VALUES ('Indonesia Open', '2022', 'Istora Senayan', 'Indonesia', '2022-06-14', '2022-06-19', 'S1000', '30000000'),
	('Malaysia Masters', '2023', 'Axiata Arena', 'Malaysia', '2023-05-23', '2023-05-28', 'S500', '10000000'),
	('Indonesia Masters', '2023', 'BICC', 'Indonesia', '2023-01-24', '2023-01-29', 'S500', '12000000')
ON CONFLICT (ID) DO NOTHING;

-- Table PARTAI_KOMPETISI

CREATE TABLE IF NOT EXISTS PARTAI_KOMPETISI
(
    Jenis_Partai CHAR(2)  NOT NULL,
    Nama_Event VARCHAR(50) NOT NULL,
    Tahun_Event INT NOT NULL,
    PRIMARY KEY (Jenis_Partai, Nama_Event, Tahun_Event),  
    FOREIGN KEY (Nama_Event, Tahun_Event) REFERENCES EVENT(Nama_Event, Tahun) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO PARTAI_KOMPETISI (jenis_partai, nama_event, tahun_event) VALUES ('TA', 'Indonesia Open', '2022'),
	('TA', 'Malaysia Masters', '2023'),
	('GA', 'Indonesia Open', '2022'),
	('GA', 'Indonesia Masters', '2023'),
	('TI', 'Indonesia Open', '2022'),
	('TI', 'Indonesia Masters', '2023'),
	('GI', 'Malaysia Masters', '2023'),
	('GI', 'Indonesia Masters', '2023'),
	('GC', 'Indonesia Open', '2022'),
	('GC', 'Malaysia Masters', '2023')
ON CONFLICT (ID) DO NOTHING;

-- Table PARTAI_PESERTA_KOMPETISI

CREATE TABLE IF NOT EXISTS PARTAI_PESERTA_KOMPETISI
(
    Jenis_Partai CHAR(2)  NOT NULL,
	Nama_Event VARCHAR(50) NOT NULL,
	Tahun_Event INT NOT NULL,
	Nomor_Peserta INT NOT NULL,
    PRIMARY KEY (Jenis_Partai, Nama_Event, Tahun_Event, Nomor_Peserta),
	FOREIGN KEY (Jenis_Partai, Nama_Event, Tahun_Event) REFERENCES PARTAI_KOMPETISI(Jenis_Partai, Nama_Event, Tahun_Event) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (Nomor_Peserta) REFERENCES PESERTA_KOMPETISI(Nomor_Peserta) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO PARTAI_PESERTA_KOMPETISI (Jenis_Partai, Nama_Event, Tahun_Event, Nomor_Peserta) VALUES ('TA', 'Indonesia Open', '2022', '4'),
	('TA', 'Indonesia Open', '2022', '5'),
	('TA', 'Indonesia Open', '2022', '10'),
	('TA', 'Malaysia Masters', '2023', '1'),
	('TA', 'Malaysia Masters', '2023', '10'),
	('TI', 'Indonesia Open', '2022', '6'),
	('TI', 'Indonesia Masters', '2023', '2'),
	('TI', 'Indonesia Masters', '2023', '6'),
	('TI', 'Indonesia Masters', '2023', '7'),
	('GA', 'Indonesia Open', '2022', '1'),
	('GA', 'Indonesia Open', '2022', '11'),
	('GI', 'Malaysia Masters', '2023', '9'),
	('GI', 'Malaysia Masters', '2023', '12'),
	('GC', 'Indonesia Open', '2022', '2'),
	('GC', 'Indonesia Open', '2022', '13')
ON CONFLICT (ID) DO NOTHING;

-- Table PESERTA_MENDAFTAR_EVENT

CREATE TABLE IF NOT EXISTS PESERTA_MENDAFTAR_EVENT
(
	Nomor_Peserta INT NOT NULL,
	Nama_Event VARCHAR(50) NOT NULL,
	Tahun INT NOT NULL,
    PRIMARY KEY (Nomor_Peserta, Nama_Event, Tahun),
	FOREIGN KEY (Nomor_Peserta) REFERENCES PESERTA_KOMPETISI(Nomor_Peserta) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Nama_Event, Tahun) REFERENCES EVENT(Nama_Event, Tahun) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO PESERTA_MENDAFTAR_EVENT (Nomor_Peserta, Nama_Event, Tahun) VALUES ('1', 'Indonesia Open', '2022'),
	('2', 'Indonesia Open', '2022'),
	('4', 'Indonesia Open', '2022'),
	('5', 'Indonesia Open', '2022'),
	('6', 'Indonesia Open', '2022'),
	('10', 'Indonesia Open', '2022'),
	('11', 'Indonesia Open', '2022'),
	('13', 'Indonesia Open', '2022'),
	('2', 'Indonesia Masters', '2023'),
	('6', 'Indonesia Masters', '2023'),
	('7', 'Indonesia Masters', '2023'),
	('1', 'Malaysia Masters', '2023'),
	('9', 'Malaysia Masters', '2023'),
	('10', 'Malaysia Masters', '2023'),
	('12', 'Malaysia Masters', '2023')
ON CONFLICT (ID) DO NOTHING;

-- Table MATCH

CREATE TABLE IF NOT EXISTS MATCH
(
	Jenis_Babak VARCHAR(20) NOT NULL,
	Tanggal DATE NOT NULL,
	Waktu_Mulai TIME NOT NULL,
	Total_Durasi INT NOT NULL,
	Nama_Event VARCHAR(50) NOT NULL,
	Tahun_Event INT NOT NULL,
	ID_Umpire UUID NOT NULL,
	PRIMARY KEY (Jenis_Babak, Tanggal, Waktu_Mulai),
	FOREIGN KEY (Nama_Event, Tahun_Event) REFERENCES EVENT(Nama_Event, Tahun) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ID_Umpire) REFERENCES UMPIRE(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO MATCH (Jenis_Babak, Tanggal, Waktu_Mulai, Total_Durasi, Nama_Event, Tahun_Event, ID_Umpire) VALUES ('R32', '2022-06-14', '10:00:00', '82', 'Indonesia Open', '2022', '340d5546-a97b-49cd-8950-97f51ba6d49d'),
	('R16', '2022-06-15', '10:00:00', '99', 'Indonesia Open', '2022', '26a00d00-541d-43b8-b2be-b88631a1a2fc'),
	('Perempatan Final', '2023-05-25', '13:00:00', '92', 'Malaysia Masters', '2023', '25d7d095-45c4-4296-ab23-c5a97d22aba6'),
	('Semifinal', '2023-05-26', '10:00:00', '118', 'Malaysia Masters', '2023', '632378c6-3c3e-4bc7-9a21-1e49b0649f9c'),
	('Final', '2023-01-29', '15:00:00', '91', 'Indonesia Masters', '2023', '04b445f9-e7d7-47a5-84ab-3dd70e3f54b8')
ON CONFLICT (ID) DO NOTHING;


-- Table PESERTA_MENGIKUTI_MATCH

CREATE TABLE IF NOT EXISTS PESERTA_MENGIKUTI_MATCH
(
	Jenis_Babak VARCHAR(20) NOT NULL,
	Tanggal DATE NOT NULL,
	Waktu_Mulai TIME NOT NULL,
	Nomor_Peserta INT NOT NULL,
	Status_Menang BOOLEAN NOT NULL,
    PRIMARY KEY (Jenis_Babak, Tanggal, Waktu_Mulai, Nomor_Peserta),
	FOREIGN KEY (Jenis_Babak, Tanggal, Waktu_Mulai) REFERENCES MATCH(Jenis_Babak, Tanggal, Waktu_Mulai) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (Nomor_Peserta) REFERENCES PESERTA_KOMPETISI(Nomor_Peserta) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO PESERTA_MENGIKUTI_MATCH (Jenis_Babak, Tanggal, Waktu_Mulai, Nomor_Peserta, Status_Menang) VALUES ('R32', '2022-06-14', '10:00:00', '1', 'FALSE'),
	('R32', '2022-06-14', '10:00:00', '2', 'TRUE'),
	('R32', '2022-06-14', '10:00:00', '4', 'FALSE'),
	('R32', '2022-06-14', '10:00:00', '5', 'TRUE'),
	('R32', '2022-06-14', '10:00:00', '6', 'FALSE'),
	('R32', '2022-06-14', '10:00:00', '10', 'TRUE'),
	('R32', '2022-06-14', '10:00:00', '11', 'FALSE'),
	('R32', '2022-06-14', '10:00:00', '13', 'TRUE'),
	('R16', '2022-06-15', '10:00:00', '2', 'FALSE'),
	('R16', '2022-06-15', '10:00:00', '4', 'FALSE'),
	('R16', '2022-06-15', '10:00:00', '5', 'TRUE'),
	('R16', '2022-06-15', '10:00:00', '6', 'TRUE'),
	('R16', '2022-06-15', '10:00:00', '10', 'FALSE'),
	('Perempatan Final', '2023-05-25', '13:00:00', '1', 'TRUE'),
	('Perempatan Final', '2023-05-25', '13:00:00', '9', 'TRUE'),
	('Perempatan Final', '2023-05-25', '13:00:00', '10', 'FALSE'),
	('Perempatan Final', '2023-05-25', '13:00:00', '12', 'FALSE'),
	('Semifinal', '2023-05-26', '10:00:00', '10', 'TRUE'),
	('Semifinal', '2023-05-26', '10:00:00', '12', 'FALSE'),
	('Final', '2023-01-29', '15:00:00', '2', 'TRUE')
ON CONFLICT (ID) DO NOTHING;

-- Table GAME

CREATE TABLE IF NOT EXISTS GAME 
(
	No_Game INT NOT NULL,
	Durasi INT NOT NULL,
	Jenis_Babak VARCHAR(20) NOT NULL,
	Tanggal DATE NOT NULL,
	Waktu_Mulai TIME NOT NULL,
	PRIMARY KEY (No_Game),
	FOREIGN KEY (Jenis_Babak, Tanggal, Waktu_Mulai) REFERENCES MATCH(Jenis_Babak, Tanggal, Waktu_Mulai) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO GAME (No_Game, Durasi, Jenis_Babak, Tanggal, Waktu_Mulai) VALUES ('1', '40', 'R32', '2022-06-14', '10:00:00'),
	('2', '42', 'R32', '2022-06-14', '10:00:00'),
	('3', '52', 'R32', '2022-06-14', '10:00:00'),
	('4', '47', 'R16', '2022-06-15', '10:00:00'),
	('5', '44', 'R16', '2022-06-15', '10:00:00'),
	('6', '48', 'Perempatan Final', '2023-05-25', '13:00:00'),
	('7', '58', 'Perempatan Final', '2023-05-25', '13:00:00'),
	('8', '60', 'Semifinal', '2023-05-26', '10:00:00'),
	('9', '44', 'Semifinal', '2023-05-26', '10:00:00'),
	('10', '47', 'Final', '2023-01-29', '15:00:00')
ON CONFLICT (ID) DO NOTHING;

-- Table PESERTA_MENGIKUTI_GAME

CREATE TABLE IF NOT EXISTS PESERTA_MENGIKUTI_GAME (
    Nomor_Peserta INT,
    No_Game INT,
    Skor INT NOT NULL,
    PRIMARY KEY (Nomor_Peserta, No_Game),
    FOREIGN KEY (Nomor_Peserta) REFERENCES PESERTA_KOMPETISI(Nomor_Peserta) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (No_Game) REFERENCES GAME(No_Game) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO PESERTA_MENGIKUTI_GAME (Nomor_Peserta, No_Game, Skor) VALUES ('11', '1', '23'),
	('10', '2', '25'),
	('9', '3', '27'),
	('9', '4', '29'),
	('5', '5', '31'),
	('7', '6', '27'),
	('7', '7', '33'),
	('8', '8', '23'),
	('10', '9', '25'),
	('4', '10', '29'),
	('9', '1', '21'),
	('1', '2', '23'),
	('1', '3', '27'),
	('6', '4', '33'),
	('11', '5', '25'),
	('5', '6', '31'),
	('2', '7', '23'),
	('4', '8', '27'),
	('6', '9', '33'),
	('9', '10', '21'),
	('1', '1', '29'),
	('2', '2', '27'),
	('10', '3', '25'),
	('4', '4', '31'),
	('12', '5', '23'),
	('4', '6', '29'),
	('1', '7', '27'),
	('5', '8', '33'),
	('4', '9', '21'),
	('13', '10', '25'),
	('8', '1', '31'),
	('9', '2', '23'),
	('6', '3', '29'),
	('5', '4', '27'),
	('1', '5', '21'),
	('2', '6', '33'),
	('3', '7', '25'),
	('1', '8', '27'),
	('6', '8', '29'),
	('6', '10', '23'),
	('3', '1', '31'),
	('3', '2', '33'),
	('5', '3', '21'),
	('9', '6', '29'),
	('13', '5', '27'),
	('7', '2', '23'),
	('5', '7', '33'),
	('10', '8', '25'),
	('5', '9', '31'),
	('12', '10', '21')
ON CONFLICT (ID) DO NOTHING;

-- Table POINT_HISTORY

CREATE TABLE IF NOT EXISTS POINT_HISTORY
(
	ID_Atlet UUID NOT NULL,
	Minggu_Ke INT NOT NULL,
	Bulan VARCHAR(20) NOT NULL,
	Tahun INT NOT NULL,
	Total_Point INT,
    PRIMARY KEY (ID_Atlet, Minggu_Ke, Bulan, Tahun),
	FOREIGN KEY (ID_Atlet) REFERENCES ATLET(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO POINT_HISTORY (ID_Atlet, Minggu_Ke, Bulan, Tahun, Total_Point) VALUES ('1802242c-6f0b-4238-bfe4-c5c4b4936b4f', '1', 'Januari', '2023', '1000'),
	('a28e95e4-acf4-46b4-a139-bd79151be1cf', '1', 'Januari', '2023', '200'),
	('db771ea3-aba5-4a1e-a439-c12219d03d20', '1', 'Januari', '2023', '20'),
	('2f6b14d4-6202-4e47-abc1-227bc67c0935', '3', 'Februari', '2023', '800'),
	('07a43f9f-b718-45bd-a37a-e794236f9649', '3', 'Februari', '2023', '100'),
	('d7bbec6c-01f4-4cc1-89b8-2be2b0cba371', '3', 'Februari', '2023', '1000'),
	('4a413283-833a-417d-857f-72c957c60ed4', '2', 'Maret', '2023', '600'),
	('6732b97e-cf4d-4cde-9372-fa1df4a103a7', '2', 'Maret', '2023', '200'),
	('1802242c-6f0b-4238-bfe4-c5c4b4936b4f', '2', 'Maret', '2023', '100'),
	('a28e95e4-acf4-46b4-a139-bd79151be1cf', '4', 'April', '2023', '200'),
	('db771ea3-aba5-4a1e-a439-c12219d03d20', '4', 'April', '2023', '100'),
	('2f6b14d4-6202-4e47-abc1-227bc67c0935', '4', 'April', '2023', '100'),
	('07a43f9f-b718-45bd-a37a-e794236f9649', '3', 'Mei', '2023', '10'),
	('d7bbec6c-01f4-4cc1-89b8-2be2b0cba371', '3', 'Mei', '2023', '75'),
	('4a413283-833a-417d-857f-72c957c60ed4', '3', 'Mei', '2023', '100'),
	('6732b97e-cf4d-4cde-9372-fa1df4a103a7', '1', 'Juni', '2023', '10'),
	('1802242c-6f0b-4238-bfe4-c5c4b4936b4f', '1', 'Juni', '2023', '300'),
	('a28e95e4-acf4-46b4-a139-bd79151be1cf', '1', 'Juni', '2023', '300'),
	('db771ea3-aba5-4a1e-a439-c12219d03d20', '4', 'Juli', '2023', '800'),
	('2f6b14d4-6202-4e47-abc1-227bc67c0935', '4', 'Juli', '2023', '1000'),
	('07a43f9f-b718-45bd-a37a-e794236f9649', '4', 'Juli', '2023', '600'),
	('d7bbec6c-01f4-4cc1-89b8-2be2b0cba371', '2', 'Agustus', '2023', '75'),
	('4a413283-833a-417d-857f-72c957c60ed4', '2', 'Agustus', '2023', '240'),
	('6732b97e-cf4d-4cde-9372-fa1df4a103a7', '2', 'Agustus', '2023', '60'),
	('1802242c-6f0b-4238-bfe4-c5c4b4936b4f', '4', 'September', '2023', '60'),
	('a28e95e4-acf4-46b4-a139-bd79151be1cf', '4', 'September', '2023', '450'),
	('db771ea3-aba5-4a1e-a439-c12219d03d20', '4', 'September', '2023', '60'),
	('2f6b14d4-6202-4e47-abc1-227bc67c0935', '1', 'Oktober', '2023', '150'),
	('07a43f9f-b718-45bd-a37a-e794236f9649', '1', 'Oktober', '2023', '750'),
	('d7bbec6c-01f4-4cc1-89b8-2be2b0cba371', '1', 'Oktober', '2023', '120'),
	('4a413283-833a-417d-857f-72c957c60ed4', '3', 'November', '2023', '1000'),
	('6732b97e-cf4d-4cde-9372-fa1df4a103a7', '3', 'November', '2023', '100'),
	('1802242c-6f0b-4238-bfe4-c5c4b4936b4f', '3', 'November', '2023', '450'),
	('a28e95e4-acf4-46b4-a139-bd79151be1cf', '1', 'Desember', '2023', '300'),
	('db771ea3-aba5-4a1e-a439-c12219d03d20', '1', 'Desember', '2023', '400'),
	('2f6b14d4-6202-4e47-abc1-227bc67c0935', '1', 'Desember', '2023', '10')
ON CONFLICT (ID) DO NOTHING;

-- TRIGGER & STORED PROCEDURE

-- Jika seorang atlet non-kualifikasi belum
-- pernah mengikuti ujian yang ia pilih tersebut
-- dan mendapatkan hasil lulus, maka status atlet
-- tersebut akan berubah dari "Not Qualified"
-- menjadi "Qualified". Sebelum proses
-- perubahan status dilakukan, sistem akan
-- menghapus seluruh riwayat ujian yang
-- pernah diambil atlet non-kualifikasi tersebut.

CREATE OR REPLACE FUNCTION mario_delete_riwayat_dan_update_status_atlet()
RETURNS TRIGGER AS $$


-- Adapun world rank dan world tour rank atlet
-- tersebut juga akan disesuaikan menjadi rank
-- terakhir dari rank keseluruhan yang ada. Untuk
-- total point atlet, akan ditambahkan sebanyak
-- 50 point (atribut minggu, bulan, dan tahun
-- diambil berdasarkan atribut tanggal pada
-- entity ujian kualifikasi yang diambil). Sistem
-- tidak perlu menyimpan data mengenai ujian
-- kualifikasi yang diambil oleh atlet tersebut jika
-- hasilnya lulus.

CREATE OR REPLACE FUNCTION mario_update_rank_atlet()
RETURNS TRIGGER AS $$
BEGIN
	IF EXISTS (SELECT * FROM ujian_kualifikasi_atlet WHERE id_atlet = NEW.id_atlet AND id_uk = NEW.id_uk) THEN
		IF NEW.hasil = 'Lulus' THEN
			UPDATE atlet SET world_rank = (SELECT world_rank FROM ujian_kualifikasi WHERE id = NEW.id_uk), world_tour_rank = (SELECT world_tour_rank FROM ujian_kualifikasi WHERE id = NEW.id_uk), total_point = total_point + 50 WHERE id = NEW.id_atlet;
		END IF;
	END IF;
	RETURN NEW;
END;

CREATE TRIGGER mario_update_rank_atlet
AFTER INSERT ON ujian_kualifikasi_atlet
FOR EACH ROW
EXECUTE PROCEDURE mario_update_rank_atlet();

-- Jika hasilnya tidak lulus, maka statusnya tidak
-- berubah dan sistem hanya akan menyimpan
-- data mengenai ujian kualifikasi yang diambil
-- oleh atlet non-kualifikasi tersebut.

CREATE OR REPLACE FUNCTION mario_update_rank_atlet2()
RETURNS TRIGGER AS $$
BEGIN
	IF EXISTS (SELECT * FROM ujian_kualifikasi_atlet WHERE id_atlet = NEW.id_atlet AND id_uk = NEW.id_uk) THEN
		IF NEW.hasil = 'Tidak Lulus' THEN
			INSERT INTO ujian_kualifikasi_atlet (id_atlet, id_uk, hasil) VALUES (NEW.id_atlet, NEW.id_uk, NEW.hasil);
		END IF;
	END IF;
	RETURN NEW;
END;

CREATE TRIGGER mario_update_rank_atlet2
AFTER INSERT ON ujian_kualifikasi_atlet
FOR EACH ROW
EXECUTE PROCEDURE mario_update_rank_atlet2();

-- Untuk atlet kualifikasi yang mengambil ujian
-- kualifikasi kembali, statusnya tidak akan
-- berubah dan data mengenai ujian yang diambil
-- tidak disimpan ke dalam sistem.

CREATE OR REPLACE FUNCTION mario_update_rank_atlet3()
RETURNS TRIGGER AS $$
BEGIN
	IF EXISTS (SELECT * FROM ujian_kualifikasi_atlet WHERE id_atlet = NEW.id_atlet AND id_uk = NEW.id_uk) THEN
		IF NEW.hasil = 'Lulus' THEN
			UPDATE atlet SET world_rank = (SELECT world_rank FROM ujian_kualifikasi WHERE id = NEW.id_uk), world_tour_rank = (SELECT world_tour_rank FROM ujian_kualifikasi WHERE id = NEW.id_uk), total_point = total_point + 50 WHERE id = NEW.id_atlet;
		END IF;
	END IF;
	RETURN NEW;
END;

CREATE TRIGGER mario_update_rank_atlet3
AFTER INSERT ON ujian_kualifikasi_atlet
FOR EACH ROW
EXECUTE PROCEDURE mario_update_rank_atlet3();
