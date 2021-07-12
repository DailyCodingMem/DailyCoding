n = int(input())
scores = list(map(int,input().split(' ')))
new_scores = []
for score in scores:
    new_scores.append(score/max(scores)*100)
print(sum(new_scores)/len(scores))