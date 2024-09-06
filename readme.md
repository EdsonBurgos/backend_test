# PRUEBA TÉCNICA CASA MECATE

## BackEnd - REACT

Proyecto creado para la prueba técnica de Casa Mecate. Fue un reto, me divertí aprendiendo a utilizar python con flask y
agradezco
por la oportunidad de salir de mi zona de confort y aprender algo nuevo.

## Ejecutar proyecto

Para poder visualizar el proyecto tenemos dos formas, la primera y más sencilla es la ejecución que ofrece el mismo
python, y la segunda forma ya es mediante un servidor, en este caso, un servidor apache2.

Una vez clonado el proyecto, es necesario ejecutar los siguientes comandos dentro del directorio raíz del proyecto

* Crear el entorno virtual para trabajar
    * `virtualenv .venv`
* Activar entorno virtual a trabajar
    * `source .venv/bin/activate`
* Instalar dependecias del proyecto
    * `pip install -r requirements.txt`

### Sin servidor

Para ejecutar el proyecto mediante python sin tener un servidor, hay que ejecutar el siguiente commando
```python run.py``` dentro del directorio raíz del proyecto.

Esto te devolvera una url local en la cual ver el proyecto

### Con Servidor [Apache](https://httpd.apache.org/)

Para configurar el servidor solo es necesario tener instalado el servidor e iniciar sus servicios.
Recomiendo revisar el
siguiente [tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04-es)
que explica de manera sencilla como montar un servidor en [ubuntu](https://ubuntu.com/)

Crea el certificado de autofirmado

* Habilita el mod WSGI
    * `sudo apt-get install libapache2-mod-wsgi -y`
* Reinicia apache
    * `sudo systemctl restart apache2`
* Crea el certificado de autofirmado
    * ```sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt```
* Completa la información solicitada
    * ![img.png](https://raw.githubusercontent.com/EdsonBurgos/frontend_test/master/img.png)
* Listo

Una vez teniendo el servidor listo vamos a hacer lo siguiente

* Ubicar el directorio de trabajo `/var/www/`
* Clonar este proyecto dentro del directorio
* Crea el vhost dentro de `/etc/apache2/sites-available/[nombre].conf`
    * nombre: el nombre que quieras ponerle a tu vhost
* Plantilla de vhost con autofirmado

```apacheconf
<VirtualHost *:80>
        ServerName [url.domain]
        Redirect / https://[url.domain]/
</VirtualHost>

<VirtualHost *:443>
    ServerName [url.domain]

    WSGIDaemonProcess backend_test user=edson group=edson threads=1
    WSGIScriptAlias / /var/www/[dir_name]/wsgi.py

    <Directory /var/www/[dir_name]>
        WSGIProcessGroup [dir_name]
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>

    ErrorLog /var/www/[dir_name]/app/logs/error.log
    CustomLog /var/www/[dir_name]/app/logs/access.log combined

    SSLEngine on
    SSLCertificateFile /etc/ssl/certs/apache-selfsigned.crt
    SSLCertificateKeyFile /etc/ssl/private/apache-selfsigned.key
</VirtualHost>

```

* Copia esta plantilla dentro de tu archivo conf
    * url.domain: Es la url donde quieras montar el proyecto
        * Agrega esta misma dentro dee tu archivo `/etc/hosts`
            * `sudo nano /etc/hosts`
            * Agrega la línea
                * 127.0.0.1       "[url.domain]"
    * dir_name: Nombre del directorio del proyecto clonado
* Habilita tu host con el siguiente comando y el nombre de tu archivo conf`sudo a2ensite [nombre].conf`
* Reinicia apache y tendrás listo tu proyecto