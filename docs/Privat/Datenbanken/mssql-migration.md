# MSSQL Migration

## Full-Backup erstellen

Um eim Full-Backup zu erstellen von der TestDB auf der MSSQL 2017 kann man den folgenden Schritten folgen:

![Bildbeschreibung](/images/mssql-migration/Bild1.png)

Rechtsklicken Tasks/Sichern...

![Bildbeschreibung](/images/mssql-migration/Bild2.png)

Entweder default Backup Pfad beibehalten oder wie folgt ändern:

![Bildbeschreibung](/images/mssql-migration/Bild3.png)

![Bildbeschreibung](/images/mssql-migration/Bild4.png)

Nachdem man den richtigen Pfad ausgewählt hat kann man auf ok drücken. Nach einer gewissen zeit sollte die folgende Nachricht kommen:

![Bildbeschreibung](/images/mssql-migration/Bild5.png)

## DB Restoren

Um die DB auf dem MSSQL 2022 wiederherzustellen kann man den folgenden Schritten folgen.

"Datenanken" Rechtsklicken und auf "Datenbank wiederherstellen..." drücken:

![Bildbeschreibung](/images/mssql-migration/Bild6.png)

.bak file auswählen:

![Bildbeschreibung](/images/mssql-migration/Bild7.png)

Kontrollieren ob alles stimmt und dann auf OK:

![Bildbeschreibung](/images/mssql-migration/Bild8.png)

Schlussendlich sollte folgende Nachricht angezeigt werden:

![Bildbeschreibung](/images/mssql-migration/Bild9.png)

## Kontrollieren ob es erfolgreich war:

Um zu kontrollieren ob das migrieren der DB erfolgreich war kann man den Inthalt der test Tabelle kontrollieren:

Auf MSSQL 2022 kontrollieren:

![Bildbeschreibung](/images/mssql-migration/Bild10.png)

Auf MSSQL 2017 kontrollieren:

![Bildbeschreibung](/images/mssql-migration/Bild11.png)
