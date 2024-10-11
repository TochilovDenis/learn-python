def similar_segment(segments: list[str], separators: set[str]) -> list[str]:
    if not segments:
        return []

    result: list[str] = ['']
    for segment in segments:
        result[-1] += segment
        if segment.strip()[-1] in separators and segment is not segments[-1]:
            result.append('')

    return result


if __name__ == '__main__':
    initial_list_str: list[str] =  ['Вышел корень из тумана; ', 'Вынул ножик из кармана. ', 'Раз, два, всё?..']
    seps = set('!?.,;')
    print(similar_segment(initial_list_str, seps))