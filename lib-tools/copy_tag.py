from mutagen import File
import os
import re

def contains_non_english_or_special_characters(s):
    # Define a regex pattern to match only English letters and special characters
    allowed_pattern = r'^[A-Za-z0-9!@#$%^&*()_+\-=\[\]{};\'\\:"|<>,./?~` ]*$'
    
    # Check if the string matches the allowed pattern
    return not re.match(allowed_pattern, s)


def copy_tag(source_file, dest_file):
    # Get tags from source_file
    source_audio = File(source_file)

    title = source_audio.tags.get("TITLE")
    if contains_non_english_or_special_characters(title):
        title = input(f"Update the title? [{title}]: ")
    
    # Send tags to dest_file