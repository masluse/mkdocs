# Wireguard Server Installation

## Installation

=== "Debian"
    Aktualisieren Sie das System und installieren Sie benötigte Pakete

    ``` bash
    sudo apt update
    sudo apt upgrade
    sudo apt install linux-headers-$(uname -r) wireguard
    ```

=== "Amazon Linux 2"

    Installieren Sie das EPEL-Repository und aktualisieren Sie das System

    ``` bash
    sudo amazon-linux-extras install epel
    sudo yum update
    sudo yum install wireguard-tools
    ```

## Allgemein:

### Schritt 1: Konfigurations Datei
Erstellen Sie die WireGuard-Konfigurationsdatei

``` bash
sudo mkdir /etc/wireguard
sudo nano /etc/wireguard/wg0.conf
```

### Schritt 2: Konfiguration
Fügen Sie die folgende Konfiguration in die Datei ein und passen Sie sie nach Bedarf an

``` conf title="/etc/wireguard/wg0.conf"
[Interface]
Address = 10.0.0.1/24, fd42:42:42::1/64
PrivateKey = <ServerPrivateKey>
ListenPort = 51820

[Peer]
PublicKey = <ClientPublicKey>
AllowedIPs = 10.0.0.2/32, fd42:42:42::2/128
```

Ersetzen Sie "ServerPrivateKey" durch den privaten Schlüssel des Servers und "ClientPublicKey" durch den öffentlichen Schlüssel des Clients.
Vergeben Sie für jeden weiteren Client eine eigene IP-Adresse und fügen Sie einen neuen [Peer]-Abschnitt hinzu.

### Schritt 3: WireGuard Starten
Aktivieren und starten Sie den WireGuard-Server

``` bash
sudo systemctl enable --now wg-quick@wg0
```

Nachdem Sie den WireGuard-Server auf Debian oder Amazon Linux 2 installiert und konfiguriert haben, müssen Sie den entsprechenden Client konfigurieren, um eine Verbindung zum Server herzustellen.