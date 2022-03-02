import numpy as np

def Forward_MM(user_dict, sentence):
    '''
    :param user_dict:
    :param sentence:
    :return: result of forward max match
    '''
    max_len = max([len(item) for item in user_dict]) # 取最长的词
    start = 0
    result = []
    while start != len(sentence):
        index = start+max_len
        if index>len(sentence):
            index = len(sentence)
        for i in range(max_len):
            if (sentence[start:index] in user_dict) or (len(sentence[start:index])==1):
                result.append(sentence[start:index])# 将匹配到的词放入列表
                start = index
                break
            index += -1
    return result


def Backward_MM(user_dict, sentence):
    '''
    :param user_dict:
    :param sentence:
    :return: result of backward max match
    '''
    length = max([len(item) for item in user_dict]) # 取最长的词
    start = len(sentence)
    result = []
    while start != 0:
        index = start - length
        if index < 0:
            index = 0
        for i in range(length):
            if(sentence[index:start] in user_dict) or (len(sentence[index:start])==1):
                result.append(sentence[index:start]) # 将匹配到的词放入列表
                start = index
                break
            index += 1
    return result

def Bidirectional_MM(user_dict,sentence):
    '''
    :param user_dict:
    :param sentence:
    :return: result of bidirectional max match, print the result
    '''
    FMM_result = Forward_MM(user_dict, sentence)
    BMM_result = Backward_MM(user_dict, sentence)
    fmm_max_len = max([len(item) for item in FMM_result])
    bmm_max_len = max([len(item) for item in BMM_result])
    fmm_num_single = np.sum([len(item)==1 for item in FMM_result])
    bmm_num_single = np.sum([len(item)==1 for item in BMM_result])
    # Rules: 比较fmm和bmm的分词结果，取所得分词中单个词最长的优先，若两者相同，则取单个词最少的
    if(fmm_max_len>bmm_max_len):
        print('\n双向最大匹配结果：')
        for item in FMM_result:
            print(item, end='/')
    elif(fmm_max_len<bmm_max_len):
        print('\n双向最大匹配结果：')
        for item in BMM_result[::-1]:
            print(item, end='/')
    elif(fmm_max_len==bmm_max_len):
        if(fmm_num_single>bmm_num_single):
            print('\n双向最大匹配结果：')
            for item in FMM_result:
                print(item, end='/')
        else:
            print('\n双向最大匹配结果：')
            for item in BMM_result[::-1]:
                print(item, end='/')

def main():
    user_dict = ['我们', '在', '在野', '生动', '野生', '动物园', '野生动物园', '物', '园', '玩']
    sentence = '我们在野生动物园玩'
    #Forward_MM(user_dict, sentence)
    #Backward_MM(user_dict, sentence)
    Bidirectional_MM(user_dict, sentence)

if __name__ == '__main__':
    main()
