# chat_solid

## Descripción

Chatbot modular en Python que sigue los principios SOLID, utilizando [ChatterBot](https://chatterbot.readthedocs.io/) como motor de respuestas. El proyecto está organizado en módulos independientes para entrada, procesamiento y salida, facilitando la mantenibilidad y escalabilidad.

---

## Principios SOLID aplicados

- **SRP (Single Responsibility Principle):** Cada clase tiene una única responsabilidad (entrada, procesamiento o salida).
- **OCP (Open/Closed Principle):** El sistema permite agregar nuevas funcionalidades (entradas, salidas, procesadores) sin modificar el código existente.
- **DI (Dependency Injection):** Las dependencias se inyectan desde `main.py`, facilitando pruebas y extensión.

---

## Estructura de Archivos

- `input_handler.py`: Gestiona la entrada del usuario.
- `output_handler.py`: Maneja la salida de mensajes al usuario.
- `response_generator.py`: Procesa la entrada utilizando ChatterBot.
- `main.py`: Orquesta la interacción entre los módulos.

---

## Requisitos

- Python 3.8, 3.9 o 3.10 (ChatterBot puede dar problemas en versiones superiores)
- [ChatterBot](https://chatterbot.readthedocs.io/)
- [spaCy](https://spacy.io/) y modelos de idioma requeridos

---

## Instalación rápida

```sh
# 1. Clona el repositorio
git clone https://github.com/tuusuario/chat_solid.git
cd chat_solid

# 2. Crea y activa un entorno virtual
python -m venv env
# En Windows:
.\env\Scripts\activate
# En Mac/Linux:
# source env/bin/activate

# 3. Instala las dependencias exactas
pip install -r requirements.txt

# 4. Instala el modelo de spaCy requerido por ChatterBot
python -m spacy download en_core_web_sm

# (Opcional) Si usas español:
python -m spacy download es_core_news_sm
```

---

## Uso

```sh
python main.py
```

Escribe tus mensajes en consola. Para salir, escribe `salir`, `adiós`, `bye`, `quit` o `exit`.

---

## Ejemplo de ejecución

```
¡Hola! Soy tu chatbot. Escribe 'salir' para terminar.
Tú: Hola
ChatBot: ¡Hola!
Tú: ¿Cómo estás?
ChatBot: Estoy bien, gracias por preguntar.
Tú: salir
ChatBot: ¡Hasta luego!
```

---

## Notas

- Si tienes problemas con la instalación de ChatterBot en Python 3.10+, revisa la [documentación oficial](https://chatterbot.readthedocs.io/) o instala desde el repositorio de GitHub.
- El archivo `db.sqlite3` es la base de datos local de ChatterBot, donde almacena el entrenamiento.
- Si necesitas generar el archivo `requirements.txt` ejecuta:
  ```sh
  pip freeze > requirements.txt
  ```

---

## Créditos

Desarrollado por Jesus Gonzalez para fines educativos.