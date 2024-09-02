def largestSubgrid(grid, maxSum):

    # 현재 정사각형 배열의 행 열 길이를 확인
    n = len(grid)

    max_sum = -1  # 초기값을 -1로 설정하여 maxSum 이하의 합을 찾을 수 있도록 함

    result = 0

    for size in range(1, n + 1): # size: 현재 하위 그리드의 크기
        current_max = -1  # 현재 하위 그리드 크기의 최대 합을 찾기 위한 초기값 설정
        for i in range(n - size + 1): # i : 더히기 시작할 현재 하위 그리드의 시작 행
            for j in range(n - size + 1): # j : 더하기 시작할 현재 하위 그리드의 시작 열
                # size의 크기만큼 열을 더하고 그 결과로 각 행을 size 크기만큼 더함
                subgrid_sum = sum(
                    sum(grid[x][j:j+size]) for x in range(i, i+size)
                )
                # 더 큰 값을 현재 격자 크기에서 최대값으로 수정
                current_max = max(current_max, subgrid_sum)

        if current_max <= maxSum and current_max > max_sum:
            max_sum = current_max
            result_n = size

    return result