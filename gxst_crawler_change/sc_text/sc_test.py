import os
import zipfile
from config.url_path_seting import abs_file_path
from utils.track_and_txt_manager import ContentTxtManger


def make_zip(source_dir, output_filename):
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
            zipf.write(pathfile, arcname)
    zipf.close()


if __name__ == '__main__':
    #make_zip(abs_file_path+'89890228-78d9-11e7-9356-48bf6bed3558',abs_file_path+'a.zip')
    a = ContentTxtManger('sichuan',task_id='a12cc3a2-78dd-11e7-b733-48bf6bed3558')
    a.zip_func()