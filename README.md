# api-modelo-red-neuronal

This project uses a pre-trained Keras model to predict images through a FastAPI endpoint.

## Setup with Docker

run the following command in the terminal to setup the project:

```sh
docker-compose up -d --build
```


## Usage

1. Go to `http://127.0.0.1:8000` to see the welcome message.

2. Use the `http://localhost:8000/project1/predicts/` endpoint to make predictions.

    example:
    ```sh
    curl -X 'POST' \
    'http://localhost:8000/project1/predicts/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "message": "¿En qué medida está satisfecho con la capacidad de la red para gestionar el tráfico IPv6 y garantizar la conectividad en el entorno de producción? teniendo en cuenta que 1 es insatisfecho y 5 es muy satisfecho.",
    "type": "implementacion"
    }'
    ```
    type options: "implementacion", "software", "planeacion", "hardware","capacitacion"

    response:

    ```json
    {
    "predictions": " Nuestra empresa ha recibido el apoyo y compromiso de la alta dirección para la planificación y ejecución de la transición a IPv6, considerando la necesidad de actualizar nuestros sistemas de gestión de la tecnología y mejorar la eficiencia en la colaboración con nuestros clientes."
    }
    ```