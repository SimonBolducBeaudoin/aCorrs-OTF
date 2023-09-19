#!/bin/env/python
#! -*- coding: utf-8 -*-

import numpy as _np
def extract_S2_from_accor(acorr):
    """
        Converst an array of acorr object
        to an array of S2
    """
    shape    = acorr.shape
    shape   += (acorr.flat[0].res.size,)
    S2      = _np.full(shape,_np.nan)
    S2.shape = (int(_np.prod(shape[:-1])),shape[-1]) # same as flatten() but not the last dimension
    for i,a in enumerate(acorr.flat) :
        S2[i,...] = a.res
    S2.shape = shape # reshape the array 
    return S2
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    