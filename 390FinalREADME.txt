This python program is the final project for 390

This program is used to derive topics of contributions that the user could make towards a GitHub repo.
It is designed to work with the README files and issues sections. Combining both together can be done as well.

To use you will need several python packages:nltk, gensim, and pyLDAvis for plotting the data.

The creating of the tokens and visualization of the data used a walkthrough guide from towardsdatascience.com
The page can be found here: https://towardsdatascience.com/topic-modelling-in-python-with-nltk-and-gensim-4ef03213cd21

Jupyter notebooks is what was used to run this program. Simply clone the github repository you wish to process and 
change the filenames in the program appropriately. You can also change the number of topics/words per topic by editing the
values. The pyLDAvis charts will load automatically.

To run issues you must either get them from the gitHub api or copy and paste them into a new file. One of the 
things I wish I could have worked on further was finding a better way of accessing the issues section. easier.