# postgres_copy
## 脚本说明：
CVE-2019-9193 postgres数据库的copy函数导致的命令执行漏洞
漏洞版本 9.3 <= postgres version <= 11.2

从版本9.3开始，Postgres新增了一个“COPY TO/FROM PROGRAM”功能。
这个功能简单来说就是允许数据库的超级用户以及pg_read_server_files组中的任何用户执行操作系统命令。

## 脚本应用:
本脚本用于实现Postgres数据库的远程连接，同时利用漏洞，使用COPY函数执行系统命令，并获取回显的结果。

## 可能出现问题:
代码在执行的过程中可能会由于编码的问题报错，导致执行的结果无法回显的问题。
例如，在windows当中，可以使用certutil进行base64编码后输出，如下：
dir > 1.txt && certutil -encode 1.txt 2.txt
certutil -encode postgresql.conf 2.txt
这样可以解决编码报错，无法得出执行结果的问题。
