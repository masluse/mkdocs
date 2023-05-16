# db2 Befehle

------------------------------------------------
## SKRIPT AUSFÜHREN
------------------------------------------------

Führe das SQL-Skript "UEB03-00.sql" aus und zeige die Ergebnisse mit "db2 -tvf" an.

``` bash
db2 -tvf UEB03-00.sql
```

------------------------------------------------
## KONFIGURATION/PARAMETER AUSLESEN
------------------------------------------------

Lese die Konfiguration der DB2-Datenbankmanager-Instanz und filtere die Ergebnisse nach dem Parameter "numdb".

``` bash
db2 get dbm cfg | grep -i numdb
```

Verbinde dich mit der Datenbank "DBBW001" und lese ihre Konfigurationsparameter aus.

``` bash
db2 connect to DBBW001
```

Filtere die Ergebnisse nach dem Parameter "log".

``` bash
db2 get db cfg | grep -i log
```

------------------------------------------------
## KONFIGURATION/PARAMETER ANPASSEN
------------------------------------------------

Aktualisiere den Diagnoselevel der Datenbankmanager-Instanz auf "1".

``` bash
db2 update dbm cfg using DIAGLEVEL 1
```

Aktualisiere die Datenbankkonfiguration.

``` bash
db2 update db cfg
```

Aktualisiere den Parameter "NUMDB" der Datenbankmanager-Instanz auf "32".

``` bash
db2 UPDATE DBM CFG USING NUMDB 32
```

Aktualisiere den Parameter "LOGSECOND" der Datenbankkonfiguration auf "15".

``` bash
db2 UPDATE DB CFG USING LOGSECOND 15
```

Aktualisiere den Parameter "LOGSECOND" der Datenbank "dbbw001" auf "15".

``` bash
db2 UPDATE DB CFG FOR dbbw001 USING LOGSECOND 15
```
