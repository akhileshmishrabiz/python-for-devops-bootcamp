import subprocess

result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
out= result.stdout

print("Raw Output:", out)
print()
data_list = out.strip().split('\n')[1:]

for line in data_list:
    parts = line.split()
    permissions = parts[0]
    links = parts[1]
    owner = parts[2]
    group = parts[3]
    size = parts[4]
    month = parts[5]
    day = parts[6]
    time_or_year = parts[7]
    filename = ' '.join(parts[8:])
    
    print(f"Filename: {filename}, Size: {size} bytes, Permissions: {permissions}")


# string = " asdf: gfds: 1234 "
# empty_list = []

# for item in string.strip().split(':'):
#     empty_list.append(item.strip())
# print(empty_list)