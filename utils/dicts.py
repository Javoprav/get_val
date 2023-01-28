# файл dicts.py
"""Функция для работы со словарями"""
data2 = {"vcs": "mercurial"}
data3 = {}
def get_val(collection, key, default='git'):
    if collection:
        return collection[key]
    else:
        return default

print(get_val(data2, "vcs"))
print(get_val(data2, "vcs", "git"))
print(get_val(data3, "vcs", "git"))
print(get_val(data3, "vcs", "bazaar"))
'''
data = {"vcs": "mercurial"}
get_val(data, "vcs")
'mercurial'
get_val(data, "vcs", "git")
'mercurial'
data = {}
get_val({}, "vcs", "git")
'git'
get_val({}, "vcs", "bazaar")
"bazaar"'''