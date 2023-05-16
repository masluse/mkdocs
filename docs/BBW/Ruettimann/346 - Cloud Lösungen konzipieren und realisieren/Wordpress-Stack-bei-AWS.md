## Wordpress Stack bei AWS

### Auftrag

![Bild01.png](/images/Wordpress-Stack-bei-AWS/Bild01.png)

![Bild02.png](/images/Wordpress-Stack-bei-AWS/Bild02.png)

### WordPress mit Amazon RDS bereitstellen

#### Erstellen einer MySQL-Datenbank mit RDS

Um eine Datenbank zu erstellen, muss unter Amazon Cloud nach RDS suchen und dann auf «Datenbank erstellen» gehen.

![Bild03.png](/images/Wordpress-Stack-bei-AWS/Bild03.png)

Als Engine-Typ benutzen wir MySQL

![Bild04.png](/images/Wordpress-Stack-bei-AWS/Bild04.png)

Als Vorlage benutzen man „Kostenloses Kontingent“

![Bild05.png](/images/Wordpress-Stack-bei-AWS/Bild05.png)

In den Einstellungen ändern man die DB-Instance-Kennung zu „WordPress“, den Hauptbenutzernamen zu „admin“ (falls anders) und das Passwort kann man selbst wählen.

![Bild06.png](/images/Wordpress-Stack-bei-AWS/Bild06.png)

Als nächstes öffnet man den Reiter „Zusätzliche Konfiguration“

![Bild07.png](/images/Wordpress-Stack-bei-AWS/Bild07.png)

Dort ändert man noch den „Anfänglicher Datenbankname“ zu wordpress

![Bild08.png](/images/Wordpress-Stack-bei-AWS/Bild08.png)

Wenn dies alles Konfiguriert ist drückt man auf Datenbank erstellen

![Bild09.png](/images/Wordpress-Stack-bei-AWS/Bild09.png)

#### Erstellen einer EC2-Instance

Um eine EC2-Instanz zu erstellen, sucht man in der Suche nach EC2 und geht dann wenn man es gefunden hat auf „Instance starten“

![Bild10.png](/images/Wordpress-Stack-bei-AWS/Bild10.png)

Als Name kann man nehmen, was man will, Ich habe mich für „EC2-WordPress“ entschieden.

![Bild11.png](/images/Wordpress-Stack-bei-AWS/Bild11.png)

Als Image kann man im Grunde jedes nehmen, Ich würde aber „Amazon Linux“ benutzen da die Befehle auf einem anderen OS eine andere Syntax haben.

![Bild12.png](/images/Wordpress-Stack-bei-AWS/Bild12.png)

Für die Kostenlose Benutzung würde ich die „t2.micro“ nehmen da diese 750 Stunden pro Monat kostenlos benutzbar ist.

![Bild13.png](/images/Wordpress-Stack-bei-AWS/Bild13.png)

Als Schlüsselpaar (SSH Key) kann man entweder einen neuen erstellen oder einen bereits vorhandenes verwenden.

![Bild14.png](/images/Wordpress-Stack-bei-AWS/Bild14.png)

In den Netzwerkeinstellungen ändert man zur einfachheitshalber den Namen und die Beschreibung zur Erkennung der Sicherheitsgruppe. Konfiguriere dann 2 Sicherheitsgruppenregel:
1. Um mit SSH auf die VM zu kommen (Am besten der Quelltyp «Meine IP», man kann aber natürlich auch «Überall» benutzen)
2. Die zweite wäre das http Traffic von überall auf die Spätere Wordpressseite Zugriff hat.

![Bild15.png](/images/Wordpress-Stack-bei-AWS/Bild15.png)

![Bild16.png](/images/Wordpress-Stack-bei-AWS/Bild16.png)

Am Schluss sollten die Konfigurationen ungefähr so angezeigt werden. Danach kann man auf „Instance starten“ drücken.

![Bild17.png](/images/Wordpress-Stack-bei-AWS/Bild17.png)

### Konfiguration ihrer RDS-Datenbank

#### Datenbank Sicherheitsgruppe anpassen

Um die Sicherheitsgruppe der Datenbank so anzupassen das nur die EC2-Instanz eine Verbindung aufbauen kann muss man auf die Datenbank gehen und dann nach VPC-Sicherheitsgruppen suchen. Wenn man diese gefunden hat, drückt man auf diese drauf und fügt eine neue Regel für den eingehenden Datenverkehr hinzu

