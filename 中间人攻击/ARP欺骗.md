# 0x01 网络传输简介

![image-20240402103216330](images/image-20240402103216330.png)

用户访问网站时发生了什么

* 浏览器先向DNS服务器发送请求目标网站demo的IP
* DNS收到请求后响应浏览器目标网站demo的IP为192.168.1.1
* 浏览器通过HTTP协议，完成应用层数据封装，向目标网站IP发送请求
* 网站收到请求后响应对应数据

![image-20240402105635440](images/image-20240402105635440.png)

根据TCP/IP传输协议

* 浏览器封装的HTTP DATA数据，到传输层将添加TCP头部信息（源端口、目的端口）
* 到网络层，需要添加IP头部信息（源IP、目的IP）
* 到数据链路层，添加Ethernet头部信息（源MAC、目的MAC地址）和`FCS帧尾`后，将数据帧传给物理层
* 到物理层，根据物理介质的不同，将数字信号转换为电信号、光信号、电磁波信号，转换完成后进行网络传输

说明

* 从应用层到传输层，需要的源端口随机分配，目的端口由服务器应用指定

* 从传输层到网络层，需要目的IP，这就是DNS请求获取到的IP地址
* 从网络层到数据链路层，需要目的MAC地址，这个的获取就需要用到**ARP协议**了



# 0x02 ARP （Address Resolution Protocol）地址解析协议

ARP协议是一种网络层协议，作用是根据目的IP地址解析对应的MAC地址。在局域网中，每台设备的MAC地址唯一，而IP是可以重复分配的，因此当需要发数据到另一台设备时，需要知道对应的MAC地址。

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSS8VS49NujaAryX1k0PRhxQIhEmBI2fkibVTWVKSYQdYA8L7vy9qTicibw.png)

ARP工作原理：每台设备都有一个`ARP缓存表`，存放IP和MAC地址的关联信息。在发送数据前，先查找ARP缓存表，如果缓存表中存在目的IP对应的MAC地址，则直接使用该MAC地址进行封装帧；如果不存在，则通过ARP来获取。

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSRVJg1JicSY2PJoT46tdXGLZC55ev0ZZKObn5872y5Hz7ZEqhCgKKUsQ.png)

当ARP缓存表为空时，主机1通过发送ARP Request报文来获取主机2的MAC地址，由于不知道目的IP，因此ARP Request请求内的目的MAC为`广播地址FF-FF-FF-FF-FF-FF`，因为是广播数据帧，交换机收到后，会对该帧进行泛洪广播（向该局域网内所有主机包括网关，发送ARP request请求报文）![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSWP56UIcic54Vga460whzHn9l0ah1dqiafKibx5hXkbRtAXMdz0Uud9QaQ.png)

局域网内所有主机收到ARP Request报文后，检查报文的目的IP和自身的IP是否匹配。当主机2发现IP匹配时，**将ARP报文中的发送端MAC低和发送端IP地址添加到自身的ARP缓存表**。

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSL5SUnZ3ibP37YCSiaU1dQ58yarQuOukZ4SXnO7HGICCyPYuvUh83u46w.png)

主机2通过ARP Reply报文响应主机1的请求，此时主机2已知主机1的MAC地址，因此ARP Reply是单播数据帧。![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJScOdFkibPwImJZI5iaHnvT0hEWdiaVBmfQLNWgoShQwyz9eC4pjcRmsy9w.png)

主机1收到ARP Reply后，检查ARP报文中目的IP和自身IP是否匹配，如果匹配，则将ARP报文中的发送端MAC和IP记录到主机1的ARP缓存表中。

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSl9RDpOaVghfv6tJfl35S8L37nyaEFOnpYeFEFsjFNJSwmnQicL0NiapA.png)

至此，ARP工作结束，获取到目的IP对应的MAC地址后，发送帧。

# 0x03 ARP欺骗

## 0x 3.1 单向欺骗

攻击者伪造ARP Request将自己的MAC地址伪装成网关IP相对应的MAC地址广播出去，主机A收到该ARP Request后将原网关IP对应的MAC地址修改为攻击者MAC地址写入ARP缓存表，然后发送ARP Reply，将本该传输给网关的数据错误的传给攻击者，使得主机A得不到网关的响应数据，导致断网。

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJS8bJ9XYbNr3z4SpRNP5ibWic2jt843qEREv6IGjCZkAFHTXsHDd6lhScA.png)

实现过程，先查看主机A的ARP缓存表，192.168.45.2当前就是系统的网关地址，主机A是可以正常上网的。

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSkf8icLIUQr1XFnmQx8fjSaaRRsW0R1E6dj6sjOzO27xN0rupnxaru2g.png)

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSnDVaqQ6yxTibsibRuYgzBR72Oq378wZ0PIFMPNa6TAFXKsr5uDoCrfiaA.png)

构造一个IP地址为192.168.45.2的虚假MAC地址的ARP Request数据包。使用科莱网络分析系统工具，首先对当前网段MAC地址进行扫描，获取到主机A的MAC地址

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSkYZHKDnFVMNWwBsmabNCDYVACdgZ12XThLodXjIh6RibCia8bRpILcaQ.png)

