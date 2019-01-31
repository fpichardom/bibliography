#!/usr/bin/env python3
import os
import json
from jinja2 import Environment, FileSystemLoader


root = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(root, 'templates')

with open(os.path.join(root,'annotated-bibliography.json'),'r') as jsonfile:
    bibliography = json.load(jsonfile)
    count = 1
    for i in bibliography:
        count += 1
        i['index'] = count


env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template('annotated_bibliography_template.html')
output_parsed = template.render(bibliography=bibliography)


with open(os.path.join(root,'index.html'), 'w') as output:
    output.write(template.render(bibliography=bibliography))


sources_help = [
    'https://code-maven.com/minimal-example-generating-html-with-python-jinja',
]