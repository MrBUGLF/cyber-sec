# cyber-sec
个人安全手册【持续更新】

![GitHub Repo stars](https://img.shields.io/github/stars/MrBUGLF/cyber-sec?style=for-the-badge&logo=undertale&logoColor=red&label=STARS&color=gold)



## 渗透测试PTES流程

### 0x01 明确目标

* 确认目标IP/域名范围
* 确认测试时间和测试内容（Web应用漏洞、业务逻辑漏洞等）

### 0x02 信息收集

* 网络信息：IP、域名/子域名、端口
* 系统信息：操作系统版本
* 应用信息：各端口对应的应用
* 中间件信息：服务器版本、中间件版本（redis、shiro等）

### 0x03 威胁建模

* 将收集到的信息进行分析，以攻击者视角确认目标可能存在弱点范围，制定测试计划

### 0x04 漏洞检测

* 漏扫工具：AWVS、AppScan等
* 公开的POC/EXP
* 手动挖掘：BurpSuite + Xray等

### 0x05 漏洞利用

* 攻击路径

### 0x06 后渗透攻击

* 内网横向移动
* 账户提权
* 持续性后门维持
* 痕迹清理

### 0x07 报告输出

* 梳理漏洞位置、漏洞类型、风险等级、漏洞POC/EXP，输出到报告模板


## 参考文档
* http://www.pentest-standard.org/