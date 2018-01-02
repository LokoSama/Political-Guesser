# Political-Guesser

## Goal

This project has the goal of creating a neural network able to guess political side based on a tweet.

## Context

The context of this project is the Project class of the Faculty of Electrical Engineering and Computing of the Univeristy of Zagreb.

## Idea

Themodel will be trained on tweets coming from United States Congress members, by requesting them using Twitter API.
Once the training is over, the goal is to have a model able to guess the political side of the person emitting the tweet, or at least give the likelihood of the class. The United States congress was chosen because of the existence of 2 major political classes, it can be imagined to continue this project with other countries thats contains more political classes.

## State of the project

We have 2 different classifiers : NB classifier with 80% accuracy and SVM classifier with 70% accuracy.

We created 2 final functions : 
- tweet_guesser : guess the political side from a tweet (based on his text) with the certainty
- account_guesser : guess the political side from a account (based on his @)
