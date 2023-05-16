# sudo ohne Passwort

## Sudo ohne Passwort

### Schritt 1: visudo öffnen
Öffnen Sie die Datei /etc/sudoers mit visudo, um sie sicher zu bearbeiten:

``` bash
sudo visudo
```

### Schritt 2: Zeile finden
Suchen Sie die Zeile, die der Gruppe, der John angehört, Sudo-Rechte gewährt:

=== "Debian/Ubuntu"

    ``` bash
    %sudo   ALL=(ALL:ALL) ALL
    ```

=== "Amazon Linux 2"

    ``` bash
    %wheel  ALL=(ALL)       ALL
    ```

### Schritt 3: Zeile bearbeiten
Duplizieren Sie die Zeile und ändern Sie sie, um NOPASSWD hinzuzufügen:

=== "Debian/Ubuntu"

    ``` bash
    %sudo   ALL=(ALL:ALL) NOPASSWD: ALL
    ```

=== "Amazon Linux 2"

    ``` bash
    %wheel  ALL=(ALL)       NOPASSWD: ALL
    ```

### Schritt 4: Speichern
Speichern Sie die Änderungen und schließen Sie den Editor.