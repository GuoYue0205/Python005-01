# 4. 以下两张基于 id 列，分别使用 INNER JOIN、LEFT JOIN、 RIGHT JOIN 的结果是什么?
# Table1
# id name
# 1 table1_table2
# 2 table1
# Table2
# id name
# 1 table1_table2
# 3 table2
# SELECT Table1.id, Table1.name, Table2.id, Table2.name
# FROM Table1
# INNER JOIN Table2
# ON Table1.id = Table2.id;

# INNER JOIN 符合条件Table1.id = Table2.id的数据会打印出来，不符合的以null填充
# LEFT JOIN 表示以左表table1为准，table1的记录会全部打印出来，符合条件Table1.id = Table2.id的table2数据会打印出来，不符合的以null填充
# RIGHT JOIN 表示以table2表为准，table2的记录会全部打印出来，符合条件Table1.id = Table2.id的table1数据会打印出来，不符合的以null填充