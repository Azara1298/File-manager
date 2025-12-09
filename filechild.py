from sketch import File
from pathlib import Path
import shutil

class MediaFile(File):
  media_extensions = {'image': ['.jpg', '.jpeg', '.png', '.gif'],
                        'video': ['.mp4', '.avi', '.mov'],
                        'audio': ['.mp3', '.wav', '.aac'],
                        'document': ['.pdf', '.docx', '.csv', '.xlsx', '.txt']}
  def __init__(self, path:Path):
    super().__init__(path)
    self.path = Path(path)
    self.__media_type = self.get_media_type()

  @property
  def media_type(self):
    return self.__media_type
  
  def get_media_type(self):
   
    ext = self.path.suffix.lower()
    for m_type, extensions in self.media_extensions.items():
      if ext in extensions:
        return m_type
      
    return None

  def __repr__(self):
    return f"MediaFile(name={self.path.name}, type={self.media_type}, folder={self.path.parent})"
  




