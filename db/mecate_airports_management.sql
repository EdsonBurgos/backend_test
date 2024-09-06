use mecate_airports_management;

CREATE TABLE airlines
(
    id_airline int unsigned auto_increment not null comment "Identificador unico de aerolinea",
    name       varchar(50)                 not null comment "Nombre de la aerolinea",
    primary key (id_airline)
) engine = InnoDb;

INSERT INTO airlines
VALUES (NULL, 'Volaris');
INSERT INTO airlines
VALUES (NULL, 'Aeromar');
INSERT INTO airlines
VALUES (NULL, 'Interjet');
INSERT INTO airlines
VALUES (NULL, 'Aeromexico');

CREATE TABLE airports
(
    id_airport int unsigned auto_increment not null comment "Identificador unico del aeropuerto",
    name       varchar(50)                 not null comment "Nombre del aeropuerto",
    primary key (id_airport)
) engine = InnoDb;

INSERT INTO airports
VALUES (NULL, 'Benito Juarez');
INSERT INTO airports
VALUES (NULL, 'Guanajuato');
INSERT INTO airports
VALUES (NULL, 'La paz');
INSERT INTO airports
VALUES (NULL, 'Oaxaca');

CREATE TABLE movements_types
(
    id_movement_type int unsigned auto_increment not null comment "Identificador de movimiento",
    name             varchar(50)                 not null comment "Nombre del movimiento",
    primary key (id_movement_type)
) engine = InnoDb;

INSERT INTO movements_types
VALUES (NULL, 'Salida');
INSERT INTO movements_types
VALUES (NULL, 'Llegada');

CREATE TABLE flights
(
    id_airline       int unsigned not null comment "Identificador unico de aerolinea",
    id_airport       int unsigned not null comment "Identificador unico del aeropuerto",
    id_movement_type int unsigned not null comment "Identificador de movimiento",
    day              date         not null comment "fecha de vuelo",
    CONSTRAINT FK_FlightAirline FOREIGN KEY (id_airline) REFERENCES airlines (id_airline),
    CONSTRAINT FK_Flightairport FOREIGN KEY (id_airport) REFERENCES airports (id_airport),
    CONSTRAINT FK_FlightMovement FOREIGN KEY (id_movement_type) REFERENCES movements_types (id_movement_type)
) engine = InnoDb;

INSERT INTO flights
VALUES (1, 1, 1, '2021-05-02');
INSERT INTO flights
VALUES (2, 1, 1, '2021-05-02');
INSERT INTO flights
VALUES (3, 2, 2, '2021-05-02');
INSERT INTO flights
VALUES (4, 3, 2, '2021-05-02');
INSERT INTO flights
VALUES (1, 3, 2, '2021-05-02');
INSERT INTO flights
VALUES (2, 1, 1, '2021-05-02');
INSERT INTO flights
VALUES (2, 3, 1, '2021-05-04');
INSERT INTO flights
VALUES (3, 4, 1, '2021-05-04');
INSERT INTO flights
VALUES (3, 4, 1, '2021-05-04');