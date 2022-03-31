from jinja2 import Template
t = Template('Hello {{ name }}!')
msg = t.render(name='World')
print(msg)
