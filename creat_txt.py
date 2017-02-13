def text_create(name, msg):   
    Air_path = '/Users/Air/'    
    full_path = Air_path + name + '.txt' 
    file = open(full_path,'w')             
    file.write(msg) 
    file.close() 
    print("Done")
# 调用函数  text_create('hello','hello world')
