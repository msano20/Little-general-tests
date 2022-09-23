# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 17:54:56 2022

-testClass = setUp Class
@author: misum
"""

class testClass():
    def __init__(self,n_dict,key,value):
        self.n_dict = n_dict
        self.key = key
        self.value = value
        self.test_list = []
        self.test_dict = {}
        self.test_dict2 = {}
        self.dict_list = [self.test_dict,self.test_dict2]
    
    
    def dictIteration(self,n_dict,key,value):
        print("Starting dictIteration...")
        print('n_dict: ',n_dict)
        #for dict_obj in self.dict_list:
        dict_str = str('self.'+n_dict)    
        print(dict_str)
        if dict_str in str(self.dict_list):    
            print(n_dict)
        

    

ideal_dict = 'test_dict2'



#testInstance = testClass('u_dict','test_key','test_val')
testInstance = testClass('test_dict','test_key','test_val')


testInstance.dictIteration('test_dict','test_key','test_val')