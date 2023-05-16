# DDNS mit Cloudflare

## Schritt 1: Installation von git und clonen

Updaten des Repositories, Herunterladen von git und Clonen des "cloudflare-ddns-updater".

``` bash
sudo su -
```

``` bash
apt update
apt install git -y
git clone https://github.com/K0p1-Git/cloudflare-ddns-updater
```

## Schritt 2: Vorbereiten des .sh Scriptes

In das Verzeichniss "cloudflare-ddns-updater" gehen, Template kopieren und in cloudflare.sh reingehen.

``` bash
cd cloudflare-ddns-updater
cp cloudflare-template.sh cloudflare.sh
nano cloudflare.sh
```

## Schritt 3: Anpassen des .sh Scriptes

Im unteren Script müssen Sie noch ein paar dinge ändern:
- auth_email: Mailadresse des Cloudflare Kontos
- auth_key: "Cloudflare Overview"/"Get your API token"/"Global API Key"
- zone_identifier: Zone ID auf der Cloudflare Overview
- record_name: Name des eintrages der per DDNS geändert werden soll z. B. www.google.com

``` bash title="cloudflare.sh"
#!/bin/bash
## change to "bin/sh" when necessary

auth_email="<auth_email>"                                       # The email used to login 'https://dash.>
auth_method="global"                                 # Set to "global" for Global API Key or "token" for Scoped API Tok>
auth_key="<auth_key>"                                         # Your API Token or Global API>
zone_identifier="<zone_identifier>"                                  # Can be found in the "Overview" ta>
record_name="<record_name>"                                      # Which record you want to be synced
ttl="3600"                                          # Set the DNS TTL (seconds)
proxy="false"                                       # Set the proxy to true or false
sitename=""                                         # Title of site "Example Site"
slackchannel=""                                     # Slack Channel #example
slackuri=""                                         # URI for Slack WebHook "https://hooks.slack.com/services/xxxxx"
discorduri=""                                       # URI for Discord WebHook "https://discordapp.com/api/webhooks/xxxx>
```

## Schritt 4: Script testen

``` bash
chmod +x cloudflare.sh
./cloudflare.sh
```

## Schritt 5: Task erstellen

``` bash
crontab -e
```

Inhalt einfügen (Jede Minute):

``` bash
*/1 * * * * /bin/bash /root/cloudflare-ddns-updater/cloudflare.sh
```

Service neustarten:
``` bash
systemctl restart cron.service
```
