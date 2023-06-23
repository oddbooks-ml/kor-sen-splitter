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

# 쓸지 말지 고민 중
def split_kiwi():
    kiwi = Kiwi()

    a = kiwi.split_into_sents(s)
    print(a)
    # print(a[0].text.replace('\n', ''))
    for i in a:
        print(i.text.replace('\n', ''))
        print('-------')  


def split_kss(txt):
    
    result_dic = {}
    num = 0

    for i in kss.split_sentences(txt, backend = 'auto'):
        print(i.replace('\n', ''))
        print('-----------')

    return result_dic


#TODO  : 나래이션 중복일때
def preprocess_sen(sentence):
    result = ''
    # if sentence.count('“') == 2 or sentence.count('”') == 2:
    #     print(False)
    
    if '”“' in sentence:
        sen_result = sentence.split('”“')
        
        sen_result = [i.replace('”','').replace('“','') for i in result]
        label = 'dialogue'
        
        # print(result)
    else:
        result = sentence.replace('”','').replace('“','')
        label = 'narration'
    return result


# TODO : labeler
def labeller(sentence):
    if
    pass


#TODO :  대화 중복일때


if __name__ == '__main__':
    
    # file_path = "./sentence.txt"  # 읽고자 하는 파일의 경로와 이름을 지정합니다.
    # s = read_txt(file_path)
    # “”
    a = "“두 시부터라고 했지?”"
    # a = '“네.”“이따 만나자.”'
    aa = preprocess_nrr(a)
    print(aa)
