#### Pair Problem

This should be fun.  Try to use `sklearn` to implement SkipGrams using the `sklearn.neural_network.MLPClassifier` class.  

**Remember**:  
- The input to SkipGrams is a one-hot encoded vector for the word under examination in a context window.
- The output is the similar one-hot vectors for the remaining words in the window

**Effectively**:  
- You can treat the outputs as if it were a multiclass, multilabel problem.  That is, each training observation (a context window) will have a 1-hot encoded vector as input (representing the middle word in the window) and 4 integers as output (representing the "classes" for that observation, with the classes here being the **indexes** of the context words in your vocabulary).
- With this formulation, you should be able to make it work with the MLPClassifier, although start with very small amounts of data.

**Data**:  
Use the 20 newsgroups data from `sklearn` but only take a small sample of the data.  word2vec is not quick.

**Suggested Steps**:
- Set a Window size (the number of words before and after the target word included in the context window, I suggest 2 for now)
- Use a CountVectorizer to establish the term indexes in your vocabulary
- For each context window, use the `CountVectorizer` to get the appropriate 1-hot vector as input and 4 integers (labels) as output (representing the 4 context words for a window size of 2)
- Plug in your observations (X=1-hot vector, and y=vector of 4 integers) and fit an MLPClassifier and see how it does!
  - That is, you need to use the `coef_` (the weights matrix W) attribute from your `CountVectorizer` to map the word vectors into the new word2vec space.  The transformation for this remember, is W'x where W' is the transpose of W and x is the 1-hot vector for a word.
  - Compute some cosine similarities between a few terms using the new W'x vectors.  Any luck at all?

  Feel free to collaborate extensively on this one.  I don't want it to take too too long but I understand it is involved.

  May the best vectors win!
