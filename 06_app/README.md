## local kubernetes cluster 

Setting up local Kubernetes with minikube focusing on easy learning and develop for Kubernetes.

### Requirement

    minikube
    kubectl
    docker

### Installation

   1. [minikube](https://minikube.sigs.k8s.io/docs/start)
   2. [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux)
   3. [Web UI (Dashboard)](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard)
   4. [Docker](https://docs.docker.com/engine/install/ubuntu/)


### Quick Start
   
   4. docker build . -t stefanpapp/springboot 
   5. nohub kubectl proxy &
   6. (Creating Service Account) kubectl apply -f dashboard-admin.yaml
   7. kubectl apply -f deployment.yml
   8. kubectl apply -f service.yml
   9. kubectl apply -f load_balancer.yml #Optional
   10. kubectl apply -f ingress.yaml
