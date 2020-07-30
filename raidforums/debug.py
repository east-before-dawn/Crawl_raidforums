import unittest



from scrapy import cmdline

# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)

if __name__ == '__main__':
    # unittest.main()
    cmdline.execute("scrapy crawl leaks_market".split())
