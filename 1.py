def perfectTeam(skills):

    if ((len(skills)<5) or (len(skills)>5*(10**5))):
        return "skills의 길이가 조건에 맞지 않습니다."

    # 각 과목의 발생 빈도를 저장할 딕셔너리 생성 후 초기화
    skill_counts = {'p': 0, 'c': 0, 'm': 0, 'b': 0, 'z': 0}
    
    # skills에서 각 기술의 발생 빈도를 계산해서 딕셔너리 수정
    for skill in skills:
        if skill not in skill_counts:
            return "학교에서 취급하지 않는 과목이 포함되어 있습니다."
        if skill in skill_counts:
            skill_counts[skill] += 1
    
    # 만약 딕셔너리에 하나라도 0인 값이 있으면 0을 리턴 (생성할 수 있는 팀이 없음)
    if any(count == 0 for count in skill_counts.values()):
        return 0
    
    # 그것이 아니라면 가장 작은 값을 리턴 (5명의 학생은 각각 무조건 다른 과목에 능숙하도록 팀이 구성되어야 함)
    return min(skill_counts.values())