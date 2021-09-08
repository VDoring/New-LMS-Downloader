import urllib.request
from requests import get
import wget
import os

os.system('mode con cols=135 lines=26')
os.system('title New LMS Downloader - v1.1.2 by VDoring')

print('< LMS 영상 다운로드 프로그램 >')
print('사용방법: https://github.com/VDoring/New-LMS-Downloader\n')

i = 1

#by VDoring. 2021.09.08
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
        try: # 시도2
            print('다운로드중입니다...', end='', flush=True)
            videoSave2(videolink, filename)
        except:
            try: # 시도3
                videoSave3(videolink, filename)
            except:
                try: # 시도4
                    videoSave4(videolink, filename)
                except:
                    try: # 시도5
                        videoSave5(videolink)
                        if videoStatusCheck('ssmovie.mp4') == True:
                            os.rename('ssmovie.mp4', filename) # 인터넷에서의 파일 이름을 사용자가 원하는 파일이름으로 교체
                            print('\n>>', filename, '저장이 완료되었습니다! <<\n\n')
                            return
                        print('\r>> 인터넷에서 인식하는 파일 이름이 ssmovie가 아닙니다. 따라서 ssmovie란 이름으로 저장하겠습니다. <<')
                        print('>>', 'ssmovie.mp4', '저장이 완료되었습니다! <<\n\n')
                        return
                    except:
                        pass
    
    if videoStatusCheck(filename) == True:
        print('\r>>', filename, '저장이 완료되었습니다! <<\n\n')
    else:
        print('\r>> 다운로드에 실패했습니다. <<\n\n')
        if os.path.isfile(filename) == True: # (재생불가,불필요한) .mp4파일이 생성된 상태라면
            os.remove(filename) # .mp4파일 제거


#by VDoring. 2021.09.07
#강의영상파일을 CRUL 방식으로 다운로드합니다. 자체 CLI Print됨
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

#by VDoring. 2021.09.08
#강의영상파일을 wget 방식으로 다운로드합니다
#매개변수: videolink
#리턴값: 없음
def videoSave5(videolink):
    wget.download(videolink)
    

#by VDoring. 2021.09.07
#강의영상파일이 정상적인지 확인합니다.
#매개변수: filename
#리턴값: True, False
def videoStatusCheck(filename):
    if os.path.isfile(filename) == True and os.path.getsize(filename) > 2097152: # 파일이 생성되었고 2MB 이상일경우
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