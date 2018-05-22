#!/usr/bin/env python3

import unittest

import classify

class Test(unittest.TestCase):
		

	def testBoundaries(self):
		classify.boundaries = [0,50,100]
		data = classify.getData(open("testData.txt"))
		candidateRanges = classify.showRanges(data)
		expectedRanges = [['John', 'Kenan'], ['Craig', 'Jeff', 'Steve', 'Will']]		
			
		self.assertEqual(candidateRanges,expectedRanges)
	def testEmptyClass(self):
		classify.boundaries = [0,10,20,50,60,100]
		data = classify.getData(open("testData.txt"))
		candidateRanges = classify.showRanges(data)
		expectedRanges = [['Kenan'], ['none'],['John'],['Steve'], ['Craig','Jeff','Will']]
		self.assertEqual(candidateRanges, expectedRanges)
		
if __name__ == '__main__':


    unittest.main()
