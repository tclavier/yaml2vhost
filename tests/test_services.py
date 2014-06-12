import unittest, sys
sys.path.append('.')
from yaml2vhost import *

class TestServices(unittest.TestCase):

    def setUp(self):
        self.sample_yaml = """
        "testyaml.domain.com":
            servers: [srv1, srv2]
            context: testYaml
            port: 1080
            container: testyaml
            version: 12.5
        """        
        self.services = services.Services()

    def testLine(self):
        #Given
        host = "srv1"

        # When
        yml = self.services.build(self.sample_yaml,host)

        # Then
        expected = "http://srv1:1080/testYaml testyaml:12.5\n"
        self.assertRegexpMatches(yml, expected)


if __name__ == '__main__':
    unittest.main()
