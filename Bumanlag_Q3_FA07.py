scores = [
    [85, 88, 90],   # Me
    [78, 82, 80],   # Friend 1
    [92, 90, 94],   # Friend 2
    [88, 85, 87],   # Friend 3
    [80, 83, 79]    # Friend 4
]

names = ["Me", "Friend 1", "Friend 2", "Friend 3", "Friend 4"]

# for printing each row and calculating totals & averages 
for i in range(len(scores)):
    total = sum(scores[i])
    average = total / len(scores[i])
    print("\n",names[i], "scores:", scores[i])
    print("  Total:", total)
    print("  Average:", average)

# for finding the maximum score in the entire dataset
max_score = scores[0][0]
for row in scores:
    for score in row:
        if score > max_score:
            max_score = score

print("\nHighest score in the dataset:", max_score)

"""
Using a 2D array made it simpler and easier to arrange and analyze several scores
for multiple people in a single structure. It enabled me to quickly compute averages
and totals and find the highest score using loops. I was able to better comprehend each
persons performance after i printed each row. I found calculating the totals and averages
to be the simplest part but i found finding the maximum valye a bit more difficult
since I had to check every element
"""