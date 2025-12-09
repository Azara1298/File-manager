from sketch import File
from pathlib import Path
from filechild import MediaFile
import os
import shutil



#now we need a function that will scan the directory and return a list of files
class Files: #this is an object with a collection of hashed files and their paths

   def __init__(self,dir_path:str):
     self.path = Path(dir_path) if dir_path else Path.cwd()
     self.files = [] # this will hold the list of files in the directory

   def scan_directory(self):
      base_path = self.path

      if base_path.exists() and base_path.is_dir():
         for item in base_path.rglob("*"): 
            if item.is_file():
                file = File(item)
                self.files.append(file)
      return self.files
   
   def deep_scan_directory(self):
      base_path = self.path

      if base_path.exists() and base_path.is_dir():
         for folder,subfolders, files, in os.walk(base_path): #os.walk() is a method that goea through a directory and all the tree directories 
            #and returns a tuple of (folder_path,names of subfolders in the path, and the files in the path)
            folder_path = Path(folder) 
            for f in files:
               file_path = folder_path / f
               file = File(file_path)
               self.files.append(file)
      return self.files
   
   def delete_duplicates(self,duplicates):
     base_path = self.path
     dup_folder = base_path / "duplicates"
     dup_folder.mkdir(exist_ok=True)

     for dup_file in duplicates:
         dup_path = Path(dup_file)
         new_location = dup_folder / dup_path.name
         if dup_path.exists():
             shutil.move(str(dup_path), str(new_location))
     
     print("Duplicates moved to 'duplicates' folder")

     
     return None
   
   def sort_by_mtype(self):
      base_path = self.path
      sorted_folders = ["images", "videos", "audios", "documents", "others"]
      if base_path.exists() and base_path.is_dir():
         #first recursively go through the directory and create a sorted files folder in each directory
         for folder, subfolders, files in os.walk(base_path): #this is a bad loop , because it will keep 
            #creating sorted files in the newly created directories
            if "sorted_files" not in subfolders:
               sorted_files = Path(folder) / "sorted_files"
               sorted_files.mkdir(exist_ok=True)
            else:
               sorted_files = Path(folder) / "sorted_files" 
            #second loop, go through all the files in that directory and its sub directories
            # and turn them into MediaFile objects
            for f in files:
               f = Path(folder) / f
               file = MediaFile(f)


                        #third loop, go through the list of folder types and check if any of the media files match the types in the list
               for mytype in sorted_folders: 
                  if file.media_type == mytype[:-1]: #we use mytype[:-1] to remove the 's' at the end of the folder name
                     type_folder = sorted_files / mytype
                     type_folder.mkdir(exist_ok=True)
                     new_location = type_folder  #final problem the files are all being moved to a single sorted files folder,
                      #which is not what we want
                      #since we are creating a sorted files folder in each directory we want to move all files to their respective sorted files folder
                     file.location = new_location
                  
      
       
           
      return None
   

   def __repr__(self):
      return f"Files(folder={self.path}, total_files={len(self.files)})"




path = r"C:\Users\User\OneDrive\Documents\coding\sims"

files = Files(path)
files.sort_by_mtype()



#Ok first problem we cant seem to move the audio files 
#its createting more than one sorted files folder
#  including inside the folders wich are being created wich is not what we want 