CREATE TABLE bericht(
berichtnr INTEGER NOT NULL,
bericht VARCHAR(140),
naam VARCHAR(255),
station VARCHAR(255),
datum DATE NOT NULL,
tijd TIME NOT NULL
);

CREATE TABLE moderator(
werknemernr INTEGER NOT NULL,
naam VARCHAR(255),
emailadres VARCHAR(255)
);
CREATE TABLE beoordeling(
beoordelingnr INTEGER NOT NULL,
datum DATE NOT NULL,
tijd TIME NOT NULL,
afgekeurd bool NOT NULL,
werknemernr INTEGER NOT NULL,
berichtnr INTEGER NOT NULL
);

ALTER TABLE bericht ADD PRIMARY KEY(berichtnr);
ALTER TABLE moderator ADD PRIMARY KEY(werknemernr);
ALTER TABLE beoordeling ADD PRIMARY KEY(beoordelingnr);

ALTER TABLE beoordeling ADD CONSTRAINT fk_werknemernr FOREIGN KEY(werknemernr) REFERENCES moderator(werknemernr);
ALTER TABLE beoordeling ADD CONSTRAINT fk_berichtnr FOREIGN KEY(berichtnr) REFERENCES bericht(berichtnr);