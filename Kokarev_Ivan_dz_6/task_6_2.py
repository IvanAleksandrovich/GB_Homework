with open('nginx_logs.txt', 'r', encoding="utf-8") as file:
    result = []
    for line in file:
        line = line.split()
        remote_addr = line[0]
        result.append(remote_addr)

print(max(set(result), key=result.count))
