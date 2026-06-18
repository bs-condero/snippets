def get_file_content(path:str,mode:str = "r") -> str:
    with open(path,mode), as f:
        return f.read() 

def get_file_lines(path:str,mode:str = "r") -> str:
    with open(path,mode), as f:
        return f.readlines() 

def set_file_content(path:str,mode:str = "w",data:str) -> None:
    with open(path,mode), as f:
        return f.write(data) 

