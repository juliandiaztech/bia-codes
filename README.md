# BIA-CODES

## **Flujo de trabajo**
- Se creó el proyecto en Django Rest Framework. Se tomó la decisión de trabajar con este framework, por el conocimiento que tengo sobre este y por la capacidad para dividir los microservicios en app que trabajan independientes.

- **Creación de modelo de datos:** modelos de datos simple con tres tablas:
    - **RAW_DOCUMENT_RECORD:** Se almacenan todos los datos del archivo CSV sin transformaciones.
    - **METADATA_FILES:** Almacena la metadata del CSV entrante.
    - **POSTCODES**: es la tabla final donde se almacenan los datos limpios con los Postcodes obtenidos desde la API. 

Se adjunta un esquema Entidad-Relación para dar más claridad.[link](https://viewer.diagrams.net/?tags=%7B%7D&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Entidad-Relaci%C3%B3n%20BIA#R7Vxdc5s4FP01nmkf0uHDjtNHf7addZqs46bdffEoIGO2gDxCjvH%2B%2BpVAGLBkF9Z2TIEZTwIXWaB7jo6EdH1b%2BsANPmGwWt4jEzotTTGDlj5saZqmdNv0H7NsI8udrkUGC9tmZFITw5P9L%2BRGhVvXtgn9TEGCkEPsVdZoIM%2BDBsnYAMZoky22QE72ritgQcHwZABHtH63TbLkregoif0ztK1lfGdV4VdcEBfmBn8JTLTJmGBAxsgj%2FBEfIXaBBz1Cr9wD%2FBPiVme0JIS1tNfSxvSzYKU%2FWAhZDgQr2%2F9gIJeaDZ8WGS%2BAazvMzamK%2Brwiejt91NIHGCESHbnBADoMqxiG6JnGB67u%2FIBZvTm%2BMLh53U5%2BKsT7vNGfyf299dh9uVE5%2BK%2FAWXMHc%2BeQbexxaFIA%2BCm9l022U%2BgAYiNvlFzpQ8%2FsMXhpodGUtpa2u%2B8TgEliRR4vOLbpk%2BlDJS6SOoeBTX7QY5Uf%2F8XsHzr8bBikig23%2FET0BHeOj9bYgEear3MCA2xBcsxNXc4PM0NO7uhPELmQ4C0tsEkouSPeMk3H2IhDF75mSQ048axdhbt7PCI75CHvx%2B24Ht6L1TslW0XUdP6tNCv2K7rNVqQpnWxFkW%2BEiuhBquGJKSRdAQKK%2FLsfzXrD3qw3H3%2BZjJ4ENtJeu2KHBLyEvAsJxGVKZ2ygwkOA7dE%2BFrHIQI4DVr4dFo8sS9sxJ2CL1iSuKD7rL%2BwAmtNIpVhZyt0JrcznVGP9Pe4L7DJwbMujxwalHrtjH0OfPssE%2BISXOEjOV4gJDI6yiV%2FV9SxGMWQpsmkdGdlulcO8ygBZFDX916oR40RbTmzgTOlYADwrhCyLCHOridFqFndCZlgxvkE8eoWRGoe%2BpyoxQA5iwHqRloTFwsZ1%2BvRDmztgYtGhDzCg52pyTj%2BsOCYD5PkEAztEA1KcNpBh1Sdoxe%2FjwEX8GJg7kx2%2FIEKouB9C9Si7fw01h1bPCa1%2BKWTbArKPfxTBFtG2LpxQ8Je2aUIv6pFsKgASvCVQSv2%2F8%2Fk%2BGPv9MCceem48UgDoBf3PK0u8Urg24FDue4DAPlp7pn8J3e0IOCNsQjynXxporZ4SDRJfH2bs77fJpLWbNZWJBrH8RmX7%2FgoYtmdNom%2Fe7vGkcwmeBK2D%2FVY7K29yVfcGxLmts%2FTLZ5vnkf68o%2FrFpL97ErJv1ONzev82t%2FerLvR3AqoecOHcRMbahXxOXy6IfynqZ%2BdA7UT8YyPilxHxj9cW8XiZrhIq%2FjG3%2B6uu4qoqwOqt3Rc6YUeLOYYGnbz7JcT5XFKenwhVlvLuYPMFfgk2wbITzEbfree%2F%2Fa83%2BmnTtkbLD2q5qr2hmMuxFSdvJezkov%2BPE7VWai53hTj%2FMjCktzTnoCIz8lMpUGUdl4%2Fw4pr648PTbPAwbDZBwuWRWHmLqvMO4PPPtcXF8hoNvQWW3dX866ll2QdRxQXyKm2E7Khbq8FY7gpxRbvZBCnIkfqN1s1b16Wk%2F%2Br7IKr41jUuo%2FTnRaCW711yV4jvXfE%2BCNv4ptrC4voUu9LbIgX4UDtZjx%2BjkfWzy%2FrVd0Y0cQm9hL08p%2F93RG1EPYYxhauDPMsmaxNGej52ENifyJcO%2BHPJewFmVFnepeuPeaLdG3n%2FX%2FJ%2B%2Fc0SyQJqCbu5CMBxptZK3%2BWuEFdZ2U8nQnmPZ%2BxVVfhTuVE%2FhReXbRuFP5PCd66u8KfFHpdM4Tu5Aai8wouLqSvkEwOlFP4ZYGMJ8Lu28r42Op%2BfIbXTeb3WW6%2BX1fm7a%2Bu8ftogXi6d12u50yp3hTh%2Bp8OeuNIT26X9Abiruuh8AYZUWeflq1niS%2F20930%2BfBh8ux99nc2no8HDdNgESDHI4tD%2F%2BJf8eXX8cj8T12o9Shf5nfjvFyClVTtASqvlsC13hTRAKrNZXtsYqQI0qd%2FY3cRIXUr9rx4jpVUrRkprYqR2rjgeIxXGxbbqESlVgBVVFnfpS2uTBuRS2v6WgVJSaH%2FTPCBHaVorXZd6QhywkyipzDb6u%2FclhPtca21NTpCDrmlyglxK0UsQG3VaXHO5NL2WWUHksIohzfLQqEprepMc5KBr2uL2yQwG4jsbYUa9vyQuy8Ms3bJg7rUN4PT4BZcyI2RLuJeR4kVWv5lEgzVBfrT3wqqmUo1%2Bwj3qSNgkwl94T%2BRuL3NuRwJ9WwLVOX4yPlXgvAuejV6%2F7XYV1dn8uV7fqILr09m16VC2RBbygJPOrI0ZPaDJ3ZuUmaCwuzGX%2FgMJ2fLtLebtLJbUf3j7g38%2FPEll1WanSVrt8CzOqy1N3y0k7Jbk%2Fc6m%2BI6avJc6%2B7L5uqM3d5EWubNuHwCZniYJ26NOmmTZ10f%2FAQ%3D%3D)

- **Análisis de los datos:** Por medio de Google Colab, se hizo un análisis de los datos para identificar si existen coordenadas fuera de UK. Las cuales no servirían para realizar los llamados a la API. Estos se actualizadon y en la columna postcode se marcó como ‘Fuera de UK’. [link](https://colab.research.google.com/drive/1zYPqemU0mdTqJBYxkOTSwfBSktiq98YP?usp=sharing)


- **Creación primer microservicio:** Este toma el archivo y lo guarda en la base de datos, así como es el encargado de hacer la limpieza de datos y hacer el llamado al otro microservicio. 
Este tiene como función almacenar y actualizar la información en la base de datos.

- **Creación Segundo microservicio:** Es el microservicio que se encarga de llamar al API de POSTCODES. Este con los datos limpios y validados que están dentro de UK:
    - **Primera opción**: Hace el llamado 1 a 1 es el menos optimo porque se tendria que hacer un llamado a la API, por cada registro.
    - **Segunda opción Microservicio:** Se estaba construyendo un metodo con Bulk Reverse Geocoding de la API, para enviar en un solo query 100 coordenadas estrategicas por request, almacenar en la base de datos y despues comparar con las coordenadas del archivo, obteniendo un postcode cercano. 


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

## NOTA
Tambien se puede probar por virtualenv. Se debe instalar la libreria virtualenv en la maquina local. Crear y activar un entorno virtual, luego con el siguiente comando instalar las librerias del archivo requirements.txt.

```
pip install -r requirements.txt
```

Posteriormente, se puede correr el proyecto con el siguiente comando.

```
python manage.py runserver
```