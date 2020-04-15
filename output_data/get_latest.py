import os
from datetime import datetime
from shutil import copyfile

def get_date(raw_file_name):
    return datetime.strptime(raw_file_name.split('covid19-')[1].replace('.csv', ''), '%Y-%m-%d')

def convert_back_to_str_file(date):
    return  'output_data/mexico-covid19-' + date.isoformat().split('T')[0] + '.csv'

if __name__ == '__main__':
    print('Finding newest file...')
    available_files = [file for file in os.listdir('output_data') if 'mexico' in file]
    max_date = max([get_date(file) for file in available_files])
    max_date_file = convert_back_to_str_file(max_date)
    print('Generating latest.csv...')
    copyfile(max_date_file, 'output_data/latest.csv')
