from collections import defaultdict

def top_commenters(events, k):
    commenters = defaultdict(int)
    user_most_recent = defaultdict(int)

    for timestamp, user in events:
        commenters[user] += 1
        user_most_recent[user] = max(user_most_recent[user], timestamp)
    

    if not commenters:
        return []
    
    commenters_sorted = sorted(commenters.items(), key=lambda item: (commenters[item[0]], user_most_recent[item[0]], item[0]), reverse=True)

    return_list = []
    for i in range(k):
        return_list.append(commenters_sorted[i][0])
    
    return return_list



events = [
    (1, "alice"),
    (2, "bob"),
    (3, "alice"),
    (4, "charlie"),
    (5, "bob"),
    (6, "alice"),
    (8, "alice"),
    (7, "charlie"),
    (8, "charlie"),
]


print(top_commenters(events, 2))

# top_commenters(events, 2)  # → ["alice", "charlie"]
# # alice: 3 comments, latest at t=6
# # charlie: 3 comments, latest at t=8  ← more recent, so ranked higher
# # bob: 2 comments
# # result ordered by: charlie first (tie on count, wins on recency), then alice
