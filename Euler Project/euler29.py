def distinct_term_sequence(limit):
    distinct_terms = set()

    for a in range(2, limit + 1):
        for b in range(2, limit + 1):
            distinct_terms.add(a ** b)

    return len(distinct_terms)


result = distinct_term_sequence(100)
print("number of distinct terms:", result)
