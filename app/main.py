from telethon import events
from app.client import get_client
from app.topic_service import list_topics
from app.file_service import get_files_from_topic

client = get_client()
chat_link = "https://t.me/+CXM7VjXkpeMzMmEy"    # My group

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond(
        "Я user-bor для получения списка файлов по темам.\n"
        "Отправь мне /topics чтобы увидеть список тем."
        )
    
@client.on(events.NewMessage(pattern="/topics"))
async def topics(event):
    topics = await list_topics(client, chat_link)

    msg = "Список тем:\n"
    for i, t in enumerate(topics, 1):
        msg += f"{i}. {t.title}\n"
    await event.respond(msg)

@client.on(events.NewMessage(patterm="/getfiles"))
async def get_files(event):
    topic_number = int(input("Введите номер темы: "))

    file_list = await get_files_from_topic(client, chat_link, topic_number)

    with open("file_list.txt", "w", encoding="utf-8") as f:
        for file in file_list:
            f.write(f"{file}\n")

    await event.respond("Список файлов сохранён в files_list.txt")


if __name__ == "__main__":
    if client.start():
        print("Бот запущен")
        client.run_until_disconnected() 