for test in range(int(input())):
    base = input()
    word = input()
    for i in range(len(word)-len(base)+1):
        if word[i:i+len(base)] == base:
            print('#{} {}'.format(test+1, 1))
            break
    else:
	    print('#{} {}'.format(test+1, 0))
