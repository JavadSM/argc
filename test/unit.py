import unittest
import argc

class Testargcr(unittest.TestCase):
    def test_detect(self):
        self.assertEqual(argc.convert("10"), 10)
        self.assertEqual(argc.convert("10.1"), 10.1)
        self.assertEqual(argc.convert('[10, "Hallo"]'), [10, "Hallo"])

        self.assertTrue(argc.convert("True"))
        self.assertFalse(argc.convert("False"))


    
    def test_argc(self):
        self.assertEqual(argc.parse(["-x", "hallo", "--use-M"]), {"-x":"hallo", "--use-M": True})
        self.assertEqual(argc.parse(["-x", "10"], True), {"-x":10})

        self.assertTrue(argc.isArg("-x"))
        self.assertFalse(argc.isArg("ads"))

class TestArgs(unittest.TestCase):
    def test(self):
        A = argc.argc(["-x", "hallo", "-m"])
        B = argc.argc(["--help"])
        A.add("-m", "PRINT", True)
        B.set("-h", "--help", "help", "Prints help message", command="there is not help for you", exitOn=True)
        self.assertEqual(A.args, {"-x":"hallo", "-m": True})
        
        with self.assertRaises(SystemExit):
            A.run()

        with self.assertRaises(SystemExit):
            B.run()


if __name__ == "__main__":
    unittest.main()
