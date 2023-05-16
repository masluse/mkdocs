# ArchRefCard-01 mit AWS Fargate (Kompetenznachweis)

## Auftrag

![Bild01.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild01.png)

![Bild02.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild02.png)

## Grafik und Diagramme

__Aufgabe:__ Erstellen Sie Grafiken und Diagramme von ECS und ECR: Wie spielen Repository, Task Definition, Task und Service zusammen?

![Bild03.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild03.png)

## ECS-Beschreiben

 __Aufgabe:__ Beschreiben Sie die Funktionalität von __ECS__:

-	__Skalierbarkeit:__ ECS bietet eine automatische Skalierung von Container-Workloads an, um den Anforderungen gerecht zu werden. Durch die Nutzung von Auto Scaling-Gruppen und Elastic Load Balancing kann die Skalierung der Container-Workloads dynamisch angepasst werden.
-	__Cluster-Management:__ ECS ermöglicht die Erstellung und Verwaltung von Clustern, bestehend aus EC2-Instanzen oder Fargate-Containern, auf denen Container-Workloads ausgeführt werden können. Innerhalb dieser Cluster können Ressourcen gemeinsam genutzt werden, um verschiedene Anwendungen und Services zu unterstützen.
-	__Integrationen:__ ECS ist eng mit anderen AWS-Diensten integriert, darunter Elastic Load Balancing, Identity and Access Management (IAM), CloudWatch und CloudFormation. Dadurch lässt sich ECS nahtlos in bestehende AWS-Infrastrukturen und Workflows integrieren. Diese Integrationen ermöglichen eine verbesserte Skalierbarkeit, Überwachung, Zugriffskontrolle und die Automatisierung von Prozessen.

## Privates Repository erstellen

__Aufgabe:__ Erstellen Sie eine ein __privates Repository__ in __ECR__ für die App Ref. Card 01

Um ein privates Repository in AWS ECR zu erstellen, geht man auf die AWS-Webseite und navigiert zum ECR (Elastic Container Registry). Dort klickt man auf die Schaltfläche "Repository erstellen". Anschließend füllt man das Formular wie folgt aus:

![Bild04.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild04.png)

Nach dem Erstellen des Repositories sollte es etwa wie folgt aussehen:

![Bild05.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild05.png)

## Optimiertes Dockerfile

__Aufgabe:__ Benutzen Sie Ihr __optimiertes Dockerfile__ aus dem Unterricht. Sollten Sie kein lauffähiges Dockerfile besitzen, verwenden Sie die Vorlage auf der nächsten Seite.

