# 1. 在 Linux 环境下，安装 MySQL5.6 以上版本，修改字符集为 UTF8mb4 并验证，新建一个数据库 testdb，并为该数据库增加远程访问的用。
# 将修改字符集的配置项、验证字符集的 SQL 语句作为作业内容提交
# 将增加远程用户的 SQL 语句作为作业内容提交
# 查看mysql字符集
show variables like '%character%';
# 查看校对规则
show variables like 'collation_%';
# 修改字符集
vim /etc/my.cnf
# 增加远程用户
GRANT ALL PRIVILEGES ON *.* TO 'xxx'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;