"""
@Project : ListView
@File    : base_listview_adapter.py
@IDE     : PyCharm
@Author  : libai
@Email   : stayhungrystayfoolish52@gmail.com
@Date    : 2024/8/11 11:11 PM
"""

from abc import ABCMeta, abstractmethod


class BaseListViewAdapter(metaclass=ABCMeta):
    @abstractmethod
    def set_data(self, data):
        pass

    def set_data_changed_notifier(self, data_changed_notifier):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def get_count(self):
        pass

    def get_item(self, index):
        pass

    @abstractmethod
    def get_item_height(self, index):
        pass

    @abstractmethod
    def get_item_view_id(self, index):
        pass

    @abstractmethod
    def create_item_view(self, container_view, index):
        pass

    @abstractmethod
    def update_view(self, index):
        pass
