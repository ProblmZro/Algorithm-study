# 테스트 3, 4 시간초과
def solution(phone_book):
    for i in phone_book:
        for j in phone_book:
            if i != j and len(i) <= len(j):
                if i == j[0:len(i)]:
                    return False

    return True


def solution(phone_book):
    # 전화번호록 딕셔너리에 저장
    book = {}
    for phone in phone_book:
        book[phone] = 1
    
    # 접두사가 전화번호록에 있는지 확인
    for phone in phone_book:
        head = ''
        for num in phone:
            head += num
            if head in book and head != phone:
                return False
    
    return True