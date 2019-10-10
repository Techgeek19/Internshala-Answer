#Using dunders 
def func(A1,A2,Target_no): 
     print ([(Target_no-i,i) for i in A2 if (Target_no-i) in A1]) 
  
if __name__ == "__main__": 
    Target_no = 10
    A1 = [2, 4, 8, 3] 
    A2 = [1, 2, 6, 7]   
    func(A1,A2,Target_no) 
