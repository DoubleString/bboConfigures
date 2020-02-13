1) 在安装bbo_postrtk脚本后，将观测值和广播星历拷贝到对应路径，执行以下命令，可以生成基线的大气
 bbo_postrtk.sh 2015 11 21 0 0 0 86400 30 sitlist_gd_rtk bslines.out G S Y 
大气文件在对应的目录下:   xxxx/rtk/2015325/results_sav/ionambcon*  ztdambcon*

2) 将大气信息拷贝至vrs/results_sav/下，执行以下命令
./bboVrs -mode vrs vrs.json -debug -post
可以生成虚拟参考坐标下的虚拟文件vrs/results_sav/fsgh3250.15o,以及内插的大气和真实的大气vrs/ion_interpxxx vrs/ztd_interpxxx等文件
利用matlab文件diffion.m可以绘制它们的差异

3）将vrs/results_sav/fsgh3250.15o文件拷贝至rtk_verify/obs/vr013250.15o,可以进行rtk模拟定位
./bamboo -mode rtk rtk.json -post -itrs -iar 
结果生成为rtk_verify/results/pos_2015325

目前这个测试是以GDEP为基准站,内插FSGH站的大气信息
也可自己选站进行内插实验,做相关大气内插测试.









