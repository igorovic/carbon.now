import re
# yaml.__version__ == 5.3.1
import yaml

YAML_DOC = """
ziprx: !regx '^([a-z ]*)(?P<zip>[0-9]+)$'
"""


# returns a compiled regular expression from a yaml string node
def regx_compile(loader, node):
    # with yaml construct_scalar we obtain a string from the yaml node
    value = loader.construct_scalar(node)
    return re.compile(value)


# tells yaml that a node with tag '!regx' should pass through 'regx_compile'
yaml.add_constructor("!regx", regx_compile)

config = yaml.load(YAML_DOC, Loader=yaml.Loader)
print(config)
# {'ziprx': re.compile('^([a-z ]*)(?P<zip>[0-9]+)$')}

# Usage example
TXT = "my zip code is 1234"
print(config["ziprx"].match(TXT).groupdict())
# {'zip': '1234'}
