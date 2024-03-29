import re
import kss
from kiwipiepy import Kiwi

kiwi = Kiwi()


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


def split_logues(text: str, q_map: dict = None, end_c: list = None) -> list:
    # input
    # - text(str): 책 한 페이지 글
    # - q_map(dict): 따옴표 종류. {'시작 따옴표'(str): ('끝 따옴표'(str), '따옴표 종류'(str))}
    # - end_c(list): 대사 마침 기호. ['기호1'(str), '기호2'(str), ...]
    # output
    # - (list) 나레이션/대사 분리 데이터. [{'type': 'narration'|'dialogue'|'monologue', 'text': 분리된 글}]

    if q_map is None:
        q_map = {'"': ('"', 'dialogue'), "“": ("”", 'dialogue'), "'": ("'", 'monologue'), "‘": ("’", 'monologue')}

    if end_c is None:
        end_c = [".", ",", "?", "!", "…", "―", "-", "~", ";"]

    logues = []
    n_logue = ""
    q_logue = ""
    q = None
    end_flag = False

    for c in text:
        if q is None:  # 따옴표 밖
            if c in q_map:  # 새로운 문자가 따옴표인 경우
                q = c
                q_logue += c

            else:  # 따옴표가 아닌 경우
                n_logue += c
                
        else:  # 따옴표 안
            q_logue += c
            if c == q_map[q][0]:  # 새로운 문자가 닫는 따옴표인 경우
                if end_flag:  # 직전 문자가 끝부호인 경우
                    n_logue = n_logue.strip()
                    q_logue = q_logue.strip()

                    if n_logue:
                        logues.append({'type': 'narration', 'text': n_logue})
                        n_logue = ""
                    if q_logue:
                        logues.append({'type': q_map[q][1], 'text': q_logue})

                else:  # 끝부호가 아닌 경우
                    n_logue += q_logue

                q_logue = ""
                q = None

        end_flag = c in end_c
    
    n_logue = n_logue.strip()

    if n_logue:
        logues.append({'type': 'narration', 'text': n_logue})

    return logues


def split_sentences(text, split_fn=split_logues, q_map=None, end_c=None, mode='kss'):
    sents = []
    
    for p in split_fn(text, q_map=q_map, end_c=end_c):
        txt = p['text'].replace("\n", " ")

        if mode == 'kiwi':
            for sent in kiwi.split_into_sents(txt):
                sents.append({'type': p['type'], 'text': sent.text})

        elif mode == 'kss':
            for sent in kss.split_sentences(txt, backend='auto'):
                sents.append({'type': p['type'], 'text': sent})
    
    return sents


def split_lines(text, split_fn=split_logues, q_map=None, end_c=None):
    lines = []
    for p in split_fn(text, q_map=q_map, end_c=end_c):
        txt = re.sub('\n+', '\n', p['text'])

        for line in txt.split('\n'):
            lines.append({'type': p['type'], 'text': line})

    return lines