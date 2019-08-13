# coding=gbk
import copy
'''
Ѱ��·��˼·��ÿ�α����ֵ䣬·��path�ͻ����[key]�������б��ͻ����[posi]��
Ȼ������������������ģ��Ͱ�·��path��ӵ���list��Ȼ�󷵻�
'''
class Find_path():
    def __init__(self,target):
        self.target=target

    def find_the_value(self,target,value,path='',path_list=None):
        '''��ȫƥ�䣬ÿ����һ��(list��dict)�����¼path���������һ���ҵ�ǰtarget����Ҫ�ҵ�Ŀ�꣬�ŰѶ�Ӧ��path��¼����
        :param target: ��������Ŀ��
        :param value: Ҫ�����Ĺؼ���
        :param path: ��ǰ���ڵ�·��
        :param path_list: �������path���б�
        �жϵ�ǰtarget���ͣ����������ֵ䣬ѭ�����ݣ�ÿ����ֵ����¼��·��path��Ȼ���Ե�ǰֵvΪ�ж�target����������������˵�path�ж�
                             ���������б�ѭ�����ݣ�ÿ��Ԫ�ض���¼��·��path��Ȼ���Ե�ǰԪ��Ϊ�ж�target����������������˵�path�ж�
                             ��������str����int����ô���жϵ�ǰtarget�Ƿ����Ҫ������value������ǣ��ǾͰ�·��path�Ž�list����'''
        if isinstance(target, dict):
            for k, v in target.items():
                path1 = copy.deepcopy(path)
                path1=path1+str([k])
                self.find_the_value(v, value, path1, path_list)

        elif isinstance(target, (list, tuple)):  # �ж��������б�
            for i in target:
                path1 = copy.deepcopy(path)
                posi = target.index(i)
                path1 = path1+'[%s]' % posi
                self.find_the_value(i, value, path1, path_list)

        elif isinstance(target, (str, int)) :
            if  str(value) ==str(target):   #������ȫ��ͬ
                path_list.append(path)


    def find_in_value(self,target,value,path='',path_list=None):
        '''����ƥ�䣬���ݸ�����һ����ֻ������ж�ʱ��ͬ'''
        if isinstance(target, dict):
            for k, v in target.items():
                path1 = copy.deepcopy(path)
                path1=path1+str([k])
                self.find_in_value(v, value, path1, path_list)

        elif isinstance(target, (list, tuple)):  # �ж��������б�
            for i in target:
                path1 = copy.deepcopy(path)
                posi = target.index(i)
                path1 = path1+'[%s]' % posi
                self.find_in_value(i, value, path1, path_list)

        elif isinstance(target, (str, int)) :
            if  str(value) in str(target):   #
                path_list.append(path)

    def find_the_key(self,target,key,path='',path_list=None):
        '''����key��ÿ����һ��(list��dict)�����¼path�����ֵ�ʱ������ǰ��k����Ҫ�ҵ�key���ǾͰѶ�Ӧ��path��¼����
                :param target: ��������Ŀ��
                :param key: Ҫ�ѵļ�
                :param path: ��ǰ���ڵ�·��
                :param path_list: �������path���б�
                �жϵ�ǰtarget���ͣ����������ֵ䣬ѭ�����ݣ�ÿ����ֵ����¼��·��path���жϵ�ǰk�Ƿ�Ҫ���ҵģ�~~~�ǣ��ǾͰ�·��path�Ž�list����
                                                                                                 ~~~���ǣ��Ե�ǰֵvΪ�ж�target����������������˵�path�ж�
                                  ���������б�ѭ�����ݣ�ÿ��Ԫ�ض���¼��·��path��Ȼ���Ե�ǰԪ��Ϊ�ж�target����������������˵�path�ж�
                                     '''
        if isinstance(target, dict):
            for k, v in target.items():
                path1 = copy.deepcopy(path)
                path1=path1+str([k])
                if str(key) == str(k):
                    path_list.append(path1)
                else:
                    self.find_the_key(v, key, path1, path_list)

        elif isinstance(target, (list, tuple)):  # �ж��������б�
            for i in target:
                path1 = copy.deepcopy(path)
                posi = target.index(i)
                path1 = path1+'[%s]' % posi
                self.find_the_key(i, key, path1, path_list)

#====================================================================================

    def in_value_path(self,value):
        '''����ƥ��value'''
        path_list=[]
        self.find_in_value(self.target, value,path_list=path_list)
        return path_list

    def the_value_path(self,value):
        '''��ȫƥ��value'''
        path_list=[]
        self.find_the_value(self.target, value,path_list=path_list)
        return path_list

    def the_key_path(self,value):
        '''ֻ����key'''
        path_list = []
        self.find_the_key( self.target, value,path_list=path_list)
        return path_list