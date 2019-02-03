# Twint Maltego transforms set

> A Maltego transforms collection for Twint

![1](https://pbs.twimg.com/media/DvrboAwV4AAH1Pt.jpg)
![2](https://i.imgur.com/j9xgZZx.png)

## Setup

Since canari profiles are not exportable, you have to compile one **for every machine** that you will play with. Every machine will need its own.

Requirements:

- Twint;
- Elasticsearch;
- Maltego;
- canari.

Once those dependencies are installed, you have to package the profile. This set of transforms is almost batteries included so be sure that you are going to connect to the right Elasticsearch instance, edit `twint/src/twint/transforms/getTweets.py` by your needs. With default setting, the tranforms will connect to a local instance of Elasticsearch (localhost:9200).

Now you have just to package:

- move to `twint/src`;
- run `canari create-profile twint` (hit `y` a couple of times).

## How-to

Import `twint.mtz` in Maltego and start playing!

## Copyrights and Credits

The Twint Project - 2018/19
