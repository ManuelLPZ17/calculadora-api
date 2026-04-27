# Calculadora API — CI/CD con Kubernetes

API REST de operaciones matemáticas desplegada en Kubernetes con pipeline CI/CD usando GitHub Actions.

## Descripción

REST API construida con FastAPI que expone cuatro operaciones matemáticas.
Cada operación se desarrolló en su propio branch e integrada a main mediante Pull Requests.
El pipeline automatiza las pruebas, la publicación de la imagen en Docker Hub
y el despliegue en un cluster de Kubernetes corriendo en AWS.

## Estructura del repositorio

calculadora-api/
├── app/
│   ├── main.py              # endpoints de la API
│   └── operations.py        # lógica de operaciones matemáticas
├── tests/
│   └── test_main.py         # tests unitarios de cada endpoint
├── k8s/
│   ├── deployment.yaml      # manifest de Kubernetes - Deployment
│   └── service.yaml         # manifest de Kubernetes - Service (NodePort)
├── .github/
│   └── workflows/
│       ├── integrate.yml    # CI: corre tests en cada PR hacia main
│       ├── delivery.yml     # CD: build y push a Docker Hub al hacer tag
│       └── deploy.yml       # CD: aplica manifests al cluster de Kubernetes
├── Dockerfile
├── requirements.txt
└── .gitignore

## Endpoints

GET /                          estado de la API
GET /suma?a=&b=                suma de dos números
GET /resta?a=&b=               resta de dos números
GET /multiplicacion?a=&b=      multiplicación de dos números
GET /division?a=&b=            división de dos números

## Pipeline CI/CD

### integrate
- Se dispara en cada Pull Request hacia main
- Instala dependencias y corre pytest
- El PR no se puede mergear si los tests fallan

### delivery
- Se dispara cuando se hace push de un tag v* (ej: v1.0.0)
- Construye la imagen Docker y la publica en Docker Hub
- Publica con el tag de versión y con latest

### deploy
- Se dispara automáticamente cuando delivery termina con éxito
- Configura kubectl con el kubeconfig del cluster
- Aplica los manifests de Kubernetes
- Verifica que el rollout se complete

## Infraestructura

Cluster de Kubernetes con K3s sobre una instancia EC2 en AWS (us-east-1).
Se usó K3s en lugar de EKS porque el Learner Lab no permite los permisos
IAM necesarios para crear roles de EKS.

## Secrets requeridos en GitHub

DOCKERHUB_USERNAME   usuario de Docker Hub
DOCKERHUB_TOKEN      personal access token de Docker Hub
KUBECONFIG_B64       kubeconfig del cluster codificado en base64

## Cómo correr localmente

pip install -r requirements.txt
pytest tests/ -v
uvicorn app.main:app --reload

## Flujo de desarrollo

# nueva operación
git checkout -b feat/nombre-operacion
git push origin feat/nombre-operacion
# crear PR en GitHub → integrate corre automáticamente
# hacer merge cuando los tests pasen

# publicar versión
git checkout main
git pull origin main
git tag v1.0.0
git push origin v1.0.0
# delivery y deploy corren automáticamente
