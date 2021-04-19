#!/bin/bash

git add .
git reset HEAD push.sh

# quitamos archivos que no queremos modificar
# git reset config/settings.py

git commit -m "modificaciones en el trabajo"

# git push -u origin master
echo "¿Quiere subir los cambios?"
select sn in "Sí" "No"; do
    case $sn in
        Sí ) git push; break;;
        No ) exit;;
    esac
done

# para descartar todos los cambios locales
# git reset --hard HEAD

# para descartar un archivo
# git reset HEAD app/PRUEBA/urls.py

# eliminamos carpeta del repositorio
# git rm -r .idea/
# git commit -m "borrar carpeta idea"
# git push

# Limpiando archivos ignorados
# git clean -Xn      - Vista previa de todos los archivos que serán limpiados
# git clean -Xf      - Se eliminarán todos los archivos ignorados del directorio actual y todos los subdirectorios

# agregar archivos al listado de ignorados (si ya fueron subidos)
# por ejemplo: quiero ignorar el archivo settings.ini que ya fue sincronizado al repositorio
# 1. eliminamos la entrada del cache
#    git rm --cached config/settings.ini
# 2. lo agregamos al archivo .gitignore
#    echo 'config/settings.ini' >> .gitignore
# 3. realize un commit y push
#    git commit -m "actuaización de archivos ignorados"
#    git push

# si queremos agregar un archivo que fue ignorado al control
# git add -f requirements.txt
