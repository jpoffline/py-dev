# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=C0413

""" Import file paths correctly """
from context import app



import app.lib.sqlite.qy_factories as qy_factories


import unittest

class TestQyFactories(unittest.TestCase):

    def test_order_get_all_from_sql_qy(self):
        table = 'TABLE'
        ord = 'id desc'
        actual = qy_factories.get_all_from_sql_qy(table, order=ord)
        expected = 'SELECT * FROM TABLE ORDER BY id desc'
        self.assertEqual(actual, expected)    
    
    def test_get_all_from_sql_qy(self):
        table = 'TABLE'
        actual = qy_factories.get_all_from_sql_qy(table)
        expected = 'SELECT * FROM TABLE'
        self.assertEqual(actual, expected)    
    def test_top_get_all_from_sql_qy(self):
        table = 'TABLE'
        actual = qy_factories.get_all_from_sql_qy(table, topn=5)
        expected = 'SELECT * FROM TABLE LIMIT 5'
        self.assertEqual(actual, expected)    
    
    def test_emptyNames_insert_into_qy(self):
        table = 'TABLE'
        names = []
        actual = qy_factories.insert_into_qy(table, names)
        expected = 'INSERT INTO TABLE () VALUES ();'
        self.assertEqual(actual, expected)    
    
    def test_withNames_insert_into_qy(self):
        table = 'TABLE'
        names = ['col1', 'col2']
        actual = qy_factories.insert_into_qy(table, names)
        expected = 'INSERT INTO TABLE (col1,col2) VALUES (?,?);'
        self.assertEqual(actual, expected)    
    
    def test_emptyFields_create_db_qy(self):
        table = 'TABLE_NAME'
        fields = []
        actual = qy_factories.create_db_qy(table, fields)
        expected = 'CREATE TABLE IF NOT EXISTS TABLE_NAME ();'
        self.assertEqual(actual, expected)    
    
    def test_withOneField_create_db_qy(self):
        table = 'TABLE_NAME'
        fields = [{'name': 'col1', 'type': 'TYPE1'}]
        actual = qy_factories.create_db_qy(table, fields)
        expected = 'CREATE TABLE IF NOT EXISTS TABLE_NAME (col1 TYPE1);'
        self.assertEqual(actual, expected)    
    
    def test_withManyFields_create_db_qy(self):
        table = 'TABLE_NAME'
        fields = [
            {
                'name': 'col1',
                'type': 'TYPE1'
            },
            {
                'name': 'col2',
                'type': 'TYPE2'
            }
        ]
        actual = qy_factories.create_db_qy(table, fields)
        expected = 'CREATE TABLE IF NOT EXISTS TABLE_NAME (col1 TYPE1, col2 TYPE2);'
        self.assertEqual(actual, expected)

    def test_select_table_name_from_db_qy(self):
        db = 'DB'
        tb = 'TB'
        actual = qy_factories.select_table_name_from_db_qy(tb)
        expected = "SELECT name FROM sqlite_master WHERE type='table' AND name='TB' LIMIT 1;"
        self.assertEqual(actual, expected)

    def test_count_nrows(self):
        actual = qy_factories.count_nrows("TB")
        expected = "SELECT Count(*) FROM TB;"
        self.assertEqual(actual, expected)

        actual = qy_factories.count_nrows("TB", where='VAL=1')
        expected = "SELECT Count(*) FROM TB WHERE VAL=1;"
        self.assertEqual(actual, expected)


    def test_sum_col(self):
        actual = qy_factories.sum_col("TB", "COL")
        expected = "SELECT SUM(COL) FROM TB;"
        self.assertEqual(actual, expected)
        actual = qy_factories.sum_col("TB", "COL", where='VAL=1')
        expected = "SELECT SUM(COL) FROM TB WHERE VAL=1;"
        self.assertEqual(actual, expected)

    def test_strftime(self):
        actual = qy_factories.strftime("%H", "COL")
        expected = "strftime('%H', COL)"
        self.assertEqual(actual, expected)

    def test_What_get_all_from_sql_qy(self):
        table = "TABLE"
        what = ["COL1", "COL2"]
        actual = qy_factories.get_all_from_sql_qy(table, what=what)
        expected = "SELECT COL1, COL2 FROM TABLE"
        self.assertEqual(actual, expected)

    def test_select_groupby_time(self):
        table = "TABLE"
        meta = {
            'fmt': "FMT",
            'timecol': "TIMECOL",
            'others': ['col2', 'col3']
        }
        actual = qy_factories.select_groupby_time(table, meta)
        expected = "SELECT strftime('FMT', TIMECOL), col2, col3 FROM TABLE" +\
            " GROUP BY strftime('FMT', TIMECOL);"
        self.assertEqual(actual, expected)

        actual = qy_factories.select_groupby_time(table, meta,where='VAL=1')
        expected = "SELECT strftime('FMT', TIMECOL), col2, col3 FROM TABLE" +\
            " GROUP BY strftime('FMT', TIMECOL) WHERE VAL=1;"
        self.assertEqual(actual, expected)

    def test_noOthersselect_groupby_time(self):
        table = "TABLE"
        meta = {
            'fmt': "FMT",
            'timecol': "TIMECOL"
        }
        actual = qy_factories.select_groupby_time(table, meta)
        expected = "SELECT strftime('FMT', TIMECOL) FROM TABLE" +\
            " GROUP BY strftime('FMT', TIMECOL);"
        self.assertEqual(actual, expected)



    def test_allowedAggLevels(self):
        self.assertEqual(qy_factories.allowed_agg_levels(), ['year','month','day','hour','minute'])


    def test_agglevels_to_formats(self):
        self.assertEqual(qy_factories.agglevel_to_format('BLAH'), False)
        self.assertEqual(qy_factories.agglevel_to_format('hour'), '%Y-%m-%d %H')
        self.assertEqual(qy_factories.agglevel_to_format('minute'), '%Y-%m-%d %H:%M')
        self.assertEqual(qy_factories.agglevel_to_format('year'), '%Y')
        self.assertEqual(qy_factories.agglevel_to_format('month'), '%Y-%m')
        self.assertEqual(qy_factories.agglevel_to_format('day'), '%Y-%m-%d')


        for item in qy_factories.allowed_agg_levels():
            self.assertIsNot(qy_factories.agglevel_to_format(item), False)

    def test_select_distinct_months(self):
        actual = qy_factories.select_distinct_months('TB','DATE')
        expected = "SELECT DISTINCT strftime('%Y-%m', DATE) FROM TB ORDER BY strftime('%Y-%m', DATE) ASC;"
        self.assertEqual(actual, expected)


    def test_withoutOthers_select_distinct_dates(self):
        meta = {'fmt':'%Y-%m','timecol':'DATE'}
        actual = qy_factories.select_distinct_dates('TB',meta)
        expected = "SELECT DISTINCT strftime('%Y-%m', DATE) FROM TB ORDER BY strftime('%Y-%m', DATE) ASC;"
        self.assertEqual(actual, expected)


    def test_withOthers_select_distinct_dates(self):
        meta = {'fmt':'%Y-%m','timecol':'DATE','others':['one']}
        actual = qy_factories.select_distinct_dates('TB',meta)
        expected = "SELECT DISTINCT strftime('%Y-%m', DATE), one FROM TB ORDER BY strftime('%Y-%m', DATE) ASC;"
        self.assertEqual(actual, expected)

    
    def test_select_in_datetime(self):
        meta = {'fmt':'%Y-%m','timecol':'DATE', 'what':['c1','c2']}
        actual = qy_factories.select_in_datetime('TB',meta, '2017-05')
        expected = "SELECT c1, c2 FROM TB WHERE strftime('%Y-%m', DATE) = '2017-05';"
        self.assertEqual(actual, expected)
