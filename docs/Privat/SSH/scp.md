# SCP (Dateien per SSH Kopieren)

## CMD Öffnen

1. Öffnen Sie die Eingabeaufforderung (CMD) auf Ihrem lokalen Computer.

## Navigieren

2. Navigieren Sie zu dem Verzeichnis, in dem sich die Dateien befinden, die Sie übertragen möchten.

## Befehl

3. Geben Sie den folgenden Befehl ein, um die Datei auf den entfernten Server zu kopieren:

``` bash
scp [lokaldatei] [benutzername]@[serveradresse]:[zielverzeichnis]
```

Ersetzen Sie [lokaldatei] durch den Namen der Datei, die Sie übertragen möchten, und [serveradresse] durch die IP-Adresse oder den Hostnamen des entfernten Servers. [benutzername] ist der Name des Benutzers, mit dem Sie sich auf dem entfernten Server anmelden möchten, und [zielverzeichnis] ist das Verzeichnis auf dem entfernten Server, in das Sie die Datei kopieren möchten.

Beispiel:

``` bash
scp mydocument.txt john@example.com:/home/john/documents/
```

Dieser Befehl kopiert die Datei "mydocument.txt" vom aktuellen Verzeichnis auf dem lokalen Computer auf den Server "example.com" im Verzeichnis "/home/john/documents/".

4. Geben Sie Ihr Passwort ein, wenn Sie dazu aufgefordert werden.

5. Sobald der Vorgang abgeschlossen ist, wird eine Bestätigung angezeigt, dass die Datei erfolgreich übertragen wurde.