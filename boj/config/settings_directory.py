import os

SETTINGS_DIRECTORY = os.path.join(os.getcwd(), '.boj')


###############################################################

print('[INFO]', f'설정 디렉토리: "{SETTINGS_DIRECTORY}"')
print('----------------------------------------------------------------')

if os.path.isdir(SETTINGS_DIRECTORY):
    print('[INFO]', '설정 디렉토리를 발견하였습니다.')

elif not os.path.exists(SETTINGS_DIRECTORY):
    print('[INFO]', '설정 디렉토리를 생성하고 있습니다...')

    os.makedirs(SETTINGS_DIRECTORY)

    # .gitignore 생성
    with open(os.path.join(SETTINGS_DIRECTORY, '.gitignore'), 'w') as gitignore_file:
        gitignore_file.write('*\n')

    print('[INFO]', f'설정 디렉토리를 생성하였습니다.')

else:
    raise FileExistsError(f'"{SETTINGS_DIRECTORY}"가 존재하여 설정 디렉토리를 생성할 수 없습니다.')

print('================================================================')
