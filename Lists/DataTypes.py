def manipulate_data(data_type, data):
    if data_type == "int":
        data = int(data) * 2
        return data
    elif data_type == "real":
        data = float(data) * 1.5
        return '{:.2f}'.format(data)
    elif data_type == "string":
        data = '$' + data + '$'
        return data


is_type = input()
par = input()
print(manipulate_data(is_type, par))
