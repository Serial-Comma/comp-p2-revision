CREATE TABLE Book (
    BookID INTEGER,
    Title TEXT,
    Price INTEGER,
    Type TEXT CHECK(Type = 'Physical' OR Type = 'Virtual'),
    PRIMARY KEY (BookID)
);
CREATE TABLE Printed (
    BookID INTEGER,
    Weight INTEGER,
    PRIMARY KEY (BookID),
    FOREIGN KEY (BookID) REFERENCES Book(BookID)
);
CREATE TABLE Virtual (
    BookID INTEGER,
    DownloadLink TEXT,
    PRIMARY KEY (BookID),
    FOREIGN KEY (BookID) REFERENCES Book(BookID)
);
