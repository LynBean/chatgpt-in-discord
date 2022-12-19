
MISSING = None

INIT_CONFIG: dict = {
    'discord.token': 'TOKEN',
    'openai.key': 'KEY',
    'openai.config': {
        'frequency_penalty': 0,
        'max_tokens': 2048,
        'presence_penalty': 0,
        'temperature': 0.9,
        'top_p': 1,
        'engine': 'text-davinci-003',
        'select_only_these_engines': [
            'ada',
            'babbage',
            'code-cushman-001',
            'code-davinci-002',
            'curie-instruct-beta' ,
            'curie',
            'davinci-instruct-beta',
            'davinci',
            'text-ada-001',
            'text-babbage-001',
            'text-curie-001',
            'text-davinci-001',
            'text-davinci-002',
            'text-davinci-003'
        ]
    }
}
