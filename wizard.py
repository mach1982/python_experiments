def wizard_name(fname,lname,mname=''):
    if mname:
        full_name =fname+' '+ mname +' '+lname
    elif lname:
        full_name  =fname+' '+lname
    else:
        full_name.title()
    return(full_name)
	
	
w=wizard_name("Harry","Potter","James")
print(w)
