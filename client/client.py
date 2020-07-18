from client.cmd import CMD
from client.messages.messagehandler import MessageHandler

import asyncio

class Client:

    def __init__(self):
        self._hostaddr = None
        self._hostport = None

        self.cmd = None

        self.msg_handler = None

        self.reader = None
        self.writer = None

    async def start(self):
        print('Paycom Broker Client: Logging into TCP Broker Server')
        print()

        self.get_server_info()

        self.reader, self.writer = await asyncio.open_connection(self._hostaddr, self._hostport)

        self.cmd = CMD(self)
        self.cmd_task = asyncio.create_task(self.cmd.start())

        self.msg_handler = MessageHandler()

        await self.keep_connection_alive()

    async def keep_connection_alive(self):
        while not self.writer.is_closing():
            try:
                line = await self.reader.readline()
                
                if line:
                    await self.handle_received_data(line)
                else:
                    self.writer.close()
                
                await self.writer.drain()
                
            except ConnectionResetError:
                self.writer.close()

    async def handle_received_data(self, line):
        line = line.decode().strip()

        await self.msg_handler.handle_msg(self, line)

    async def send_json(self, **kwargs):
        if not self.writer.is_closing():
            line = await self.msg_handler.encode_json(**kwargs)
            line += '\n'

            self.writer.write(line.encode('utf-8'))

    def get_server_info(self):
        self._hostaddr = input('Enter the host address: ')
        self._hostport = int(input('Enter a numerical port number: '))

        print()

    def disconnect(self):
        self.writer.close()
        self.cmd_task.cancel()