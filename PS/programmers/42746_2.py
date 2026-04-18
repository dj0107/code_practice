from functools import cmp_to_key


def solution(numbers):
    # 문자열로 변환 후, 두 수를 이어붙였을 때 더 큰 순서대로 정렬
    arr = list(map(str, numbers))
    arr.sort(key=cmp_to_key(compare), reverse=True)

    joined = ''.join(arr)
    # 모두 0인 경우 "0" 하나만 반환
    return '0' if joined and joined[0] == '0' else joined


def compare(a: str, b: str) -> int:
    # a+b vs b+a 중 더 큰 쪽이 앞에 오도록 비교
    ab = a + b
    ba = b + a
    if ab > ba:
        return 1
    if ab < ba:
        return -1
    return 0


if __name__ == "__main__":
    print(solution([6, 10, 2]))
    print(solution([3, 30, 34, 5, 9]))
