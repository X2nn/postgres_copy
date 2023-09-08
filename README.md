# postgres_copy

CVE-2019-9193 postgres copy函数 命令执行漏洞
漏洞版本 9.3 <= version <= 11.2

说明：
从版本9.3开始，Postgres新增了一个“COPY TO/FROM PROGRAM”功能。这个功能简单来说就是允许数据库的超级用户以及pg_read_server_files组中的任何用户执行操作系统命令
