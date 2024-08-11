"""
@Project : ListView
@File    : poetry.py
@IDE     : PyCharm
@Author  : libai
@Email   : stayhungrystayfoolish52@gmail.com
@Date    : 2024/8/11 11:11 PM
"""


class Poetry:
    def __init__(self, title, author, main_text, publish_time, address, subtitle=None, introduce=None, collection=None,
                 recite_progress=0, art_picture_path=None):
        self.__title = title
        self.__subtitle = subtitle
        self.__author = author
        self.__main_text = main_text
        self.__publish_time = publish_time
        self.__address = address
        self.__introduce = introduce
        self.__collection = collection
        self.__recite_progress = recite_progress
        self.__art_picture_path = art_picture_path

    def title(self):
        return self.__title

    def subtitle(self):
        return '•{}'.format(self.__subtitle) if self.__subtitle else ''

    def title_subtitle(self):
        return self.__title if not self.__subtitle else ''.join([self.__title, '•{}'.format(self.__subtitle)])

    def author(self):
        return self.__author

    def main_text(self):
        return self.__main_text

    def introduce_main_text(self):
        return self.__main_text if not self.__introduce else ''.join([self.__introduce, '\n', self.__main_text])

    def publish_time(self):
        return self.__publish_time

    def address(self):
        return self.__address

    def introduce(self):
        return self.__introduce

    def collection(self):
        return self.__collection

    def set_recite_progress(self, progress):
        self.__recite_progress = progress

    def recite_progress(self):
        return self.__recite_progress

    def art_picture_path(self):
        return self.__art_picture_path

    def profile(self):
        profile_info = ''.join(['Poetry {\n',
                                '\ttitle: {},\n'.format(self.__title),
                                '\tsubtitle: {},\n'.format(self.__subtitle),
                                '\tauthor: {},\n'.format(self.__author),
                                '\tintroduce: {},\n'.format(self.__introduce),
                                '\tmain_text: {},\n'.format(self.__main_text),
                                '\tpublish_time: {},\n'.format(self.__publish_time),
                                '\taddress: {},\n'.format(self.__address),
                                '\tcollection: {},\n'.format(self.__collection),
                                '\trecite_progress: {},\n'.format(self.__recite_progress),
                                '\tart_picture_path: {},\n'.format(self.__art_picture_path),
                                '}'])
        return profile_info
