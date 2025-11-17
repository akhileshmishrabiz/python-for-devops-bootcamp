# get the lambda data json and store in a file
import boto3
import json
# print(response)

# # old way - open, read, then close
# f = open('readme.txt', 'r')
# content = f.read()
# print(content)
# f.close()


# with open('readme.txt', 'r') as f:
#     content = f.read()

# print(content)
# print(type(content))  # str

# with open('readme.txt', 'r') as f:
#     lines = f.readlines()
# print(lines)

# for i in lines:
#     # print(i)
#     print(i.strip('\n'))  # remove extra new line characters

# with open('newfile.txt', 'w') as f:
#     for l in lines:
#         fixed_l = '##' + l.strip('\n') + ' **' 
#         # print(fixed_l)
#         f.write(fixed_l + '\n')

client = boto3.client('lambda')

response = client.get_function(FunctionName='iam-key-rotation')


# json.loads()  # str to dict
# json.dumps()  # dict to str
# with open('lambda-function.json', 'w') as file:
#     file.write(json.dumps(response, indent=4))


with open("lambda-function.json", 'r') as f:
    data = f.read()  # file to dict
    # print(type(data))  # str
    json_data = json.loads(data)
    # print(type(json_data))  # dict
    print(json_data['Configuration']['FunctionName'])
    print(json_data['Configuration']['Runtime'])
