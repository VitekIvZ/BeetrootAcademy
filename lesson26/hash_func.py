def compute_hash(W, T):
    h = 0
    for c in W:
        index = h ^ ord(c)
        h = T[index]
    return h

# Приклад використання
W = "example"
T = [i for i in range(256)]  # Приклад таблиці T, яка містить значення від 0 до 255

result = compute_hash(W, T)
print(f"Hash: {result}")
