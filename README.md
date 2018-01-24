# Political-Guesser

## Goal

This project has the goal of creating a neural network able to guess political side based on a tweet.

## Context

The context of this project is the Project class of the Faculty of Electrical Engineering and Computing of the Univeristy of Zagreb.

## Idea

The model will be trained on tweets coming from United States Congress members, by requesting them using Twitter API.
Once the training is over, the goal is to have a model able to guess the political side of the person emitting the tweet. The United States congress was chosen because of the existence of 2 major political classes, it can be imagined to continue this project with other countries thats contains more political classes.

## State of the project

We have 2 different classifiers : NB classifier with 80% accuracy and SVM classifier with 73% accuracy.

We created 2 final functions : 
- tweet_prediction : guess the political side from a tweet (based on his text) with the certainty
- account_prediction : guess the political side from a account (based on his @)

The account prediction accuracy is 99% with NB classifier and 87% with SVM classifier.

## Remove hashtags from dataset

To remove hashtags from the datasets, add the following code in the filtering part of the CSV

delete_tags = lambda x:re.sub(r'#\S+', '', x) 

dataset[2] = dataset[2].apply(delete_tags)
