backup_repos
============

需求  
1. 有些项目不想占用star的list  
2. 需要的时候找出来  
3. 防止有些项目中途被删除时找不到  

做了这个脚本   

使用时的目录结构:  
├─ backup.py  
├─ git  
└─ list  

list里面随时添加需要备份的github项目地址  
crontab里面定时执行python 路径/backup.py即可
