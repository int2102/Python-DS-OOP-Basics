CREATE DATABASE IF NOT EXISTS peaks;
USE peaks;
CREATE TABLE IF NOT EXISTS countries_details(
    Rank_europe INT,
    Country VARCHAR(30),
    Peak_name VARCHAR(40),
    Elevation INT
);
TRUNCATE TABLE countries_details;

INSERT INTO countries_details(Rank_europe,Country,Peak_name,Elevation) VALUES
(1,"Russia","Elbrus",5642),(2,"Georgia","Shkhara",5193),(3,"Turkey","Ararat",5137),(4,"Italy/France","Mont Blanc",4808),(5,"Switzerland","Dufourspitze",4634),(6,"Azerbaijan","Bazarduzu",4466),
(7,"Armenia","Mount Aragats",4090),(8,"Austria","Grossglockner",3798),(9,"Spain","Teide",3718),(10,"Norway","Gunnbjorn Fjeld",3694),(11,"Germany","Zugspitze",2962),(12,"Andorra","Coma Pedrosa",2943),
(13,"Bulgaria","Musala",2925),(14,"Greece","Mount Olympus GR",2917),(15,"Slovenia","Triglav",2864),(16,"Albania/North Macedonia","Mount Korab",2764),(17,"Kosovo/Serbia","Velika Rudoka",2660),(18,"Slovakia","Gerlachovsky",2655),
(19,"Liechtenstein","Vorder Grauspitz",2599),(20,"Romania","Moldoveanu",2544),(21,"Muntenegro","Zla Kolata",2534),(22,"Poland","Rysy",2499),(23,"Norway","Galdhopiggen",2469),(24,"Bosnia and Herzegovina","Maglic",2386),
(25,"Portugal","Mount Pico",2351),(26,"Iceland","Hvannadalshnukur",2110),(27,"Sweden","Kebnekaise",2097),(28,"Ukraine","Hoverla",2061),(29,"Cyprus","Mount Olympus CY",1952),(30,"Croatia","Dinara",1831),
(31,"Czechia","Snezka",1603),(32,"UK/Scotland","Ben Nevis",1345);

USE peaks;
CREATE TABLE IF NOT EXISTS peak_details(
    Peak_name VARCHAR(40),
    Elevation INT,
    Proeminence INT,
    Mountain_range VARCHAR(30)
);
TRUNCATE TABLE peak_details;
INSERT INTO peak_details(Peak_name,Elevation,Proeminence,Mountain_range) VALUES
("Elbrus",5642,4741,"Caucasus"),("Shkhara",5193,1357,"Caucasus"),("Ararat",5137,3611,"Armenian Mounts"),("Mont Blanc",4808,4696,"Alps"),("Dufourspitze",4634,2165,"Alps"),("Bazarduzu",4466,2454,"Caucasus"),
("Mount Aragats",4090,2143,"Armenian Mounts"),("Grossglockner",3798,2423,"Alps"),("Teide",3718,3718,"Stratovolcano"),("Gunnbjorn Fjeld",3694,3694,"Watkins Range"),("Zugspitze",2962,1746,"Alps"),("Coma Pedrosa",2943,434,"Pyrenees"),
("Musala",2925,2473,"Rila"),("Mount Olympus GR",2917,2353,NULL),("Triglav",2864,1280,"Alps"),("Mount Korab",2764,2169,"Korab"),("Velika Rudoka",2660,230,"Sar Mountains"),("Gerlachovsky",2655,955,"Carpathians"),
("Vorder Grauspitz",2599,353,"Alps"),("Moldoveanu",2544,2046,"Carpathians"),("Zla Kolata",2534,54,"Alps"),("Rysy",2499,161,"Carpathians"),("Galdhopiggen",2469,2436,"Jotunheimen"),("Maglic",2386,51,"Alps"),
("Mount Pico",2351,2351,NULL),("Hvannadalshnukur",2110,2110,"Vulcano"),("Kebnekaise",2097,1738,"Scandinavian Mountains"),("Hoverla",2061,721,"Carpathians"),("Mount Olympus CY",1952,1952,"Troodus"),("Dinara",1831,1086,"Alps"),
("Snezka",1603,1197,"Giant Mountains"),("Ben Nevis",1345,1345,NULL);
