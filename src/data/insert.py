import sqlite3

from src import config


class InsertData(object):
    def __init__(self, params):
        self.__params = params
        self.__conn = sqlite3.connect(config.db_path)
        self.__cursor = self.__conn.cursor()

    def __del__(self):
        self.__conn.commit()
        self.__conn.close()

    def add_member_info(self):
        sql = 'insert into user (userId, name, passwd, formerName, idNo, typeId, sex, age, classId, birthday, ' \
            'national, nativePlace, politicalLandscape, admissionDate, mail, schoolYear, memo) ' \
                'values ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}", ' \
              '"{7}", "{8}", "{9}", "{10}", "{11}", "{12}", "{13}", "{14}", "{15}", "{16}")'.format( \
            self.__params['userId'], self.__params['name'], self.__params['passwd'], self.__params['formerName'], \
            self.__params['idNo'], self.__params['typeId'], self.__params['sex'], self.__params['age'], self.__params['classId'], \
            self.__params['birthday'], self.__params['national'], self.__params['nativePlace'], self.__params['politicalLandscape'], \
            self.__params['admissionDate'], self.__params['mail'], self.__params['schoolYear'], self.__params['memo'] )
        result = self.__cursor.execute(sql)
        if result.rowcount > 0:
            return True
        else:
            return False