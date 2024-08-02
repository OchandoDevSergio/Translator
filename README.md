# TRADUCTOR IA

## Tecnologías y dependencias
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat)](https://docs.python.org/3/) [![OpenAI Badge](https://img.shields.io/badge/OpenAI-412991?logo=openai&logoColor=fff&style=flat)](https://platform.openai.com/docs/concepts) [![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff&style=flat)](https://developer.mozilla.org/en-US/docs/Glossary/Git)


## Indice 

- [Descripción general del proyecto :speech_balloon:](#descripción-general-del-proyecto)

- [Modo de empleo :on:](#modo-de-empleo)

- [Vistas :computer:](#vistas) 

- [Funcionamiento :arrow_forward:](#funcionamiento)

- [Recursos alternativos y fuentes :art:](#recursos-alternativos-y-fuentes)  

#

### Descripción general del proyecto

El presente proyecto se propone desarrollar una aplicación web desde la que poder capturar audio en castellano para posteriormente traducirlo a diferentes idiomas y devolverlo como audio locutado en los mismos.

### Modo de empleo

Pasos para lanzar la aplicación:

1- Abrir un terminal y situándose en el directorio del proyecto, generar un entorno virtual con el comando:
  python -m venv "nombre del entorno"
Activar el entorno virtual con el comando correspondiente según el terminal.

2-Instalar las dependencias necesarias, ejecutándo en el mismo terminal el comando:
  pip install -r requirements.txt

3-Ejecutar el fichero **main.py**

4- Se accede a través del buscador a la URL:

http://127.0.0.1:7860

***En caso de no disponer de servicio en la api de elevenlabs, generar una cuenta y sustituir la API key del fichero **.env** por la de la nueva cuenta generada.

### Vistas

La aplicación dispone de una única vista con componentes gennerados por Gradio, en la que se muestra en la parte izquierda un capturador de audio y en la parte derecha los outputs en los diferentes idiomas disponibles.

<img src="https://i.ibb.co/nLykdHk/Sin-t-tulo.jpg" alt="Sin-t-tulo" border="0" />

### Funcionamiento

Esta aplicación se ha desarrollado principalmente en el fichero main.py con sólo 85 líneas de código. Para ello hemos empleado la tecnología **Gradio** que consta de una librería de componentes pregenerados. Hemos seteado que se introduzca un input de audio, este se pase por la función *translator_function()* que hemos desarrollado y dé lugar a 4 outputs de audio, uno por cada idioma a los que se traduce.

La función *translator_function()* emplea la tecnología **whisper** de openAI para tomar el audio, que introducimos por el micrófono o por un sistema de upload y transcribirlo a texto. A continuación emplea la tecnología **translate** de python para traducir el texto transcrito a los 4 idiomas y por último emplea la tecnología de **elevenlabs** para locutar cada traducción, mostrándolas en sus respectivos outputs.

### Recursos alternativos y fuentes

https://www.gradio.app/

https://openai.com/index/whisper/

https://pypi.org/project/translate/

https://pypi.org/project/python-dotenv/

https://elevenlabs.io/

https://tutorialmarkdown.com/emojis

https://badges.pages.dev/

https://imgbb.com/