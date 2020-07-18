import asyncio
from client.client import Client

if __name__ == '__main__':
    try:
        client_object = Client()

        asyncio.run(client_object.start())
    except KeyboardInterrupt:
        print('Disconnecting from broker server...')
        client_object.disconnect()