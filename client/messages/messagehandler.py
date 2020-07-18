from client.messages.handlers import general

import json

class MessageHandler:

    async def handle_msg(self, client, line):
        try:
            decoded_line = await self.decode_json(line)
            function_name = decoded_line.pop('action').lower()

            module_functions = [curr_name for curr_name, func in general.__dict__.items() \
                                if hasattr(func, '__call__')]

            if function_name in module_functions:
                return await getattr(general, function_name)(client, **decoded_line)

            print(f'Action function {function_name} does not exist to handle')
        except TypeError:
            print('Could not parse invalid JSON message for action')
    
    async def encode_json(self, **kwargs):
        return json.dumps(kwargs, separators=(',', ':'))

    async def decode_json(self, line):
        return json.loads(line)
    