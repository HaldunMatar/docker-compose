import mysql.connector
import sys
sys.path.append('../../OBJECT_DETECTION')

from setting import *

global ipDBsever 
ipDBsever='100.103.105.34'
# if not local :
#     #ipDBsever='100.98.164.136'
#     ipDBsever='100.74.149.25'
#     ipDBsever='100.98.164.136'
    

#     ipDBsever='100.103.105.34'
    
#     #ipDBsever='localhost' 
#     ipDBsever='100.103.105.34'
#     ipDBsever='100.74.149.25' 
#     ipDBsever='100.103.105.34' 
#     ipDBsever='100.94.180.13'   

try:
    
    print(' new strat ')
except Exception :
    print(Exception)

def get_connection():
    
    #host='172.17.0.2'
    host='host.docker.internal'
    database='MADB'
    password='Password123$'
    user='dba' 
   
    host_name= get_host_name()
    
    # if host_name=='Halduns-MacBook-Pro.local':
    # if host_name=='Halduns-MacBook-Pro.local':
    if(1==1)  :  
        print('get_connection test' , ' hostname ',host_name )
        if(not is_docker):
            host='127.0.0.1'
        database='MADB'
        password='12345678'
        user='root'                                  
    elif host_name=='inas':
        if(not is_docker):
            host='127.0.0.1'
        database='madb'
        password=''
        user='root'
 
    elif host_name=='mainsight-desktop':
        if(not is_docker):
            host='100.103.105.34'
        database='madb'
        password='Password123$'
        user='dba'

    elif host_name=='anas-desktop':  
        if(not is_docker):          
            host='100.74.149.25'
        database='MADB'
        password='Password123$'
        user='dba'

    elif host_name=='gama':
        if(not is_docker):        
            host='100.66.253.61'
        database='madb'
        password='Password123$'
        user='dba'
                                                 
 
    elif host_name=='delta':
        if(not is_docker):         
            host='100.69.135.43'
        host='100.66.253.61'
        database='madb'
        password='Password123$'
        user='dba'    
    
    
    #print('getConnection ', host ,database ,password ,user  )                                  
               
    return mysql.connector.connect(
        
                host=host,
                database=database,
                password=password,
                user=user                               
                )          







     
#36
# connection.get_connection() = mysql.connector.connect(
#     host=ipDBsever,
#     database='MADB',
#     password='123',
#     user='root'                                       
#     )

# local
# connectionDB = mysql.connector.connect(
#     #host='100.74.149.25',
#     host=ipDBsever,

#                 #     database='MADB',
#                 # password='Password123$',
#                 # user='dba'   
#     database='MADB',
#     password='12345678',
#     user='root'                                       
#     )

# connection.get_connection() = mysql.connector.connect(
#                     host='localhost',
#                     user='root',
#                     password='',
#                     database='test'
# beta (test)                )
# connection.get_connection() = mysql.connector.connect(
#     host=ipDBsever,
#     database='MADB',
#     password='Password123$',
#     user='dba'                                      
#     )

#alpha                
# connection.get_connection() = mysql.connector.connect(
#     host=ipDBsever,
#     database='MADB',
#     password='Password123$',
#     user='dba'                                      
#     )