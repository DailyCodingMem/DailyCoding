def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        # Miss
        try:
            if city.capitalize() not in cache:
                if len(cache) < cacheSize:
                    cache.append(city.capitalize())
                    answer += 5
                else:
                    cache.pop(0)
                    cache.append(city.capitalize())
                    answer += 5
            # Hit
            else:
                cache.pop(cache.index(city.capitalize()))
                cache.append(city.capitalize())
                answer += 1
        # cacheSize가 0일때 index에러가 발생한다(pop(0)때문), 그래서 예외처리!
        except:
            answer = 5 * len(cities)
    return answer
