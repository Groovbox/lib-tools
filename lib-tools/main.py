from mutagen import File
import os

def fix_tags(file_path) -> None:
    """
    Correctly splits tags that are just delimited by a comma or semi colon
    """

    audio = File(file_path)

    if not audio:
        raise ValueError("File is not an audio file.")
    
    if not audio.tags:
        raise AttributeError("Music file does not have any tags??")
    
    artists = audio.tags.get("artist") or audio.tags.get("ARTIST")
    genres = audio.tags.get("genre") or audio.tags.get("GENRE")
    
    artists = split_tag(artists)
    genres = split_tag(genres)

    if artists:
        print("Fixing artists tag for ", audio["TITLE"])
        audio["ARTIST"] = artists
    if genres:
        print("Fixing genres tag for ", audio["TITLE"])
        audio["GENRE"] = genres
    audio.save()


def split_tag(tag) -> list[str]:
    if tag is None:
        return
    
    if isinstance(tag, list):
        if len(tag) > 1:
            return
        tag_str = tag[0]
    else:
        tag_str = tag

    if ";" in tag_str:
        print("Changing delimeter from ;")
        return [x.strip() for x in tag_str.split(";")]
    if "," in tag_str:
       print("Changing delimeter from ,")
       return [x.strip() for x in tag_str.split(",")] 
    else:
        return None

if __name__ == "__main__":
    with open("done.txt", "w+") as file:
        files = file.readlines()

        directory = input("Enter music library: ")
        for root, _, files in os.walk(directory):
            for file in files:
                now_file= os.path.join(root, file)

                if now_file in files:
                    continue

                try:
                    fix_tags(now_file)
                    files.append(now_file)
                except ValueError:
                    continue
                    
        print("Edited ", len(files), " files!!!")
        file.writelines(files)
    