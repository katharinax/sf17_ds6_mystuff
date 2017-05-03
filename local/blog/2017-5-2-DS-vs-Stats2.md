---
layout: post
title: A data scientist is a statistician who lives in San Francisco - Part II
---

This is the second part of my take on whether statisticians and data scientists are the same. You can find the first part [here](2017-4-17-DS-vs-Stats2.md).

# Philosophy

## Inference vs Prediction

To simplify, data scientists predict and statisticians infer. Most data science machine learning methods I've learned about thus far are prediction-oriented. What products are out-of-stock? What is the weather forecast? Does this image contain a face? There is a clear outcome - a value, an answer - data scientists generate. Statisticians emphasize on statistical inference. Throughout my life, until recently, I allocated a great deal of time to unrevealing the statistical models themselves. Statisticians asked questions such as, is higher education significantly related to higher income levels? How much is gender interacting with age in affecting the magnitude of cancer progression?

Due to this nature, a good statistician always feel an obligation to interpret their analyses in layman language. As graduate students, we were told time and again to pick parsimonious models. Sometimes data transformation was preferred for technical reasons, and we scratch our heads trying to come up with a straightforward description in our PowerPoints. One graph says a hundred words; when we presented our capstone projects, professors habitually spent time on critiquing our graphs - title, label, legend, font, size, color, readability.

Parsimony is a good way to avoid ugly collinearity and to guarantee the "at least 30 observations per independent variable" rule of thumb, but more importantly, if the models are too complicated to explain, clients will not understand. Statisticians' ultimate goal is to explain real life phenomenons; if people cannot understand our results, no matter how great the statistical analyses are, it would still be somewhat pointless.  

A good data scientist always feel an obligation to yield accurate results. Call me crazy but people probably don't want to buy self-driving cars that crashes. To squeeze out that extra one percent of accuracy from 96% to 97%, the algorithms can get complicated really fast. Within each algorithm, data scientists try out things such as layering up the neural network or having iterations and loops, and you render a model that is not very human decipherable. I've had a little bit of exposure to statistical papers on meta-analysis, but the way data scientists use ensemble methods to predict an outcome was a real eye opener.

## Black box and object-oriented programming

Data science along with a wide range of computer-related people have this term called a black box. The first time I heard it, I took it as a criticism on my interpretation skills and proceeded with making two more slides about my algorithms. I quickly realized black box was a commendatory term related to object-oriented programming which emphasizes the fact that general users of my statistical results really didn't need to see any slides about my algorithms.

Coming from a MUST-interpret-everything mindset, I cannot tell you how much I hate this phrasing. But the concept of a black box is necessary. Computer science is about division of labor. Each developer work with each other to build a big picture just like how each module passing around data to form a web of complex programming. The developers working on one module doesn't have to know how another module works as long as the input and output are standardized. To paraphrase in layman terms: We Google everyday, but it doesn't mean we all need to know how those search results are ranked in the backend.

While the black box quickly grew on me, I grew weary of the ambience of no one every explaining anything. I was angry at people tossing out foreign and seemingly unspecific acronyms such as big-O, cache, driver, wrapper, core, thread, performance. This antsiness was mixed with my feeling inferior as I caught up with git, Agile methodology, and an object-oriented way of programming. Roughly half a year in to my new job, the data scientists were finalizing version 1.0 of our prediction tool, and I was responsible for giving two hour-long orientations to our new tool. I had a lot of help from my teammates with slides. As I learned the meaning of diagrams such as data flow and module structure, I was not very sure that this level of technical details should be presented. Actually, many product managers I met in California had a technical background themselves, and many people were interested in the technical aspects of software applications; it is simply that I personally would prefer a less technical presentation style given our audience.

