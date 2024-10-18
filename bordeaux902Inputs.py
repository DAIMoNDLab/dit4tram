# -*- coding: utf-8 -*-
"""
Test variables manually inputted
"""
import numpy as np
import pandas as pd
import random
import pickle

class Inputs:

    
    def __init__(self):
        
        self.junction_pos = (68.55, 57.76) # Example - (353.12, -34.55)      
        self.sumo_m_map = {0:  '000100000000000000000000000000000000',
                           1:  '000011000000000000000000000000000000',
                           2:  '000000100000000000000000000000000000',
                           3:  '000000000010000000000000000000000000',
                           4:  '000000000001100000000000000000000000',
                           5:  '000000000000010000000000000000000000',
                           6:  '000000000000000001000000000000000000',
                           7:  '000000000000000000110000000000000000',
                           8:  '000000000000000000001100000000000000',
                           9:  '000000000000000000000000010000000000',
                           10: '000000000000000000000000001100000000',
                           11: '000000000000000000000000000011000000',
                           12: '201000020100002010000020100000000000',
                           13: '010000000000000000000000000000000000',
                           14: '000000001000000000000000000000000000',
                           15: '000000000000000100000000000000000000',
                           16: '000000000000000000000001000000000000',
                           17: '000000000000000000000000000000100000',
                           18: '000000000000000000000000000000010000',
                           19: '000000000000000000000000000000001000',
                           20: '000000000000000000000000000000000100',
                           21: '000000000000000000000000000000000010',
                           22: '000000000000000000000000000000000001',
                           } # Bikes phase; 2 is 'right on red' for bikes
                                                            # ^^^^^^ crossing movements
        
        self.m_detector_list = ['e6_01', 'e6_02', 'e6_03', 'e2_04', 'e2_05', 'e10_06', # detectors placed in lane for each movement
                                'e4_07', 'e4_08', 'e4_09', 'e0_10', 'e0_11', 'e8_12']  # ID: d_m, where d is real detector ID, m is movement
        self.b_detector_list = ['e16', 'e22', 'e18', 'e20'] # bike queue detectors (for bike movement 13)
        self.q_detector_list = ['e7','e5','e12','e0'] # car queue detectors (can repeat from list above, but count differently in logic)
        self.q_serv_detector_list = ['e7','e5','e12']
        self.q_serv_movementIndices = {'e7':1,'e24':2,'e5':4,'e12':5,'e4_07':6,'e4_08':7,'e0_10':9,'e0_11':10} # movement indices for car queue detectors
        self.q_speed_threshold = 0.1/3.6 # speed threshold for car queue detectors

        self._M = int(len(self.sumo_m_map))
        
        self.carW=1
        self.cbW=10
        self.hovW=0


        self.prrCyclist = 15 * 1 * 25 / 3.6  #set to the distance traversed with speed 25km/h in nPred time steps
       
        self.nHOVs = 20
        self.v_f = 45
        self.prrHOV = 15 * 1 * 45 / 3.6  #set to the distance traversed with speed 45km/h in nPred time steps

        self.conflictMatrix=np.zeros((self._M,self._M))
        self.conflictMatrix[0,1]=4
        self.conflictMatrix[0,4]=3
        self.conflictMatrix[0,6]=1
        self.conflictMatrix[0,10]=2
        self.conflictMatrix[0,16]=0
        self.conflictMatrix[0,18]=4
        self.conflictMatrix[0,20]=2
        self.conflictMatrix[0,22]=0
        self.conflictMatrix[1,0]=6
        self.conflictMatrix[1,12]=6
        self.conflictMatrix[2,3]=1
        self.conflictMatrix[2,4]=2
        self.conflictMatrix[2,6]=3
        self.conflictMatrix[2,8]=3
        self.conflictMatrix[2,16]=4
        self.conflictMatrix[2,18]=0
        self.conflictMatrix[2,20]=0
        self.conflictMatrix[2,22]=2
        self.conflictMatrix[3,2]=12
        self.conflictMatrix[3,10]=12
        self.conflictMatrix[4,0]=2
        self.conflictMatrix[4,2]=4
        self.conflictMatrix[4,5]=1
        self.conflictMatrix[4,6]=4
        self.conflictMatrix[4,8]=4
        self.conflictMatrix[4,9]=4
        self.conflictMatrix[4,10]=2
        self.conflictMatrix[4,12]=2
        self.conflictMatrix[4,14]=4
        self.conflictMatrix[4,16]=4
        self.conflictMatrix[4,18]=2
        self.conflictMatrix[4,20]=2
        self.conflictMatrix[4,22]=4
        self.conflictMatrix[5,4]=10
        self.conflictMatrix[6,0]=4
        self.conflictMatrix[6,2]=2
        self.conflictMatrix[6,4]=4
        self.conflictMatrix[6,7]=1
        self.conflictMatrix[6,8]=3
        self.conflictMatrix[6,10]=3
        self.conflictMatrix[6,11]=4
        self.conflictMatrix[6,12]=4
        self.conflictMatrix[6,14]=2
        self.conflictMatrix[6,16]=2
        self.conflictMatrix[6,18]=4
        self.conflictMatrix[6,20]=4
        self.conflictMatrix[6,22]=1
        self.conflictMatrix[7,6]=8
        self.conflictMatrix[8,2]=4
        self.conflictMatrix[8,4]=3
        self.conflictMatrix[8,6]=2
        self.conflictMatrix[8,9]=4
        self.conflictMatrix[9,4]=7
        self.conflictMatrix[9,8]=7
        self.conflictMatrix[9,14]=4
        self.conflictMatrix[9,16]=1
        self.conflictMatrix[9,18]=2
        self.conflictMatrix[9,20]=1
        self.conflictMatrix[9,22]=4
        self.conflictMatrix[10,0]=4
        self.conflictMatrix[10,3]=1
        self.conflictMatrix[10,4]=2
        self.conflictMatrix[10,6]=3
        self.conflictMatrix[10,11]=5
        self.conflictMatrix[10,12]=4
        self.conflictMatrix[10,16]=1
        self.conflictMatrix[10,18]=1
        self.conflictMatrix[10,20]=4
        self.conflictMatrix[10,22]=1
        self.conflictMatrix[11,6]=7
        self.conflictMatrix[11,10]=6
        self.conflictMatrix[12,1]=4
        self.conflictMatrix[12,4]=3
        self.conflictMatrix[12,6]=1
        self.conflictMatrix[12,10]=2
        self.conflictMatrix[12,16]=0
        self.conflictMatrix[12,18]=4
        self.conflictMatrix[12,20]=2
        self.conflictMatrix[12,22]=0
        self.conflictMatrix[14,4]=2
        self.conflictMatrix[14,6]=3
        self.conflictMatrix[14,8]=3
        self.conflictMatrix[14,16]=4
        self.conflictMatrix[14,18]=0
        self.conflictMatrix[14,20]=0
        self.conflictMatrix[14,22]=2
        self.conflictMatrix[16,0]=6
        self.conflictMatrix[16,2]=6
        self.conflictMatrix[16,4]=7
        self.conflictMatrix[16,6]=6
        self.conflictMatrix[16,8]=4
        self.conflictMatrix[16,10]=4
        self.conflictMatrix[16,12]=5
        self.conflictMatrix[16,14]=6
        self.conflictMatrix[18,0]=6
        self.conflictMatrix[18,2]=4
        self.conflictMatrix[18,4]=4
        self.conflictMatrix[18,6]=7
        self.conflictMatrix[18,8]=4
        self.conflictMatrix[18,10]=6
        self.conflictMatrix[18,12]=6
        self.conflictMatrix[18,14]=4
        self.conflictMatrix[20,0]=3
        self.conflictMatrix[20,2]=8
        self.conflictMatrix[20,4]=5
        self.conflictMatrix[20,6]=5
        self.conflictMatrix[20,8]=5
        self.conflictMatrix[20,10]=5
        self.conflictMatrix[20,12]=3
        self.conflictMatrix[20,14]=8
        self.conflictMatrix[22,0]=8
        self.conflictMatrix[22,2]=4
        self.conflictMatrix[22,4]=6
        self.conflictMatrix[22,6]=5
        self.conflictMatrix[22,8]=5
        self.conflictMatrix[22,10]=5
        self.conflictMatrix[22,12]=8
        self.conflictMatrix[22,14]=4


        
                

        
    def __call__(self, **kwargs):
        """
        :param kwargs: different inputs for the attributes than the default ones
        :return: updates the attributes with given kwargs.
        raises AttributeError if keyword is not found in the attributes.
        """
        for key, val in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, val)
            else:
                raise AttributeError(f'Class {self.__class__.__name__} has no attribute {key}. \n Check again')

        if 'mLenDict' in kwargs and len(self.mLenDict) != self._M:
            self._M = int(len(self.mLenDict))
            dependentAttrs = {'capDict', 'tgMin', 'tgMax', 'ty', 'tau', 'inColor', 'inTime', 'inTimeAg', 'inW'}
            others = dependentAttrs - set(kwargs)
            if others:
                raise AttributeError(
                    f'The number of movements has changed. The following attributes also need to be updated '
                    f'accordingly: \n {others}')

inputs = Inputs()

if __name__ == '__main__':
    try:
        inputs(mLenDict={'02': 40, '04': 20, '06': 50, '11': 40, '12': 50, '22': 40, '33': 40})
    except AttributeError as error:
        print('\nError captured: \n', error, '\n')
    try:
        inputs(foo='bar')
    except AttributeError as error:
        print('\nError captured: \n', error)
