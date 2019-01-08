import json

from elasticsearch import Elasticsearch
from canari.maltego.entities import Person, Twit, Hashtag, Location
from canari.maltego.transform import Transform

es = Elasticsearch()
class getTweetsFromUser(Transform):
    input_type = Person

    def do_transform(self, request, response, config):
        person = request.entity
        _body = {
                'query': {
                    'match' :
                        {
                            'username': person.value
                        }
                },
                'size': request.limits.hard
            }
        res = es.search(index="twinttweets", body=_body)
        for hit in res['hits']['hits']:
            tweet = hit['_source']
            r = Twit()
            r.id = int(tweet['id'])
            r.content = tweet['tweet'].encode('ascii', 'ignore')
            r.name = tweet['tweet'].encode('ascii', 'ignore')
            r.title = tweet['tweet'].encode('ascii', 'ignore')[:30]
            r.pubdate = tweet['date']
            r.author = tweet['username']
            r.author_uri = 'https://twitter.com/' + tweet['username']
            response += r
        return response

class getUsersFromTweets(Transform):
    input_type = Twit

    def do_transform(self, request, response, config):
        tweet = request.entity
        _body = {
                'query': {
                    'match' :
                        {
                            'id': tweet.id
                        }
                },
                'size': request.limits.hard
            }
        res = es.search(index="twinttweets", body=_body)
        for hit in res['hits']['hits']:
            tweet = hit['_source']
            r = Person()
            r.name = tweet['name'].encode('ascii', 'ignore')
            r.value = tweet['username']
            r.url = 'https://twitter.com/' + tweet['username']
            response += r
        return response

class getHashtagsFromTweets(Transform):
    input_type = Twit

    def do_transform(self, request, response, config):
        tweet = request.entity
        try:
            _body = {
                    'query': {
                        'match' :
                            {
                                'id': tweet.id
                            }
                    },
                    'size': request.limits.hard
                }
            res = es.search(index="twinttweets", body=_body)
            for hit in res['hits']['hits']:
                tweet = hit['_source']
                hashtags = tweet['hashtags']
                for h in hashtags:
                    r = Hashtag()
                    r.value = h
                    response += r
        except UnicodeEncodeError:
            pass
        return response

class getLocationFromTweets(Transform):
    input_type = Twit

    def do_transform(self, request, response, config):
        tweet = request.entity
        _body = {
                'query': {
                    'match' :
                        {
                            'id': tweet.id
                        }
                },
                'size': request.limits.hard
            }
        res = es.search(index="twinttweets", body=_body)
        for hit in res['hits']['hits']:
            tweet = hit['_source']
            r = Location()
            if tweet['location']:
                r.name = tweet['location']
                response += r
        return response

class getPlaceFromTweets(Transform):
    input_type = Twit

    def do_transform(self, request, response, config):
        tweet = request.entity
        _body = {
                'query': {
                    'match' :
                        {
                            'id': tweet.id
                        }
                },
                'size': request.limits.hard
            }
        res = es.search(index="twinttweets", body=_body)
        for hit in res['hits']['hits']:
            tweet = hit['_source']
            r = Location()
            if tweet['place']:
                r.name = tweet['place']
                response += r
        return response

class getNearFromTweets(Transform):
    input_type = Twit

    def do_transform(self, request, response, config):
        tweet = request.entity
        _body = {
                'query': {
                    'match' :
                        {
                            'id': tweet.id
                        }
                },
                'size': request.limits.hard
            }
        res = es.search(index="twinttweets", body=_body)
        for hit in res['hits']['hits']:
            tweet = hit['_source']
            r = Location()
            try:
                r.longitude = tweet['geo_near']['lon']
                r.latitude = tweet['geo_near']['lon']
                r.city = tweet['near']
                response += r
            except KeyError:
                pass
        return response

class getFollowersFromUser(Transform):
    input_type = Person

    def do_transform(self, request, response, config):
        user = request.entity
        _body = {
                'query': {
                    'match' :
                        {
                            'follow': user.value
                        }
                },
                'size': request.limits.hard
            }
        res = es.search(index="twintgraph", body=_body)
        for hit in res['hits']['hits']:
            _user = hit['_source']
            r = Person()
            r.value = _user['user']
            response += r
        return response

class getFollowingFromUser(Transform):
    input_type = Person

    def do_transform(self, request, response, config):
        user = request.entity
        _body = {
                'query': {
                    'match' :
                        {
                            'user': user.value
                        }
                },
                'size': request.limits.hard
            }
        res = es.search(index="twintgraph", body=_body)
        for hit in res['hits']['hits']:
            _user = hit['_source']
            r = Person()
            r.value = _user['follow']
            response += r
        return response
