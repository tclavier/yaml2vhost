import unittest, sys
sys.path.append('.')
from yaml2vhost import *

class TestVhost(unittest.TestCase):
    def testProxyPassLine(self):
        #Given
        data = """
        "testdocker.camaieu.fr":
            prod: [apldock1, apldock2]
            context: testDocker
            port: 1080
        """        
        host = "apldock1"

        # When
        obj = vhost.Vhost()
        yml = obj.build(data,host)

        # Then
        expected = "ProxyPass /testDocker http://localhost:1080/testDocker"
        self.assertRegexpMatches(yml, expected)

    def testBadHost(self):
        #Given
        data = """
        "testdocker.camaieu.fr":
            prod: [apldock1, apldock2]
            context: testDocker
            port: 1080
        """        
        host = "apldock3"

        # When
        obj = vhost.Vhost()
        yml = obj.build(data,host)

        # Then
        expected = ""
        self.assertEquals(yml, expected)

if __name__ == '__main__':
    unittest.main()
