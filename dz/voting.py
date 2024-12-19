votes_cnt = {}
n = int(input())
for i in range(n):
    film = input().strip()
    if film in votes_cnt:
        votes_cnt[film] += 1
    else:
        votes_cnt[film] = 1

k = int(input())
votes_items = list(votes_cnt.items())

def vote_num(item):
    return item[1]

votes_items.sort(key=vote_num, reverse=True)

for i in range(k):
    print('film:', votes_items[i][0], '  ','votes:', votes_items[i][1])
