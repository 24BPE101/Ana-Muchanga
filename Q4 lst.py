lst = ['madam','python',"malayalam",12321]
lst = ("Palindromes in the list are :-",list(filter(lambda x:str(x)==str(x)[::-1],lst)))
