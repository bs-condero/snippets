def get_file_content(path:str,mode:str = "r") -> str:
    with open(path), as f:
        return f.read() 

def get_file_lines(path:str,mode:str = "r") -> str:
    with open(path), as f:
        return f.readlines() 

