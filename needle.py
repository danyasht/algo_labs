def find_needle(haystack, needle):
    comparisons = 0
    last_index = -1 

    needle_length = len(needle)
    haystack_length = len(haystack)

    for i in range(haystack_length - needle_length + 1):
        match = True

        for j in range(needle_length):
            comparisons += 1
            if haystack[i + j] != needle[j]:
                match = False
                break
        
        if match:
            last_index = i

    return last_index, comparisons

haystack = "This is a haystack and we're looking for a needle in this haystack needle"
needle = "needle"

result_index, comparisons = find_needle(haystack, needle)
print(f"Last in index of the '{needle}' in haystack: {result_index}")
print(f"Number of comparisons: {comparisons}")

