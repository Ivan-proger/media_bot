import os

class media():
    my_dir = os.getcwd()
    j0in = os.path.join(my_dir, 'media')
    files = os.listdir(path=j0in)

latest_video = files[0]


print(files)
print(files[0]) 