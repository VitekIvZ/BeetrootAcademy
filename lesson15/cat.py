def count_age_cat(n):
    if n >= 12:
        age_cat = (n-12)*3 + (12-3)*4 + 24
    elif n >= 3 and n < 12:
        age_cat = (n-3)*4 + 24
    elif n < 3 and n >= 2:
        age_cat = 24
    elif n < 2 and n >= 1:
        age_cat = 15
    else:
        age_cat = 0
        
    return age_cat


if __name__ == "__main__":
    print(count_age_cat(7))