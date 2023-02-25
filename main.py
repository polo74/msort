import os
import ffmpeg
import re

destination_dir = os.path.abspath('/home/paul/test2')
source_dir = os.path.abspath('/home/paul/test')

files = os.listdir(source_dir)

for file in files:

    # Set the default folders
    file_source = os.path.join(source_dir, file)
    data = ffmpeg.probe(file_source)

    # Get the video date
    creation_time = data['format']['tags']['creation_time']
    regex = "\d+"
    res = re.findall(regex, creation_time)
    [year, month, day, hour, minute, second, _] = res

    # Get full date (ex: 01.01.2001-01:01:01)
    year_full = year
    month_full = year + '-' + month
    day_full = month_full + '-' + day
    hour_full = day_full + '§' + hour
    minute_full = hour_full + ':' + minute
    second_full = minute_full + ':' + second

    # Set and create the folders if not exist
    year_path = os.path.join(destination_dir, year_full)
    month_path = os.path.join(year_path, month_full)
    day_path = os.path.join(month_path, day_full)

    if year_full not in os.listdir(destination_dir):
        os.mkdir(year_path)
    if month_full not in os.listdir(year_path):
        os.mkdir(month_path)
    if day_full not in os.listdir(month_path):
        os.mkdir(day_path)

    # Rename and copy the file in the right folder
    _, extension = os.path.splitext(file_source)
    new_filename = second_full + extension

    file_destination = os.path.join(day_path, new_filename)
    os.replace(file_source, file_destination)
