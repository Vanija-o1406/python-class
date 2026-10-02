total = 0

def increase():
    total = 0
    total += 5
    return total

print(increase(), increase(), total)


LIMIT = 75

def needs_attention(value):
    return value >= LIMIT

print(needs_attention(82))
print(needs_attention(64))


score = 0

def update_score():
    local_score = 0
    local_score += 1
    return local_score

print(update_score())


score = 0

def update_global_score():
    global score
    score += 1
    return score

print(update_global_score(), update_global_score(), update_global_score())
print("score outside function:", score)


def next_score(value):
    return value + 1

score = 0
score = next_score(score)
score = next_score(score)
score = next_score(score)

print("final score:", score)


records = 0

def create_summary():
    entries = ["start"]
    entries.append("finish")
    return len(entries)

print(create_summary())
print(create_summary())
print("records" in dir())