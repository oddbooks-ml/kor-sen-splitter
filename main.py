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

file_path = "./sentence.txt"  # 읽고자 하는 파일의 경로와 이름을 지정합니다.

s = read_txt(file_path)
# print(s)

# kiwi = Kiwi()

# a = kiwi.split_into_sents(s)
# print(a)
# # print(a[0].text.replace('\n', ''))
# for i in a:
#     print(i.text.replace('\n', ''))
#     print('-------') 


for i in kss.split_sentences(s, backend = 'auto'):
    print(i.replace('\n', ''))
    print('-----------')
