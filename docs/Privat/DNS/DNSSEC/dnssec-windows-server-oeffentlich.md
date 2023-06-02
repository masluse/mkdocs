# DNSSEC auf Windows DNS einrichten (Öffentlich)

## DNSSEC Status Kontrollieren

Als erstest kontrolliert man den DNSSEC stand mit den folgenden 2 Seiten.

[https://dnssec-analyzer.verisignlabs.com/](https://dnssec-analyzer.verisignlabs.com/)

![Bild01.png](/images/dnssec-windows-server-oeffentlich/Bild01.png)

Wie man im Oberen Bild sehen kann ist DNSSEC für die Domain .ch möglich aber wurde noch nicht konfiguriert für die Domain fenacotest.ch

[https://dnsviz.net/d/fenacotest.ch/dnssec/](https://dnsviz.net/d/fenacotest.ch/dnssec/)

![Bild02.png](/images/dnssec-windows-server-oeffentlich/Bild02.png)

Hier würde man als Bild sehen dass kein DNSSEC konfiguriert wurde.

## DNSSEC auf Windows Server konfigurieren

Im DNS-Manager navigieren Sie zu Ihrem Domänennamen. Klicken Sie mit der rechten Maustaste auf den Domänennamen und wählen Sie "DNSSEC" aus. Anschließend klicken Sie auf "Zone signieren".

![Bild03.png](/images/dnssec-windows-server-oeffentlich/Bild03.png)

Im Interface des Zone Signing Wizard klicken Sie auf "Weiter".

![Bild04.png](/images/dnssec-windows-server-oeffentlich/Bild04.png)

Im Interface für die Signierungsoptionen klicken Sie auf __"Customize zone signing parameters"__ und anschließend auf "Weiter".

Durch die Auswahl von __"Customize zone signing parameters"__ haben Sie die Möglichkeit, die Signierungseinstellungen für Ihre Zone individuell anzupassen. Dies ermöglicht Ihnen eine feinere Kontrolle über den Signierungsprozess und die Sicherheit Ihrer DNS-Zone.

Alternativ dazu können Sie auch andere Optionen in Betracht ziehen, wie z.B. __"Use default settings to sign the zone"__, bei dem vorgegebene Signierungseinstellungen automatisch angewendet werden. Diese Option ist empfehlenswert, wenn Sie sich nicht mit den detaillierten Parametern der Signierung befassen möchten und eine einfache, standardisierte Konfiguration bevorzugen.

Durch die Auswahl der Option __"Sign the zone with parameters of an existing zone"__ können Sie die bereits konfigurierten Signaturparameter einer anderen Zone übernehmen und für die Signierung Ihrer aktuellen Zone verwenden. Dies kann nützlich sein, wenn Sie bereits eine Zone mit den gewünschten Signaturparametern haben und diese für die neue Zone wiederverwenden möchten, anstatt die Parameter manuell anzupassen.


![Bild05.png](/images/dnssec-windows-server-oeffentlich/Bild05.png)

Als Keymaster-Server sollte ein dedizierter und hochsicherer Server verwendet werden. Idealerweise sollte der Keymaster-Server nicht derselbe Server sein, der auch für die DNS-Infrastruktur oder andere kritische Dienste verwendet wird. Dadurch wird das Risiko einer Kompromittierung der Schlüssel reduziert.

Die Hauptfunktionen eines Keymaster-Servers:

__Schlüsselgenerierung__: Der Keymaster-Server erzeugt neue kryptografische Schlüssel nach den gewünschten Standards und Algorithmen.

__Schlüsselspeicherung__: Der Keymaster-Server verwaltet den sicheren Speicher der erzeugten Schlüssel. Dies kann entweder in einer speziellen Hardwarekomponente wie einem Hardware Security Module (HSM) oder in verschlüsselten Software-Tresoren erfolgen.


![Bild06.png](/images/dnssec-windows-server-oeffentlich/Bild06.png)

Der KSK (Key Signing Key) ist ein spezieller kryptografischer Schlüssel, der für das Signieren von Zonenschlüsseln in DNSSEC verwendet wird.
Er dient dazu, die Vertrauenskette im DNSSEC-System zu etablieren und sicherzustellen, dass die signierten Zonenschlüssel gültig und vertrauenswürdig sind.
Der KSK ist eine wichtige Komponente für die Sicherheit und Integrität des Domain Name Systems.

![Bild07.png](/images/dnssec-windows-server-oeffentlich/Bild07.png)

![Bild08.png](/images/dnssec-windows-server-oeffentlich/Bild08.png)

__Cryptographic algorithm__ = Es gibt verschiedene Algorithmen wie RSA, DSA oder ECDSA.

__Key length (Bits)__ = Die Schlüssellänge gibt an, wie lang der KSK in Bits ist. Eine längere Schlüssellänge bietet normalerweise eine höhere Sicherheit, aber auch eine größere Berechnungs- und Verarbeitungszeit. Die empfohlene Schlüssellänge für den KSK kann von den Standards und Best Practices der jeweiligen DNSSEC-Implementierung abhängen. In der Regel sind Schlüssellängen von 2048 Bits oder höher angemessen.

__Select a key storage provider to generate and store keys__ = Bei der Auswahl eines Key Storage Providers geht es darum, einen sicheren Speicherort für den KSK zu wählen. Dies kann ein Hardware Security Module (HSM), ein spezielles Sicherheitsgerät oder ein verschlüsselter Software-Tresor sein. Die Wahl des Anbieters hängt von den Sicherheitsanforderungen, der Skalierbarkeit und den verfügbaren Optionen ab.

__DNSKEY RRSET signature validity period (hours)__ = Die Gültigkeitsdauer der DNSKEY RRSET-Signatur gibt an, wie lange die Signatur für den KSK gültig ist, bevor sie erneuert oder aktualisiert werden muss. Eine längere Gültigkeitsdauer reduziert die Notwendigkeit häufiger Signaturaktualisierungen, erhöht jedoch auch das Risiko bei Kompromittierung des Schlüssels.

__Enable automatic rollover__ = Die automatische Rollover-Funktion ermöglicht die automatische Aktualisierung und Erneuerung des KSKs nach einer bestimmten Zeit oder nach festgelegten Ereignissen. Dies gewährleistet eine kontinuierliche Sicherheit und Schlüsselaktualisierung, um mögliche Sicherheitsrisiken zu minimieren. Die Aktivierung der automatischen Rollover-Funktion wird empfohlen, um den KSK regelmäßig zu erneuern und sicherzustellen, dass er immer auf dem aktuellen Stand ist.

![Bild09.png](/images/dnssec-windows-server-oeffentlich/Bild09.png)

![Bild10.png](/images/dnssec-windows-server-oeffentlich/Bild10.png)

ZSK steht für "Zone Signing Key" und ist ein kryptografischer Schlüssel, der zur Signierung von DNS-Zonen verwendet wird. Er dient dazu, die Integrität und Authentizität von DNS-Daten sicherzustellen. Der ZSK wird normalerweise regelmäßig gewechselt, um die Sicherheit der Signierung zu gewährleisten.

Der Hauptunterschied zwischen ZSK und KSK besteht darin, dass ZSKs verwendet werden, um DNS-Zonen zu signieren, während KSKs verwendet werden, um die ZSKs selbst zu signieren. KSKs haben eine längere Lebensdauer und dienen dazu, die Vertrauenskette im DNSSEC-System zu etablieren und zu erhalten, während ZSKs häufiger gewechselt werden, um die Sicherheit der Signierung zu gewährleisten. Zusammen arbeiten ZSKs und KSKs, um die Integrität und Authentizität von DNS-Daten sicherzustellen und eine sichere Kommunikation im DNSSEC-System zu ermöglichen.


![Bild11.png](/images/dnssec-windows-server-oeffentlich/Bild11.png)

![Bild12.png](/images/dnssec-windows-server-oeffentlich/Bild12.png)

__Cryptographic algorithm__ = Es gibt verschiedene Algorithmen wie RSA, DSA oder ECDSA.

__Key length (Bits)__ = Die Schlüssellänge gibt an, wie lang der KSK in Bits ist. Eine längere Schlüssellänge bietet normalerweise eine höhere Sicherheit, aber auch eine größere Berechnungs- und Verarbeitungszeit. Die empfohlene Schlüssellänge für den KSK kann von den Standards und Best Practices der jeweiligen DNSSEC-Implementierung abhängen. In der Regel sind Schlüssellängen von 2048 Bits oder höher angemessen.

__Select a key storage provider to generate and store keys__ = Bei der Auswahl eines Key Storage Providers geht es darum, einen sicheren Speicherort für den KSK zu wählen. Dies kann ein Hardware Security Module (HSM), ein spezielles Sicherheitsgerät oder ein verschlüsselter Software-Tresor sein. Die Wahl des Anbieters hängt von den Sicherheitsanforderungen, der Skalierbarkeit und den verfügbaren Optionen ab.

__DNSKEY Signature Validity Period (hours)__ = Dies bezieht sich auf die Gültigkeitsdauer der digitalen Signatur für den DNSKEY-Eintrag, der den öffentlichen Teil des ZSK enthält. Es gibt an, wie lange die Signatur als gültig betrachtet wird, bevor sie erneuert werden muss. Die empfohlene Wertebereich liegt in der Regel zwischen 24 und 48 Stunden.

__DS Signature Validity Period (hours)__ = Dies bezieht sich auf die Gültigkeitsdauer der digitalen Signatur für den DS-Eintrag, der den öffentlichen Teil des KSK (Key Signing Key) repräsentiert. Der DS-Eintrag wird von der übergeordneten DNS-Zone verwendet, um den KSK des untergeordneten Bereichs zu überprüfen. Auch hier empfiehlt sich ein Wertebereich von 24 bis 48 Stunden.

__Zone Record Validity Period (hours)__ = Dies bezieht sich auf die Gültigkeitsdauer anderer DNS-Zoneneinträge, die von der ZSK signiert wurden. Es gibt an, wie lange diese Einträge als gültig betrachtet werden, bevor sie erneuert werden müssen. Der empfohlene Wertebereich liegt normalerweise zwischen 24 und 72 Stunden, abhängig von den spezifischen Anforderungen des Systems und der beabsichtigten Aktualisierungsfrequenz.


![Bild13.png](/images/dnssec-windows-server-oeffentlich/Bild13.png)

![Bild14.png](/images/dnssec-windows-server-oeffentlich/Bild14.png)

__NSEC__ = (Next Secure) ist eine Methode, bei der ein spezieller DNS-Datensatz verwendet wird, um die Existenz einer DNS-Ressource zu bestätigen und gleichzeitig Lücken in der Namensraumabdeckung offenzulegen. NSEC-Einträge werden in einer sortierten Reihenfolge präsentiert und ermöglichen es DNS-Clients, effizient zu überprüfen, ob eine bestimmte DNS-Ressource existiert oder nicht. NSEC hat jedoch den Nachteil, dass es Informationen über die vorhandenen DNS-Ressourcen preisgibt.

__NSEC3__ ist eine Weiterentwicklung von NSEC, die entwickelt wurde, um die Offenlegung von Informationen in NSEC zu reduzieren. Bei NSEC3 werden die DNS-Namen mit einem kryptografischen Hash-Algorithmus und einem sogenannten Salz (Salt) verschlüsselt, um die Lücken in der Namensraumabdeckung zu verbergen. Durch die Verwendung von NSEC3 können DNS-Clients immer noch überprüfen, ob eine bestimmte DNS-Ressource existiert, ohne dass alle vorhandenen DNS-Namen offengelegt werden.

__Iterations__ = Die Anzahl der Iterationen bestimmt die Anzahl der Hash-Berechnungen, die bei der Verwendung von NSEC3 durchgeführt werden. Eine höhere Anzahl von Iterationen erhöht die Sicherheit, kann jedoch auch die Leistung beeinträchtigen. Ein guter Kompromiss ist normalerweise eine ausreichende Anzahl von Iterationen, um Brute-Force-Angriffe zu erschweren, ohne die Leistung signifikant zu beeinträchtigen.

__Generate and use a random salt of length__ = Das Salz (Salt) ist eine zufällige Zeichenfolge, die zusammen mit dem DNS-Namen verwendet wird, um die Hash-Werte in NSEC3 zu berechnen. Die Länge des Salzes kann variieren und sollte ausreichend sein, um Kollisionen zu vermeiden. Ein zufälliges und langes Salz erhöht die Sicherheit des Systems.

__Use opt-out to cover unsigned delegations__ = Opt-out ermöglicht es, dass NSEC3-Einträge für nicht signierte Subdomänen automatisch generiert werden. Dies kann die Größe der DNSSEC-Daten reduzieren und die Effizienz verbessern. Allerdings sollten die Auswirkungen auf die Sicherheit und die Kompatibilität mit DNS-Clients sorgfältig abgewogen werden.

![Bild15.png](/images/dnssec-windows-server-oeffentlich/Bild15.png)

__"Enable the distribution of trust anchors for this zone"__ = Durch das Aktivieren dieser Option ermöglichen Sie die Verteilung der Trust-Anchors für Ihre DNS-Zone an andere DNS-Resolver. Trust-Anchors sind öffentliche Schlüssel, die von Resolvern verwendet werden, um die DNSSEC-Signaturen in Ihrer Zone zu überprüfen. Die Verteilung der Trust-Anchors erleichtert die Überprüfung der DNSSEC-Authentizität durch andere Systeme, die Ihre Zone abfragen.

__"Enable automatic update of trust anchors on key rollover (RFC 5011)"__ = Wenn Sie diese Option aktivieren, erlauben Sie die automatische Aktualisierung der Trust-Anchors bei einem Schlüsselwechsel (Key Rollover). RFC 5011 ist ein Standard, der beschreibt, wie DNSSEC-Resolver automatisch aktualisierte Trust-Anchors empfangen und akzeptieren können, ohne dass eine manuelle Intervention erforderlich ist. Diese Option gewährleistet, dass Resolver immer die aktuellen und gültigen Trust-Anchors verwenden, wenn sich die Schlüssel in Ihrer DNS-Zone ändern.

![Bild16.png](/images/dnssec-windows-server-oeffentlich/Bild16.png)

__DS record generation algorithm__ = Dies bezieht sich auf den Algorithmus, der verwendet wird, um den DS (Delegation Signer) Record zu generieren. Der DS Record enthält den öffentlichen Teil des Key Signing Key (KSK) und wird in der übergeordneten DNS-Zone verwendet, um die DNSSEC-Validierung der untergeordneten Zone zu ermöglichen. Der Algorithmus bestimmt, wie der DS Record aus dem KSK generiert wird und kann beispielsweise RSA, DSA oder ECDSA sein.

__DS record TTL__ = TTL steht für "Time-to-Live" und gibt an, wie lange der DS Record im Cache der DNS-Resolver gültig bleibt, bevor er erneut abgefragt werden muss. Ein niedriger TTL-Wert bedeutet, dass der DS Record häufiger aktualisiert und abgefragt wird, während ein höherer TTL-Wert die Caching-Zeit verlängert und die Anzahl der Abfragen reduziert.

__DNSKEY record TTL__ = Ähnlich wie der DS Record TTL gibt der DNSKEY Record TTL an, wie lange der DNSKEY Record, der den öffentlichen Teil des Zone Signing Key (ZSK) enthält, im Cache der DNS-Resolver gültig bleibt, bevor er erneut abgefragt werden muss. Auch hier beeinflusst der TTL-Wert die Caching-Zeit und die Häufigkeit der Abfragen für den DNSKEY Record.

__Signature inception__ = Dies bezieht sich auf den Zeitpunkt, an dem die digitale Signatur für die DNS-Ressourcenaufzeichnungen (wie A-, MX- oder CNAME-Einträge) in einer DNS-Zone erstellt wird. Die Signature Inception gibt an, ab wann die Signaturen als gültig betrachtet werden und für die Validierung der DNSSEC-Antworten verwendet werden können. Die Signature Inception ist normalerweise ein Zeitpunkt in der Zukunft, um sicherzustellen, dass alle DNS-Resolver die neuen Signaturen erhalten, bevor sie verwendet werden müssen.

![Bild17.png](/images/dnssec-windows-server-oeffentlich/Bild17.png)

![Bild18.png](/images/dnssec-windows-server-oeffentlich/Bild18.png)

## DS Eintrag erstellen und am Registrator geben

Wenn man das obere konfiguriert hat, kann man zum überprüfen und zum herausfinden welches der oberste DNSKEY ist wieder auf den folgenden link gehen:

[https://dnsviz.net/d/fenacotest.ch/dnssec/](https://dnsviz.net/d/fenacotest.ch/dnssec/)

![Bild19.png](/images/dnssec-windows-server-oeffentlich/Bild19.png)

Wie man im oberen sieht sind jetzt 4 DNSKEYs dazu gekommen. 2 wurden vom KSK ausgesstellt und die anderen 2 vom ZSK. Wir merken uns den obersten also id=6076

Danach um den DS Wert herauszufinden gibt es mehrere wege aber da keiner davon bei mir funktioniert hat habe ich mir kurz einen Docker Webserver gemacht der mir die DS informationen generiert.

Image selber Builden:
Github: [https://github.com/masluse/DNSKEY-to-DS](https://github.com/masluse/DNSKEY-to-DS)

Docker Befehl:
``` bash
docker run -p 5000:5000 masluse/dnskey-to-ds-converter:latest
```

Danach kann man über den Browser auf die adresse [http://localhost:5000](http://localhost:5000)

![Bild20.png](/images/dnssec-windows-server-oeffentlich/Bild20.png)

Dort kommen jetzt 2 einträge. Wir brauchen aber nur den mit der ID die wir uns vorher gemerkt haben also ID / Key Tag = 6076

Wenn man das gemacht hat geht man zum Domain Registrator, sucht wo man DS records eintragen kann und gibt alle nötigen informationen ein.

![Bild21.png](/images/dnssec-windows-server-oeffentlich/Bild21.png)

Es kann danach je nach anbieter bis zu 1 Stunde dauern bis dieser eintrag von den TLD Servern genommen wird. Danach kann man nochmal auf [https://dnssec-analyzer.verisignlabs.com/](https://dnssec-analyzer.verisignlabs.com/) und auf [https://dnsviz.net/d/fenacotest.ch/dnssec/](https://dnsviz.net/d/fenacotest.ch/dnssec/)

![Bild22.png](/images/dnssec-windows-server-oeffentlich/Bild22.png)

![Bild23.png](/images/dnssec-windows-server-oeffentlich/Bild23.png)
