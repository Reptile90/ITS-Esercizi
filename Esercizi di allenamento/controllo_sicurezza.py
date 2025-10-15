def check_security_alarm(s1,s2,s3):
    if s1 == True and s2 == True or s3 == True:
        return "Allarme attivato"
    else:
        return "Nessun allarme"
    
    
    
    
print(check_security_alarm(True,False,False))
print(check_security_alarm(True,True,False))
print(check_security_alarm(True,False,True))