import urllib.request
import os
from requests import get

os.system('mode con cols=134 lines=17')
os.system('title New LMS Video Downloader - CLI type v1.0.4 by VDoring')

print('< LMS 영상 다운로드 프로그램 >')
print('사용방법: https://github.com/VDoring/New-LMS-Downloader\n')

i = 1

def videoSaveManager(videolink, filename):
    try: # 시도1
        print('다운로드중...', end='', flush=True)
        videoSave1(videolink, filename)
        print('\r>', filename, '저장이 완료되었습니다! <\n')
    except:
        try: # 시도2
            videoSave2(videolink, filename)
            print('\r>', filename, '저장이 완료되었습니다! <\n')
        except:
            try: # 시도3
                videoSave3(videolink, filename)
                print('\r>', filename, '저장이 완료되었습니다! <\n')
            except:
                print('\r> 다운로드에 실패했습니다. <\n')


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
    print('[' + str(i) + '번째 다운로드' + ']')
    user_videolink = input('영상 링크를 입력하세요: ')
    user_filename = input('파일 이름을 입력하세요: ')
    user_filename = user_filename + '.mp4'

    videoSaveManager(user_videolink, user_filename)
    i += 1