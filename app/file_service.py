async def get_files_from_topics(client, chat_link, topic_number):
    """Getting list of files from specified group / channel"""

    entity = await client.get_entity(chat_link)

    #Getting all messages
    messages = await client.get_messages(entity, limit=1000)    # Limit можно убрать потом

    files = []
    for msg in messages:
        if msg.document:
            file_name = msg.file.name or "Noname"
            files.append(file_name)

        return files
