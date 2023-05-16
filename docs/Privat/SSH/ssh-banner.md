# SSH Banner

## Nachricht vor dem Anmelden Anzeigen

### Schritt 1: Banner.txt Erstellen
Erstellen Sie eine Datei mit Ihrer benutzerdefinierten Nachricht, z. B. /etc/ssh/banner.txt:

``` bash
sudo nano /etc/ssh/banner.txt
```

### Schritt 2: Banner.txt befüllen
Fügen Sie Ihre Nachricht hinzu, z. B.:

``` title="/etc/ssh/banner.txt"
Willkommen auf dem Server! Bitte beachten Sie die Nutzungsbedingungen.
```

### Schritt 3: SSH-Konf öffnen
Öffnen Sie die SSH-Konfigurationsdatei /etc/ssh/sshd_config:

``` bash
sudo nano /etc/ssh/sshd_config
```

### Schritt 4: SSH-Konf bearbeiten
Fügen Sie die folgende Zeile am Ende der Datei hinzu:

``` title="/etc/ssh/sshd_config"
Banner /etc/ssh/banner.txt
```

### Schritt 5: SSH Neustarten
Starten Sie den SSH-Dienst neu, um die Änderungen zu übernehmen:

``` bash
sudo systemctl restart sshd
```