---
layout: post
title: A data scientist is a statistician who lives in San Francisco - Part I
---

If you've been in the analytics field for a while, you are probably sick of people debating on the differences between a statistician and a data scientist. But as it turns out that part of my homework is to write a blog post, allow me to take this subject personally.

When I started out as a SAS analyst, I firmly believed that a data scientist was just a fancier term for a statistician. A higher hierarchy was implied, but likewise, statistician was just a fancier term reserved for PhD level data analysts. This is cheap sarcasm on stereotypes (my bad), but invisible ceilings indeed existed at a research institute for master level analysts like moi. I wanted more than cleaning data for others, which eventually led to my leap into the industry on the west coast. I joined a fairly computer science-heavy software company as a data scientist upon moving to California, and thus embarked on a journey to discovering the stark differences between a statistician and a data scientist.

#  Models/Algorithms

First thing first - the backbones. People from a mathy background call it statistical models; people from a techy background call it algorithms. You see, statisticians and data scientists are accustomed to different models/algorithms.

The statistical model 101 is linear regression, then logistic regression. From there, we gradually incorporate discrete data, categorical data into generalized linear models and mixed models. When I started to specialize in K - 12 educational surveys, I began to run into researchers who used a model called G study. I am not sure, but my impression is that it was a variation on mixed model which took into account random and fixed effects of categorical and continuous data.

Data scientists can also talk your ears off about linear regressions, but I hear much more mentions about regression model regularizations such as LASSO and ridge after moving to California. Perhaps it is purely by chance that I wasn't exposed to regularization methods before, however, I suspect it is that data scientists aim to achieve accurate predictions by tuning regularization parameters with the help of computing power, while statisticians focus on deriving different models that comply with the given data distribution.

I believe another beginner level go-to model for data scientists is random forest. From one decision tree, you grow a random forest. While random forest grows the trees all at the same time and comes up with an aggregated statistics, gradient boosting adds one tree at a time and eventually arrives at a statistics. I was lucky to had been guided by a talented senior staff during my one year stint imposing as a data scientist. We designed a merchandise out-of-stock prediction tool from scratch using extreme gradient boosting.

When you hear algorithms such as neural network and deep learning, applied to facial recognition or self-driving cars, you know you have ventured into data science.

Support vector machines is too similar to logistic regression, plus, I've seen it used quite a bit in survey research, so I personally consider it to be in between statistics and data science. Other "in-betweens" include principal component analysis and factor analysis. They are popular methods for dimension reduction. Data scientists classify them as unsupervised machine learning algorithms; I am not aware that we statisticians have the terms "supervised" and "unsupervised learning", but the essence of the analyses are identical. As a matter of fact, the first time I was truly introduced to the terminology "machine learning" was after I quit my data science job and took Andrew Ng's [Machine Learning](https://www.coursera.org/learn/machine-learning) on Coursera.

In public health and biostatistics, we had a big branch of research using survival analysis. I had the honor to be taught survival analysis by Jack Kalbfleisch and still have a textbook with his autograph on. Too bad I was always more interested in social science and those cox proportional hazard models never really stick with me. In data science, there is a big branch of analysis on time series. Time series and survival analysis are different except they both deal with time. Survival analysis handles data censored over time. I am not familiar with time series though I had been maintaining the company's R codes on moving averages and ARIMA. I believe it is popular for data scientists to use past data to predict future data with ARIMA. In contrast, "past data" is not a common concept for statisticians. Statisticians are usually given unrelated independent variables to explain an outcome; if a statistician is lucky to have longitudinal data, they usually use methods for repeated measurement or survival analysis.

In epidemiology and clinical trials, we loved our treatment and control studies. I was told, and please don't quote me on this, that treatment/control studies are called A/B testing in the land of data science. A/B testing appears to be popular in advertising and marketing where you compare the effectiveness of market strategies.

Statisticians use imputation to fill missing data. Bayesian statisticians use empirical methods to estimate posterior. These can be compute-intensive, and so I am a bit surprised that I haven't run into people doing these things since I became a Silicon Valley data scientist. Instead, I have been hearing data scientists talk a lot about iterations. Cannot find a solution? No worries! We'll iterate to find the answer. Prediction not accurate enough? No worries! We'll iterate to tune parameters.

So I'm running out of time to do other homework, but if there's gonna be another post, it will be my attempt to tell you my take on two opposite philosophies from statisticians and from data scientists based on fragments of personal experience.
