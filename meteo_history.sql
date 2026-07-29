CREATE DATABASE IF NOT EXISTS meteo_history;
USE meteo_history;

CREATE TABLE IF NOT EXISTS global_extremes (
    record_id INT PRIMARY KEY,
    loc_code VARCHAR(15),
    city VARCHAR(40),
    country VARCHAR(40),
    event_date DATE,
    temperature DECIMAL(5,1),
    event_type VARCHAR(20)
);

TRUNCATE TABLE global_extremes;

INSERT INTO global_extremes(record_id, loc_code, city, country, event_date, temperature, event_type) VALUES
(1, 'US-CA', 'Furnace Creek', 'USA', '1913-07-10', 56.7, 'Heatwave'),
(2, 'RU-SA', 'Oymyakon', 'Russia', '1933-02-06', -67.7, 'Extreme Cold'),
(3, 'AQ-VO', 'Vostok Station', 'Antarctica', '1983-07-21', -89.2, 'Extreme Cold'),
(4, 'IR-KH', 'Ahvaz', 'Iran', '2017-06-29', 54.0, 'Heatwave'),
(5, 'KW-JA', 'Mitribah', 'Kuwait', '2016-07-21', 53.9, 'Heatwave'),
(6, 'PK-BA', 'Turbat', 'Pakistan', '2017-05-28', 53.7, 'Heatwave'),
(7, 'CN-HL', 'Mohe', 'China', '2023-01-22', -53.0, 'Extreme Cold'),
(8, 'AU-QL', 'Cloncurry', 'Australia', '1889-01-16', 53.1, 'Heatwave'),
(9, 'CA-BC', 'Lytton', 'Canada', '2021-06-29', 49.6, 'Heatwave'),
(10, 'GR-AT', 'Athens', 'Greece', '1977-07-10', 48.0, 'Heatwave'),
(11, 'IT-SI', 'Siracusa', 'Italy', '2021-08-11', 48.8, 'Heatwave'),
(12, 'PT-BE', 'Amareleja', 'Portugal', '2003-08-01', 47.3, 'Heatwave'),
(13, 'ES-AN', 'Montoro', 'Spain', '2021-08-14', 47.4, 'Heatwave'),
(14, 'RU-SA', 'Verkhoyansk', 'Russia', '2020-06-20', 38.0, 'Heatwave'),
(15, 'CA-YK', 'Snag', 'Canada', '1947-02-03', -63.0, 'Extreme Cold'),
(16, 'US-AK', 'Prospect Creek', 'USA', '1971-01-23', -62.2, 'Extreme Cold'),
(17, 'MN-UB', 'Ulan Bator', 'Mongolia', '2015-01-25', -40.5, 'Extreme Cold'),
(18, 'NO-NO', 'Bodoe', 'Norway', '2019-07-27', 34.6, 'Heatwave'),
(19, 'AR-CH', 'Sarmiento', 'Argentina', '1907-06-01', -32.8, 'Extreme Cold'),
(20, 'MA-FE', 'Ifrane', 'Morocco', '1935-02-11', -23.9, 'Extreme Cold'),
(21, 'NO-FI', 'Karasjok', 'Norway', '1886-01-01', -51.4, 'Extreme Cold'),
(22, 'FI-LA', 'Sodankyla', 'Finland', '1999-01-28', -51.5, 'Extreme Cold'),
(23, 'RS-VO', 'Novi Sad', 'Serbia', '2007-07-24', 44.8, 'Heatwave'),
(24, 'BA-HE', 'Mostar', 'Bosnia', '1901-07-31', 46.2, 'Heatwave'),
(25, 'RO-BV', 'Bod', 'Romania', '1942-01-25', -38.5, 'Extreme Cold'),
(26, 'RO-BR', 'Ion Sion', 'Romania', '1951-08-10', 44.5, 'Heatwave');
