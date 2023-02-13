# BIA-CODES

## **Flujo de trabajo**
- Se creó el proyecto en Django Rest Framework. Se tomó la decisión de trabajar con este framework por el conocimiento que tengo y por la capacidad para dividir los microservicios en app que trabajan independientes.

- **Creación de modelo de datos:** modelos de datos simple con tres tablas:
    - **RAW_DOCUMENT_RECORD:** Se almacenan todos los datos del archivo CSV sin transformaciones.
    - **METADATA_FILES:** Almacena la metadata del CSV entrante.
    - **POSTCODES**: es la tabla final donde se almacenan los datos limpios con los Postcodes obtenidos desde la API. 

- **Análisis de los datos:** Por medio de Google Colab, se hizo un análisis de los datos para identificar si existen coordenadas fuera de UK, las cuales no nos servirían para realizar los llamados a la API. Estos se actualizadon y en la columna postcode se marcó como ‘Fuera de UK’. [link](https://colab.research.google.com/drive/1zYPqemU0mdTqJBYxkOTSwfBSktiq98YP?usp=sharing)


- **Creación primer microservicio:** Este toma el archivo y lo guarda en la base de datos, así como es el encargado de hacer la limpieza de datos y hacer el llamado al otro microservicio.

- **Creación Segundo microservicio:** Es el microservicio que se encarga de llamar al API de POSTCODES. Este con los datos limpios y validados que están dentro de UK:
    - **Primera opción**: Hace el llamado 1 a 1 es el menos optimo porque se tendria que hacer un llamado a la API, por cada registro.
    - **Segunda opción Microservicio:** Se estaba construyendo un metodo con Bulk Reverse Geocoding de la API, para enviar en un solo query 100 coordenadas estrategicas por request para almacenar en la base de datos y despues comparar con las coordenadas del archivo, obteniendo un postcode cercano. 


## Instalación del Proyecto

### Descargar proyecto
Se debe descargar o clonar el proyecto, posteriormente debemos guardar el proyecto en un entorno local (computador) en la carpeta que se prefiera.

### Construir imagen Docker para el proyecto

```
docker build -t devrrior/bia_codes . 
```

### Correr el proyecto

```
docker run -p 8000:8000 devrior/docker-django 
```
### Probar la API
Cuando el proyecto ya esté corriendo desde local. Recibe el metodo POST a la ruta especificada abajo. Por medio de un header, se pasa como parametro 'file' y se adjunta el archivo. En el archivo Metodos_BIA_CODES se hace una especificación.
```
http://127.0.0.1:8000/file-csv
```
Cuando el proceso termine, obtendra como respuesta "Archivo Procesado".