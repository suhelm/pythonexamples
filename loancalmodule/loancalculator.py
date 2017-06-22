import datetime
import calendar

def add_months(sourcedate,months):
       month = sourcedate.month - 1 + months
       year = int(sourcedate.year + month / 12 )
       month = month % 12 + 1
       day = min(sourcedate.day,calendar.monthrange(year,month)[1])
       return datetime.date(year,month,day)
    
def loancal(loanamt:int,roi:int,term:int):
    repayments={}
    print('welcome to loan calculator')
    print(datetime.date.today())
    emiamount=loanamt*roi*term/100
    print(emiamount)
    
    for i in range(1,term+1):
        nextmothdate=add_months(datetime.date.today(),i)
        ##print(i) 
        ##print(nextmothdate)
        repayments[i]={'Emi No':i,'Emi Date':nextmothdate}
    print (repayments)
    return repayments
            


#loancal(1000,12,24)



