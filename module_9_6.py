def all_variants(text):
    for i in range(1, len(text)+1):
        for j in range(len(text)):
            if i+j < len(text)+1:
                yield text[j:i+j]
                continue




a = all_variants("abc")
for i in a:
    print(i)