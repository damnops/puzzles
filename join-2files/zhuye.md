```
gawk 'NR==FNR{a[$1]=$1","$2","$3" "$4}NR!=FNR {b[$1]=$2","$3" "$4}END {for (i in a) {print a[i]","b[i]}}' file2.txt file1.txt > newfile
```

使用`gawk`是因为mac下面的原生`awk`不支持一些高级功能

awk多文件还有以下几种办法：

1、ARGIND 当前被处理参数标志: 
```
awk 'ARGIND==1{...}ARGIND==2{...}ARGIND==3{...}... ' file1 file2 file3 ...
```
2、ARGV 命令行参数数组: 
```
awk 'FILENAME==ARGV[1]{...}FILENAME==ARGV[2]{...}FILENAME==ARGV[3]{...}...' file1 file2 file3 ...
```
3、把文件名直接加入判断: 
```
awk 'FILENAME=="file1"{...}FILENAME=="file2"{...}FILENAME=="file3"{...}...' file1 file2 file3 ... 
```
第三种没有前两种通用，因为需要判断文件名。

NR和FNR这种模式只能支持两个文件对比，超过两个文件就不行了。