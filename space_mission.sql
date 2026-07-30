CREATE DATABASE IF NOT EXISTS space_exploration;
USE space_exploration;

CREATE TABLE IF NOT EXISTS space_missions (
    mission_id INT PRIMARY KEY,
    company VARCHAR(30),
    rocket_name VARCHAR(30),
    launch_date DATE,
    cost_millions DECIMAL(10,2),
    mission_status VARCHAR(20),
    orbit_type VARCHAR(20)
);

TRUNCATE TABLE space_missions;

INSERT INTO space_missions(mission_id, company, rocket_name, launch_date, cost_millions, mission_status, orbit_type) VALUES
(1, 'SpaceX', 'Falcon 9', '2020-05-30', 50.00, 'Success', 'LEO'),
(2, 'NASA', 'Space Shuttle', '2011-07-08', 450.00, 'Success', 'LEO'),
(3, 'Roscosmos', 'Soyuz', '2018-10-11', 45.00, 'Failure', 'LEO'),
(4, 'SpaceX', 'Falcon Heavy', '2018-02-06', 90.00, 'Success', 'HEO'),
(5, 'ESA', 'Ariane 5 (James Webb)', '2021-12-25', 10000.00, 'Success', 'HEO'),
(6, 'Blue Origin', 'New Shepard', '2021-07-20', NULL, 'Success', 'Suborbital'),
(7, 'NASA', 'Saturn V (Apollo 11)', '1969-07-16', 1160.00, 'Success', 'Lunar'),
(8, 'SpaceX', 'Starship', '2023-04-20', 3000.00, 'Failure', 'LEO'),
(9, 'ISRO', 'PSLV', '2013-11-05', 73.00, 'Success', 'Martian'),
(10, 'Rocket Lab', 'Electron', '2020-07-04', 7.50, 'Failure', 'LEO'),
(11, 'NASA', 'Atlas V (Perseverance)', '2020-07-30', 2700.00, 'Success', 'Martian'),
(12, 'SpaceX', 'Falcon 9', '2023-03-02', 50.00, 'Success', 'LEO'),
(13, 'JAXA', 'H-IIA', '2014-12-03', 150.00, 'Success', 'Asteroid'),
(14, 'SpaceX', 'Falcon Heavy', '2023-10-13', 90.00, 'Success', 'HEO'),
(15, 'Virgin Galactic', 'SpaceShipTwo', '2021-07-11', NULL, 'Success', 'Suborbital');