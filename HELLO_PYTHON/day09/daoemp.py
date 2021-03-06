import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='python', charset='utf8')
        #pymysql.cursors.DictCursor 딕션러니(json) 형태로 만들어줌...
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    def select(self,e_id):
        sql = f"""
            select e_id,e_name,sex,addr 
            from emp
            where e_id='{e_id}'
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows[0]
    
    def selects(self):
        sql = "select * from emp"
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows
        
    def insert(self,e_name,sex,addr):
        sql = f"""
            insert into emp
                (e_name,sex,addr)
            values 
                ('{e_name}','{sex}','{addr}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    def update(self,e_id,e_name,sex,addr):
        sql = f"""
            update emp
            set
                e_name = '{e_name}',
                sex = '{sex}',
                addr = '{addr}'
            where
                e_id = '{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    def delete(self,e_id):
        sql = f"""
            delete from emp 
            where e_id='{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    cntInsert = de.insert('99','9','99')
    print("cntInsert " ,cntInsert)
    
    # cntUpdate = de.update('19', '9', '9', '9')
    # print("cntUpdate " ,cntUpdate)
    
    # cntDelete = de.delete('19')
    # print("cntDelete",cntDelete)