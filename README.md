# Political-Guesser

## Goal

This project has the goal of creating a neural network able to guess political side based on a tweet.

## Context

The context of this project is the Project class of the Faculty of Electrical Engineering and Computing of the Univeristy of Zagreb.

## Idea

The neural network will be trained on tweets coming from United States Congress members, by requesting them using Twitter API.
Once the training is over, the goal is to have a neural network able to guess the political side of the person emitting the tweet, or at least give the likelihood of the class. The United States congress was choose because of the existence of 2 major political classes, it can be imagined to continue this project with other countries thats contains more political classes.

## Tasks 

- get the tweets from US congress members through Twitter API, and store them (existence of a verified list of memebers account)
- get the political class of each member of the congress, store that
- setup neural network and datasets
- train neural network
