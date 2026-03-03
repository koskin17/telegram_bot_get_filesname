from telethon.tl.types import Channel, Chat
from telethon.tl.functions.channels import GetFullChannelRequest

async def list_topics(client, chat_link):
    """Return list of topics in specified group / channel"""

    entity = await client.get_entity(chat_link)
    full = await client(GetFullChannelRequest(channel=entity))

    topics = []

    # Проверяем, есть ли топики
    if hasattr(full.full.chat, 'forum_topic'):
        topics.append(full.full_chat)

    return topics