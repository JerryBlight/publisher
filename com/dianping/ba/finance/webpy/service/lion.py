__author__ = 'will'

import urllib
import json
import operator


def compare_conf(project):

    alpha_dict = get_project_conf("alpha", project)
    beta_dict = get_project_conf("qa", project)
    beta_dict['newkey'] = "hello"

    for k, v in alpha_dict.items():
        if k not in beta_dict.keys():
            print(k + " not in beta")
    for k, v in beta_dict.items():
        if k in alpha_dict.keys():
            if operator.ne(v, alpha_dict[k]) != 0:
                print(k + " updated in beta,value: " + v)
            else:
                print(k + " added in beta,value:" + v)


#根据环境和项目名获取lion配置，放到一个dict对象中
def get_project_conf(env, project):
    data = {}
    data['id'] = '2'
    data['env'] = env
    data['prefix'] = project
    return lion_conn('get', data)

def get_single_config(env, key):
    data = {}
    data['id'] = '2'
    data['env'] = env
    data['key'] = key
    return lion_conn('get', data)

def create_conf(env, project, key, value, desc):
    data = {}
    data['id'] = '2'
    data['env'] = env
    data['key'] = key
    data['project'] = project
    data['desc'] = desc
    lion_conn('create', data)
    data['value'] = value
    lion_conn('set', data)


def lion_conn(behave, data):
    url = 'http://lionapi.dp:8080/config2/' + behave
    url_values = urllib.parse.urlencode(data)
    ful_url = url + '?' + url_values
    response = urllib.request.urlopen(ful_url)
    content = response.read()
    json_dic = json.loads(bytes.decode(content))
    result = json_dic['result']
    return result

# compare_conf("ba-finance-accounting-web")
create_conf('dev', 'ba-finance-workflow-web', 'testkey', 'testvalue', 'just test')
