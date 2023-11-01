CREATE TABLE bericht(
bericht VARCHAR(140),
naam VARCHAR(255),
station VARCHAR(255),
datum DATE NOT NULL,
tijd TIME NOT NULL,
berichtnr  SERIAL NOT NULL
);

CREATE TABLE moderator(
naam VARCHAR(255),
emailadres VARCHAR(255),
werknemernr SERIAL
);
CREATE TABLE beoordeling(
datum DATE NOT NULL,
tijd TIME,
afgekeurd bool NOT NULL,
werknemernr INTEGER,
berichtnr INTEGER,
beoordelingnr SERIAL
);

ALTER TABLE bericht ADD PRIMARY KEY(berichtnr);
ALTER TABLE moderator ADD PRIMARY KEY(werknemernr);
ALTER TABLE beoordeling ADD PRIMARY KEY(beoordelingnr);

ALTER TABLE beoordeling ADD CONSTRAINT fk_werknemernr FOREIGN KEY(werknemernr) REFERENCES moderator(werknemernr);
ALTER TABLE beoordeling ADD CONSTRAINT fk_berichtnr FOREIGN KEY(berichtnr) REFERENCES bericht(berichtnr);