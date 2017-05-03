









# Software


sas
(stata)
r is inbetween  (genetics)

sas's phylosophy


Python

I know so many people who think that SAS is a dying dinosaur, but SAS held my hand through my undergrad thesis, my master's degree, and the first seven years of my career. It will always have a special place in my heart.


######

This is a shorter post to wrap up a few observations I wanted to but didn't get a chance to talk about in previous posts.


## Model diagnosis tools? other tools? domain knowledge?

most people I met are cs back ground -> DS


train/test

algorithm
big O
performance memory

git (for my data team, for music)
java




stats:
proability

p-value

"performance"
focus on bias/variance

bias in statistics (formula)
coding /algorithm

model diagnosis
(examples)






## t-shirt

different t-shirt
frequentist vs bys
(i haven't met one but should)
sudo rm -rf /

<div style="text-align:center"><img src="./nopvalue.png" width="300"></div>


used case



# Terminology

Let's take a minute to appreciate the Tower of Babel.

## Variable

When looking at an Excel spreadsheet, a vertical list of cells to me is a variable, a column to my non-technical clients, and the database engineers I used to work with called them a field. For something as simple as using age to estimate height, the height is the y or the dependent variable to statistical analysts. Colloquially the height is also known as the outcome, though in the social science world, we scarcely draw causal inferences but merely associations. I've recently learned that for machine learning data scientists, the height is referred to as the label of the data - most likely because that height value is the focus of what the rest of the data are trying to predict. The difference between the observed height and the statistical models's estimated height is often referred to as various kinds of errors by statisticians. In some sense, we are always in pursuit of the perfect model; perfect models don't exist in the statistics world, thus the error terms. Data scientists expand on error and generalize it into the cost (aka loss) functions. Deep-rooted in predictive results, the aim is to describe the cost of inaccurate predictions.

## Automation

I was asked during the data scientist job interview whether I had experience automating jobs. Heck! No only was I the only SAS programmer in the research team, I single handedly set up all of the Windows Task Schedulers that generated daily PDF reports from SAS. Arriving at my new job, my confidence was at its prime when my boss asked me, "Can you set up a SQL agent job?" Abashed, I said, "Sorry I am not very familiar with that." Boss said, "Message queue?" I was like, "Hmm, Q?" "Why don't you download the JAVA driver to our Linux server and we can go from there?" "...Who da driver?" It would be another story if you want to know how my kind colleague repeatedly answered my question on "downloading" JAVA driver from the command line and finally realized I was having trouble "installing."

## "Big" data

One of my lesser known duty in the early days was to maintain the US Census data files for our survey research team. I occasionally built preliminary analysis models on the data to assist with stratification and clustering decisions. At the Census block level, number of records can easily go up to 10M+. Some models run more than 20 minutes. 20 minutes! Around that era, the vague phrase "big data" started gaining it's popularity; as I was beautifying my resume, I thought it was justifiable that I hop on this hot tamale train. Few years later, I met an Amazon gal who had to use parallel computing just to crunch out a mean - I have since quietly removed the mention of "big data" on my resume.

After one year living in California as a data scientist, I am now able to independently whip up a working version in R utilizing ```foreach``` and ```doParallel``` packages with performance/memory usage reports attached. I look forward and see Spark as another mountain to conquer, but I also look back and reminisce over the afternoons sitting in front of SAS 9.2 patiently awaiting results. Technology has come a long way in the last few years. So have I.

# Some ideas for t-shirts



Are we gonna talk about the elephant in the room or what? Show of hands. Who here is still using SAS? Let's discuss software in another post.



# Epilogue of a personal tale

As of now, I believe statistics and data science is a spectrum. Data science is an emerging field. Albeit a very promising field, the definition of it is very vague due to its recency. On one side you have statistics, on the other, you have computer science; I imagine they converge in the middle to create data science and everything in between. I think we rely on computing to implement statistics, and apply statistics to explain and predict real life. I luckily had a glimpse of both ends of the spectrum and met a variety of interesting people during the journey. With the broadness and fluidity of data science, I have hopes that I will soon find something more suitable for myself in this new city, in this young field, with its ever evolving knowledge.
