import numpy as np

def present_as_matrix(x):
    for el in x:
        print (el)

import itertools
def all_combinations(x):
    ret=[]
    for i in range(1,len(x)):
        ret+=list(itertools.combinations(base,i))
    return ret

def fact_in_base(a,B, n):
    rel=[]
    
    base=B[1:]
    org_a=a
    for el in B:
        rel.append(0)
        
    for j in range(0,len(base)):
        while(a % base[j]==0):
            a=a/base[j]
            rel[j+1]=rel[1+j]+1

            if(a==1):
                return rel
    rel=[]
    for el in B:
        rel.append(0)
    rel[0]=1
    a=(org_a*-1) % n
    
    for j in range(0,len(base)):
        while(a % base[j]==0):
            a=a/base[j]
            rel[j+1]=rel[1+j]+1

            if(a==1):
                return rel
    
    return None

def is_lin_indep(matx,row):
    A=np.row_stack([matx,row])
    _, s, _ =np.linalg.svd(A)
    for el in s:
        if el<10**-10:
            return False
    return True

def relations_calc(a,n,B):
    relations=[]
    relation=[]
    matrix=[]
    e_matrix=[]
    rez=[]
        
    i=0
    while len(relations)<len(B):
        i+=1
        pow_a_i=pow(a,i,n)
        relation=fact_in_base(pow_a_i,B,n)
        if(relation!=None):
            if(matrix==[]):
                matrix.append(relation[:])
                rez.append(i)
                relation.append(i)
                relations.append(relation)
            else:
                if(is_lin_indep(matrix,relation)):
                    matrix.append(relation[:])
                    rez.append(i)
                    relation.append(i)
                    relations.append(relation)
        
    return relations, matrix, rez



def print_as_eq(m,b):
    j=0
    for row in m:
        ch=ord('a')
        string=""
        for i in range(0,len(row)):
            string+="+"+str(row[i])+chr(ch+i)
        string+="="+str(b[j])+"\n"
        j+=1
        print (string)

def end_calc_log(fact,rez,rand,n):
    val=0
    for i in range(0,len(fact)):
        val= (val + fact[i]*rez[i])
    val=(val-rand)%n
    return val

def calc_log(beta,res,alfa,prime,base):
    import random
    
    fac=None
    
    while fac==None:
        rand_int=random.randint(0,1235789)
        fac=fact_in_base(beta*pow(alfa,rand_int,prime),base,prime)
    return end_calc_log(fac,res,rand_int,prime-1)

def mul_array(x):
    ret=1
    for el in x:
       ret*=el
    return ret

def mul_known_logs(x,known_logs):
    ret=0
    print(x)
    for e in x:
        ret+=known_logs[str(e)]
    return ret

def calc_log_with_known_base_logs(beta,res,alfa,prime,base,known_logs):
    fac=None
    no=None
    for el in all_combinations(base):
        fac=fact_in_base(beta*mul_array(el),base,prime)
        if(fac!=None):
            no=el
            break
    if no==None:
        return None
    return end_calc_log(fac,res,mul_known_logs(no,known_logs),prime-1)




if __name__=="__main__":

    base=[-1,2,3,5,7,11,13,17,19,23]
    prime=1235789
    alfa=89
    
    _,m,r=relations_calc(alfa,prime,base)

    print_as_eq(m,r)

    # res pridobljen s pomočjo: https://www.dcode.fr/modular-equation-solver (modulo p-1)
    # c1 sem nastavil na 1
    res=[617894,
        742467,
        412095,
        446710,
        1730346,
        1589954,
        1290570,
        675722,
        1718773,
        577037
        ]

    logs_base={}
    for el in base:
        logs_base[str(el)]=calc_log(el,res,alfa,prime,base)
    print(logs_base)
    '''
    back_base=[]
    for e in logs_base:
        back_base.append(pow(alfa,e,prime))
    print(back_base)
    '''
    print(calc_log_with_known_base_logs(354333,res,alfa,prime,base,logs_base))
    print(calc_log_with_known_base_logs(134864,res,alfa,prime,base,logs_base))
    print(calc_log_with_known_base_logs(1087339,res,alfa,prime,base,logs_base))

