# SSH Anmeldung hinzufügen

## SSH Anmeldung zu User hinzufügen

### Schritt 1: Key generieren
Auf dem lokalem Rechner: Erstellen Sie ein SSH-Schlüsselpaar, falls noch nicht vorhanden. Öffnen Sie ein Terminal und führen Sie den folgenden Befehl aus:

``` bash
ssh-keygen
```

Folgen Sie den Anweisungen und akzeptieren Sie die Standardwerte, es sei denn, Sie möchten einen anderen Dateinamen oder ein anderes Verzeichnis für den Schlüssel angeben.

### Schritt 2: Schlüssel kopieren
Auf dem lokalem Rechner: Zeigen Sie den öffentlichen Schlüssel an und kopieren Sie den Inhalt:

``` bash
cat ~/.ssh/id_rsa.pub
```

Kopieren Sie den gesamten Inhalt, der angezeigt wird (beginnend mit "ssh-rsa").

### Schritt 3: Anmelden
Auf dem entfernten Server: Melden Sie sich als Benutzer John an

### Schritt 4: Verzeichnis erstellen
Auf dem entfernten Server: Erstellen Sie das .ssh-Verzeichnis im Home-Verzeichnis von John und legen Sie die richtigen Berechtigungen fest:

``` bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
```

### Schritt 5: Key hinzufügen
Auf dem entfernten Server: Erstellen Sie die Datei authorized_keys im .ssh-Verzeichnis von John und fügen Sie den zuvor kopierten öffentlichen Schlüssel ein:

``` bash
echo "PASTE_YOUR_PUBLIC_KEY_HERE" >> ~/.ssh/authorized_keys
```

Ersetzen Sie PASTE_YOUR_PUBLIC_KEY_HERE durch den zuvor kopierten öffentlichen Schlüssel.

### Schritt 6: Berechtigung
Auf dem entfernten Server: Legen Sie die richtigen Berechtigungen für die authorized_keys-Datei fest:

``` bash
chmod 600 ~/.ssh/authorized_keys
```

### Schritt 7: Testen
Auf dem entfernten Server: Melden Sie sich von Johns Konto ab:

``` bash
exit
```

Nun kann John sich über SSH mit dem entfernten Server verbinden, indem er den folgenden Befehl auf seinem lokalen Rechner ausführt:

``` bash
ssh john@REMOTE_SERVER_IP
```

Ersetzen Sie REMOTE_SERVER_IP durch die IP-Adresse oder den Hostnamen des entfernten Servers. Da John seinen privaten Schlüssel verwendet, wird er nicht nach einem Passwort gefragt.
