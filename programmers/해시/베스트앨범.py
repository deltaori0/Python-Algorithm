def solution(genres, plays):
    answer = []
    
    album = {}
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        if genre in album:
            album[genre]['total'] += play
            album[genre]['music'].append((play, i))
        else:
            album[genre] = {'total': play, 'music': [(play, i)]}
    
    # 가장 많이 재생된 장르 순으로 정렬
    items = sorted(album.items(), key=lambda x: x[1]['total'], reverse=True)
    
    for i in items:
        # 재생 횟수, 고유 번호 순으로 우선 순위 정렬
        info = sorted(i[1]['music'], key=lambda x: (x[0], -x[1]), reverse=True)
        
        # 장르에 속한 곡이 하나라면, 하나의 곡만 선택
        if len(info) == 1:
            answer.append(info[0][1])
        else:
            answer += [info[0][1], info[1][1]]
    
    return answer