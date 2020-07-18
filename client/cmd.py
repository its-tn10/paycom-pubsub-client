
from client.commands import general

import asyncio

class CMD:

    def __init__(self, client):
        self.client = client
    
    async def start(self):
        print('Successfully connected - listening to commands!')
        print('Would you like to /CONNECT with an existing account or /CREATE one?')

        print()

        await self.listen_to_cmds()
    
    async def listen_to_cmds(self):
        try:
            while True:
                cmd = input()
                if cmd[0:1] == '/':
                    parsed_cmd = cmd[1:].strip().lower()

                    module_functions = [curr_name for curr_name, func in general.__dict__.items() \
                                        if hasattr(func, '__call__')]

                    if parsed_cmd in module_functions:
                        await getattr(general, parsed_cmd)(self.client)
                        continue

                    print(f'Command {parsed_cmd} does not exist to handle')
        except asyncio.CancelledError:
            raise