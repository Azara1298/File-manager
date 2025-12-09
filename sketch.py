from pathlib import Path
import os
import shutil
import hashlib #haslib is a module that provides away to hash files
# hashing is a way to convert data into a fixed-size string of characters, which is typically a sequence of numbers and letters






class File:
    def __init__(self, path):
       self.path = Path(path)
       self.__size = os.path.getsize(path) # the os module provides a way to interact with the os and 
       #getsize() is a method that returns the size of a file in bytes
       self.__location = self.path.parent #.parent is an attribute from pathlib that returns the parent directory of a path
       self.__name = self.path.name #.name is an attribute from pathlib that returns the name of the file or folder from a path
       #the double underscore before location and name makes them private attributes meaning they cannot be accessed directlyfrom outside the class

    def hash(self):
        hasher = hashlib.new("sha256")
        with open(self.path, "rb") as f:
            while chunk := f.read(8192): # while chunk := this means while there is data(chunk): 
              #the = is assigning the value of the first (f.read(8192)) bytes to chunk
                hasher.update(chunk)
            return hasher.hexdigest()
    
    @property #this decorator allows us to define a method that can be accessed like an attribute
    def name(self):
       return self.__name
    
    @name.setter #this decorator allows us to define a method that can be used to set the value of an attribute
    def name(self, new_name):
       new_path = self.path.parent / new_name
       self.path.rename(new_path)
       #we also have to update the path
       self.path = new_path
       self.__name = new_name
       return self.__name

    @property
    def location(self):
      
       return self.__location
    
    @location.setter
    def location(self, new_location:str):
       new_path = Path(new_location)/self.name
       shutil.move(self.path, new_path) #shutil is a module that provides a way to move files and folders
       self.path = new_path
       self.__location = new_path.parent
       return self.__location
    
    @property
    def size(self):
       size = self.__size
       readable_size = 0
       if size < 1024:
          readable_size= f"{size}b"
       elif size >= 1024 and size < 1048576:
          size_kb = size / 1024
          readable_size = f"{size_kb:.2f}kb"
       elif size >= 1048576 and size < 1073741824:
          size_mb = size / 1048576
          readable_size= f"{size_mb:.2f}mb"
       else:
          size_gb = size / 1073741824
          readable_size = f"{size_gb:.2f}gb"
       return readable_size

       


    
    def __repr__(self): #this method is used to define how the object is represented as a string
       return f"File(name={self.name}, Location={self.location}, Size={self.size})"



                 
                   
            
   
   
      

                               

   
   
         
      
      
      
      

