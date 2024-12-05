# CSC110
# Project 9 - Test Script
# Hwansu Kim (Billy)


import unittest
import Project9HwansuKim


class FunctionTest(unittest.TestCase):

    def test_findLongest(self):
        self.assertEqual(("Hannibal", 8),
                         Project9HwansuKim.findLongest({"Michael", "Jason", "Freddy", "Hannibal"}))

        self.assertEqual(("Clarice", 7),
                         Project9HwansuKim.findLongest({"Laurie", "Ginny", "Nancy", "Clarice"}))

        self.assertEqual(("Candyman", 8),
                         Project9HwansuKim.findLongest({"Pinhead", "Chucky", "Rose", "Candyman"}))

        self.assertEqual(("Kirsty", 6),
                         Project9HwansuKim.findLongest({"Kirsty", "Andy", "Abra", "Helen"}))

        self.assertEqual(("", 0),
                         Project9HwansuKim.findLongest({""}))

        self.assertTrue([("Wesker", 6), ("Claire", 6)],
                        Project9HwansuKim.findLongest({"Chris", "Barry", "Wesker", "Claire"}))

    def test_generateSortedList(self):
        self.assertEqual(["Freddy", "Hannibal", "Jason", "Michael"], Project9HwansuKim
                         .generateSortedList({"Michael", "Jason", "Freddy", "Hannibal"}))

        self.assertEqual(["Aim", "Air", "Ape", "Ate"], Project9HwansuKim
                         .generateSortedList({"Ate", "Ape", "Aim", "Air"}))

        self.assertEqual(["Bin", "Tin", "bin", "tin"], Project9HwansuKim
                         .generateSortedList({"Tin", "bin", "Bin", "tin"}))

        self.assertEqual(["", " ", "Zebra", "Zebras"], Project9HwansuKim
                         .generateSortedList({"Zebra", "Zebras", "", " "}))

    def test_generateLenFreqs(self):
        self.assertEqual([0, 0, 0, 0, 1, 1, 1, 1], Project9HwansuKim
                         .generateLenFreqs({"Michael", "Jason", "Freddy", "Hannibal"}, 8))

        self.assertEqual([0, 0, 0, 0, 2, 1, 1], Project9HwansuKim
                         .generateLenFreqs({"Laurie", "Ginny", "Nancy", "Clarice"}, 7))

        self.assertEqual([0, 0, 0, 1, 0, 1, 1, 1], Project9HwansuKim
                         .generateLenFreqs({"Pinhead", "Chucky", "Rose", "Candyman"}, 8))

        self.assertEqual([0, 0, 0, 2, 1, 1], Project9HwansuKim
                         .generateLenFreqs({"Kirsty", "Andy", "Abra", "Helen"}, 6))

        self.assertEqual([], Project9HwansuKim
                         .generateLenFreqs({}, 0))

    def test_readFile(self):
        self.assertEqual({"the", "flood", "is", "a", "species", "of", "parasitic", "organisms"},
                         Project9HwansuKim.readFile("TestDoc.txt"))

        self.assertEqual({"bethesda", "has", "released", "fifteen", "times", "skyrim"},
                         Project9HwansuKim.readFile("TestDoc2.txt"))

        self.assertEqual({"myth", "mesopotamian", "ancient", "in", "hero", "a", "was", "gilgamesh"},
                         Project9HwansuKim.readFile("TestDoc3.txt"))

    def test_writeWordFile(self):
        self.assertTrue("TestDocOutput.txt", Project9HwansuKim
                        .writeWordFile("TestDocOutput.txt", ["Apple", "Banana", "Citrus", "Dirt"]))

        self.assertTrue("TestDocOutput2.txt", Project9HwansuKim
                        .writeWordFile("TestDocOutput2.txt", ["a", "bench", "on", "park", "sleep"]))

        self.assertTrue("TestDocOutput3.txt", Project9HwansuKim
                        .writeWordFile("TestDocOutput3.txt", ["alpaca", "smells", "spit"]))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(FunctionTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


main()