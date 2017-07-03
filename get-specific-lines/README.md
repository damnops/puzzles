## 问题描述

现有文件(ofile.txt)内容如下，我只需要有机器名的那行。

```
ap-southeast-2b
 
i-840a024b
 
1form/prod_migration
 
t2.micro
 
$9.87
 
0.0%
 
0.00MB
 
12
 
...........
 
ap-southeast-2a
 
i-008a9b8b2b0a46e0e
 
1form/b_admin
 
c3.large
 
$74.67
 
0.2%
 
0.06MB
 
11
```

即最后输出结果如下：

```
1form/prod_migration
...........
1form/b_admin
```

