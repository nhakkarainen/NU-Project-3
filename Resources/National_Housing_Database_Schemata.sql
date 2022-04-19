-- Delete pre-existing tables
DROP TABLE IF EXISTS days_on_market;
DROP TABLE IF EXISTS housing_prices;

-- Create new tables:
CREATE TABLE days_on_market (
	StateID INT NOT NULL PRIMARY KEY,
	StateName VARCHAR(50) NOT NULL,
	"Feb2018" INT,
	"Mar2018" INT,
	"Apr2018" INT,
	"May2018" INT,
	"Jun2018" INT,
	"Jul2018" INT,
	"Aug2018" INT,
	"Sep2018" INT,
	"Oct2018" INT,
	"Nov2018" INT,
	"Dec2018" INT,
	"Jan2019" INT,
	"Feb2019" INT,
	"Mar2019" INT,
	"Apr2019" INT,
	"May2019" INT,
	"Jun2019" INT,
	"Jul2019" INT,
	"Aug2019" INT,
	"Sep2019" INT,
	"Oct2019" INT,
	"Nov2019" INT,
	"Dec2019" INT,
	"Jan2020" INT,
	"Feb2020" INT
);

CREATE TABLE housing_prices (
	"Index" INT NOT NULL PRIMARY KEY,
	CityID INT,
	CityName VARCHAR(50) NOT NULL,
	"State" VARCHAR(50) NOT NULL,
	CountyName VARCHAR(50) NOT NULL,
	NoOfBeds INT,
	"Mar2018" INT,
	"Apr2018" INT,
	"May2018" INT,
	"Jun2018" INT,
	"Jul2018" INT,
	"Aug2018" INT,
	"Sep2018" INT,
	"Oct2018" INT,
	"Nov2018" INT,
	"Dec2018" INT,
	"Jan2019" INT,
	"Feb2019" INT,
	"Mar2019" INT,
	"Apr2019" INT,
	"May2019" INT,
	"Jun2019" INT,
	"Jul2019" INT,
	"Aug2019" INT,
	"Sep2019" INT,
	"Oct2019" INT,
	"Nov2019" INT,
	"Dec2019" INT,
	"Jan2020" INT,
	"Feb2020" INT,
	"Mar2020" INT
);

-- Import datasets into each table in order tables created; account for headers.
-- Verify datasets imported correctly:
SELECT * FROM days_on_market;
SELECT * FROM housing_prices;