#import numpy
import numpy as np

#definition of function
def calculate(a_ele):
    
    #create a 3*3 matrix
    m_ele = a_ele.reshape(3,3)
    
    #calculate the mean, variance, std, max, min and sum of the matrix
    l_mean = [np.mean(m_ele, axis=0).tolist(), np.mean(m_ele, axis=1).tolist(),np.mean(m_ele).tolist()]
    l_var = [np.var(m_ele, axis=0).tolist(), np.var(m_ele, axis=1).tolist(),np.var(m_ele).tolist()]
    l_std = [np.std(m_ele, axis=0).tolist(), np.std(m_ele, axis=1).tolist(),np.std(m_ele).tolist()]
    l_max = [np.max(m_ele, axis=0).tolist(), np.max(m_ele, axis=1).tolist(),np.max(m_ele).tolist()]
    l_min = [np.min(m_ele, axis=0).tolist(), np.min(m_ele, axis=1).tolist(),np.min(m_ele).tolist()]
    l_sum = [np.sum(m_ele, axis=0).tolist(), np.sum(m_ele, axis=1).tolist(),np.sum(m_ele).tolist()]
    
    #load dictionary with above values
    mean_var_std = {
        'mean': l_mean,
        'variance': l_var,
        'standard deviation': l_std,
        'max': l_max,
        'min': l_min,
        'sum': l_sum
    }   
    
    #return results
    return mean_var_std

if __name__ == "__main__":
    print("Please run the file: main.py")