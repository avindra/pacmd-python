#!/usr/bin/env python
from lib.cli import run
import json

data = run('list-sinks')
print(json.dumps(data, indent=2))