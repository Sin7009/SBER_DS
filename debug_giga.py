import os
import sys
from langchain_community.chat_models import GigaChat
from langchain_core.messages import HumanMessage, SystemMessage

def test_connection():
    """
    Минимальный скрипт для проверки соединения с GigaChat API.
    """
    print("Запускаю тест соединения с GigaChat...")

    if 'GIGACHAT_CREDENTIALS' not in os.environ:
        print("ОШИБКА: Переменная окружения GIGACHAT_CREDENTIALS не найдена.")
        sys.exit(1)

    credentials = os.environ['GIGACHAT_CREDENTIALS']
    print("Учетные данные найдены.")

    try:
        chat = GigaChat(
            credentials=credentials,
            verify_ssl_certs=False,
            scope='GIGACHAT_API_PERS'
        )
        print("Объект GigaChat инициализирован.")

        messages = [
            SystemMessage(content="Ты простой бот для теста."),
            HumanMessage(content="Скажи 'тест'"),
        ]

        print("Отправляю сообщение в GigaChat...")
        response = chat.invoke(messages)
        print("Ответ получен.")
        print(f"Ответ GigaChat: {response.content}")
        print("Тест успешно завершен!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_connection()
