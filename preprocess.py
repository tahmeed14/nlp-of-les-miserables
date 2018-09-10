# Name: Tahmeed Tureen
# SI 330 w/ Chris Teplovs
# Fall 2017
# Worked w/ 

# Import nltk module for Natural Language Processing
import nltk
nltk.download('punkt')

# Note that the lesmis.txt file does not have a preamble, postamble nor any chapter headings
# These were all taken out manually

lesmis_file = open('lesmis.txt', 'r')
lesmis_text = lesmis_file.read()

# print(type(lesmis_text))

sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')


# Process the current lesmis.txt to create a txt file that has valid sentences for further analysis
with open('lesmissentences.txt','w') as f:
	f.write('\n'.join(sentence_detector.tokenize(lesmis_text.strip().replace("\n"," "))))




