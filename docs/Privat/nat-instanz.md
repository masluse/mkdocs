# NAT-Instanz

## Schritt 1: Instanz Erstellen
Erstellen Sie eine neue Amazon Linux 2-Instanz

Erstellen Sie eine neue EC2-Instanz in der AWS Management Console. Wählen Sie als Betriebssystem "Amazon Linux 2". Stellen Sie sicher, dass die Instanz in der richtigen VPC und Subnetz ist.

## Schritt 2: Sicherheitsgruppen konfigurieren

Erstellen Sie eine Sicherheitsgruppe für die NAT-Instanz. Diese sollte ausgehenden Datenverkehr für das private Subnetz erlauben und eingehenden Datenverkehr nur für dasjenige zulassen, was für die Administration erforderlich ist (z.B. SSH). Vergessen Sie nicht, die Sicherheitsgruppe für die NAT-Instanz in der EC2-Instanzkonfiguration auszuwählen.

## Schritt 3: IP-Weiterleitung
Aktivieren Sie die IP-Weiterleitung

Melden Sie sich über SSH bei der EC2-Instanz an und führen Sie den folgenden Befehl aus, um die IP-Weiterleitung zu aktivieren:

``` bash
sudo sysctl -w net.ipv4.ip_forward=1
```

Um diese Einstellung dauerhaft zu machen, öffnen Sie die Datei /etc/sysctl.conf mit einem Texteditor (z.B. vi oder nano) und fügen Sie die folgende Zeile hinzu:

``` conf title="/etc/sysctl.conf"
net.ipv4.ip_forward = 1
```

## Schritt 4: Source/Dest Check
Konfigurieren Sie Source/Destination Check

Gehen Sie zur EC2-Managementkonsole und wählen Sie die NAT-Instanz aus. Klicken Sie im Detailbereich auf "Aktionen" und wählen Sie "Netzwerkschnittstellen ändern". Klicken Sie auf das Eingabefeld und wählen Sie die Netzwerkschnittstelle aus, die der Instanz zugeordnet ist. Klicken Sie auf das Zahnradsymbol und deaktivieren Sie die Option "Source/Destination Check".

## Schritt 5: iptables
Konfigurieren Sie die iptables-Regeln

Führen Sie die folgenden Befehle aus, um die iptables-Regeln für die NAT-Instanz zu konfigurieren:

``` bash
sudo iptables -t nat -A POSTROUTING -o eth0 -s 10.0.0.0/16 -j MASQUERADE
```

Ersetzen Sie eth0 durch den Namen der Netzwerkschnittstelle, die mit dem Internet verbunden ist, und 10.0.0.0/16 durch den CIDR-Block Ihres privaten Subnetzes.

Speichern Sie die iptables-Regeln dauerhaft, indem Sie den folgenden Befehl ausführen:

``` bash
sudo iptables-save | sudo tee /etc/sysconfig/iptables
```

## Schritt 6: VPC Route Erstellen
Erstellen Sie eine neue Route für das private Subnetz

Gehen Sie zur VPC-Managementkonsole und wählen Sie die Routingtabelle für das private Subnetz aus. Fügen Sie eine neue Route hinzu, bei der das Ziel 0.0.0.0/0 ist und die Ziel-Instanz-ID die ID Ihrer NAT-Instanz ist.

## Schritt 7: Testen
Testen Sie die Verbindung

Melden Sie sich bei einer Instanz im privaten Subnetz an und testen Sie die Verbindung
