# Ticket system (Peppermint)

## Hardware
Als erster Schritt benötigt man Hardware. Man kann das entweder on-premises oder in der Cloud durchführen. Für dieses Beispiel habe ich mich für die Hetzner Cloud entschieden, aber es funktioniert auch mit anderen Anbietern.

![Bildbeschreibung](/images/ticket-system/Bild1.png)

![Bildbeschreibung](/images/ticket-system/Bild2.png)

## Verbinden und Peppermint Installieren (Docker)

Nachdem man ein System hat, auf dem man Peppermint installieren möchte, verbindet man sich damit.

![Bildbeschreibung](/images/ticket-system/Bild3.png)

Danach führt man folgende Befehle aus:

``` bash
sudo apt update
sudo apt upgrade -y
sudo apt install docker.io docker-compose -y
mkdir peppermint
cd peppermint
nano docker-compose.yml
```

In das docker-compose.yml-File fügt man den folgenden Inhalt ein:

``` yml title="docker-compose.yml"
version: "3.1"

services:
  postgres:
    container_name: postgres
    image: postgres:latest
    restart: always
    volumes:
      - ./docker-data/db:/data/db
    environment: 
      POSTGRES_USER: peppermint
      POSTGRES_PASSWORD: 1234
      POSTGRES_DB: peppermint

  client:
    container_name: peppermint
    image: pepperlabs/peppermint:latest
    ports:
      - 5000:5000
    restart: on-failure
    depends_on:
      - postgres
    environment:
      PORT: 5000
      DB_USERNAME: peppermint
      DB_PASSWORD: 1234
      DB_HOST: 'postgres'
      BASE_URL: "http://{Your IP or DNS}:5000"
```
Quelle: https://github.com/Peppermint-Lab/peppermint

Wenn dies erledigt ist, speichern Sie die Datei und führen Sie die folgenden Befehle aus:

``` bash
sudo docker-compose up -d
sudo docker ps
```

![Bildbeschreibung](/images/ticket-system/Bild4.png)

## Testen / Anmelden

Wenn alles erledigt ist, verbinden Sie sich / melden Sie sich auf der Seite http://{Ihre IP oder DNS}:5000 an.

![Bildbeschreibung](/images/ticket-system/Bild5.png)

![Bildbeschreibung](/images/ticket-system/Bild6.png)