![Bild18.png](/images/Wordpress-Stack-bei-AWS/Bild18.png)

![Bild19.png](/images/Wordpress-Stack-bei-AWS/Bild19.png)

Diese Regel sollte ungefähr so aussehen wie die auf der linken Seite.

![Bild20.png](/images/Wordpress-Stack-bei-AWS/Bild20.png)

#### Per SSH auf EC2 Instanz Verbinden

Wie man sich mit der EC2 Instanz verbindet, kann man auf der linken Seite erkennen.

![Bild21.png](/images/Wordpress-Stack-bei-AWS/Bild21.png)

#### MySQL installieren, auf Datenbank verbinden und User erstellen

``` bash
sudo yum update 
sudo yum install -y mysql
```

Nachdem man das Repository geupdatet und MySQL installiert hat kann man sich auf die Datenbank verbinden, um den Wordpress MySQL User zu erstellen. Dafür muss man die Endpunkt Adresse herausfinden die man in der AWS-Konsole unter RDS/Databases/“WordPress Datenbank“ findet.

![Bild22.png](/images/Wordpress-Stack-bei-AWS/Bild22.png)

![Bild23.png](/images/Wordpress-Stack-bei-AWS/Bild23.png)

Um die Endpunkt Adresse hinzuzufügen, benutzt man den Befehl: 
export MYSQL_HOST=<your-endpoint>

![Bild24.png](/images/Wordpress-Stack-bei-AWS/Bild24.png)

Mit diesen Befehlen verbindet man sich auf die Datenbank und erstellt einen Benutzer mit dem Namen „wordpress“ der „ALL PRIVILEGES“ hat.

![Bild25.png](/images/Wordpress-Stack-bei-AWS/Bild25.png)

![Bild26.png](/images/Wordpress-Stack-bei-AWS/Bild26.png)

### Konfigurieren von WordPress auf EC2

#### Webservice Installieren

Hier installiert man den Webserver von Apache.

``` bash
sudo yum install -y httpd
sudo service httpd start
```

![Bild27.png](/images/Wordpress-Stack-bei-AWS/Bild27.png)

#### WordPress herunterladen und Installieren

Man lädt das neuste WordPress .tar.gz herunter und entpackt es.

``` bash
wget https://wordpress.org/latest.tar.gz
tar -xzf latest.tar.gz
```

![Bild28.png](/images/Wordpress-Stack-bei-AWS/Bild28.png)

Nachher geht man in das Directory wordpress und kopiert die Sample config zur wirklichen WordPress config.

``` bash
cd wordpress
cp wp-config-sample.php wp-config.php
```

In dem wp-config.php File ändert man die Database Settings zu den eigenen

![Bild29.png](/images/Wordpress-Stack-bei-AWS/Bild29.png)

