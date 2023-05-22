# Ref Card 03 mit RDS Mysql Datenbank

## Projektbeschreibung
Das Ref-Card-03-Projekt ist ein Docker-Utility, das Entwicklern ermöglicht, Docker-Container mit dem NGINX-Webserver und einer einfachen HTML-Datei bereitzustellen.

## Voraussetzungen
Betriebssystem: Das Ref-Card-03-Projekt kann auf Linux (WSL) ausgeführt werden.
Docker: Stellen Sie sicher, dass Docker auf Ihrem System installiert ist und Sie die erforderlichen Berechtigungen haben, um Docker-Container auszuführen.

## Git Repository herunterladen

Github Repository: [https://github.com/masluse/ref-card-03](https://github.com/masluse/ref-card-03)

Klonen Sie das Repository auf Ihren lokalen Computer und navigieren Sie in das Projektverzeichnis:
``` bash
git clone https://github.com/masluse/ref-card-03
cd ref-card-03
```

## RDS Instanz Erstellen

Um die RDS Instanz zu erstellen kann man den folgenden Schritten folgen:

Änderungen:

- Engine type = MariaDB

- Templates = Free tier

![Bild01.png](/images/ref-card-03/Bild01.png) 

Änderungen:

- DB instance identifier = jokedb

- Master username = 'Username'

- Master password = 'Password'

- Confirm master password = 'Password'

![Bild02.png](/images/ref-card-03/Bild02.png) 

Änderungen:

- Public access = Yes

- VPC security group = 3306 von deinem Client aus erreichbar

![Bild03.png](/images/ref-card-03/Bild03.png) 

Änderungen:

- Initial database name = jokedb

![Bild04.png](/images/ref-card-03/Bild04.png) 

## Git Repository umkonfigurieren

Änderungen:

- Endpoint in docker-compose.yml hinzufügen

- DB-USERNAME = 'Username' und DB_PASSWORD = 'Password' anpassen

![Bild05.png](/images/ref-card-03/Bild05.png) 

## Testen

``` bash
docker compose up
```

![Bild06.png](/images/ref-card-03/Bild06.png) 

Browser: localhost:8080

![Bild07.png](/images/ref-card-03/Bild07.png) 