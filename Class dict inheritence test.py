# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 17:54:56 2022

@author: misum
"""

class testClass():
    def __init__(self):

        self.test_list = []
        self.test_dict = {}
        self.test_dict2 = {}
        self.test_dict3 = {}
        self.dict_list = [self.test_dict,self.test_dict2,self.test_dict3]
        self.translation_dict = {'test_dict':self.test_dict,'test_dict2':self.test_dict2,'test_dict3':self.test_dict3}
    
    
    def dictIteration(self,n_dict,key,value):
        self.n_dict = n_dict
        self.key = key
        self.value = value
        print("Starting dict Iteration...")
        #print('n_dict: ',n_dict)
        dict_str = str(n_dict)    
        #print('dict_str:',dict_str)
        for k, v in self.translation_dict.items():
            if dict_str == k:    
                print(k)
                print(v)
                v.update({self.key:self.value})
        #print(self.translation_dict)


#testInstance = testClass('u_dict','test_key','test_val')
testInstance = testClass()


testInstance.dictIteration('test_dict3','test_key','test_val')

print(testInstance.translation_dict)