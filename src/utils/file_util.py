"""
文件工具类

"""
import hashlib
from pathlib import Path


class FileUtil:
    """
    文件工具类

    """

    @staticmethod
    def get_file_content(file_path: Path) -> bytes:
        """
        获取文件内容

        :param file_path: 文件路径
        :return:
        """
        with open(file_path, 'rb') as f:
            return f.read()

    @staticmethod
    def get_file_md5(file_content: bytes) -> str:
        """
        生成文件的MD5值

        :param file_content: 文件内容
        :return: MD5值
        """
        return hashlib.md5(file_content).hexdigest()

    @staticmethod
    def create_file(file_path: Path):
        """
        创建文件

        :param file_path: 指定路径的文件
        :return:
        """
        file_path.touch()


if __name__ == '__main__':
    file_path_list = [r'E:\4k', r'D:\Data\Wallpaper', r'E:\wallpaper', r'E:\迅雷下载\QTDownLoads',
                      r'F:\AI Painting', r'F:\File', r'F:\welfare girl', r'F:\鬼刀17年到21年壁纸合集']
    d = {'image_dir_list': file_path_list}
    import json

    print(json.dumps(d, ensure_ascii=False, indent=4))
