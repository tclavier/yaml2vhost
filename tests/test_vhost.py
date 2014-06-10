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
            cache: disk
        """        
        self.vhost = vhost.Vhost()

    def testMissingServers(self):
        #Given
        data = """
        "testyaml.domain.com":
            bad_key: [apldock1, apldock2]
            context: testYaml
            port: 1080
        """        
        host = "apldock1"

        # When / Then
        with self.assertRaises(KeyError):
            yml = self.vhost.build(data,host)

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

    def testCacheDisk(self):
        #Given
        host = "apldock2"

        # When
        yml = self.vhost.build(self.sample_yaml,host)

        # Then
        expected = "CacheEnable disk /"
        self.assertRegexpMatches(yml, expected)

    def testNoCache(self):
        #Given
        host = "apldock2"
        data = """
        "testyaml.domain.com":
            servers: [apldock1, apldock2]
            context: testYaml
            port: 1080
        """        

        # When
        yml = self.vhost.build(data,host)

        # Then
        expected = "CacheEnable"
        self.assertNotRegexpMatches(yml, expected)

if __name__ == '__main__':
    unittest.main()
