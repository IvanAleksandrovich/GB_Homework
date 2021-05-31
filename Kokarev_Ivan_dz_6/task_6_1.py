with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    result = []
    for line in file:
        line = line.split()
        remote_addr = line[0]
        request_type = line[5][1:]
        requested_resource = line[6]
        tuple_result = (remote_addr, request_type, requested_resource)
        result.append(tuple_result)

print(result)
