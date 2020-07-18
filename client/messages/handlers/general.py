async def success(client, message):
    print('Successful action completed')

async def error(client, message):
    print(f'ERROR: {message}')

async def broadcast(client, message):
    print(f'NEW MESSAGE: {message}')

async def list_topics(client, topics):
    print(f'TOPICS LIST: {topics.join(",")}')

async def unread(client, message):
    print(f'UNREAD MESSAGE: {message}')