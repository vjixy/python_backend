def _values_to_str(values):
    str_value = ""

    for value in values:
        try:
            str_value+="'"+value+"',"
        except:
            str_value+=value.__str__()+","
        
    return str_value[:-1]

print(_values_to_str(["name",1,"batata"]))