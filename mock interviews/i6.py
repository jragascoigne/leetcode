from collections import defaultdict

class NotificationInbox:
    def __init__(self):
        self.timestamp = 0
        self.users_inbox = defaultdict(list) # name for key, list of tuples for values (notification items)
        self.users_unread = defaultdict(int) # stores number of unread messages
    
    def send(self, user, message):
        self.timestamp += 1
        self.users_inbox[user].append((self.timestamp, message, False)) # new message, with timestamp, message and isRead
        self.users_unread[user] += 1

    def mark_read(self, user, message):
        for index, (ts, msg, read) in enumerate(self.users_inbox[user]):
            if msg == message:
                if not read:
                    self.users_inbox[user][index] = (ts, msg, True)
                    self.users_unread[user] -= 1
                
                return
                
        raise ValueError("Notification does not exist")
    
    def mark_all_read(self, user):
        self.users_inbox[user] = [(ts, msg, True) for (ts, msg, _) in self.users_inbox[user]]
        self.users_unread[user] = 0
    
    def get_unread(self, user):
        list_unread = [msg for (ts, msg, read) in self.users_inbox[user] if not read]
        return list(reversed(list_unread))

    def get_all(self, user):
        list_all = [msg for (ts, msg, _) in self.users_inbox[user]]
        return list(reversed(list_all))

    def unread_count(self, user):
        return self.users_unread[user]

inbox = NotificationInbox()
inbox.send("alice", "Your PR was approved")
inbox.send("alice", "New comment on PAGE-1")
inbox.send("alice", "Build failed")

print(inbox.get_unread("alice"))
# → ["Build failed", "New comment on PAGE-1", "Your PR was approved"]

inbox.mark_read("alice", "Build failed")
print(inbox.unread_count("alice"))  # → 2

inbox.mark_all_read("alice")
print(inbox.get_unread("alice"))    # → []
print(inbox.get_all("alice"))
# → ["Build failed", "New comment on PAGE-1", "Your PR was approved"]

inbox.mark_read("alice", "Doesn't exist")  # → raises ValueError
