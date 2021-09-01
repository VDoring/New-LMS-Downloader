# urllib는 requests 라이브러리를 설치하면 사용할 수 있습니다.#
import urllib.request
import os

i = 1

os.system('mode con cols=134 lines=17')
os.system('title New LMS Video Downloader - CLI type v1.0.1 by VDoring')

print('< LMS 영상 다운로드 프로그램 >')
print('사용방법: https://github.com/VDoring/New-LMS-Downloader\n')

def save_video(video_url, savename):
    try:
        print('다운로드중...')
        urllib.request.urlretrieve(video_url, savename)
        print(savename, '저장이 완료되었습니다!\n')
    except:
        print('[!] 올바른 링크가 아닙니다! [!]\n')

while True:
    print('[' + str(i) + '번째 다운로드' + ']')
    user_videolink = input('영상 링크를 입력하세요: ')
    user_filename = input('파일 이름을 입력하세요: ')
    user_filename = user_filename + '.mp4'

    save_video(user_videolink, user_filename)

    i += 1