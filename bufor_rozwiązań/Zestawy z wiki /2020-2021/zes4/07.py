def flatten(T1):
    while len(T1) > 1:
        multilist = []
        
        for lists in range(0, len(T1), 2):
            if lists == len(T1)-1:
                multilist.append(T1[lists])
                continue
            
            print(T1[lists])
            print(T1[lists+1])
            print("---------")

            tmp = []
            i, j = 0, 0
            while i < len(T1[lists]) and j < len(T1[lists+1]):
                # if T1[lists][i] == T1[lists+1][j]:
                #     i += 1
                #     j += 1
                #     continue
                if T1[lists][i] <= T1[lists+1][j]:
                    # if len(tmp) == 0 or tmp[-1] != T1[lists][i]:
                    tmp.append(T1[lists][i])
                    i += 1
                else:
                    # if len(tmp) == 0 or tmp[-1] != T1[lists+1][j]:
                    tmp.append(T1[lists+1][j])
                    j += 1

            for elem in T1[lists][i:]:
                if tmp[-1] != elem:
                    tmp.append(elem)
                    print("a",end="")
            for elem in T1[lists+1][j:]:
                if tmp[-1] != elem:
                    tmp.append(elem)
                    print("b", end="")

            multilist.append(tmp)
        T1 = multilist
        multilist = []
    

    return T1[0]

print(flatten([[1,4,5,6,7], [3,6,7], [1,6,7,9]]))