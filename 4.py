def findSchedules(workHours, dayHours, pattern):

    if workHours<1 or workHours>56:
        return "주중에 일하는 시간이 범위에 맞지 않습니다"
    
    if dayHours<1 or dayHours>8:
        return "하루에 일하는 시간이 범위에 맞지 않습니다"
    
    if len(pattern) !=7 :
        return "패턴은 7자리여야 합니다"
    
    for i in pattern:
        if i not in [0,1,2,3,4,5,6,7,8,'?']:
            return  "패턴은 1~8 그리고 ? 로만 입력해야 합니다"

    # 백트레킹 함수 정의 (중간에 유효하지 않은 값이라면 되돌아감)
    def backtrack(i, hours_left, current_pattern):
        # 남은 시간이 0보다 작으면 유효하지 않은 경우이므로 종료
        if hours_left < 0:
            return
        
        # 패턴의 끝까지 도달했을 때 남은 시간이 0이면 결과에 현재 패턴을 추가 (유효하지 않다면 추가하지 않고 되돌아감)
        if i == len(pattern):
            if hours_left == 0:
                result.append(''.join(map(str, current_pattern)))
            return
        
        # 현재 패턴이 '?'인 경우 가능한 모든 시간을 시도
        if pattern[i] == '?':
            for h in range(0, dayHours + 1):
                current_pattern[i] = h
                backtrack(i + 1, hours_left - h, current_pattern)
                current_pattern[i] = '?'

        # '?'가 아닌 경우 해당 시간을 그대로 사용
        else:
            current_pattern[i] = int(pattern[i])
            # 해당 시간 만큼을 제외하고 남은 시간으로 계산
            backtrack(i + 1, hours_left - current_pattern[i], current_pattern)
            current_pattern[i] = '?'

    result = []

    backtrack(0, workHours, list(pattern))

    return result