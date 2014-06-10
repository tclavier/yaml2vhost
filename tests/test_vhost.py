import unittest, sys
sys.path.append('.')
from yaml2vhost import *

class TestVhost(unittest.TestCase):

    def setUp(self):
        self.sample_yaml = """
        "testyaml.domain.com":
            servers: [apldock1, apldock2]
            context: testYaml
            port: 1080
        """        
        self.vhost = vhost.Vhost()

    def testProxyPassLine(self):
        #Given
        host = "apldock1"

        # When
        yml = self.vhost.build(self.sample_yaml,host)

        # Then
        expected = "ProxyPass /testYaml http://localhost:1080/testYaml"
        self.assertRegexpMatches(yml, expected)

    def testProxyPassReverseLine(self):
        #Given
        host = "apldock1"

        # When
        yml = self.vhost.build(self.sample_yaml,host)

        # Then
        expected = "ProxyPassReverse /testYaml http://localhost:1080/testYaml"
        self.assertRegexpMatches(yml, expected)

    def testServerNameLine(self):
        #Given
        host = "apldock1"

        # When
        yml = self.vhost.build(self.sample_yaml,host)

        # Then
        expected = "ServerName testyaml.domain.com"
        self.assertRegexpMatches(yml, expected)

    def testBadHost(self):
        #Given
        host = "apldock3"

        # When
        yml = self.vhost.build(self.sample_yaml,host)

        # Then
        expected = ""
        self.assertEquals(yml, expected)

if __name__ == '__main__':
    unittest.main()
