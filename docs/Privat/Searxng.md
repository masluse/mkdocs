# Eigener Browser (Searxng)

## Schritt 1: Installation

``` bash
apt update && apt upgrade -y
apt install docker.io docker-compose git -y
```

## Schritt 2: Git clonen und .env ändern

``` bash
cd /usr/local
git clone https://github.com/searxng/searxng-docker.git
cd searxng-docker
nano .env
```


``` bash title=".env"
# By default listen on https://localhost
# To change this:
# * uncomment SEARXNG_HOSTNAME, and replace <host> by the SearXNG hostname
# * uncomment LETSENCRYPT_EMAIL, and replace <email> by your email (require to create a Let's Encrypt certificate)

SEARXNG_HOSTNAME=example.com
LETSENCRYPT_EMAIL=example@example.com
```

Searxng starten:

``` bash
sed -i "s|ultrasecretkey|$(openssl rand -hex 32)|g" searxng/settings.yml
cd /usr/local/searxng-docker
sudo docker-compose up -d
```