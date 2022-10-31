# MERUBAH DATA KE DATA LAIN

# INTEGER KE DATA LAIN
print("=====INTEGER=====")
data_int = 10

data_int = int(data_int)
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika int = 0
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_bool, ",type =", type(data_bool))

# FLOAT KE DATA LAIN
print("=====FLOAT=====")
data_float = 10.5

data_float = float(data_float)
data_int = int(data_float) # akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika sloat = 0
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_bool, ",type =", type(data_bool))

# BOOLEAN KE DATA LAIN
print("=====BOOLEAN=====")
data_bool = True

data_bool = bool(data_bool)
data_float = float(data_bool)
data_int = int(data_bool)
data_str = str(data_bool)
print("data = ", data_bool, ",type =", type(data_bool))
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_str, ",type =", type(data_str))

# STRING KE DATA LAIN
print("=====STRING=====")
data_str = "valen"

data_str = str(data_str)
data_float = float(data_str) # str tdk dapat dirubah ke float (str harus angka)
data_int = int(data_str) # str tdk dapat dirubah ke int (str harus angka)
data_bool = bool(data_str)  # false jika string kosong
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_bool, ",type =", type(data_bool))