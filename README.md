# Fapro - Interview

## Contenido

* [Ejecutar con Docker](#ejecutar-con-docker)
* [Ejecutar con virtualenv](#ejecutar-con-virtualenv)
* [Endpoints](#endpoints)

## Ejecutar con Docker

1. Hacer build de la imagen de docker.

```sh
docker build -t desanchezca/fapro_interview:v1.0 .
```

2. Ejecutar el contenedor.

```sh
docker run --rm -p 8080:8080 desanchezca/fapro_interview:v1.0
```

- Ejecutar tests:

```sh
docker run --rm desanchezca/fapro_interview:v1.0 pytest
```


## Ejecutar con virtualenv

1. Crear y habilitar en entorno virtual

```sh
python3 -m venv venv
source venv/bin/activate
```

2. Instalar paquetes

```sh
python -m pip install -r requirements.txt
```

3. Iniciar aplicación

```sh
python src/main.py
```


- Ejecutar tests:

```sh
pytest
```


## Endpoints

- URL base: http://localhost:8080

| Metodo |     Ruta      |                            Descripción                             |                           Parametros                           |            Ejemplo            |
|--------|:-------------:|:------------------------------------------------------------------:|:--------------------------------------------------------------:|:-----------------------------:|
| GET    | /fomento_unit | Consultar el valor de la unidad de fomento en una fecha especifica | date (Por defecto: Hoy), formato "dia-mes-año" e.g. 25-12-2023 | /fomento_unit?date=25-12-2022 |
