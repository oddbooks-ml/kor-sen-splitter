def read_txt(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()  # 파일의 내용을 읽어옵니다.
            # print(contents)  # 내용을 화면에 출력하거나 원하는 작업을 수행합니다.
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    except IOError:
        print("파일을 읽는 중에 오류가 발생했습니다.")

    return contents


def union_qmark(text: str) -> str:
    # 여러 종류의 큰 따옴표를 ascii code 값이 34인 " 따옴표로 변환
    targets = ['“', '”']
    for t in targets:
        text = text.replace(t, '"')
    return text


def split_line(text: str, conn_line: dict[str, str] = None) -> tuple[bool, list]:
    # input
    # - text(str): 책 한 페이지 글
    # - conn_line(dict): 이전 페이지에서 대사가 미완결된 경우 마지막 대사 데이터
    # output
    # - (bool) 마지막에 대사가 완결되었는지 여부. True: 완결 / False: 미완결
    # - (list) 나레이션/대사 분리 데이터. [{'type': 'line' 또는 'narration', 'content': 분리된 글}]
    
    lines = text.split('"')
    res = []
    if conn_line:
        lines.reverse()
        conn_line['content'] += lines.pop()
        res.append(conn_line)
        lines.reverse()
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) == 0:
            continue

        if i % 2 == 0:
            res.append({'type': 'narration', 'content': line})
        else:
            res.append({'type': 'line', 'content': line})

    return i % 2 == 0, res