Hier fügt man noch die API secret-keys ein damit man sicherer ist. Diese können in [diesem Link](https://api.wordpress.org/secret-key/1.1/salt/) generiert werden.

![Bild30.png](/images/Wordpress-Stack-bei-AWS/Bild30.png)

``` bash
sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
cd /home/ec2-user
sudo cp -r wordpress/* /var/www/html/
sudo service httpd restart
```

Und wenn man die letzten Konfigurationen, die man oben sieht, ausführt. Sollte am Schluss im Browser die WordPress Seite zu sehen sein.

![Bild31.png](/images/Wordpress-Stack-bei-AWS/Bild31.png)

### Backup

#### Amazon EC2 Backup and Restore using AWS Backup

Gehe auf den AWS Backup Service und erstelle einen On-Demand-Backup.

![Bild32.png](/images/Wordpress-Stack-bei-AWS/Bild32.png)

Auf den Ressourcentyp wählt man entweder EC2 und RDS und dann die Instance-ID des RDS (WordPress) und EC2 (WordPress).
Die Aufbewahrungszeitraum soll 7 Tage betragen und der Backup-Tresor ist WordPress (kann auch Default sein).
Leider geht diese Methode nicht da wir nicht die nötigen Berechtigungen haben.

![Bild33.png](/images/Wordpress-Stack-bei-AWS/Bild33.png)

### EC2 Snapshot

Hier sind die Schritte, um ein Snapshot-Image von einer EC2-Instanz zu erstellen:

1. Öffnen Sie das AWS Management Console und melden Sie sich mit Ihrem AWS-Konto an.
2.	Navigieren Sie zum Bereich "EC2" und wählen Sie die Instanz aus, von der Sie ein Snapshot-Image erstellen möchten.
3.	Klicken Sie auf die Schaltfläche "Action" und wählen Sie "Image" > "Create Image" aus.

    ![Bild34.png](/images/Wordpress-Stack-bei-AWS/Bild34.png)

4.	Geben Sie im Dialogfeld "Create Image" einen Namen und eine Beschreibung für das Snapshot-Image ein.
5.	Wählen Sie "No Reboot" aus, wenn Sie möchten, dass die Instanz während des Erstellens des Snapshot-Images läuft. Wählen Sie "Reboot" aus, wenn Sie möchten, dass die Instanz neu gestartet wird, bevor das Snapshot-Image erstellt wird.
6.	Klicken Sie auf die Schaltfläche "Create Image".

    ![Bild35.png](/images/Wordpress-Stack-bei-AWS/Bild35.png)

7.	Das Snapshot-Image wird im Hintergrund erstellt und kann in der Liste der AMIs (Amazon Machine Images) im AWS Management Console angezeigt werden, wenn es abgeschlossen ist.
    ![Bild36.png](/images/Wordpress-Stack-bei-AWS/Bild36.png)

Es ist wichtig zu beachten, dass das Snapshot-Image nur die Inhalte der EBS-Volumes sichert, die an die EC2-Instanz angefügt sind. Wenn Sie andere Daten auf der Instanz haben, die nicht in einem EBS-Volume gespeichert sind, müssen Sie diese Daten separat sichern. Sie können zum Beispiel ein Backup von der EC2-Instanz auf S3 speichern, um zusätzliche Sicherheit zu gewährleisten.

Von Snapshot Volume Wiederherstellen:

![Bild37.png](/images/Wordpress-Stack-bei-AWS/Bild37.png)

![Bild38.png](/images/Wordpress-Stack-bei-AWS/Bild38.png)

![Bild39.png](/images/Wordpress-Stack-bei-AWS/Bild39.png)

![Bild40.png](/images/Wordpress-Stack-bei-AWS/Bild40.png)

#### RDS Backup

##### RDS Backup Automatisch

Um die automatischen Backups für Ihre RDS-Instanz zu nutzen, müssen Sie diese zunächst einrichten. Hier sind die Schritte, wie Sie das tun können:

1.	Öffnen Sie die Amazon RDS-Konsole und wählen Sie die Instanz aus, für die Sie Backups einrichten möchten.
    ![Bild41.png](/images/Wordpress-Stack-bei-AWS/Bild41.png)

2.	Klicken Sie auf die Registerkarte "Backups" und dann auf "Edit Backup Retention Period".
3.	Geben Sie die Anzahl der Tage an, für die Sie Backups aufbewahren möchten, und klicken Sie dann auf "Save Changes". Standardmäßig werden Backups für eine Retention-Zeit von einem Tag erstellt.
    ![Bild42.png](/images/Wordpress-Stack-bei-AWS/Bild42.png)


Wichtig: Wenn Sie die Retention-Zeit auf 0 Tage ändern, werden automatische Backups deaktiviert.
Sobald die automatischen Backups eingerichtet sind, werden täglich Backups Ihrer RDS-Instanz erstellt und für die angegebene Anzahl von Tagen aufbewahrt. Sie können diese Backups in der RDS-Konsole unter der Registerkarte "Backups" anzeigen und verwalten.

##### RDS Backup Manuell

Um manuelle Snapshots von Ihrer RDS-Instanz zu erstellen, folgen Sie diesen Schritten:

1.	Öffnen Sie die Amazon RDS-Konsole und wählen Sie die Instanz aus, für die Sie einen Snapshot erstellen möchten.
    ![Bild43.png](/images/Wordpress-Stack-bei-AWS/Bild43.png)

2.	Klicken Sie auf die Registerkarte "Snapshots" und dann auf "Create DB Snapshot".
    ![Bild43.png](/images/Wordpress-Stack-bei-AWS/Bild43.png)
    ![Bild44.png](/images/Wordpress-Stack-bei-AWS/Bild44.png)

3.	Geben Sie einen Namen für den Snapshot an und klicken Sie auf "Create DB Snapshot".

Der Snapshot-Prozess kann einige Zeit in Anspruch nehmen, abhängig von der Größe Ihrer Datenbank. Während des Prozesses wird Ihre RDS-Instanz möglicherweise kurzzeitig nicht verfügbar sein.
Sobald der Snapshot erstellt wurde, wird er in der Liste der Snapshots angezeigt, die Sie in der RDS-Konsole unter der Registerkarte "Snapshots" finden. Sie können auf den Namen des Snapshots klicken, um weitere Informationen anzuzeigen und ihn zu verwalten.
Hinweis: Manuell erstellte Snapshots bleiben solange erhalten, bis Sie sie manuell löschen. Es ist daher wichtig, dass Sie regelmäßig überflüssige Snapshots löschen, um Speicherplatz zu sparen.

Von Backup Datenbank erstellen:

![Bild45.png](/images/Wordpress-Stack-bei-AWS/Bild45.png)

![Bild46.png](/images/Wordpress-Stack-bei-AWS/Bild46.png)

Wenn man Wiederherstellen drückt kann man eine Neue DB erstellen mit den Informationen

![Bild47.png](/images/Wordpress-Stack-bei-AWS/Bild47.png)

### Was Bedeutet Stateless Architecture:

Eine stateless architecture bedeutet, dass keine Informationen über den Zustand einer Anwendung auf dem Server gespeichert werden. Dies bedeutet, dass jeder Request, den ein Benutzer an die Anwendung sendet, alle notwendigen Informationen enthält, um die Anforderung zu verarbeiten. Der Server muss keine Informationen aus einem vorherigen Request speichern, um den aktuellen Request zu verarbeiten.

Ein Beispiel für eine stateless architecture wäre eine Wordpress-Installation, bei der alle Benutzerinformationen in der Datenbank gespeichert werden und jeder Request, den ein Benutzer an die Anwendung sendet, die erforderlichen Informationen von der Datenbank abruft, um die Anforderung zu verarbeiten. Die Anwendung muss keine Informationen über den Zustand des Benutzers auf dem Server speichern, um Anforderungen von diesem Benutzer zu verarbeiten.

![Bild48.png](/images/Wordpress-Stack-bei-AWS/Bild48.png)

### Bash Script

Da mir diese Schritte aber zu lang gingen habe ich noch ein kurzes Bash Script geschrieben. (Zuunterst sieht man noch einen Link zum Test Video)

``` bash title="wordpress.sh"
#!/bin/bash

sudo yum -y update
sudo yum install -y mysql
sudo yum install -y httpd
sudo service httpd start
wget https://wordpress.org/latest.tar.gz
tar -xzf latest.tar.gz
cp wordpress/wp-config-sample.php wordpress/wp-config.php

# Set the new values for the database variables
new_db_name='wordpress'
new_db_user='wordpress'
new_db_password='5ztDByGKq49aKm3S'
new_db_host='wordpressdb.csj4fgsm0wsp.us-east-1.rds.amazonaws.com'

# Replace the old values in the wp-config.php file
sed -i "s/define( 'DB_NAME', 'database_name_here' );/define( 'DB_NAME', '$new_db_name' );/" wordpress/wp-config.php
sed -i "s/define( 'DB_USER', 'username_here' );/define( 'DB_USER', '$new_db_user' );/" wordpress/wp-config.php
sed -i "s/define( 'DB_PASSWORD', 'password_here' );/define( 'DB_PASSWORD', '$new_db_password' );/" wordpress/wp-config.php
sed -i "s/define( 'DB_HOST', 'localhost' );/define( 'DB_HOST', '$new_db_host' );/" wordpress/wp-config.php

# Ersetze die Zeilen mit den 'unique phrase' durch die neuen Werte
sed -i -s 's{define( '\''AUTH_KEY'\'',         '\''put your unique phrase here'\'' );{define('\''AUTH_KEY'\'',         '\''0ozpHN_tE]U?[L.)kvnCDrC-H*qI:UgzQvV9Ga+)k+*~RlZZZHD,kB>[<Y6|RJXC'\'' );{' wordpress/wp-config.php
sed -i -s 's?define( '\''SECURE_AUTH_KEY'\'',  '\''put your unique phrase here'\'' );?define('\''SECURE_AUTH_KEY'\'',  '\''{G!dia+f!={U>8vI%Ch0Y-{/xO~Eew^q_ETOyG]~EUeK;C2v3JRx8)N [vi[tO}<'\'' );?' wordpress/wp-config.php
sed -i -s 's}define( '\''LOGGED_IN_KEY'\'',    '\''put your unique phrase here'\'' );}define('\''LOGGED_IN_KEY'\'',    '\''!*^I0Q?teip2%gg8W=ssNTeB,M?7/+++U7bJ`GHN9/-i#Y<{n`hK5lNO[gOB~|#y'\'' );}' wordpress/wp-config.php
sed -i -s 's!define( '\''NONCE_KEY'\'',        '\''put your unique phrase here'\'' );!define('\''NONCE_KEY'\'',        '\''W*L:-+4kkn4{hX_8TH`P3Z0yq1==vy)4M~OBRkJ*e}u:1ttc_}Kb8HmMV+|yO>1 '\'' );!' wordpress/wp-config.php
sed -i -s 's}define( '\''AUTH_SALT'\'',        '\''put your unique phrase here'\'' );}define('\''AUTH_SALT'\'',        '\''*vb,woc2_=4|[5$di(?Ata;{vQ6,!nf3OT.#( #<poS7AdkX_BU1Px~~8nY!y[1x'\'' );}' wordpress/wp-config.php
sed -i -s 's{define( '\''SECURE_AUTH_SALT'\'', '\''put your unique phrase here'\'' );{define('\''SECURE_AUTH_SALT'\'', '\''*o:<yV#gpxt/cS#HrsHeX?[A*;hm+!`oufT}WZWBum1Bn:;0hM6jyNZScN<tC)! '\'' );{' wordpress/wp-config.php
sed -i -s 's}define( '\''LOGGED_IN_SALT'\'',   '\''put your unique phrase here'\'' );}define('\''LOGGED_IN_SALT'\'',   '\''DY+PZ8;3?*~/~GnaQk)T<=47o|)x#Ht(o,^Zs3K,{*UtX2CBB[Ia;1Y!0:h]Q^#C'\'' );}' wordpress/wp-config.php
sed -i -s 's}define( '\''NONCE_SALT'\'',       '\''put your unique phrase here'\'' );}define('\''NONCE_SALT'\'',       '\'',abD~m/;Ws0NJ]I]EodiE[{a,x|DU/W%w/aK15j Ee?]> 7L-i$u[?C,5=qt<q{8'\'' );}' wordpress/wp-config.php

sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
sudo cp -r wordpress/* /var/www/html/
sudo service httpd restart

```
Video: [https://youtu.be/b2QCiFxmGvw](https://youtu.be/b2QCiFxmGvw)

### Ansible Playbook

Da mir diese Schritte aber zu lang gingen habe ich noch ein kurzes Ansible Playbook geschrieben. (Zuunterst sieht man noch einen Link zum Test Video)

``` yml title="wordpress.yml"
---
- name: Install and configure WordPress
  hosts: all
  become: true
  vars:
    new_db_name: wordpress
    new_db_user: wordpress
    new_db_password: 5ztDByGKq49aKm3S
    new_db_host: wordpress02.csj4fgsm0wsp.us-east-1.rds.amazonaws.com
    
  tasks:
    - name: Update package manager cache and install MySQL, Apache, and PHP
      package:
        name:
          - mysql
          - httpd
          - amazon-linux-extras
        state: latest
      register: pkg_result

    - name: Start Apache service
      service:
        name: httpd
        state: started

    - name: Download latest WordPress tarball
      get_url:
        url: https://wordpress.org/latest.tar.gz
        dest: /tmp/latest.tar.gz

    - name: Extract WordPress tarball
      unarchive:
        src: /tmp/latest.tar.gz
        dest: /tmp
        remote_src: yes

    - name: copy files task
      shell: cp /tmp/wordpress/wp-config-sample.php /tmp/wordpress/wp-config.php

    - name: Set database variables in wp-config.php
      replace:
        path: /tmp/wordpress/wp-config.php
        regexp: "define\\(\\s*'DB_NAME',\\s*'.*'\\s*\\)"
        replace: "define( 'DB_NAME', '{{ new_db_name }}' );"

    - name: Set database user in wp-config.php
      replace:
        path: /tmp/wordpress/wp-config.php
        regexp: "define\\(\\s*'DB_USER',\\s*'.*'\\s*\\)"
        replace: "define( 'DB_USER', '{{ new_db_user }}' );"

    - name: Set database password in wp-config.php
      replace:
        path: /tmp/wordpress/wp-config.php
        regexp: "define\\(\\s*'DB_PASSWORD',\\s*'.*'\\s*\\)"
        replace: "define( 'DB_PASSWORD', '{{ new_db_password }}' );"

    - name: Set database host in wp-config.php
      replace:
        path: /tmp/wordpress/wp-config.php
        regexp: "define\\(\\s*'DB_HOST',\\s*'.*'\\s*\\)"
        replace: "define( 'DB_HOST', '{{ new_db_host }}' );"

    - name: Set unique phrases in wp-config.php
      replace: 
        path: /tmp/wordpress/wp-config.php
        regexp: "define\\( 'AUTH_KEY',\\s+'put your unique phrase here' \\);"
        replace: "define('AUTH_KEY', '0ozpHN_tE]U?[L.)kvnCDrC-H*qI:UgzQvV9Ga+)k+*~RlZZZHD,kB>[<Y6|RJXC');"
      replace: 
        path: /tmp/wordpress/wp-config.php
        regexp: "define\\( 'SECURE_AUTH_KEY',\\s+'put your unique phrase here' \\);"
        replace: "define('SECURE_AUTH_KEY', '{G!dia+f!={U>8vI%Ch0Y-{/xO~Eew^q_ETOyG]~EUeK;C2v3JRx8)N [vi[tO}<');"
      replace: 
        path: /tmp/wordpress/wp-config.php
        regexp: "define\\( 'LOGGED_IN_KEY',\\s+'put your unique phrase here' \\);"
        replace: "define('LOGGED_IN_KEY', '!*^I0Q?teip2%gg8W=ssNTeB,M?7/+++U7bJ`GHN9/-i#Y<{n`hK5lNO[gOB~|#y');"
      replace: 
        path: /tmp/wordpress/wp-config.php
        regexp: "define\\( 'NONCE_KEY',\\s+'put your unique phrase here' \\);"
        replace: "define('NONCE_KEY', 'W*L:-+4kkn4{hX_8TH`P3Z0yq1==vy)4M~OBRkJ*e}u:1ttc_}Kb8HmMV+|yO>1 ');"
      replace: 
        path: /tmp/wordpress/wp-config.php
        regexp: "define\\( 'AUTH_SALT',\\s+'put your unique phrase here' \\);"
        replace: "define('AUTH_SALT', '*vb,woc2_=4|[5$di(?Ata;{vQ6,!nf3OT.#( #<poS7AdkX_BU1Px~~8nY!y[1x');"
      replace: 
        path: /tmp/wordpress/wp-config.php
        regexp: "define\\( 'SECURE_AUTH_SALT',\\s+'put your unique phrase here' \\);"
        replace: "define('SECURE_AUTH_SALT', '*o:<yV#gpxt/cS#HrsHeX?[A*;hm+!`oufT}WZWBum1Bn:;0hM6jyNZScN<tC)! ');"
      replace: 
        path: /tmp/wordpress/wp-config.php
        regexp: "define\\( 'LOGGED_IN_SALT',\\s+'put your unique phrase here' \\);"
        replace: "define('LOGGED_IN_SALT', 'DY+PZ8;3?*~/~GnaQk)T<=47o|)x#Ht(o,^Zs3K,{*UtX2CBB[Ia;1Y!0:h]Q^#C');"
      replace: 
        path: /tmp/wordpress/wp-config.php
        regexp: "define\\( 'NONCE_SALT',\\s+'put your unique phrase here' \\);"
        replace: "define('NONCE_SALT', 'abD~m/;Ws0NJ]I]EodiE[{a,x|DU/W%w/aK15j Ee?]> 7L-i$u[?C,5=qt<q{8');"

    - name: Install lamp-mariadb10.2-php7.2
      command: "sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2"

    - name: copy files task
      shell: sudo cp -r /tmp/wordpress/* /var/www/html/

    - name: Restart Apache service
      service:
        name: httpd
        state: restarted
```

Video: [https://youtu.be/Nb9mF5vab7M](https://youtu.be/Nb9mF5vab7M)