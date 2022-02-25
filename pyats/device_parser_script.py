from pyats.topology import loader
from pprint import pprint

testbed = loader.load("testbed.yml")

testbed.connect(log_stdout=False)

parsed_output = testbed.parse("show users")
pprint(parsed_output["nx-sw1"])