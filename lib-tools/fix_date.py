from mutagen import File
import os

def fix_date(file_location):
    """
    release_date -> standard date
    """
    audio = File(file_location)

    rel_date = audio.tags.get("RELEASE DATE") or audio.tags.get("release date")

    if not rel_date:
        return
    
    audio["DATE"] = rel_date

    audio.save()

if __name__ == "__main__":
    directory = input("Enter music library: ")
    for root, _, files in os.walk(directory):
        for file in files:
            now_file= os.path.join(root, file)
            try:
                fix_date(now_file)
            except Exception as e:
                print(e)
                continue
