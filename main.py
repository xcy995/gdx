import json
import os
from happy_python.cmd import hlog, get_exit_code_of_cmd
website_details = []
# 定义各个变量的路径命令

class Config(LoadCustomizeZymodConfig):
    def __init__(self):
        super().__init__()

        self.section = 'zymod.custom'
        self.node_exec_path = ''
        self.node_exec_script_path = ''
        self.google_chrome_path = ''
        self.node_js_command_line_parameters = ''
        self.env_node_modules_path = ''
        self.url_access_log = ''

def main():
    node = '/usr/bin/node '
    js = '/home/yyf/FANGXIE/zhiyan.js'
    chrome = '/usr/bin/google-chrome-stable'
    url = 'https://zhiyan.cdgeekcamp.com'
    json1 = '/home/yyf/FANGXIE/2023_09_11_10_09_45_45.json'
    jpg = '/home/yyf/FANGXIE/2023_09_11_10_09_45_45.jpg'

    node_modules_path = '/home/yyf/workspace/ZhiYanModule/zhiyan-mod-browser/node_modules'
# 构建node和js命令
    node_js_command = '%s %s %s %s %s %s' % (node, js, chrome, url, json1, jpg)

    hlog.info(node_js_command)
# 设置变量环境
    os.putenv('NODE_PATH', node_modules_path)
# 执行node命令执行结果
    code = get_exit_code_of_cmd(cmd=node_js_command, is_show_error=True, is_show_output=True)
# 清楚环境变量
    os.unsetenv('NODE_PATH')
# 检查命令执行结果
    if code != 0:
        return "error"

# 读取json并提取url
    with open(json1) as f:
        log_entries =json.load(f)['log']['entries']
        for i in log_entries:
            website_details.append(i['request']['url'])

    hlog.info(website_details)
    hlog.info(len(website_details))

if __name__ == '__main__':
    main()