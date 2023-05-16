# SSH Installation

## SSH Installieren

### Schritt 1: Installation
SSH Installieren auf Debian und Amazon Linux 2

Debian/Ubuntu:

``` bash
sudo apt update
sudo apt install openssh-server
```

Amazon Linux 2:

``` bash
sudo yum update
sudo yum install openssh-server
```

### Schritt 2: Autostart
Starten Sie den SSH-Dienst und aktivieren Sie ihn beim Systemstart:

``` bash
sudo systemctl start sshd
sudo systemctl enable sshd
```