def powfunction (x:float,i):
    if i==0:
        return 1
    else:
         answer=x
         for z in range(1,i):
             answer = answer*x
    return answer



def exponent (x:float):
     answer=1
     for i in  range(1,100):
         answer=answer+(powfunction(x,i)) /assembly( i)
     return answer



def assembly (i):
    if i<1:
        return 1
    else:
        answer=i
        for z in range(1,i):
            answer = answer*z
        return answer 
    


def absolute(x:float):
    if x>0 :
        return x
    else:
        return x*-1
    
def even (x:float):
    if x%2!=0:
        return True
    else:
        return False
    
    
def Ln(x:float):
    if x<=0:
        return 0 
    answer=x-1
    var=0
    while absolute(var-answer)>0.001:
        var=answer
        answer=answer+2*((x-exponent(answer))/ (x+exponent(answer)))
    return answer


def XtimesY (x:float,y:float):
    if x<0:
        return 0.0
    if y==0:
        return 1.0
    elif y==1:
        return float(x)
    else:
        answer=exponent(y*Ln(x))
        return answer


def sqrt (x:float,y:float):
    if y==0:
        return 0.0
    if y<0 and even(x):
        answer=XtimesY(-y, 1/x)
        return -1*answer
    answer=XtimesY(y, 1/x)
    return answer



def calculate(x:float):
    answer=exponent(x)*XtimesY(x,-1)*XtimesY(7,x)*sqrt(x,x)
    return float('%0.6f' % answer)