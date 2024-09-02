def raisingPower(arr):

    if len(arr)<1 or len(arr)>10**5:
        return "배열의 길이가 조건에 부합하지 않습니다" 

    for i in range(0, len(arr)):
        if arr[i]<1 or arr[i]>100:
            return "배열 요소 중 조건에 부합하지 않는 값이 존재합니다."                   

    # 계산 정보를 저장할 빈 리스트 생성
    arr2 = []

    #나눌 값
    MOD = 10**9 + 7

    for i in range(0, len(arr)-1):
        # 리스트 마지막 요소를 제외하고 각 리스트를, 다음 리스트만큼 제곱
        # 그 후 MOD로 나누고 나머지 값을 arr2에 추가
        arr2.append((arr[i]**arr[i+1])%MOD)

    #생성된 리스트에서 가장 큰 값을 확인
    max_value = max(arr2)

    #해당 값의 인덱스를 반환한다. 이 때, 같은 크기의 값이 중복되어 있으면 선행되는 인덱스를 반환
    min_index = arr2.index(max_value)
    
    # 문제에서는 인덱스 값을 1부터 시작했으므로 +1
    return min_index+1
