import urllib.request
import os
from requests import get

os.system('title New LMS Video Downloader - CLI type v1.0.4-Advanced by VDoring')

print('< LMS 영상 다운로드 프로그램 - Advanced Mode >\n')

i = 1

def videoSave1(videolink, filename):
    urllib.request.urlretrieve(videolink, filename)

def videoSave2(videolink, filename):
    response = get(videolink)
    with open(filename, 'wb') as file:
        file.write(response.content)

def videoSave3(videolink, filename):
    video_read = urllib.request.urlopen(videolink).read()
    with open(filename, 'wb') as file:
        file.write(video_read)

while True:
    print('[' + str(i) + '번째 다운로드' + '] - ', end='')
    print('다운로드할 방법을 선택하세요.')
    print(' [1] urlretrieve')
    print(' [2] get')
    print(' [3] urlopen')
    user_select = input('숫자입력: ')
    
    if user_select == '1' or user_select == '2' or user_select == '3':
        user_videolink = input('영상 링크를 입력하세요: ')
        user_filename = input('파일 이름을 입력하세요: ')
        user_filename = user_filename + '.mp4'

        print('> 다운로드중... ', end='', flush=True)
        if user_select == '1':
            try:
                videoSave1(user_videolink, user_filename)
                print('>', user_filename, '저장이 완료되었습니다! <\n')
            except:
                print('방법 1 실패했습니다.\n')

        elif user_select == '2':
            try:
                videoSave2(user_videolink, user_filename)
                print('>', user_filename, '저장이 완료되었습니다! <\n')
            except:
                print('방법 2 실패했습니다.\n')

        elif user_select == '3':
            try:
                videoSave3(user_videolink, user_filename)
                print('>', user_filename, '저장이 완료되었습니다! <\n')
            except:
                print('방법 3 실패했습니다.\n')

    else:
        print('> 다시 입력하세요.\n')
    i += 1