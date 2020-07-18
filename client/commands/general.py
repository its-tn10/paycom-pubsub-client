from aioconsole import ainput

async def connect(client):
    user_email = (await ainput('Enter the e-mail you have registered with: ')).strip()
    await client.send_json(action = 'connect', user_email = user_email)

async def create(client):
    user_email = (await ainput('Enter the e-mail you want to register with: ')).strip()
    is_pub = (await ainput('Will you be a publisher? (Y/N): ')).strip().lower() == 'y'

    user_type = 'subscriber'
    if is_pub:
        user_type = 'publisher'

    await client.send_json(action = 'create', user_email = user_email, \
                    user_type = user_type)



async def topics(client):
    await client.send_json(action = 'list_topics')

async def subscribe(client):
    topic_name = (await ainput('Enter the topic name you would want to subscribe: ')).strip()
    await client.send_json(action = 'subscribe', topic_name = topic_name)

async def unsubscribe(client):
    topic_name = (await ainput('Enter the topic name you would want to unsubscribe: ')).strip()
    await client.send_json(action = 'unsubscribe', topic_name = topic_name)



async def newtopic(client):
    topic_name = (await ainput('Enter the topic name you would want to create: ')).strip()
    await client.send_json(action = 'create_topic', topic_name = topic_name)

async def publish(client):
    topic_name = (await ainput('Enter the topic name you want to publish to: ')).strip()
    message = (await ainput('Enter the message: ')).strip()
    await client.send_json(action = 'publish_msg', topic_name = topic_name, msg = message)