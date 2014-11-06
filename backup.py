 # -*- coding:utf8 -*-

import os

cur_dir = os.path.split(os.path.realpath(__file__))[0]

def get_repo_list():
    ret = []
    list_file = os.path.join(cur_dir, 'list')

    for line in open(list_file).readlines():
        if line.startswith('https://github.com'):
            ret.append(line[:-1] + '.git')
    return ret

def clone(git_url, base_path):
    git_name = os.path.basename(git_url)
    des_name = os.path.join(base_path, git_name)
    if os.path.exists(des_name):
        cmd = ' '.join(['cd', des_name, '&&', 'git pull'])
    else:
        cmd = ' '.join(['git clone', git_url, des_name])
    os.system(cmd)

if __name__ == '__main__':
    git_dir = os.path.join(cur_dir, 'git')
    for url in get_repo_list():
        clone(url, git_dir)
