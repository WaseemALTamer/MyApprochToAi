from numba import jit, cuda
import numpy as np
from timeit import default_timer as timer   
import main
import time

def func():
    main.timer = time.time()                      
    main.function()
 
@jit(target_backend='cuda')                         
def func2():
    main.timer = time.time()
    main.function()

if __name__=="__main__":
 
     
    start = timer()
    func2()
    print("with GPU:", timer()-start)