# 说明
在EVM过滤注释结果后，得到的注释文件中的基因名比较混乱。

因此，可以通过gffutils来对所有的基因进行重命名。

使用的python脚本参考了https://www.jianshu.com/p/e2f13e2f42ba

命名原则:物种名+染色体号+基因序号
# 过程：
先解决配置文件bed.txt
```
chr01	Fh01
chr02	Fh02
chr03	Fh03
chr04	Fh04
chr05	Fh05

```
由于python脚本仅对bed中的chr进行重命名，这里没有保留较短的scaffold，所以就先去掉注释文件中的scaffold，否则会报错
```
grep -v scaffold fh.gff3 > fh_clean.gff3
```
然后一步搞定
```
python rename_gff.py -g fh_clean.gff3 -c bed.txt
```
# 此外
因为Fh这个物种原有注释文件中的染色体号是'Hic_asm_*'这种格式，因此在配置bed.txt前

使用**TBtools**中的**Batch String Replace**先对原有的scaffold进行了更改

改名文件格式如下
```
Hic_asm_0	chr01
Hic_asm_1	chr02
Hic_asm_2	chr03
Hic_asm_3	chr04
Hic_asm_4	chr05
```
### 结束啦，是不是很简单~
