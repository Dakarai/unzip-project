# instructions:
# unzip the contents
# search through all files to find a phone number in the form of XXX-XXX-XXXX

import zipfile
import os
import re


def search(file, pattern):
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''


if __name__ == '__main__':
    zip_obj = zipfile.ZipFile("unzip_me_for_instructions.zip", 'r')
    zip_obj.extractall()

    phone_pattern = r'\d{3}-\d{3}-\d{4}'
    results = []

    for folder, subfolders, files in os.walk(os.getcwd() + '\\extracted_content'):
        for file in files:
            results.append(search(folder + '\\' + file, phone_pattern))

    for result in results:
        if result != '':
            print(result.group())
        else:
            pass
