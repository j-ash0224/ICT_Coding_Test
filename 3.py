def doesCircleExistForCommand(command):

    if len(command)<1 or len(command)>2500:
        return "문자열의 길이가 조건에 부합하지 않습니다" 

    # 시작점의 좌표와 방향을 설정
    x, y = 0, 0
    direction = 0
    
    # 움직임에 따라 방향을 확인하고 그에 따라서 좌표를 수정하는 함수를 선언
    # 방향이 0일때는 위로 이동
    # 방향이 1일때는 오른쪽으로 이동
    # 방향이 2일때는 아래로 이동
    # 방향이 3일때는 왼쪽로 이동
    def move(x, y, direction):
        if direction == 0:  
            y += 1
        elif direction == 1: 
            x += 1
        elif direction == 2: 
            y -= 1
        elif direction == 3: 
            x -= 1
        return x, y
    

    # 명령어를 네 번 반복하여 로봇의 움직임을 확인
    # 네 번 반복하면 원을 그리는지 혹은 원을 벗어나지 않는지 확인 가능
    for i in range(4):  
        for cmd in command:
            if cmd not in ['G','R','L']:
                return  "조건에 부합하지 않는 문자가 포함"
            if cmd == 'G':
                x, y = move(x, y, direction)
            elif cmd == 'L':
                direction = (direction - 1) % 4
            elif cmd == 'R':
                direction = (direction + 1) % 4
    
    # 로봇이 처음 위치로 돌아왔다면 , 방향이 처음과 다를 경우 4번을 반복했을 때 원을 그리거나 특정 크기의 원에서 벗어나지 않는 것으로 간주 가능
    if (x == 0 and y == 0) or direction != 0:
        return "YES"
    else:
        return "NO"


# 각 명령어 문자열을 요소로 가진 리스트를 파라미터로 가짐
def doesCircleExist(commands):

    if len(commands)<1 or len(commands)>10:
        return "배열의 길이가 조건에 부합하지 않습니다" 
    
    # 결과 저장을 위한 리스트 생성
    results = []
    #파라미터의 각 문자열을 각각 확인하고 결과를 저장
    for command in commands:
        results.append(doesCircleExistForCommand(command))
    
    #결과 반환
    return results