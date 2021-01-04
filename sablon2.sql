BEGIN TRANSACTION;
DROP TABLE IF EXISTS `paylasim_gruplari`;
CREATE TABLE IF NOT EXISTS `paylasim_gruplari` (
	`p_grup_id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`p_grup_adi`	TEXT,
	`grup_id_havuzu`	TEXT,
	`k_id`	int
);
DROP TABLE IF EXISTS `paylasilan_ileti`;
CREATE TABLE IF NOT EXISTS `paylasilan_ileti` (
	`ileti_id`	INTEGER,
	`p_grup_id`	TEXT,
	`gruplar_id`	TEXT,
	`paylasim_tarihi`	TEXT
);
DROP TABLE IF EXISTS `kullanici`;
CREATE TABLE IF NOT EXISTS `kullanici` (
	`kullanici_id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`kullanici_eposta`	TEXT,
	`kullanici_sifre`	TEXT,
	`kullanici_bilgi_kaydetme`	BLOB
);
DROP TABLE IF EXISTS `iletiler`;
CREATE TABLE IF NOT EXISTS `iletiler` (
	`ileti_id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`ileti_baslik`	TEXT,
	`ileti_icerik`	TEXT,
	`ileti_durum`	BLOB DEFAULT 0,
	`kullanici_id`	INTEGER,
	`payslasim_gruplari`	text,
	`gruplar`	text
);
DROP TABLE IF EXISTS `gruplar`;
CREATE TABLE IF NOT EXISTS `gruplar` (
	`grup_id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`grup_adi`	TEXT,
	`fb_grup_id`	INTEGER,
	`fb_grup_linki`	TEXT,
	`k_id`	int
);
COMMIT;
