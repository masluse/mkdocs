# Capture The Flag vorbereitung

-----------------------------------------------------------

## Dockerfile

Als ersten Schritt forken wir das Repository, das uns als Aufgabe gestellt wurde:

![Bild01.png](/images/capture-the-flag/Bild01.png)

Anschließend erstellen wir ein Dockerfile, welches einen ausführbaren Docker-Container generiert (Testen in einer VM oder im WSL, wenn auf Sicherheit geachtet werden soll). Nachfolgend sehen Sie ein beispielhaften Code:

![Bild02.png](/images/capture-the-flag/Bild02.png)

``` Dockerfile title='Dockerfile Java 11'
FROM maven:3-openjdk-11-slim as builder
COPY src /src
COPY pom.xml /
RUN mvn -f pom.xml clean package
FROM adoptopenjdk/openjdk11:alpine-jre
COPY --from=builder /target/*.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
```
 
``` Dockerfile title='Dockerfile Java 13'
FROM maven:3.6.1-jdk-13-alpine as builder
COPY src /src
COPY pom.xml /
RUN mvn -f pom.xml clean package
FROM adoptopenjdk/openjdk13:alpine-jre
COPY --from=builder /target/*.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
```
 
``` Dockerfile title='Dockerfile Java 17'
FROM maven:3.8.5-openjdk-17-slim as builder
COPY src /src
COPY pom.xml /
RUN mvn -f pom.xml clean package
FROM eclipse-temurin:17-jre-alpine
COPY --from=builder /target/*.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
```

-----------------------------------------------------------

## Repository erstellen

Nachdem das Dockerfile erstellt wurde, starten wir das Learner-Lab, navigieren zum Service ECR und erstellen ein neues privates Repository.

![Bild03.png](/images/capture-the-flag/Bild03.png)

![Bild04.png](/images/capture-the-flag/Bild04.png)

-----------------------------------------------------------

## GitLab-Variablen

Um geheime Informationen für CI/CD nicht für jeden zugänglich zu machen, müssen wir Secret Variables erstellen. Die ersten drei finden wir im Learner Lab, wenn wir auf AWS-Details und dann auf AWS CLI klicken. Die Variablen heißen: "AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY" und "AWS_SESSION_TOKEN".

![Bild05.png](/images/capture-the-flag/Bild05.png)

Die weiteren drei Variablen finden wir im neu erstellten Repository. Die Variablen und ihre Werte sind: "AWS_DEFAULT_REGION" = "us-east-1", "CI_AWS_ECR_REGISTRY" = "910977011815.dkr.ecr.us-east-1.amazonaws.com" und "CI_AWS_ECR_REPOSITORY_NAME" = "refcard-03".

![Bild06.png](/images/capture-the-flag/Bild06.png)

-----------------------------------------------------------

## .gitlab-ci.yml erstellen

Im Folgenden wird ein .gitlab-ci.yml vorgestellt, das dazu dient, ein Docker-Image zu generieren und es in ein AWS-Repository hochzuladen.

![Bild07.png](/images/capture-the-flag/Bild07.png)

``` yaml title='.gitlab-ci.yml'
image: docker:23.0.4

variables:
  DOCKER_HOST: tcp://docker:2375
  DOCKER_TLS_CERTDIR: ""

services:
  - docker:23.0.4-dind

package:
  stage: build
  before_script:
    - apk add --no-cache py3-pip
    - pip install awscli
    - aws --version

    - aws ecr get-login-password | docker login --username AWS --password-stdin $CI_AWS_ECR_REGISTRY

  script:
    - docker build --cache-from $CI_AWS_ECR_REGISTRY/$CI_AWS_ECR_REPOSITORY_NAME:latest -t $CI_AWS_ECR_REGISTRY/$CI_AWS_ECR_REPOSITORY_NAME:latest .
    - docker push $CI_AWS_ECR_REGISTRY/$CI_AWS_ECR_REPOSITORY_NAME:latest
```

Sobald diese Datei erstellt wurde, sollte automatisch ein Runner gestartet werden, vorausgesetzt ein solcher ist konfiguriert. Dies kann man unter Settings - CI/CD - Runners überprüfen.

![Bild08.png](/images/capture-the-flag/Bild08.png)

-----------------------------------------------------------

## Erstellen eines ECS Clusters

Anschließend beginnen wir mit der Erstellung eines ECS Clusters. Der Name spielt hierbei keine Rolle, wichtig ist nur, den Namespace zu entfernen, damit das Cluster im Learner Lab erstellt werden kann.

![Bild09.png](/images/capture-the-flag/Bild09.png)

-----------------------------------------------------------

## Datenbank erstellen (optional)

Für refcard03 war es notwendig, eine Datenbank zu verbinden, daher habe ich ein RDS erstellt. Für die Capture The Flag Aufgabe ist dies jedoch nicht erforderlich.

![Bild10.png](/images/capture-the-flag/Bild10.png)

-----------------------------------------------------------

## Erstellung einer Task Definition

Nun erstellen wir eine Taskdefinition mit der Image-URL des Repositories (am Ende sollte :latest stehen). Der Port ist vom Image abhängig und die Environment-Variablen werden nur mit der RDS-Datenbank benötigt.

![Bild11.png](/images/capture-the-flag/Bild11.png)

Für Task-Rolle und Task-Ausführungsrolle sollten wir "LabRole" auswählen.

![Bild12.png](/images/capture-the-flag/Bild12.png)

-----------------------------------------------------------

## Änderung der Security Group

Aus Gründen der Schnelligkeit kann man in der Default Security Group festlegen, dass jeder eingehende Traffic zugelassen wird.

![Bild13.png](/images/capture-the-flag/Bild13.png)

-----------------------------------------------------------

## Erstellung eines Services im ECS Cluster

Folgen Sie den untenstehenden Konfigurationen (je nach Docker-Image können Änderungen erforderlich sein).

![Bild14.png](/images/capture-the-flag/Bild14.png)

![Bild15.png](/images/capture-the-flag/Bild15.png)

![Bild16.png](/images/capture-the-flag/Bild16.png)

-----------------------------------------------------------

## Testen des Loadbalancers

Um den Loadbalancer zu testen, können wir zu EC2 gehen und dort auf Loadbalancer klicken. Anschließend kopieren wir den DNS-Namen.

![Bild17.png](/images/capture-the-flag/Bild17.png)

Diesen Loadbalancer-Namen geben wir dann in den Browser ein und nach einiger Zeit sollten wir die Webanwendung sehen.

![Bild18.png](/images/capture-the-flag/Bild18.png)