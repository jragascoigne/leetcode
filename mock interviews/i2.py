# we want to store users in the hash map as the key, and a queue as the value
# this will allow the most recent activities to be displayed and the oldest ones to 'drop off'

class ActivityFeed:

    def __init__(self, feed_length):
        self.feed_length = feed_length # > 0
        self.feed = {} # key = user, value = stack []
        self.index = 0

    def record(self, user, activity):
        self.index += 1
        if user not in self.feed:
            self.feed[user] = [(activity, self.index)]
        
        else:
            if len(self.feed[user]) >= self.feed_length:
                self.feed[user].pop(0) # removes the first item in the array (oldest activity)
            self.feed[user].append((activity, self.index))
    
    def get_recent(self, user, n):
        if user not in self.feed:
            return []
        
        if len(self.feed[user]) >= n:
            return [a for a, _ in self.feed[user][-1:-n-1:-1]]
        else:
            return [a for a, _ in self.feed[user][::-1]]
    
    def get_all_recent(self):
        all_recent = []

        for user, activity in self.feed.items():
            for title, index in activity:
                all_recent.append((index, user, title))
        
        all_recent.sort(reverse=True)

        return [(u, a) for _, u, a in all_recent]

    def remove_user(self, user):
        if user not in self.feed:
            return False
        else:
            del self.feed[user]
            return True


feed = ActivityFeed(feed_length=4)
feed.record("alice", "edited page")
feed.record("alice", "created page")
feed.record("alice", "3")
feed.record("alice", "4")
feed.record("bob",   "commented")
feed.record("alice", "deleted page")   # "edited page" is dropped (oldest)

print(feed.get_recent("alice", 2))   # → ["deleted page", "created page"]
print(feed.get_recent("alice", 10))  # → ["deleted page", "created page"]  (only 2 stored now... wait, 3 were stored before the drop)
print(feed.get_all_recent())         # → [("alice", "deleted page"), ("alice", "created page"),
                              #    ("bob", "commented"), ("alice", "edited page")]
                              # wait — ordered by insertion time across all users

feed.remove_user('alice')
print(feed.get_recent("alice", 2))   # → ["deleted page", "created page"]
print(feed.get_recent("alice", 10))  # → ["deleted page", "created page"]  (only 2 stored now... wait, 3 were stored before the drop)
print(feed.get_all_recent())         # → [("alice", "deleted page"), ("alice", "created page"),
                              #    ("bob", "commented"), ("alice", "edited page")]
                              # wait — ordered by insertion time across all users



# #java code
# class ActivityFeed {
#     public void record(String user, String activity) {
#         // ...
#     }
    
#     public ArrayList getRecent(String user, Integer n) {
#         // ...
#     }
    
    
#     public ArrayList getAllRecent() {
#         // ...
#     }
    
#     public boolean removeUser(String user) {
#         // ...
#     }

# }