Im folgenden Link findet man meine Version des optimierten Dockerfiles mit allen dazugehörigen files:
Dockerfile: [https://github.com/masluse/m346-ref-card-01](https://github.com/masluse/m346-ref-card-01)

### Testen

Zunächst überprüfen wir das Image mit dem Befehl 'docker build' und starten dann einen Container daraus.

``` bash
docker build -t archrefcard-01:latest .
```

![Bild06.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild06.png)

Um sicherzustellen, dass Ihr erstelltes Image einwandfrei funktioniert, können Sie es mithilfe der Befehle "docker images" oder "docker inspect" überprüfen. Sobald Sie die notwendigen Informationen über Ihr Image erhalten haben, können Sie es lokal ausführen, indem Sie den Befehl "docker run" verwenden. Vergewissern Sie sich, dass die Ausführung des Images ohne Fehler erfolgt.

``` bash
docker run -d -p 8080:8080 archrefcard-01:latest
```

![Bild07.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild07.png)

### Image hochladen

1. Als erstes sollte man die push befehle in der AWS Konsole öffnen:

    ![Bild08.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild08.png)

2. Als nächstes sollte man den Token herausfinden:

    ``` bash
    aws ecr get-login-password --region us-east-1
    ```

    ![Bild09.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild09.png)

3. In Ihrem lokalen Terminal geben Sie nun den zweiten Teil des Befehls nach dem | ein.

    ``` bash
    echo "<TOKEN>" | docker login --username AWS --password-stdin 1234EXAMPLE.dkr.ecr.us-east-1.amazonaws.com
    ```

    ![Bild10.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild10.png)

4. Zum schluss muss das Image nur noch generiert und hochgeladen werden mit den folgenden befehlen:

    ``` bash
    docker build -t regli/rechsteiner-app-ref-card-01 .
    docker tag regli/rechsteiner-app-ref-card-01:latest 12345EXAMPLE.dkr.ecr.us-east-1.amazonaws.com/regli/rechsteiner-app-ref-card-01:latest
    docker push 12345EXAMPLE.dkr.ecr.us-east-1.amazonaws.com/regli/rechsteiner-app-ref-card-01:latest
    ```

    ![Bild11.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild11.png)

## VPC

Anschließend haben wir ein neues VPC erstellt, um unsere Arbeit zu erleichtern. Der Vorteil besteht darin, dass wir die Container in den privaten Subnetzen platzieren und über NAT-Instanzen eine Verbindung zum Internet herstellen können. Uns ist aufgefallen, dass die Container ohne Internetzugang nicht richtig starten und dass die Kosten in die Höhe getrieben werden, wenn jeder Container eine öffentliche IP-Adresse hat. Ein weiterer Punkt ist, dass es sicherer ist, wenn der Service selbst keine öffentliche IP-Adresse hat, sondern alles über den Load Balancer läuft.

![Bild11-01.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild11-01.png)

## ECS Cluster

__Aufgabe:__ Erstellen und dokumentieren sie einen __ECS-Cluster__. Achten Sie auf sinnvoll benannte Objekte, verwenden Sie keine generischen Namen mehr (z.Bsp. nicht nginx-custom oder fargate-service), sondern Ihren __nachnamen-refcard01__. 

Im folgenden sieht man die konfigruation die wir für das Cluster verwendet haben:

![Bild12.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild12.png)

![Bild13.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild13.png)

## Task Definition

__Aufgabe:__ Erstellen Sie eine __Task Definition__ für App Ref. Card 01. Recherchieren oder testen Sie die Minimal anforderungen an Prozessor und Speicher. 

Die Task-Definition war sehr einfach, da man nur das Image ":latest", einen Namen für den Container und einen Port angeben musste, der nach außen gemappt werden soll. Wir fanden es jedoch schade, dass man aus irgendeinem Grund nur den Container-Port angeben konnte und nicht noch separat den Host-Port, da wir später über Port 80 auf den Webserver zugreifen wollten. Wir haben dieses Problem jedoch einfach mit dem Load Balancer umgangen, indem wir ihm gesagt haben, dass er auf Port 8080 auf den Containern hören soll, aber von außen über Port 80 erreichbar sein soll.

![Bild14.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild14.png)

Die Aufgabe, die minimale Anforderungen an Prozessor und Speicher hatte, konnten wir schnell lösen. Wir haben uns für eine Konfiguration mit 0,25 vCPU und 0,5 GB RAM entschieden, da dies das niedrigste auswählbare Angebot war und der Container damit funktioniert hat.

![Bild15.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild15.png)

## Load-Balancer

__Aufgabe:__ Erstellen Sie sich einen __Load-Balancer__ vor Ihrem ECS Service

Um einen Load Balancer zu erstellen, navigiert man zuerst zur EC2-Konsole und wählt dann "Load Balancer" aus. Dort kann man einen neuen Load Balancer erstellen. Im nächsten Schritt muss man dann die Konfiguration des Load Balancers anpassen, je nach den spezifischen Anforderungen des eigenen Projekts. Hier ist ein Beispiel für die Konfiguration, die wir für unseren Load Balancer verwendet haben:

![Bild16.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild16.png)

![Bild17.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild17.png)

Sicherheitsgruppe für Loadbalancer erstellen:

![Bild18.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild18.png)

Target Gruppe für Loadbalancer erstellen:

![Bild19.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild19.png)

![Bild20.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild20.png)

## VPC Security Groups

__Aufgabe:__ Befassen Sie sich mit den __VPC Security Groups__. Verwenden Sie für die Fallstudie nicht die Default Security Group, sondern erstellen Sie eine neue, sauber benannte Security Group und sichern Sie diese nach "least privilege" ab. 

In der Security Group ist es speziell so konfiguriert, dass der einzige Inbound-Traffic, der erlaubt ist, über den Port 8080 kommt und ausschließlich vom Load Balancer stammt. Dadurch wird verhindert, dass Traffic, der nicht vom Load Balancer kommt, zu den Containern gelangen kann.

![Bild20-01.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild20-01.png)

## Service erstellen

Folgend sieht man die Konfiguration unseres Services

![Bild21.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild21.png)

![Bild22.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild22.png)

Besonders beim folgenden ist das die Container nur in die Privaten Subnetze kommen:

![Bild23.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild23.png)

Loadbalancer hinzufügen:

![Bild24.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild24.png)

Endergebnis:

![Bild25.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild25.png)

## Neue Versionen

__Aufgabe:__ Dokumentieren Sie den Ablauf für neue Versionen der ref-card-01: welche ECS Komponenten müssen aktualisiert werden? Dokumentieren Sie die benötigten Zeiten für den Neustart und wie lange mehrere Versionen aufrufbar sind.
__Zusatzaufgabe:__ Automatisieren Sie diesen Ablauf mit der AWS CLI.

=== "Aufgabe"

    src/main/resources/templates/index.html so bearbeiten das man nachher einen unterschied sieht:

    ![Bild26.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild26.png)

    Image erneut hochladen:

    ![Bild27.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild27.png)

    Auf dem Service den Neue Bereitstellung erzwingen Hacken auswählen und speichern:

    ![Bild28.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild28.png)

    Webserver kontrollieren:

    ![Bild29.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild29.png)

=== "Zusatzaufgabe"

    src/main/resources/templates/index.html so bearbeiten das man nachher einen unterschied sieht:

    ![Bild30.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild30.png)

    Image erneut hochladen:

    ![Bild31.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild31.png)

    Auf das AWS CLI gehen und den folgenden befehl ausführen:
    
    ``` bash
    aws ecs update-service --cluster <cluster-name> --service <service-name> --force-new-deployment
    ```

    ![Bild32.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild32.png)

    Webserver kontrollieren:

    ![Bild33.png](/images/ArchRefCard-01-mit-AWS-Fargate/Bild33.png)