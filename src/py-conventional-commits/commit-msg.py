#!/usr/bin/env python

import os
import re
import sys

message_file = open(sys.argv[1], 'r')
message = message_file.readline()

options = [
    'fix',
    'feat',
    'chore',
    'docs',
    'style',
    'refactor',
    'perf',
    'test',
    'improvement',
]

options_with_pipe = '|'.join(options)

regex = fr'^({options_with_pipe})(\(\w+\))?: \w+.*$'

matches = re.search(regex, message)

if not matches:
    error_color = '\033[91m'
    reset_color = '\033[0m'
    terminal_size = os.get_terminal_size()
    separator = ''.join(map(lambda _: '-', range(terminal_size.columns)))

    print(error_color + separator)
    print(f'Commit message "{message}" not follow conventional commits')
    print(
        'To see the full specification'
        ' https://www.conventionalcommits.org/en/v1.0.0/#specification'
    )
    print(separator + reset_color)
    exit(1)
