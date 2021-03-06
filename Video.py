import urllib.request
import os.path

class Video:
    video_log = None

    def __init__(self):
        self.episode_num = -1
        self.web_page = ''
        self.video_page = ''
        self.id = ''
        self.video_file = None
        self.video_file_size = -1

    def __init__(self, web_page):
        self.episode_num = -1
        self.web_page = web_page
        self.video_page = ''
        self.id = ''
        self.video_file = None
        self.vide_file_size = -1

    def __init__(self, web_page, id, num):
        self.episode_num = num
        self.web_page = web_page
        self.video_page = ''
        self.id = id
        self.video_file = None
        self.vide_file_size = -1

    def set_pages(self, web_page = '', video_page = ''):
        self.web_page = web_page
        self.video_page = video_page

    def set_web_page_url(self, url = ''):
        self.web_page = url

    def get_web_page_url(self):
        return self.web_page

    def set_video_page_url(self, url = ''):
        self.video_page = url

    def get_video_page_url(self):
        return self.video_page

    def set_id(self, id = -1):
        self.id = id

    def get_id(self):
        return self.id

    def set_episode_num(self, n):
        self.episode_num = n

    def get_episode_num(self):
        return self.episode_num

    def get_video_file(self, url = ''):
        video_log = open('finished_video_list.txt', 'a')
        print('Getting video file')
        if url != '':
            self.set_video_page_url(url)
        self.id = self.get_web_page_url().rpartition('/')[2].partition('?')[0]
        print(self.id + ' in progress')
        if not os.path.isfile(self.get_id() + '.mp4'):
            self.video_file = urllib.request.urlretrieve(self.get_video_page_url(), str(self.id) + '.mp4')
            video_log.write(self.get_web_page_url() + '\n')
        #self.video_file_size = self.video_file.info().getheaders('Content-Length')[0]

        video_log.write(self.get_web_page_url() + '\n')
        video_log.close()
