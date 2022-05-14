CREATE DATABASE Project;
USE Project;

SET FOREIGN_KEY_CHECKS = 0;

/* Create a user for the database. */
/* after IDENTIFIED: WITH mysql_native_password */
CREATE USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';
GRANT ALL PRIVILEGES ON `Project` . * TO 'root'@'localhost';
FLUSH PRIVILEGES; 

/* Create Table */
CREATE TABLE IF NOT EXISTS Building
(
	Address VARCHAR(30) NOT NULL,
    Owner_Company VARCHAR(20),
    Zip_Code VARCHAR(10) NOT NULL, /* Zip Codes are 5 digits, sometimes a hyphen and 4 more digits */
    PO_Box INT,
    Building_ID VARCHAR(7),
    PRIMARY KEY(Building_ID)
);

CREATE TABLE IF NOT EXISTS Unit
(
	Unit_ID VARCHAR(7) NOT NULL,
    Unit_Number INT,
    Unit_Floor INT,
    Unit_Type VARCHAR(20),
    Num_of_Bedrooms INT,
    Num_of_Bathrooms INT,
    Balcony BOOL, /* We'll find out whether BOOL works; conflicting as to whether they do */
    Availability BOOL, /* We'll find out whether BOOL works; conflicting as to whether they do */
    Building_ID VARCHAR(7) NOT NULL,
    FOREIGN KEY(Building_ID) REFERENCES Building(Building_ID),
    PRIMARY KEY(Unit_ID)
);

CREATE TABLE IF NOT EXISTS Person
(
	ID VARCHAR(7),
    Person_Name VARCHAR(22),
    SSN VARCHAR(10), /* Value should be only the numbers */
    Permanent_Address VARCHAR(30),
    PRIMARY KEY(ID),
    PRIMARY KEY(SSN)
);

CREATE TABLE IF NOT EXISTS Lease
(
	Direct_or_Guarantor CHAR, /* D will mean Direct; G will mean Guarantor */
    Lease_ID VARCHAR(7),
    Renter_ID VARCHAR(7),
    Unit_ID VARCHAR(7),
    PRIMARY KEY(Lease_ID),
    FOREIGN KEY(Unit_ID) REFERENCES Unit(Unit_ID)
);

CREATE TABLE IF NOT EXISTS Payment_Ledger
(
	Lease_ID VARCHAR(7),
    Unit_ID VARCHAR(7),
    Renter_ID VARCHAR(7),
    Parking_Payment_ID VARCHAR(7),
    Work_Order_ID VARCHAR(7),
    PRIMARY KEY(Lease_ID, Unit_ID, Renter_ID),
    FOREIGN KEY(Lease_ID) REFERENCES Lease(Lease_ID),
	FOREIGN KEY(Unit_ID) REFERENCES Unit(Unit_ID),
    FOREIGN KEY(Renter_ID) REFERENCES Tenant(Renter_ID)
);

CREATE TABLE IF NOT EXISTS Inspection
(
	Inspection_Date_Time DATETIME, /* Year-Month-Day Hour:Minute:Second */
    Performed_By VARCHAR(20),
    Unit_ID VARCHAR(7),
    Building_ID VARCHAR(7),
    Inspection_ID VARCHAR(7),
    Reason LONGTEXT,
    PRIMARY KEY(Unit_ID, Building_ID, Inspection_ID),
    FOREIGN KEY(Unit_ID) REFERENCES Unit(Unit_ID),
    FOREIGN KEY(Building_ID) REFERENCES Building(Building_ID),
	FOREIGN KEY(Performed_By) REFERENCES Staff(Staff_ID)
);

CREATE TABLE IF NOT EXISTS Parking
(
	Permit_Number MEDIUMINT,
    License_Plate VARCHAR(7), 
    Govt_ID VARCHAR(12), /* We'll assume just MD Driver's Licenses which are 12 characters */
    Allowed_Floor INT,
    Parking_Payment_ID VARCHAR(7),
    PRIMARY KEY(Govt_ID, Permit_Number, Parking_Payment_ID),
    FOREIGN KEY(Govt_ID) REFERENCES Tenant(Govt_ID)
);

CREATE TABLE IF NOT EXISTS Maintenance_Request
(
	Unit_ID VARCHAR(7),
    Issue VARCHAR(30),
    Work_Order_ID VARCHAR(7),
    PRIMARY KEY(Unit_ID, Work_Order_ID),
    FOREIGN KEY(Unit_ID) REFERENCES Unit(Unit_ID)
);

CREATE TABLE IF NOT EXISTS Rent_Payment
(
	Payment_Deadline DATETIME NOT NULL,
    Payment_Date DATETIME NOT NULL,
    Amount_Paid DECIMAL(5, 2), /* Hopefully there are no rent payments over 5 figures */
    Payment_ID VARCHAR(7) NOT NULL,
    Unit_ID VARCHAR(7) NOT NULL,
    PRIMARY KEY(Payment_ID),
    FOREIGN KEY(Unit_ID) REFERENCES Unit(Unit_ID)
);

CREATE TABLE IF NOT EXISTS Amenities
(
	Location VARCHAR(20)
);