# db2 Befehle

------------------------------------------------
## SCRIPT AUSFÜHREN
------------------------------------------------

Für das Ausführen des SQL-Skripts "UEB03-00.sql" und das Anzeigen der Ergebnisse, nutzt du den "db2 -tvf"-Befehl. Hier ist der komplette Befehl:

``` bash
db2 -tvf UEB03-00.sql
```

------------------------------------------------
## KONFIGURATION/PARAMETER AUSLESEN
------------------------------------------------

Um die Konfiguration der DB2-Datenbankmanager-Instanz auszulesen und die Ergebnisse nach dem Parameter "numdb" zu filtern, verwendest du den folgenden Befehl:

``` bash
db2 get dbm cfg | grep -i numdb
```

Zum Verbinden mit der Datenbank "DBBW001" und Auslesen ihrer Konfigurationsparameter, nutze diesen Befehl:

``` bash
db2 connect to DBBW001
db2 get db cfg | grep -i log
```

------------------------------------------------
## KONFIGURATION/PARAMETER ANPASSEN
------------------------------------------------

Zur Aktualisierung des Diagnoselevels der Datenbankmanager-Instanz auf "1" und zur Anpassung von Konfigurationsparametern, verwendest du diese Befehle:

``` bash
db2 update dbm cfg using DIAGLEVEL 1
db2 update db cfg
db2 UPDATE DBM CFG USING NUMDB 32
db2 UPDATE DB CFG USING LOGSECOND 15
db2 UPDATE DB CFG FOR dbbw001 USING LOGSECOND 15
```

------------------------------------------------
## BERECHTIGUNGEN VERWALTEN
------------------------------------------------

Um Berechtigungen zu vergeben, nutzt du die folgenden SQL-Statements. Sie spezifizieren die gewünschten Autorisierungen für bestimmte Nutzergruppen und individuelle Nutzer.

``` bash
db2 CONNECT TO DBBW001;

-- Autorisierungen für die Gruppe dbusrgrp
db2 GRANT DATAACCESS ON DATABASE TO GROUP dbusrgrp;

-- Autorisierungen für die Gruppe dbadmgrp
db2 GRANT DBADM WITHOUT DATAACCESS ON DATABASE TO GROUP dbadmgrp;

db2 CONNECT TO DBBW002;

-- Autorisierungen für die Gruppe dbusrgrp
db2 GRANT DATAACCESS ON DATABASE TO GROUP dbusrgrp;

-- Autorisierungen für die Gruppe dbadmgrp
db2 GRANT DBADM WITHOUT DATAACCESS ON DATABASE TO GROUP dbadmgrp;

-- Autorisierungen für User dbuser10
db2 GRANT CREATETAB, IMPLICIT_SCHEMA ON DATABASE TO USER dbuser10;
db2 GRANT USE OF TABLESPACE USERSPACE1 TO USER dbuser10;

-- Autorisierungen für User dbuser11
db2 GRANT CREATETAB, IMPLICIT_SCHEMA ON DATABASE TO USER dbuser11;
db2 GRANT USE OF TABLESPACE USERSPACE1 TO USER dbuser11;

-- Autorisierungen für User dbuser12
db2 GRANT CREATETAB, IMPLICIT_SCHEMA ON DATABASE TO USER dbuser12;
db2 GRANT USE OF TABLESPACE USERSPACE1 TO USER dbuser12;
```

Zum Erstellen einer Rolle und zum Setzen von Berechtigungen für diese Rolle, nutze die folgenden Befehle:

``` bash 
db2 CONNECT TO DBBW002;

-- Erstellen der Rolle "TESTER"
db2 CREATE ROLE TESTER;

-- Autorisierungen für die Rolle "TESTER"
db2 GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE DBUSER10.TDBS_PERSON TO ROLE TESTER;
db2 GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE DBUSER11.TDBS_PERSON TO ROLE TESTER;
db2 GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE DBUSER12.TDBS_PERSON TO ROLE TESTER;

db2 GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE DBUSER10.TDBS_ABTEILUNG TO ROLE TESTER;
db2 GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE DBUSER11.TDBS_ABTEILUNG TO ROLE TESTER;
db2 GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE DBUSER12.TDBS_ABTEILUNG TO ROLE TESTER;

-- Setzen der Rolle "TESTER" für die Benutzer "tester01" und "tester02"
db2 GRANT ROLE TESTER TO USER tester01;
db2 GRANT ROLE TESTER TO USER tester02;

db2 GRANT CONNECT ON DATABASE TO ROLE TESTER;
db2 GRANT USAGE ON WORKLOAD SYSDEFAULTUSERWORKLOAD TO ROLE TESTER;
db2 GRANT EXECUTE ON PACKAGE NULLID.SQLC2P31 TO ROLE TESTER;
```