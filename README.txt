si330 Homework 6 - README
Name: Tahmeed Tureen
Note: Use Sublime Text if there are formatting issues when viewing this doc

This folder contains: lesmis.txt, lesmissentences.txt, preprocess.py, mrbigram.py

Documentation for each task for Homework 6: MapReduce and Introduction
to Natural Language Processing



**Task #1:
 1. The preamble was deleted manually
	Every single line until the line that mentions the BOOK number 
	was defined as the preamble
 2. The postamble/postable lines were manually deleted
	Every single line until the very last line of Les Miserables
	was defined as the postamble

This is how lesmis.txt was created from the original txt file



**Task #2:
CODE : Code for Task 2 can be found in the preprocessing.py file

The lines that do not correspond to sentences were manipulated using the nlkt
python module to convert lines into appropriate sentences so we can read the 
bigrams.

This was run on a local machine and NOT on Hadoop.

This is how lesmissentences.txt were created from the lesmis.txt file



**Task #3:
CODE: Code for Task 3 can be found in the mrbigram.py file
CODE LINES: 20-45

This is where I defined my mapper function for MapReduce (refer to .py file)

At first, I used the nltk module to create a list of words from each line, then I
filtered the words by using list comprehension and took out all of the stopwords
(This is Task #6 done inside Task #3)

I used the bigrams() method function from the nltk module to create a list of 
bigrams from each line. 

Then from this list of bigrams, I omitted bigrams that
included words like 'chapter', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x' 
because these had potential of altering the top 50 bigrams for Les Miserables

After the manipulation, the mapper function yields a tuple with the bigram on
the left and the integer 1 on the right.



** Task #4:
CODE: Code for Task 4 can be found in the mrbigram.py file
CODE LINES: 50-52

To count the number of each bigram, I defined a combiner function (lines 50-52)
that yields the bigram as key and the count of the bigram as the value

After creating the combiner, I decided to create two reducers.

The first one, reducer_count_bigrams (similar to the combiner) yields a tuple 
with the key = None and the value = (bigram, bigram count) 

ex. (Node, (bigram, bigram count)

I chose to make the key the same for all of the bigrams so I can use the
second reducer to sort based on the the value which is (bigram,bigram count)

Note that if I didn't do this I would have multiple key, value tuples so it would be
difficult to process and sort. So, I decided to make the key as "None" and the
value as the tuple.



** Task #5:
CODE: Code for Task 5 can be found in the mrbigram.py file
CODE LINES: 66-72

To complete this task, I decided to create a second reducer functions

I created a second reducer that uses the sorted function on
the inputted bigrams. It is sorted in descending order based on the 2nd element 
in the tuple value which is the bigram count that was yielded from the first reducer.

This reducer then yields the first 50 bigrams from the sorted list which represents
the top 50 bigrams based on counts in Victor Hugo's Les Miserables



** Task #6:
Refer to Task #3



** Task#7: 
What are the top 50 bigrams, excluding the stopwords, from Victor Hugo's Les Miserables?

Ans: 

BIGRAM 					COUNT

["jean", "valjean"]     1108
["let", "us"]           240
["rue", "de"]           184
["old", "man"] 		    173
["de", "la"]    		113
["monsieur", "le"]      111
["one", "day"]  		102
["one", "would"]        88
["de", "l"]     		80
["rue", "des"]  		78
["young", "man"]        78
["young", "girl"]       76
["old", "woman"]        74
["good", "god"] 		70
["madame", "magloire"]  70
["thousand", "francs"]  68
["rue", "saint"]        67
["hundred", "francs"]   65
["every", "day"]        64
["every", "one"]        61
["years", "ago"]        60
["le", "maire"] 		59
["rue", "du"]   		59
["wine", "shop"]        59
["rue", "plumet"]       54
["caught", "sight"]     53
["petit", "picpus"]     52
["grave", "digger"]     50
["low", "voice"]        50
["turned", "round"]     49
["first", "place"]      47
["grape", "shot"]       47
["great", "deal"]       46
["human", "race"]       46
["long", "time"]        46
["said", "jean"]        45
["la", "chanvrerie"]    44
["said", "marius"]      44
["took", "place"]       43
["father", "madeleine"] 42
["one", "side"] 		42
["first", "time"]       41
["five", "hundred"]     41
["following", "day"]    40
["little", "girl"]      40
["young", "girls"]      40
["one", "knows"]        39
["taken", "place"]      39
["l", "homme"]  		38
["louis", "philippe"]   38


Thank you for reading!

This project was conducted by Tahmeed Tureen for SI 330: Data Manipulation at the University of Michigan
Instructor Acknowledgement: Dr. Chris Teplovs, School of Information, University of Michigan