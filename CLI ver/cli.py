import urllib.request
import os
from requests import get

os.system('mode con cols=135 lines=26')
os.system('title New LMS Downloader - v1.1.1 by VDoring')

print('< LMS 영상 다운로드 프로그램 >')
print('사용방법: https://github.com/VDoring/New-LMS-Downloader\n')

i = 1

#by VDoring. 2021.09.04
#강의영상파일 다운로드 매니저입니다.
#매개변수: videolink, filename
#리턴값: 없음
def videoSaveManager(videolink, filename):
    nospace_filename = filename.replace(' ','') # 시도1 작동을 위해 파일이름 띄어쓰기 제거
    videoSave1(videolink, nospace_filename) # 시도1
    if videoStatusCheck(nospace_filename) == True:
        os.rename(nospace_filename, filename) # 실제 .mp4파일에선 띄어쓰기 복구
        print('>>', filename, '저장이 완료되었습니다! <<\n\n')
        return
    else:
        print('다운로드중...', end='', flush=True)
        try: # 시도2
            videoSave2(videolink, filename)
        except:
            try: # 시도3
                videoSave3(videolink, filename)
            except:
                try: # 시도4
                    videoSave4(videolink, filename)
                except:
                    pass
    
    if videoStatusCheck(filename) == True:
        print('\r>>', filename, '저장이 완료되었습니다! <<\n\n')
    else:
        print('\r>> 다운로드에 실패했습니다. <<\n\n')
        if os.path.isfile(filename) == True: # (재생불가,불필요한) .mp4파일이 생성된 상태라면
            os.remove(filename) # .mp4파일 제거

#by VDoring. 2021.09.07
#강의영상파일을 CRUL 방식으로 다운로드합니다
#매개변수: videolink, filename
#리턴값: 없음
def videoSave1(videolink, filename):
    cmd = "curl " + videolink + " --output " + filename
    os.system(cmd)

#by VDoring. 2021.09.01
#강의영상파일을 urlretrieve 방식으로 다운로드합니다
#매개변수: videolink, filename
#리턴값: 없음
def videoSave2(videolink, filename):
    urllib.request.urlretrieve(videolink, filename)

#by VDoring. 2021.09.04
#강의영상파일을 requests get 방식으로 다운로드합니다
#매개변수: videolink, filename
#리턴값: 없음
def videoSave3(videolink, filename):
    response = get(videolink)
    with open(filename, 'wb') as file:
        file.write(response.content)

#by VDoring. 2021.09.04
#강의영상파일을 urlopen 방식으로 다운로드합니다
#매개변수: videolink, filename
#리턴값: 없음
def videoSave4(videolink, filename):
    video_read = urllib.request.urlopen(videolink).read()
    with open(filename, 'wb') as file:
        file.write(video_read)

#by VDoring. 2021.09.07
#강의영상파일이 정상적인지 확인합니다.
#매개변수: filename
#리턴값: True, False
def videoStatusCheck(filename):
    if os.path.isfile(filename) == True and os.path.getsize(filename) > 3145728: # 파일이 생성되었고 3MB 이상일경우
        return True
    return False

# 메인코드 #
while True:
    print('[' + str(i) + '번째 다운로드' + ']')
    user_videolink = input('영상 링크를 입력하세요: ')
    user_filename = input('파일 이름을 입력하세요: ')
    user_filename = user_filename + '.mp4'

    videoSaveManager(user_videolink, user_filename)
    i += 1