生成数据包

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSh7TUtb2rOVswhmjG3IicOA0AVxWQicrKZZqlrTpsBwAWMcDibvY0wRT6w.png)

添加ARP数据包

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSUwQrS5hTw1vV9DAdy1KiaPDfqDunHd97Hh4J8tUs8OrvXt40bFf1wUw.png)

输入目的MAC和目的IP（主机A），源MAC地址任意即可，源IP地址输入网关IP地址

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJS9rEGjgmsAibVll4DJ6ibDCp82KaNpZjbvEDbtN52ZHKCNcljicSrhiaexg.png)

点击循环发送

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSU9DRGibCRtg0Yavx7ClhYUPrJp22rnr1fUn9N5RN8RzQSLibIvKXJzwg.png)

抓包看一下当前网络状况，源MAC为00-01-02-03-04-05（这是攻击者伪造的）寻找目的IP地址为192.168.45.131的ARP Request已经发出

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSsUV0qA3Fv2ibQ10Qt37jDmzh9hn20lQGmKoOugKibw1HJVSTtKkoCEDw.png)

查看主机A的ARP地址表变化，对应网关IP192.168.45.5的MAC地址已经修改成攻击者伪造的MAC地址，主机A此时无法上网

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSHd0YcR6N5uYpu4ibR1F8ic4dE5Wzc2IAgzg0od1vR2OPP5Tp7cwtVyKQ.png)

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSBy8jvHJpzicug2zAppnxMDs6FwAiaRDlibtwHSyU08dmNCY6M0U63uInQ.png)

## 0x 3.2 双向欺骗

攻击者一直发送伪造的ARP Reply，欺骗网关自己是主机A，同时欺骗主机A自己是网关，同时开启路由转发功能，就可以让主机A在正常上网的情况下，攻击者截获主机A和网关通信的数据包。

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSFvfibZsicMP3oFrvUgFibfttrZWib2H14O3YWQ1VQib3lsw8l3ibxr0jALkQ.png)

实现过程，Kali Linux自带的`arpspoof`工具，先在kali上开启数据转发功能

```
# 终止
echo 0 > /proc/sys/net/ipv4/ip_forward
# 允许
echo 1 > /proc/sys/net/ipv4/ip_forward
```

kali攻击机的MAC地址为`00:0C:29:4B:AE:FB`，使用arpspoof进行双向毒化攻击

```
arpspoof -i eth0 -t 192.168.45.143 -r 192.168.45.2
```

抓包查看当前网络情况，同时发出了两个ARP Reply，源IP分别为网关和主机A，源MAC为攻击机的MAC地址

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJShCdplibtAaNG0CVVyFNfByaUyFweEicHVHHd64RXAB6iaQMwENDw0nxcw.png)

查看主机A的ARP缓存表，192.168.45.2对应的MAC地址为攻击机MAC，主机A可以正常上网

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSolD9micXy1fEkLicJGAWG869q0QJuZR4WgA7IbQ6Y7CPf80av2ypZVMA.png)

ARP双向欺骗可以实现流量劫持、DNS劫持。假设主机A想访问百度，可以毒化DNS让主机A跳转到钓鱼网站，使用kali的ettercap工具，使用前先修改DNS配置文件

```
$ vim /etc/ettercap/etter.dns
# 添加DNS解析
*.baidu.com A 192.168.45.129<钓鱼网站IP>
```

打开ettercap，点击开始

```
ettercap -G
```

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSBOMohWq6N3RePpq8jdkJYownA7ytapMltK2AV1RAgvJpSjNmFHiaibsg.png)

扫描当前网络

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSLEDG5LFwo9VSAtiaysgBB4Muicicj1ZLHBZS1xOhlAh48iaseg5k1Fyib8Q.png)

将目标主机和网关分别添加到Target1和2中

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSAGjaYFuVibryDGricPFB8XnhwWbibkkNftkvjnRHIo5NI6DicfPaClzicgw.png)

添加完成后，打开ARP poisoning，选择Sniff remote connections，点击OK

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSnXsSCM0zq3A28ptVGC2tmibm79tzUZVDLhpibf6D9mG0xrmf4cuwibUng.png)

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSptNtqPictooYXiaQU5iaOib1mpbCldueQceHPbqjjW4IibaHicIPdfpssISw.png)

选择Plugins-Manager Plugins，勾选DNS_Spoof

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSDmPlex3p4FpIUhPsLPQW7bmoTrX4jOz53z8hYKaYK0GCxU0t6pP28Q.png)

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSB0huwEG9mvP5Ysia4bAHCHic1q8OPIz65Gy3q0jYxyFicoOicibufs1Libibw.png)

点击start开始

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSEI9CdxwhhrkzkJcvH0cO4UWOHUS8icQghekRZJc714iazoE1QJB0p4yQ.png)

再次访问百度跳转到钓鱼网站

![img](images/rTicZ9Hibb6RX6f7JooorQ71iaEPFgHGDJSDVODticgcca5WIpCiaibq7RPseGQ9jtBhwsmyFblAVUFPwc6tzQ33JcQg.png)