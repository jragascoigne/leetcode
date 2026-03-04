# intuition
I had just done some interview prep questions where I made something similar so this logic came pretty quick. However, I realised that I wanted two data structures:
a list for the feed, and a set for the following. This was because i knew we could use a hash map with a stack for values for the feed which will return
the most recent values (what we want) and a hash map with a hash set to handle following. This was because the following needed to be checked with 'in'
efficiently and this allowed no duplicates of followees following followed users.

follow and unfollow logic was simple and just adds or discards from the set, with discard being used to avoid keyerror.

# code
```py
class Twitter:

    def __init__(self):
        self.global_id = 0
        self.feed = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.global_id += 1
        self.feed[userId].append((self.global_id, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = list(self.feed[userId])

        for followeeId in self.following[userId]:
            if followeeId != userId:
                all_tweets.extend(self.feed[followeeId])

        all_tweets.sort(key=lambda x: x[0], reverse=True)
        return [tweetId for _, tweetId in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
```
