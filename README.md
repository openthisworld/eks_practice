# eks_practice
EKS + simple python web app + docker + automate create container



Docker usage:

    docker build -t my-flask-app .

    docker run -p 8080:8080 my-flask-app

Add secrets for GitHub Actions:

    DOCKERHUB_USERNAME

    DOCKERHUB_TOKEN