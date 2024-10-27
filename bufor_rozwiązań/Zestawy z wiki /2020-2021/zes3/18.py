def menchester_algorithm(arr):
    
    def preprocess(arr):
        return ["#"] + list(
            '#'.join(str(i)
            for i in arr)
            ) + ["#"]

    
    # print(preprocess(arr))

    arr = preprocess(arr)


    palindrome = [0]*len(arr)
    right = 0
    center = 0

    for i in range(len(arr)):
        i_mirrored = center - (i - center)

        if right > i:
            palindrome[i] = min(palindrome[i_mirrored], right-i)
        
        while i+1+palindrome[i] < len(arr) and i-1-palindrome[i] >= 0 and arr[i+1+palindrome[i]] == arr[i-1-palindrome[i]]:
            palindrome[i] += 1
        
        if i + palindrome[i] > right:
            right = i + palindrome[i]
            center = i
    
    return max(palindrome)


# print(menchester_algorithm([3,4,3,7,2,3,7,3,1]))

def split_by_even(arr):
    answer = []
    curr_list = []

    for el in arr:
        if el % 2 == 1:
            curr_list.append(el)
        else:
            if len(curr_list) > 0:
                answer.append(curr_list)

            curr_list = []

    if len(curr_list) > 0:
        answer.append(curr_list)
    
    return answer


def ex18(arr):
    maxi = 0
    for candidate in split_by_even(arr):
        maxi = max(menchester_algorithm(candidate), maxi)
    
    return maxi



print(ex18([1,1,1,6,1,1,1,6,1,3,1,1,3,5]))