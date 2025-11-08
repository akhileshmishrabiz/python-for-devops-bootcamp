# os is a built in module in python to interact with the operating system
import os

# print("current working directory is:", os.getcwd())
# print( os.listdir('/Users/akhilesh/projects/livingdevops-platform'))
# os.mkdir('cool_project')
# command = os.system('rm *.txt')
# print(os.WEXITSTATUS(command))

# def count_dirs_files(path):
#     dir_count = 0
#     file_count = 0
#     for root, dirs, files in os.walk(path):
#         dir_count += len(dirs)
#         file_count += len(files)
#     return dir_count, file_count

# path_to_check = '/Users/akhilesh/projects/python-for-devops'
# dirs, files = count_dirs_files(path_to_check)
# print(f"Directories: {dirs}, Files: {files}")

# def get_large_files(path, min_size_kb=10):
#     large_files = []
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             file_path = os.path.join(root, file)
#             try:
#                 if os.path.getsize(file_path) > min_size_kb * 1044:
#                     large_files.append(file_path)
#             except Exception:
#                 pass
#     return large_files

# path_to_check = '/Users/akhilesh/projects/livingdevops-platform'
# large_files = get_large_files(path_to_check)
# print(f"Files larger than 10KB: {len(large_files)}")
# for f in large_files:
#     print(f)

# path = '/Users/akhilesh/projects/python-for-devops-bootcamp/'

# for root, dirs, files in os.walk(path):
#     print("Root:", root)
#     print("Directories:", dirs)
#     print("Files:", files)
#     print("-----")

# size = os.path.getsize("/Users/akhilesh/projects/python-for-devops-bootcamp/class1/test.py")
# print("File size in bytes:", size)

# output = os.system('ls')
# print(type(output))

# print(output)



print(os.getenv('my_life_stor' , 'env var not found'))