import mysql.connector

def sqlconnect(UserName,PasswordText,HostName,DatabaseName,SqlText):
    cnx = mysql.connector.connect(user=UserName, password=PasswordText, host=HostName, database=DatabaseName)
    cur = cnx.cursor()
    cur.execute(SqlText)
    returndata = cur.fetchall()
    cnx.close()
    return returndata


def TableSize(DataSet):
    Number_Rows=len(DataSet)
    Number_Columns=len(list(DataSet[0]))
    return(Number_Rows,Number_Columns)




sql = 'select * from monthly_expense'
data = sqlconnect('debi','debi','127.0.0.1','debi_financials',sql)
mylist=[[1,2,3],('a','b','c')]

print('Number of rows:%d and Number of columns:%d' % TableSize(data))





