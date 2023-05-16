# Db2 Hofstetter Aufgabe 2

## Aufgabe 2

------------------------------------------------------------------------------------------

### Aufgabenstellung:

In dieser Übung sollen Sie die folgenden Objekte erstellen. Ziel dieses Auftrages ist es, dass Sie sich mit den entsprechenden CREATE Statements auseinandersetzen und auch lernen wie Sie mit SQL-Fehlern umgehen müssen
resp. wie Sie diese beheben.

Es sollen zwei Tabellen in der Datenbank DBBW001 erstellt werden. Für das Erstellen der benötigten Objekte soll
der Instanz-User db2inst1 verwendet werden.

• Erstellen Sie eine Tabelle BBWM141.TKLASSE mit folgenden Attributen (die Daten dieser Tabelle sollen
physisch im Tablespace SKLASSE gespeichert werden):

◦ Die Spalte TKLASSEID soll als Primärschlüssel definiert werden. Als Datentyp soll INTEGER für diese
Spalte gewählt werden.

◦ Die Spalte KLASSE ist ein eindeutiger Wert mit der Bezeichnung der Klasse (z.B. 5ip21a, 5ip21b,
etc.). Für diese Spalte muss immer ein Wert erfasst werden. Als Datentyp soll VARCHAR mit einer maximalen Grösse von 15 Zeichen definiert werden.

◦ In der Spalte KLASSENLEHRPERSON soll der Name des zuständigen Klassenlehrers erfasst werden. Als Datentyp soll VARCHAR mit einer maximalen Grösse von 50 Zeichen definiert werden. Das
Erfassen dieser Information ist optional.

◦ In der Spalte LASTUPDATE soll festgehalten werden WANN dieser Datensatz gespeichert wurde.
Dazu soll als Datentyp TIMESTAMP (Datum und Zeit) festgelegt werden. Falls beim Erfassen des Datensatzes kein Wert (Timestamp) angegeben wird, soll der DBM (Database Manager) diesen Wert automatisch einfügen.

• Erstellen Sie eine Tabelle BBWM141.TLERNENDE mit folgenden Attributen (die Daten dieser Tabelle sollen physisch im Tablespace SLERNENDER gespeichert werden):

◦ TLERNENDEID soll als Primärschlüssel festgelegt werden. Als Datentyp soll INTEGER für diese Spalte definiert werden. Wird beim Erfassen kein Primärschlüssel mitgegeben, soll der DBM diesen selbständig vergeben (IDENTITY).

◦ Die Spalte TKLASSEID soll als Fremdschlüssel definiert werden, damit die Zuteilung eines Lernenden
zu einer Klasse möglich ist. Das Erfassen der Klasse ist optional. Die Beziehung zwischen den beiden
Tabellen soll vom DBM verifiziert werden (RESTRICT Option).

◦ Die Spalten NAME und VORNAME sind als VARCHAR Felder mit einer maximalen Grösse von 50
Zeichen zu definieren. Beide Werte müssen zwingend erfasst werden.
Zusätzlich soll für diese beiden Spalten auch ein kombinierter Index (Name und Vorname) definiert
werden, damit Abfragen mit den Namen schnell sind.

◦ MAILADDR, in diesem Feld soll optional die Mail-Adresse erfasst werden können. Eine Mail-Adresse
kann maximal 50 Zeichen lang sein.

◦ In der Spalte LASTUPDATE soll festgehalten werden WANN dieser Datensatz gespeichert wurde.
Dazu soll als Datentyp TIMESTAMP (Datum und Zeit) festgelegt werden. Falls beim Erfassen des Datensatzes kein Wert (Timestamp) angegeben wird, soll der DBM (Database Manager) diesen Wert automatisch einfügen.
Erstellen Sie dazu folgende drei SQL-Scripts (Files):

• AUFG02D.sql – in diesem SQL-Script sollen die Objekte vorgängig gelöscht werden, damit jederzeit eine
"saubere" Ausgangslage erstellt werden kann.

• AUFG02C.sql – in diesem SQL-Script sollen alle benötigten Objekte erstellt werden.

• AUFG02INS.sql – in diesem SQL-Script sollen Sie in beiden Tabellen mittel INSERT Statement mindestens einen Datensatz einfügen (z.B. Ihre Klasse und Ihre Personen-Daten).

------------------------------------------------------------------------------------------

### Scripte:

------------------------------------------------------------------------------------------

``` sql title="AUFG02D.sql"
-- Löschen der Tabellen, falls vorhanden
DROP TABLE IF EXISTS BBWM141.TLERNENDE;
DROP TABLE IF EXISTS BBWM141.TKLASSE;
```

------------------------------------------------------------------------------------------

``` sql title="AUFG02C.sql"
/*
CREATE TABLESPACE SKLASSE
   PAGESIZE 4K
   MANAGED BY AUTOMATIC STORAGE;
  
CREATE TABLESPACE SLERNENDER
   PAGESIZE 4K
   MANAGED BY AUTOMATIC STORAGE;  
*/
  
  
-- Erstellen der Tabelle BBWM141.TKLASSE
CREATE TABLE BBWM141.TKLASSE (
    TKLASSEID INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1, INCREMENT BY 1),
    KLASSE VARCHAR(15) NOT NULL,
    KLASSENLEHRPERSON VARCHAR(50),
    LASTUPDATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (TKLASSEID)
) IN SKLASSE;

-- Erstellen der Tabelle BBWM141.TLERNENDE
CREATE TABLE BBWM141.TLERNENDE (
    TLERNENDEID INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1, INCREMENT BY 1),
    TKLASSEID INTEGER,
    NAME VARCHAR(50) NOT NULL,
    VORNAME VARCHAR(50) NOT NULL,
    MAILADDR VARCHAR(50),
    LASTUPDATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (TLERNENDEID),
	FOREIGN KEY (TKLASSEID) REFERENCES BBWM141.TKLASSE (TKLASSEID) ON DELETE RESTRICT ON UPDATE NO ACTION
) IN SLERNENDER;

-- Erstellen des kombinierten Index für BBWM141.TLERNENDE
CREATE INDEX IX_TLERNENDE_NAME_VORNAME ON BBWM141.TLERNENDE (NAME, VORNAME);
```

------------------------------------------------------------------------------------------

``` sql title="AUFG02INS.sql"
-- Einfügen von Daten in BBWM141.TKLASSE
INSERT INTO BBWM141.TKLASSE (KLASSE, KLASSENLEHRPERSON) VALUES ('5ip21a', 'Max Mustermann');
INSERT INTO BBWM141.TKLASSE (KLASSE, KLASSENLEHRPERSON) VALUES ('5ip21b', 'Maria Musterfrau');

-- Einfügen eines Datensatzes mit MAILADDR
INSERT INTO BBWM141.TLERNENDE (NAME, VORNAME, MAILADDR) VALUES ('Schmidt', 'Peter', 'peter.schmidt@example.com');

-- Einfügen eines Datensatzes ohne MAILADDR
INSERT INTO BBWM141.TLERNENDE (NAME, VORNAME) VALUES ('Müller', 'Anna');

-- Einfügen eines Datensatzes mit einem nicht existierenden TKlasseID
INSERT INTO BBWM141.TLERNENDE (NAME, VORNAME, MAILADDR) VALUES ('Bauer', 'Hans', 'hans.bauer@example.com');

```

------------------------------------------------------------------------------------------
