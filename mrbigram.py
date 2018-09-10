
## Name: Tahmeed Tureen
## SI 330 - HW6 - MapReduce Bigrams
## Fall 2017 w/ Dr. Teplovs
## Worked w/ Lauren Sigurdson
## Resources Read for Guidance: https://pythonhosted.org/mrjob/

from mrjob.job import MRJob
from mrjob.step import MRStep

import nltk
nltk.download('punkt')
from nltk.tokenize import RegexpTokenizer


class MR_LESMIS(MRJob):
	
	# Create Mapper for lesmissentences.txt that will yiled bigrams
	# Make sure you omit the words you don't want
	def mapper_get_bigrams(self, _, line):
		# Task 3
		# Split the sentences into words using the nltk module
		tokenizer = RegexpTokenizer('\w+')
		words_str = tokenizer.tokenize(line)

		# Convert all words to lower case using list comprehension
		words_str = [word.lower() for word in words_str]

		# We need to omit these words from our bigrams, this is Task #6
		words_to_omit = ['their', 'she', 'did', 'not', 'needn', 'have', 'all', 'a', 'has', 'between', 'shouldn', 'where', 'these', 'had', 'ours', 'who', 'further', 'does', 's', 't', 'are', 'isn', 'should', 'both', 'against', 'll', 're', 'can', 'that', 'few','out', 'no', 'hers', 'myself', 'but', 'at', 'too', 'once', 'the', 'there', 'o', 'this', 'down', 'in', 'some', 'and', 'weren', 'we', 'own', 'into', 'don', 'other', 'him', 'during', 'himself', 'having', 'them', 'why', 'ain', 'each', 'it', 'when', 'were', 'will', 'mightn', 'very', 'aren', 'am', 'mustn', 'they', 'ourselves', 'only', 'd', 'or', 'than', 'if', 'itself', 'from', 'i', 'being', 'her', 'me', 'after', 'yourselves', 'more', 'yours', 'through', 'those', 'of', 'you', 'doesn', 'about', 'to', 'y', 'your', 'doing', 'just', 'herself', 'now', 'wouldn', 'its', 'been', 'under', 'hadn', 'wasn', 'above', 'any', 'nor', 'over', 'because', 'on', 'shan', 'themselves', 've', 'off', 'while', 'then', 'how', 'so', 'until', 'most', 'our', 'up', 'is', 'yourself', 'was', 'what', 'before', 'which', 'same', 'again', 'didn', 'haven', 'ma', 'be', 'do', 'with', 'won', 'm', 'couldn', 'whom', 'my', 'theirs', 'below', 'such', 'for', 'his', 'an', 'by', 'hasn', 'as', 'here', 'he']

		# Use the bigrams member function to get a generator of bigrams
		bigrams = nltk.bigrams(words_str)

		# Omit all the words we don't like, using list comprehension, this is Task #6
		bigrams_new = [tup for tup in bigrams if (tup[0] not in words_to_omit and tup[1] not in words_to_omit)]
		
		# Get rid of bigrams that alter the type of result we want, we want to omit bigrams with these words:
		chapters = ['chapter', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
		bigrams_new = [tup for tup in bigrams_new if (tup[0] not in chapters and tup[1] not in chapters)]

		for bigram in bigrams_new:
			# For each element in the bigrams object, emit the bigram as the key
            # and the number 1 as the value. We do this because we want to aggregate across the bigrams (i.e. count all the bigrams)
			yield bigram, 1


	# Combiner for counting the bigrams, Task #4
	# Inputs: The key is the bigram that we yield from our mapper
	def combiner_count_bigrams(self, key, values):
		# print(key, sum(values))
		yield (key, sum(values))

	# Reducer for counting the bigrams, Task #4, very useful for task 5
	# Inputs: The key is the bigram that we yield from our mapper
	def reducer_count_bigrams(self, key, values):
		# Documentation: https://pythonhosted.org/mrjob/job.html
		
		# Yield a key that is constant for all bigrams!
		yield (None, (key, sum(values))) 
		# These will be run on the sort function and the key is None meaning it's the same for every bigram and we will sort based on 
		# the bigram's count value in the tuple value

		
  
  	# Reducer for sorting the bigrams based on Count, Task #5
	def reducer_sort_bigrams(self, _, bigrams):
		top_50_bigrams = sorted(bigrams, key=lambda tup: tup[1], reverse = True)

		for bigram in top_50_bigrams[0:50]:
			yield bigram

	def steps(self):
  		return [MRStep(mapper = self.mapper_get_bigrams, combiner = self.combiner_count_bigrams, reducer = self.reducer_count_bigrams), MRStep(reducer = self.reducer_sort_bigrams)]
  
                
if __name__ == '__main__':
  MR_LESMIS.run()