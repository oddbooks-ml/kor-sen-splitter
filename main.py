import kss
from kiwipiepy import Kiwi


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


if __name__ == '__main__':

    # file_path = "./sentence.txt"  # 읽고자 하는 파일의 경로와 이름을 지정합니다.
    file_path = "./sentence(refined).txt"

    text = read_txt(file_path)
    print(text)
    print("----------\n")

    # kiwi
    print("kiwi\n")

    kiwi = Kiwi()
    kiwi_res = kiwi.split_into_sents(text)
    print(kiwi_res, "\n")

    for sent in kiwi_res:
        print(repr(sent.text))
    print("----------\n")

    # kss mecab
    print("kss mecab\n")
    kss_res = kss.split_sentences(text, backend='mecab')
    print(kss_res, "\n")

    for sent in kss_res:
        print(repr(sent))
    print("----------\n")

    # kss pecab
    print("kss pecab\n")
    kss_res = kss.split_sentences(text, backend='pecab')
    print(kss_res, "\n")

    for sent in kss_res:
        print(repr(sent))
    print("----------\n")

    # kss puncturation
    print("kss puncturation\n")
    kss_res = kss.split_sentences(text, backend='punct')
    print(kss_res, "\n")

    for sent in kss_res:
        print(repr(sent))
    print("----------\n")

