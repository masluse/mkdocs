# Minecraft mit Ansible

## Auftrag

![Bild01.png](/images/minecraft-mit-ansible/Bild01.png)

## Ansible Installation und Setup

### Installation

#### Alte Ansible Version entfernen

``` bash
sudo apt remove ansible
sudo apt --purge autoremove
```

#### Update und Upgrade Rep

``` bash
sudo apt update
sudo apt upgrade
```

#### Personal Package Archives auf die neuste Version konfigurieren

``` bash
sudo apt -y install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
```

#### Installieren von Ansible

``` bash
sudo apt install ansible
```

![Bild02.png](/images/minecraft-mit-ansible/Bild02.png) 

Source: [https://www.cyberciti.biz/faq/how-to-install-and-configure-latest-version-of-ansible-on-ubuntu-linux/](https://www.cyberciti.biz/faq/how-to-install-and-configure-latest-version-of-ansible-on-ubuntu-linux/)

### SSH Keys auf Ansible System kopieren

![Bild03.png](/images/minecraft-mit-ansible/Bild03.png) 

### Inventory File erstellen

``` yaml title="inventory"
[minecraft]
primary ansible_host=192.168.66.71 ansible_user=manuel
```

### Inventory Konfiguration testen

``` bash
ansible all -i inventory --list-hosts
```

![Bild04.png](/images/minecraft-mit-ansible/Bild04.png) 

``` bash
ansible all -i inventory –m ping
```

### Playbook

#### Erstellen

``` yaml title="playbook.yml"
---
- hosts: all
  tasks:
    - name: Print message
      debug:
        msg: Hello Ansible World
```

#### Testen

``` bash
ansible-playbook -i inventory playbook.yml
```

![Bild05.png](/images/minecraft-mit-ansible/Bild05.png)

### Minecraft Docker Ansible Skript

#### Erstellen

``` yaml title="minecraft.yml"
---
- hosts: all
  become: yes
  tasks:
    - name: Install docker
      ansible.builtin.apt:
        name: docker.io
        update_cache: yes

    - name: Pull und run Minecraft Server
      community.docker.docker_container:
        name: mcserver
        image: itzg/minecraft-server
        restart_policy: always
        ports:
          - "25565:25565"
        env:
          EULA: "TRUE"
          VERSION: "1.18.2"
```

#### Testen

##### Mit Ansible auf die VM Installieren

``` bash
ansible-playbook -i inventory minecraft.yml
```

![Bild06.png](/images/minecraft-mit-ansible/Bild06.png)

##### Auf VM kontrollieren ob Docker Container am laufen ist + Kontrollieren ob Container Automatisch startet.

![Bild07.png](/images/minecraft-mit-ansible/Bild07.png)

##### Auf Minecraft Server verbinden.

![Bild08.png](/images/minecraft-mit-ansible/Bild08.png)

![Bild09.png](/images/minecraft-mit-ansible/Bild09.png)

### Schwierigkeiten

community.docker.docker_container hat zu anfangs nicht funktioniert da ich auf der Version 2.9.6 arbeitete (Per Teams Anleitung Installiert) und diese laut GitHub viele Bugs aufzuweisen hat. 