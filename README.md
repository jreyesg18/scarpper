# scrapper

# BuscaJob

BuscaJob es un script en Python que extrae ofertas de trabajo para desarrolladores desde el sitio web. Utiliza la biblioteca `requests` para realizar solicitudes HTTP y `BeautifulSoup` para analizar y extraer datos de las páginas web.

## Requisitos

- Python 3.9+
- `requests` (biblioteca de Python)
- `beautifulsoup4` (biblioteca de Python)

## Instalación

1. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/tu-usuario/BuscaJob.git
    cd BuscaJob
    ```

2. Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```

3. Activa el entorno virtual:

    - En macOS y Linux:
        ```bash
        source venv/bin/activate
        ```
    - En Windows:
        ```bash
        .\venv\Scripts\activate
        ```

4. Instala las dependencias necesarias:
    ```bash
    pip install requests beautifulsoup4
    ```

## Uso

1. Asegúrate de tener activado el entorno virtual.

2. Ejecuta el script principal:
    ```bash
    python main.py
    ```

El script realizará una solicitud a la página web especificada, extraerá la información relevante sobre las ofertas de trabajo y la mostrará en la consola.

## Notas

Si ves una advertencia relacionada con `urllib3` y `LibreSSL`, puedes ignorarla o deshabilitarla agregando las siguientes líneas al inicio de tu script:

```python
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')
warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL 1.1.1+")
