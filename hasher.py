from sketch import File
from files import Files
from pathlib import Path 




class FileHasher:
   def __init__(self,files:Files):
      self.files = files
      self.hash_map = {}
  
   def hash_files(self):
      for file in self.files.files:
         file_hash = file.hash()
         self.hash_map[file.path] = file_hash
      return self.hash_map
   
   def find_duplicates(self,hash_map):
      reverse_map = {}
      duplicates = []
      for file, file_hash in hash_map.items():
         if file_hash not in reverse_map:
            reverse_map[file_hash] = file
         elif file_hash in reverse_map:
            duplicates.append(file)
          
      return duplicates