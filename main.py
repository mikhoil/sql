import sqlite3
import re
import html
from pprint import pprint

cur = sqlite3.connect('works.sqlite').cursor()
# 1
cur.execute('''CREATE TABLE IF NOT EXISTS genders(
    gender text, FOREIGN KEY (gender) REFERENCES works (gender)
)''')
cur.execute('INSERT INTO genders SELECT gender FROM works')
pprint(list(cur.execute('SELECT * FROM genders')))
# 2
cur.execute('''CREATE TABLE IF NOT EXISTS educationTypes(
    educationType text, FOREIGN KEY (educationType) REFERENCES works (educationType)
)''')
cur.execute('INSERT INTO educationTypes SELECT educationType FROM works')
pprint(list(cur.execute('SELECT * FROM educationTypes')))
# 3
cur.execute('''CREATE TABLE IF NOT EXISTS jobTitles(
    jobTitle text, FOREIGN KEY (jobTitle) REFERENCES works (jobTitle)
)''')
cur.execute('INSERT INTO jobTitles SELECT jobTitle FROM works')
pprint(list(cur.execute('SELECT * FROM jobTitles')))
# 4
cur.execute('''CREATE TABLE IF NOT EXISTS qualifications(
    qualification text, FOREIGN KEY (qualification) REFERENCES works (qualification)
)''')
cur.execute('INSERT INTO qualifications SELECT qualification FROM works')
pprint(list(cur.execute('SELECT * FROM qualifications')))

# 5
def delete_html(string):
    return html.unescape(re.sub('<[^<]+?>', '', string))


info_without_html = {}
for [ID, skill, otherInfo] in cur.execute('SELECT ID, skills, otherInfo FROM works'):
    info_without_html[ID] = (delete_html(skill), delete_html(otherInfo))

for ID, (skill, otherInfo) in info_without_html.items():
    cur.execute('UPDATE works SET skills = ?, otherInfo = ? WHERE ID = ?', [skill, otherInfo, ID])

pprint(list(cur.execute('SELECT * FROM works')))
# 6
cur.execute('''CREATE TABLE IF NOT EXISTS skills (
    skill text, FOREIGN KEY (skill)
)''')
cur.execute('INSERT INTO skills SELECT skills FROM works')
pprint(list(cur.execute('SELECT * FROM skills')))
# 7
cur.execute('''CREATE TABLE IF NOT EXISTS otherInfo (
    otherInfo text, FOREIGN KEY (otherInfo)
)''')
cur.execute('INSERT INTO otherInfo SELECT otherInfo FROM works')
pprint(list(cur.execute('SELECT * FROM otherInfo')))
