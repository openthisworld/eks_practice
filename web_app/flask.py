from flask import Flask
import socket

app = Flask(__name__)

# Получаем уникальный идентификатор контейнера
def get_container_id():
    return socket.gethostname()

# Определяем маршрут для обработки запросов
@app.route('/')
def hello():
    container_id = get_container_id()
    return f'Hello! I am container: {container_id}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
