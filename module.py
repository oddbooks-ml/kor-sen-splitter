import kss


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
    # 여러 종류의 작은 따옴표를 ascii code 값이 39인 ' 따옴표로 변환
    targets = '“”'
    for t in targets:
        text = text.replace(t, '"')

    targets = "‘’"
    for t in targets:
        text = text.replace(t, "'")

    return text


def split_lines(text: str) -> list:
    # input
    # - text(str): 책 한 페이지 글
    # output
    # - (list) 나레이션/대사 분리 데이터. [{'type': 'narration'|'dialogue'|'monologue', 'text': 분리된 글}]

    def strip_line():
        lines[-1]['text'] = lines[-1]['text'].strip()
        if len(lines[-1]['text']) == 0:
            lines.pop()

    lines = [{'type': None, 'text': ""}]

    for c in text:
        ltype = {'"': 'dialogue', "'": 'monologue'}.get(c, 'narration')

        if lines[-1]['type'] == 'narration' != ltype:
            strip_line()
            lines.append({'type': ltype, 'text': ""})
        elif lines[-1]['type'] == ltype != 'narration':
            strip_line()
            lines.append({'type': None, 'text': ""})
        elif lines[-1]['type'] is None:
            lines[-1]['type'] = ltype
            lines[-1]['text'] += c
        else:
            lines[-1]['text'] += c

    strip_line()
    return lines


def split_sentences(text):
    sents = []
    
    for line in split_lines(text):
        txt = line['text'].replace("\n", "")
        for sent in kss.split_sentences(txt, backend='auto'):
            sents.append({'type': line['type'], 'text': sent})
    
    return sents