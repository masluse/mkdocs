# Container mit AWS Fargate betreiben

Quelle: [https://bbwin.gitlab.io/m169-aws-fargate](https://bbwin.gitlab.io/m169-aws-fargate)

## Arbeitsumgebung
Für diesen Auftrag benötigen Sie:

- AWS Academy Learner Lab
- Windows mit WSL2 / Ubuntu / Mac
- Docker Desktop mit aktivierter WSL2 Integration

### Arbeitsverzeichnis

Starten Sie ein Terminal (WSL2 mit Ubuntu unter Windows) und erstellen Sie sich in Ihrem Homeverzeichnis ein neues Verzeichnis.

``` bash
mkdir m169-aws-fargate
cd m169-aws-fargate
```

### Docker

Wir arbeiten mit dem alpine-slim Nginx-Image, welches wir mit einem Dockerfile personalisieren. Die Grundlagen haben Sie im Auftrag 10.6_Docker Images erstellen erarbeitet.

Erstellen Sie die Datei Dockerfile (Gross-/Kleinschreibung beachten, keine Dateiendung):

``` dockerfile title="dockerfile"
FROM nginx:alpine-slim

COPY index.html /usr/share/nginx/html/index.html
```

Zusätzlich erstellen Sie sich die Datei index.html:

``` html title="index.html"
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>AWS Fargate Tutorial</title>
</head>

<body bgcolor="PaleGreen">
<p style="font-family: Helvetica">AWS Fargate Tutorial</p>
</body>

</html>
```

![Bildbeschreibung](/images/M169-AWS-Fargate/Bild2.png)

Als erster Arbeitsschritt prüfen wir docker build und starten daraus einen Container

``` bash
docker build -t nginx-custom:latest .
```

![Bildbeschreibung](/images/M169-AWS-Fargate/Bild3.png)

Überprüfen Sie Ihr erstelltes Image mit den bereits bekannten Befehlen images oder inspect, lassen Sie anschliessend Ihr Image lokal mit docker run laufen und stellen Sie eine fehlerfreie Ausführung sicher.

``` bash
sudo docker run -d -p 8080:80 nginx-custom:latest
```

![Bildbeschreibung](/images/M169-AWS-Fargate/Bild4.png)

## Amazon Elastic Container Registry

Im nächsten Schritt laden wir unser lokal erstelltes Image in die Amazon Elastic Container Registry, kurz ECR.

Dazu benötigen Sie Zugang zu Ihrem AWS Academy Learner Lab. Starten Sie Ihr Lab und öffnen Sie die AWS Management Console.

1. In der AWS Management Console, suchen Sie den Service Elastic Container Registry

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild5.png)

2. Wählen Sie Get Started um ein neues Repository zu erstellen

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild6.png)

3. Wählen Sie als Visibilitiy settings Private und als Repository name nginx-custom. Alle anderen Einstellungen können Sie wie vorausgewählt belassen.

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild7.png)

4. Wählen Sie Ihr soeben erstelltes Repository nginx-custom aus

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild8.png)

5. Rechts finden Sie View push commands. Es enthält personalisierte Befehle damit Sie sich authentifzieren und Ihr Image in Ihre Repository pushen zu können.

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild9.png)

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild10.png)

6. In Ihrem lokalen Terminal geben Sie nun den zweiten Teil des Befehls nach dem | ein.

    ``` bash
    echo "<TOKEN>" | docker login --username AWS --password-stdin 1234EXAMPLE.dkr.ecr.us-east-1.amazonaws.com
    ```

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild11.png)

7. Führen Sie nun die Schritte 2, 3 und 4 aus der Push commands for nginx-custom Anweisung in Ihrer Elastic Container Registry lokal im Terminal aus.

    ``` bash
    docker build -t nginx-custom .

    docker tag nginx-custom:latest 12345EXAMPLE.dkr.ecr.us-east-1.amazonaws.com/nginx-custom:latest

    docker push 12345EXAMPLE.dkr.ecr.us-east-1.amazonaws.com/nginx-custom:latest
    ```

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild12.png)

## Amazon Elastic Container Service

### Konzept

Amazon Elastic Container Service (ECS) ist vergleichbar mit Kubernetes, Docker Swarm, and Azure Container Service.

ECS unterstützt zwei unterschiedliche Betriebsmodelle:

- Fargate: Diese Option ist serverless - Sie können Container betreiben, ohne dass Sie Ihre Infrastruktur verwalten müssen. Geeignet für kleine Applikationen, Applikationen mit kurzzeitig hohen Lasten oder schnell wechselnde Lasten
- EC2: Sie konfigurieren EC2-Instanzen (Virtuelle Machinen) in Ihrem Cluster und stellen Sie sie bereit, um Ihre Container auszuführen. Geeignet für Applikationen mit konstant hoher CPU und Speichernutzung, Preisoptimierung oder Applikationen mit hohem Specherbedarf.

