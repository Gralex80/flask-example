from jinja2 import Template
t = Template('Hello {{ name }}!\n{% for i in range(5) %}{{name}} {{i}}\n{% endfor %}')
msg = t.render(name='World')
print(msg)