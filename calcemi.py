import loancalculator

repayments1={}
loanamount=input('input a loan amount')
loaninterest=input('input a rate of interest')
term=input('input a term in month')
repayments1=loancalculator.loancal(int(loanamount),int(loaninterest),int(term))
print (repayments1)
