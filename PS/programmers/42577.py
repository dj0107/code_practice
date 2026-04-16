def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        curr = phone_book[i]
        next = phone_book[i+1][:len(phone_book[i])]
        if curr in next:
            return False
    return True