# TriviaGameBot
I created script that gives you the answer to a trivia question in under 8 seconds. 
This is not for use in game, but is rather to demonstrate a proof of concept. 

##HOW IT WORKS

The script takes a screenshot of my phone which is mirrored onto the laptop. Then I use the Python Imaging Library to crop the image, make it grayscale, and process other attributes of the picture. This is done to make the image easier to read for the OCR(Optical Character Recognition). The OCR then recognizes the characters in the picture, and then the script parses the question from the answers. Then it uses a wikipedia search to find the answer that shows up the most. This is the answer that is printed for user. The accuracy so far is about 75%. I am planning on adding parallel searching algorithms with Google's search API to make it more consistent. I am also planning on using Google's Cloud Vision API to to make the OCR much more accurate.
