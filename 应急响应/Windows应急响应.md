## 1、系统账号

```bash
#查询当前登录系统的会话
query user

#把用户踢出会话
logoff ID
```

打开`lusrmgr.msc`，查看是否有新增/可疑的账号

用D盾 -> 查看服务器是否存在隐藏账号、克隆账号

## 2、网络连接

```bash
#查看本机所有的tcp,udp端口连接及其对应的pid
#可用findstr过滤，类似Linux的grep命令
netstat -ano

#打印路由表
route print

#查看网络代理配置情况
REG QUERY "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings"
```

## 3、进程 

```bash
#列出所有进程
tasklist

#强制停止某进程
taskkill /T /F /PID
```



## 4、启动项 

```bash
#查看系统开机时间
net statistics workstation

#查看系统计划任务
schtasks /query /fo LIST /v

#查看程序启动信息
wmic startup get command,caption

#查看主机服务信息
wmic service list brief
```

## 5、杀软工具

火绒-火绒剑：https://www.huorong.cn/

## 6、日志审计

运行框输入`eventvwr.msc`，打开事件查看器

**系统日志**

> 记录操作系统组件产生的事件，主要包括驱动程序、系统组件和应用软件的崩溃以及数据丢失错误等。 系统日志中记录的时间类型由Windows NT/2000操作系统预先定义。 默认位置：`%SystemRoot%System32WinevtLogsSystem.evtx`

**应用程序日志**

> 包含由应用程序或系统程序记录的事件，主要记录程序运行方面的事件 例如数据库程序可以在应用程序日志中记录文件错误，程序开发人员可以自行决定监视哪些事件。 如果某个应用程序出现崩溃情况，那么我们可以从程序事件日志中找到相应的记录，也许会有助于你解决问题。 默认位置：`%SystemRoot%System32WinevtLogsApplication.evtx`

**安全日志**

> 记录系统的安全审计事件，包含各种类型的登录日志、对象访问日志、进程追踪日志、特权使用、帐号管理、策略变更、系统事件。 安全日志也是调查取证中最常用到的日志。 默认设置下，安全性日志是关闭的，管理员可以使用组策略来启动安全性日志 或者在注册表中设置审核策略，以便当安全性日志满后使系统停止响应。 默认位置：`%SystemRoot%System32WinevtLogsSecurity.evtx`

系统和应用程序日志存储着故障排除信息，对于系统管理员更为有用。

安全日志记录着事件审计信息，包括用户验证（登录、远程访问等）和特定用户在认证后对系统做了什么，对于调查人员而言，更有帮助。

**对于Windows事件日志分析，不同的EVENT ID代表了不同的意义**

| 事件ID | 说明                             |
| :----- | :------------------------------- |
| 4624   | 登录成功                         |
| 4625   | 登录失败                         |
| 4634   | 注销成功                         |
| 4647   | 用户启动的注销                   |
| 4672   | 使用超级用户（如管理员）进行登录 |
| 4720   | 创建用户                         |