That month of presentation preparation was also a month of self-discovery. Public speaking didn't come naturally to me, but I did have a preferred style of presentation due to my educational background. On the other hand, most of my colleagues were not client-facing, so who am I to expect them to have interdisciplinary communication savvy? Little by little, my sense of inferiority along with anger melted away. We were all just from different backgrounds, bringing in different know-hows to the emerging data science field. Shortly after the presentation, I resigned from the company and joined the acclaimed [Metis](https://www.thisismetis.com/) Data Science Bootcamp. The main wish is to fill my gaps with a more systematic education, but it is sometimes amusing to think that I left an overall promising and friendly team because I couldn't make peace with the presentation style. Perhaps I am not that different from Richard, who broke up with Winnie because she indented her codes with spaces.

<div style="text-align:center"><img src="http://i.imgur.com/VUGVNkP.jpg" width="600"></div>

## Interlude

These are just my humble opinions. As I write this blog, I fear I am wrongly generalizing my personal experience. Presentation styles for an examples, really largely depends on the audience, the purpose, and the company culture. As for parsimony or not, one of my closest friends from grad school now works in genetics. She uses R and runs complicated models on huge genome data. When it comes to prediction versus inference, the senior data scientist I worked with could interpret data and models much better than I did. He used these insights to guide his feature engineering and parameter tuning decisions. It's not always clear where the distinction lies between a statistician and a data scientist; perhaps there wasn't a line to start with.

## Feature engineering

The first time I saw how feature engineering was done, my jaw dropped to the basement. Take an independent variable, say past sales records, calculate its  five-number summary by group, and you get five additional columns. Group it another way, and you get five more. Transpose all historical sales records that existed in a column into one row (```proc transpose``` in SAS, ```dcast``` for R data tables, and as I am learning this week, ```.agg```/```.apply``` or ```pivot_table``` with Python Pandas), and all in a sudden you are utilizing the entire sales trend to predict one outcome. This is just one out of many amazing tricks.

Don't get me wrong: Statisticians praise creativity in generating new features/independent variables too - extracting day of week from timestamp, regrouping ethnicity, taking the differences or interactions, and all that jazz. But statisticians (or maybe just me) mostly work with harder-to-acquire data with oceans of Institutional Review Board procedures, and we cry with joy to see datasets with more than 300 variables. On top of that, with parsimony in mind, I had actually never thought to think outside the box.

While data scientists care about bias/variance tradeoff, with parsimony being less of a concern, they usually have more leeway in stuffing features in a model. In fact, when it comes to avoiding overfitting, I believe data scientists obey a "at least 12ish observations per independent variable" rule of thumb, which is less than the 30ish for statisticians.

## Theory vs Practicality

Due to the result-oriented nature of predictive analytics, data scientists seemed a bit more down to earth to me. Roughly one and a half years ago, I was introduced to the practice of training and testing in machine learning. The beauty of it is the belief that we are capable of improving through trial and error (keep calm and iterate!) and that a weaker beginning is okay. On the other side of the spectrum, statisticians ponder a lot on math assumptions of models, but empirical methods cross their minds less often. In terms of data, statisticians - especially we survey people - talk a lot about the representativeness of the samples we work with. We compare weighted data distributions to make sure samples are random enough. This has everything to do with how well our analytical inferences can be generalized. In terms of model, statisticians provide a list of Goodness of Fit indices, ranging from R-squared, AIC/BIC, to q-q plots, Cook's D, and DFFITS, to make sure the models are robust enough for our data.

After all these, statisticians conservatively utter a conclusion that goes alone the line of, "there's probably not much evidence to say this is bad..." Or, "there's a high chance we cannot keep hypothesizing like this..." Data scientists don't beat around the bushes. They walk up to you, throw a proof-of-concept in your face, slam one finger on the table, and tell you this shit works. And sometimes, this shit works great.

Disclaimer: All of my statistics experiences came from academia and all industry experiences were data science, so please excuse my confusion if I am incorrectly labeling people.


Now. Are we gonna talk about the elephant in the room or what? Show of hands. Who here is still using SAS? Let's discuss software in another post.
