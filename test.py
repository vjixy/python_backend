import webcolors
import numpy as np
from sklearn.metrics import mean_squared_error
rms_lst = []
c = [
      121,
      101,
      76
    ]
hex_values = []
nb_values = []
for img_clr, img_hex in webcolors.CSS3_NAMES_TO_HEX.items():
    hex_values.append(img_hex)
    nb_values.append(int(img_hex[1:],16))

print(hex_values)
print(nb_values)
# def find_nearest(array, value):
#     array = np.asarray(array)
#     idx = (np.abs(array - value)).argmin()
#     return hex_values[idx]
hex_color="#79654c"
hex_nb = int(hex_color[1:],16)
print(hex_nb)
# mArray = array([4,1,88,44,3])
print(min([i for i in nb_values if hex_nb<i]))
first = hex_values[nb_values.index(min([i for i in nb_values if hex_nb<i]))]
print(webcolors.hex_to_name(first))
print(first)

# print(nb_values[nb_values < hex_nb].max())
# print(find_nearest(img_hex,int(hex_color[1:],16)))
# closest_color = rms_lst[rms_lst.index(min(rms_lst))]
# print("#############3")
# print(closest_color)
# print("#############3")


# # webcolors.rgb_percent_to_name
# print(webcolors.rgb_percent_to_name(closest_color))



# def _values_to_str(values):
#     str_value = ""

#     for value in values:
#         try:
#             str_value+="'"+value+"',"
#         except:
#             str_value+=value.__str__()+","
        
#     return str_value[:-1]

# print(_values_to_str(["name",1,"batata"]))