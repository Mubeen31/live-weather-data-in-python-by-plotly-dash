# import sqlalchemy
# import pandas as pd
# import time

# from github import Github
#
# g = Github('qs6272527@gmail.com', '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')
#
#
# repos =g.search_repositories(query = 'language:python')
# for repo in repos:
#     repo
#
# for repo in g.get_user().get_repos():
#     print(repo.name)
# while True:
#     time.sleep(2)
#     def sql_data():
#         engine = sqlalchemy.create_engine('mysql+pymysql://root:sql_root_45t6@127.0.0.1:3306/arduino_sensor_data')
#         df = pd.read_sql_table('datatable', engine)
#         df1 = df.tail(10)
#         return df1
#     print(sql_data())
