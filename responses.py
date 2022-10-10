from datetime import datetime

def sample_responses(message):
    user_message = str(message).lower()

    if user_message in ("Привет", "Привет!", "Прив"):
        return "Привет!"
    
    if user_message in ("Кто ты?", "Что ты за бот?"):
        return ("Привет, я Психология бот")
    
    if user_message in ("Время?", "Время"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)