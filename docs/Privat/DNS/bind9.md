# Bind9

=== "Debian"
    ## Debian

    ### Schritt 1: Installation
    Aktualisieren Sie das System und installieren Sie Bind9:

    ``` bash
    sudo apt update
    sudo apt install bind9 bind9utils bind9-doc
    ```

    ### Schritt 2: Zone erstellen
    Erstellen Sie eine neue Zone-Datei für Ihre Testdomain (z. B. example.com).
    Erstellen Sie die Datei /etc/bind/zones/db.example.com und fügen Sie den folgenden Inhalt ein:

    ``` bash title="/etc/bind/zones/db.example.com"
    $TTL    86400
    @       IN      SOA     ns1.clearsky.com. admin.clearsky.com. (
                        2022032201         ; Serial
                                3600         ; Refresh
                                1800         ; Retry
                                604800         ; Expire
                                86400 )       ; Minimum TTL

    ; Name Servers
    clearsky.com.     IN      NS      ns1.clearsky.com.

    ; A records
    ns1  IN      A       192.168.1.1
    clearsky.com.   IN      A       192.168.1.2

    ; Alias records
    erp.clearsky.com.    IN      CNAME   clearsky.com.
    www.clearsky.com.    IN      CNAME   clearsky.com.
    ```

    Passen Sie den Domainnamen, die E-Mail-Adresse und die IP-Adressen entsprechend Ihren Anforderungen an.

    ### Schritt 3: Zone hinzufügen
    Öffnen Sie die Bind9-Konfigurationsdatei /etc/bind/named.conf.local und fügen Sie Ihre Zone hinzu:

    ``` bash title="/etc/bind/named.conf.local"
    zone "example.com" {
    type master;
    file "/etc/bind/zones/db.example.com";
    };
    ```

    ### Schritt 4: Trust Lokalem Netzwerk
    Ändern Sie die Bind9-Optionen in der Datei /etc/bind/named.conf.options.

    Zum Beispiel, um DNS-Anfragen von Ihrem lokalen Netzwerk zuzulassen, fügen Sie die folgenden Zeilen hinzu:

    ``` bash title="/etc/bind/named.conf.options."
    acl "trusted" {
    192.168.1.0/24;
    };

    options {
    ...
    allow-query { trusted; };
    ...
    };
    ```

    ### Schritt 5: bind9 neustarten
    Starten Sie den Bind9-Dienst neu, um die neuen Einstellungen zu übernehmen:

    ``` bash
    sudo systemctl restart bind9
    ```

    ### Schritt 6: Check Konfiguration
    Überprüfen Sie die Bind9-Konfiguration und stellen Sie sicher, dass keine Fehlermeldungen auftreten:

    ``` bash
    sudo named-checkconf
    sudo named-checkzone example.com /etc/bind/zones/db.example.com
    ```

    ### Schritt 7: Testen
    Testen Sie Ihre DNS-Konfiguration mit dig:

    ``` bash
    dig @localhost example.com
    dig @localhost www.example.com
    ```

    Nun haben Sie erfolgreich Bind9 installiert und eine Testzone konfiguriert. Wenn Sie weitere Zonen hinzufügen oder die vorhandene Zone aktualisieren möchten, wiederholen Sie die Schritte 2-6 und passen Sie die Dateien und Einstellungen entsprechend an.

=== "Amazon Linux 2"

    ## Amazon Linux 2

    ### Schritt 1: Installation
    Aktualisieren Sie das System und installieren Sie Bind9:

    ``` bash
    sudo yum update
    sudo yum install bind bind-utils
    ```

    ### Schritt 2: Zone erstellen
    Erstellen Sie eine neue Zone-Datei für Ihre Testdomain (z. B. example.com).

    Erstellen Sie die Datei /var/named/db.example.com und fügen Sie den folgenden Inhalt ein:

    ``` bash title="/var/named/db.example.com"
    $TTL    86400
    @       IN      SOA     ns1.clearsky.com. admin.clearsky.com. (
                        2022032201         ; Serial
                                3600         ; Refresh
                                1800         ; Retry
                                604800         ; Expire
                                86400 )       ; Minimum TTL

    ; Name Servers
    clearsky.com.     IN      NS      ns1.clearsky.com.

    ; A records
    ns1      IN      A       192.168.1.1
    clearsky.com.   IN      A       192.168.1.2

    ; Alias records
    erp.clearsky.com.    IN      CNAME   clearsky.com.
    www.clearsky.com.    IN      CNAME   clearsky.com.
    ```

    Passen Sie den Domainnamen, die E-Mail-Adresse und die IP-Adressen entsprechend Ihren Anforderungen an.

    ### Schritt 3: Zone hinzufügen
    Öffnen Sie die Bind9-Konfigurationsdatei /etc/bind/named.conf.local und fügen Sie Ihre Zone hinzu:

    ``` bash title="/etc/bind/named.conf.local"
    zone "example.com" {
    type master;
    file "/var/named/db.example.com";
    };
    ```

    ### Schritt 4: Trust Lokalem Netzwerk
    Ändern Sie die Bind9-Optionen in der Datei /etc/named.conf.

    Zum Beispiel, um DNS-Anfragen von Ihrem lokalen Netzwerk zuzulassen, fügen Sie die folgenden Zeilen hinzu:

    ``` bash title="/etc/named.conf."
    acl "trusted" {
    192.168.1.0/24;
    };

    options {
    ...
    allow-query { trusted; };
    ...
    };
    ```

    ### Schritt 5: named neustarten
    Starten Sie den Bind9-Dienst neu, um die neuen Einstellungen zu übernehmen:

    ``` bash
    sudo systemctl restart named
    ```

    ### Schritt 6: Check Konfiguration
    Überprüfen Sie die Bind9-Konfiguration und stellen Sie sicher, dass keine Fehlermeldungen auftreten:

    ``` bash
    sudo named-checkconf
    sudo named-checkzone example.com /var/named/db.example.com
    ```

    ### Schritt 7: Testen
    Testen Sie Ihre DNS-Konfiguration mit dig:

    ``` bash
    dig @localhost example.com
    dig @localhost www.example.com
    ```

    Nun haben Sie erfolgreich Bind9 auf Amazon Linux 2 installiert und eine Testzone konfiguriert. Wenn Sie weitere Zonen hinzufügen oder die vorhandene Zone aktualisieren möchten, wiederholen Sie die Schritte 2-6 und passen Sie die Dateien und Einstellungen entsprechend an.
