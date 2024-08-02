import unittest

from err import err

class MainTest(unittest.TestCase):
    logged_in = True

    @property
    def username(self):
        return None

    @classmethod
    def setUpClass(cls):
        print('Account created ✅✅✅')
        print(f'Logged in: {cls.logged_in}')
        cls.account = 'waltertaya'

    @classmethod
    def tearDownClass(cls):
        print('Account deleted ❎❎❎')
        cls.account = None
        cls.logged_in = False

    # def setUp(self):
    #     print('Account created ✅')
    #     self.account = 'Taya'
    
    # def tearDown(self):
    #     print('Account deleted ❎')
    #     self.account = None

    def test_is(self):
        self.assertIs(11 + 2, 13)

    def test_is_none(self):
        self.assertIsNone(self.username)
    
    def test_in(self):
        self.assertIn(23, [67, 56,23, 78])
        self.assertIn('taya', 'waltertaya')

    def test_not_in(self):
        self.assertNotIn('tayaw', 'waltertaya', msg='a not in b')
    
    def test_is_instance(self):
        self.assertIsInstance('waltertaya', str)
    
    def test_raises(self):
        with self.assertRaises(TypeError):
            err()

if __name__ == '__main__':
    unittest.main()