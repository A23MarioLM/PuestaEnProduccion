## Escenario2

### Crear un archivo sensible

```bash
echo "Este es un archivo sensible" > archivo_secreto.txt
```



#### Permisos actuales  del archivo sensible

> -rw-rw-r--



### Crear un archivo de configuración para Nginx

```bash
echo "server {
    listen 80;
    server_name localhost;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }

    location /archivos {
        alias /archivos_restringidos;
    }
}" > nginx.conf
```



### Crear un contenedor Nginx con el archivo de configuración

```bash
docker run -d -p 8080:80 -v $(pwd):/archivos_restringidos -v $(pwd)/nginx.conf:/etc/nginx/conf.d/default.conf --name nginx-container nginx
```



### Acceder al container

```bash
docker exec -ti nginx-container /bin/sh
```



### Instalamos utilidades necesarias para luego

```bash
apt update
apt install -y nano
apt install -y apache2-utils
```



#### Cambiar contraseña de "root"

```bash
bash
passwd root
#abc123.
```



### Añadimos un nuevo usuario

```bash
useradd mario
passwd mario
#abc123.
```



### Intentar acceder al archivo sensible sin autorización

```bash
curl http://localhost/archivos/archivo_secreto.txt
```

**tenemos acceso**



\***Ahora desde fuera del container**

### Intentar acceder al archivo sensible sin autorización

```bash
curl http://localhost:8080/archivos/archivo_secreto.txt
```

**tenemos acceso**



<span style="color:red">**\*Ahora mismo no tenemos seguridad, cualquiera puede ver el contenido del archivo_secreto. Para arreglarlo haremos lo siguiente:***</span>




### Accedemos de nuevo al container

```bash
docker exec -ti nginx-container /bin/sh
```



### Crear un archivo de contraseñas

```bash
htpasswd -c archivos_restringidos/.htpasswd mario
#abc123.
```



### Modificamos el archivo de configuración nginx.conf

```bash
server {
    listen 80;
    server_name localhost;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }

    location /archivos {
        alias /archivos_restringidos;

        # Configuración de autenticación básica
        auth_basic "Acceso restringido";
        auth_basic_user_file /archivos_restringidos/.htpasswd;
    }
}

```



### Reiniciamos el container

```bash
docker restart nginx-container
```



### Hacemos la pruebas desde el propio container

### Accedemos de nuevo al container

```bash
docker exec -ti nginx-container /bin/sh
```



#### Intentar acceder al archivo sensible sin autorización

```bash
curl http://localhost/archivos/archivo_secreto.txt
```

**no tenemos acceso**



### Intentar acceder al archivo sensible con autorización

```bash
curl --user mario http://localhost/archivos/archivo_secreto.txt
```

**tenemos acceso**



### Hacemos la pruebas desde local

#### Intentar acceder al archivo sensible sin autorización

```bash
curl http://localhost:8080/archivos/archivo_secreto.txt
```

**no tenemos acceso**



### Intentar acceder al archivo sensible con autorización

```bash
curl --user mario http://localhost:8080/archivos/archivo_secreto.txt
```

**tenemos acceso**