#### Task Definition
Die Task Definition ist eine Vorlage, die beschreibt, welche Docker-Container ausgeführt werden sollen und Ihre Anwendung darstellt. In unserem Beispiel wären es ein nginx-custom Container. Es beschreibt die zu verwendenden Images, die nötige CPU Rechenleistung, Speicher, die Umgebungsvariablen, die freizugebenden Ports und die Interaktion der Container.

#### Task
Aus einer Task Definition können Instanzen gestartet werden, welche die Container gemäss dieser Konfiguration beinhaltet. Aus einer Task Definition können beliebig viele identische Tasks erstellt werden.

#### Service
Definiert die minimale und maximale Anzahl von Tasks einer Task Definition, die zu einem bestimmten Zeitpunkt ausgeführt werden, sowie die automatische Skalierung und das Loadbalancing.

Falls die CPU durch den einzigen laufenden Task ausgelastet ist, kann der Service automatisch zusätzliche Tasks hinzufügen. Es erlaubt zudem die maximale Anzahl der Tasks zu begrenzen, die ausgeführt werden können. Dies hilft, die Kosten von AWS unter Kontrolle zu halten

#### Cluster
Der Service muss seine Tasks nun irgendwo ausführen können, damit sie zugänglich sind. Er muss einem Cluster zugeordnet werden und der Containerverwaltungsdienst sorgt selbstständig dafür, dass er genügend ECS-Instanzen für Ihren Cluster bereitstellt.

### Umsetzung

1. In der AWS Management Console, suchen Sie den Service Elastic Container Service

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild13.png)

2. Erstellen Sie unter Cluster mit Create cluster einen neuen Cluster. Verwenden Sie als Cluster name fargate-cluster

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild14.png)

3. Wählen Sie links im Menü Task definitions und erstellen Sie eine neue Task Definition mittels Create new task definition. Verwenden Sie nginx-custom als Cluster name und als Image URI Ihre persönliche URL zum privaten Repository aus dem Abschnitt Elastic Container Registry (Beispiel: 12345EXAMPLE.dkr.ecr.us-east-1.amazonaws.com/nginx-custom:latest)

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild15.png)

4. Nachdem Sie mittels Next zum Teil Configure environment, storage, monitoring, and tags gelangt sind, stellen Sie sicher, dass Sie unter Environment AWS Fargate (serverless) verwenden, setzen Sie CPU auf .25 vCPU und Memory auf .5 GB.

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild16.png)

5. Wählen Sie links im Menü Cluster und erstellen Sie einen neuen Service.

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild17.png)

6. Als Compute options wählen Sie Launch type und belassen die restlichen Voreinstellungen.

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild18.png)

7. Application type muss ein Service sein. Bei Task definition wählen Sie unter Family die zuvor erstellte Task definition nginx-custom mit Revision latest. Desired tasks ist in unserem Fall 1.

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild19.png)

8. Erstellen Sie eine neue Security Group mit dem Namen fargate-service und einer Beschreibung. Erlauben Sie Type HTTP und Source Anywhere.

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild20.png)

9. Loadbalancer.

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild21.png)

    ![Bildbeschreibung](/images/M169-AWS-Fargate/Bild22.png)

## Aktualisiertes Docker Image

Ihr Container läuft nun mit einer öffentlichen IP in AWS. Sie stören sich aber an der Hintergrundfarbe der Webseite und möchten deshalb eine neue Version Ihres nginx-custom erstellen.

Öffnen Sie dazu die Datei index.html in einem Editor (nano index.html oder falls Sie die Visual Studio Code Remote Development Extension aktiviert haben indem Sie das Verzeichnis mit code . in VS Code öffnen). Wählen eine neue Hintergrundfarbe und ersetzen Sie den Wert <body bgcolor="CornflowerBlue"> mit der gewählten Farbe. 

Wiederholen SIe die Push commands for nginx-custom aus dem Abschnitt Amazon Elastic Container Registry.

``` bash
docker build -t nginx-custom .
docker tag nginx-custom:latest 12345EXAMPLE.dkr.ecr.us-east-1.amazonaws.com/nginx-custom:latest
docker push 12345EXAMPLE.dkr.ecr.us-east-1.amazonaws.com/nginx-custom:latest
```

In Ihrem private Repository in AWS ECR finden Sie nun zwei Images.

![Bildbeschreibung](/images/M169-AWS-Fargate/Bild23.png)

Um den neuen Container im Service zu Deployen wähle den Service aus und gehe dann auf Aktualisieren.

![Bildbeschreibung](/images/M169-AWS-Fargate/Bild24.png)

Danach muss man den hacken "Neue Beretistellung erzwingen" auswählen und dann auf Aktualisieren. Wenn man dann eine weile wartet sollte die Loadbalancer URL umschalten.

![Bildbeschreibung](/images/M169-AWS-Fargate/Bild25.png)

![Bildbeschreibung](/images/M169-AWS-Fargate/Bild26.png)