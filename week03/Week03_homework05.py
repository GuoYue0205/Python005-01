# 5. 使用 MySQL 官方文档，学习通过 sql 语句为上题中的 id 和 name 增加索引，并验证。根据执行时间，增加索引以后是否查询速度会增加？请论述原因，并思考什么样的场景下增加索引才有效。
添加主键索引：ALTER TABLE 'table1' ADD PRIMARY KEY （'id')  # 主键
添加唯一索引：ALTER TALBE 'table1' ADD UNIQUE KEY('id') # 不会重复的字段添加
添加普通索引：ALTER TABLE 'table1' ADD INDEX index_name('id') # 一般使用普通索引
添加全文索引：ALTER TABLE 'table1' ADD FULLTEXT ('id') # 基本不会使用到？
添加多行索引： ALTER TABLE 'table1' ADD INDEX ('id','name') # 多行索引对顺序有要求 如where后必须为id=xxx and name=xxx

# 结论：
# 当表中的数据特别多，需要快速找到时，增加索引会加快查询速度，但如果表数据很少，整表查询反而速度更快，无需添加索引