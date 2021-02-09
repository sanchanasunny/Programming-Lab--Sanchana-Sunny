#Sort dictionary in ascending and descending order.

y={'carl':40,'alan':2,'bob':1,'danny':3} 
                                       
lst=list(y.items()) 
print('original is :\n',lst)  

lst.sort()
print('Ascending order is :\n',lst)  

lst=list(y.items())
lst.sort(reverse=True)
print('Descending order is : \n',lst)

dict=dict(lst)
print("Dictionary :\n",dict) 