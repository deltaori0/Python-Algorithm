def solution(phone_book):
    phone_book.sort(key = lambda x: len(x))
    for i, p in enumerate(phone_book):
        for q in phone_book[i+1:]:
            if q.startswith(p):
                return False
    return True