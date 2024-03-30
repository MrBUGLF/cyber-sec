# cyber-sec
个人安全手册【持续更新】

![GitHub Repo stars](https://img.shields.io/github/stars/MrBUGLF/cyber-sec?style=for-the-badge&logo=undertale&logoColor=red&label=STARS&color=gold)



## 渗透测试PTES流程

### 0x01 明确目标

* 目标IP/域名范围
* 测试时间
* 测试内容（Web应用漏洞、业务逻辑漏洞、APP漏洞等）
* 测试强度(提权/getshell/脱库/DDOS等)

### 0x02 信息收集

* 网络信息：IP、域名/子域名、端口
* 系统信息：操作系统版本
* 应用信息：各端口对应的应用
* 中间件信息：服务器版本、中间件版本（redis、shiro等）

**可用工具**:
* :bulb: [SiteScan](https://github.com/kracer127/SiteScan): 集成域名ip历史解析、nmap常见端口爆破、子域名信息收集、旁站信息收集、whois信息收集、网站架构分析、cms解析、备案信息收集、CDN信息解析、是否存在waf检测等功能
* :bulb: [wappalyzer](https://www.wappalyzer.com/): 网站指纹识别插件
* :bulb: [WhatWeb](https://github.com/urbanadventurer/WhatWeb): 网站指纹识别工具
* :bulb: [dirsearch](https://github.com/maurosoria/dirsearch): 网站目录扫描

### 0x03 威胁建模

* 识别主要和次要资产并对其进行分类
* 针对目标资产，以攻击者视角确认目标可能存在威胁类型
* 制定测试计划

**可用工具**:
* :bulb: [STRIDE 模型](https://learn.microsoft.com/zh-cn/azure/security/develop/threat-modeling-tool-threats#stride-model)
* :bulb: [微软威胁建模工具](https://aka.ms/threatmodelingtool)
* :bulb: [OWASP威胁建模工具](https://github.com/mike-goodwin/owasp-threat-dragon)
### 0x04 漏洞检测

* 漏扫工具：AWVS、AppScan等
* 公开的POC/EXP
* 手动挖掘：BurpSuite + Xray等

### 0x05 漏洞利用

* 根据检测到可能存在漏洞的点进行具体利用, 包括bypass waf/AV/shellcode等
* 记录攻击路径和过程

### 0x06 后渗透攻击

* 内网横向移动
* 账户提权
* 持续性后门维持
* 痕迹清理

### 0x07 报告输出

* 梳理漏洞位置、漏洞类型、风险等级、漏洞POC/EXP，输出到报告模板


## 参考文档
* http://www.pentest-standard.org/