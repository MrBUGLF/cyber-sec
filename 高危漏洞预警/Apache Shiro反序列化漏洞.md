## 1.漏洞原理

Apache Shiro是一款java安全框架，提供身份验证、授权、密码学和会话管理。

该框架提供记住密码功能（RememberMe），用户登录成功后会生成经过加密并编码的cookie，在服务端接收cookie后，再进行Base64解码->AES解密->反序列化。

攻击者只要找到AES加密的密钥，就可以构造恶意攻击对象，对其进行序列化->AES加密->Base64编码，然后将其作为cookie的RememberMe字段发送，shiro将RememberMe进行解密并且反序列化执行。

在 1.2.4 版本前,是默认ASE秘钥,Key: kPH+bIxk5D2deZiIxcaaaA==,可以直接反序列化执行恶意代码 		在1.2.4之后,ASE秘钥动态生成,需要获取到Key才可以进行渗透

## 2.漏洞复现

https://blog.csdn.net/m0_46363249/article/details/122259407