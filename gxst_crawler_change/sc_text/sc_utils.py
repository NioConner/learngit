import json
import os
import zipfile

from config.url_path_seting import abs_file_path


class sc_util():
    def write_txt(self,dictory,task_id,file_id):
        if file_id == 'person'or file_id == 'inv':
            gen_file = abs_file_path + task_id + '/'+file_id+'/'+file_id+'.json'
            gen_dir = abs_file_path + task_id + '/'+file_id
        elif file_id == 'alter'or file_id =='busilice':
            gen_file = abs_file_path + task_id + '/'+file_id+'.json'
            gen_dir = abs_file_path + task_id
        else:
            gen_file = abs_file_path+task_id+'/inv/'+file_id+'.json'
            gen_dir = abs_file_path+task_id+'/inv'

        try:
            with open(gen_file, 'w') as fp:
                json.dump(dictory, fp, ensure_ascii=False, indent=4)

        except FileNotFoundError:
            os.makedirs(gen_dir)
            with open(gen_file, 'w') as fp:
                json.dump(dictory, fp, ensure_ascii=False, indent=4)

        #self.make_zip(source_dir=abs_file_path + task_id, output_filename=task_id)


    def make_zip(source_dir, output_filename):
        zipf = zipfile.ZipFile(output_filename, 'w')
        pre_len = len(os.path.dirname(source_dir))
        for parent, dirnames, filenames in os.walk(source_dir):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
                zipf.write(pathfile, arcname)
        zipf.close()