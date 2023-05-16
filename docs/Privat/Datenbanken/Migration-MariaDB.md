# MariaDB Migration

## Schritt 1: Vorbereitung

Notieren Sie sich die Zugangsdaten (Benutzername, Passwort) und Konfigurationsdetails Ihrer aktuellen MariaDB-Instanz auf EC2.

## Schritt 2: RDS DB Erstellen
Erstellen Sie eine RDS-Instanz

a. Melden Sie sich bei der AWS Management Console an und navigieren Sie zum RDS-Dashboard.

b. Klicken Sie auf "Datenbank erstellen" und wählen Sie "MariaDB" als Datenbank-Engine aus.

![Bildbeschreibung](/images/mariadb-migration/Bild1.png)

c. Konfigurieren Sie die RDS-Instanz gemäß Ihren Anforderungen (DB-Instanzklasse, Speicher, Multi-AZ-Bereitstellung usw.).

![Bildbeschreibung](/images/mariadb-migration/Bild2-v02.png)

![Bildbeschreibung](/images/mariadb-migration/Bild3.png)

d. Geben Sie die Zugangsdaten und den Datenbanknamen an, die Sie in Schritt 1b notiert haben.

![Bildbeschreibung](/images/mariadb-migration/Bild4.png)

e. Whlen Sie die richtige VPC und Sicherheitsgruppe, um die Kommunikation zwischen Ihrer EC2-Instanz und der RDS-Instanz zu ermöglichen.

![Bildbeschreibung](/images/mariadb-migration/Bild5.png)

f. Klicken Sie auf "Datenbank erstellen" und warten Sie, bis der Vorgang abgeschlossen ist.

![Bildbeschreibung](/images/mariadb-migration/Bild6.png)

## Schritt 3: Dump Erstellen
Erstellen Sie einen Datenbank-Dump von Ihrer EC2-Instanz

a. Melden Sie sich bei Ihrer EC2-Instanz über SSH an.

![Bildbeschreibung](/images/mariadb-migration/Bild7.png)

b. Stellen Sie sicher, dass der mysqldump-Befehl installiert ist.

![Bildbeschreibung](/images/mariadb-migration/Bild8.png)

c. Führen Sie den folgenden Befehl aus, um einen Datenbank-Dump zu erstellen:

``` bash
mysqldump -u [BENUTZERNAME] -p --databases [DATENBANKNAME] --single-transaction --compress --order-by-primary > backup.sql
```

Ersetzen Sie [BENUTZERNAME] und [DATENBANKNAME] durch die entsprechenden Werte.

![Bildbeschreibung](/images/mariadb-migration/Bild9.png)

## Schritt 4: Dump Importieren
Importieren Sie den Datenbank-Dump in Ihre RDS-Instanz

a. Notieren Sie sich die Endpunkt-URL Ihrer RDS-Instanz aus dem RDS-Dashboard.

![Bildbeschreibung](/images/mariadb-migration/Bild10.png)

b. Führen Sie den folgenden Befehl aus, um den Datenbank-Dump in die RDS-Instanz zu importieren:

``` bash
mysql -h [RDS-ENDPUNKT] -u [BENUTZERNAME] -p [DATENBANKNAME] < backup.sql
```

Ersetzen Sie [RDS-ENDPUNKT], [BENUTZERNAME] und [DATENBANKNAME] durch die entsprechenden Werte.

![Bildbeschreibung](/images/mariadb-migration/Bild11.png)

## Schritt 5: Aktualisieren
Aktualisieren Sie Ihre Anwendung, um die RDS-Instanz zu verwenden

a. Aktualisieren Sie die Datenbankverbindungsparameter in Ihrer Anwendung, um auf die RDS-Instanz zu verweisen.

b. Starten Sie Ihre Anwendung neu, um die Änderungen zu übernehmen.

## Schritt 6: Testen
Testen und überwachen Sie Ihre Anwendung
