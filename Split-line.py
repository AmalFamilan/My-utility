# para = """The poet sees different sceneries while travelling by train. 
# He sees bridges, houses, ditches and hedges. Meadows, where horses and cattle are gazing, 
# hills, plains and painted buildings of railway stations can be seen. 
# The poet also sees a child climbing up a steep ground collecting blackberries, 
# a homeless man standing and watching as the train passes""" 

file_path = r"D:\localhost-slow.log"
time = 'Time: 2024-02-16T05'

with open(file_path,'r') as file:
    # print(file)
    lines = file.readlines()
    # print(lines)

    for i in range(len(lines)):
        # print(i)
        # print(lines[i])
        if time in lines[i]:
            print(str(lines[i]))
            for j in range(i+1, min(i+3, len(lines))): 
                print(lines[j])
    
        


