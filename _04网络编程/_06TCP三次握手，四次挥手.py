"""
三次握手：
第一次握手：客户端发送SYN请求包
第二次握手：服务器接收到SYN请求包后，发送回复确认收到包(SYN+ACK)
第三次握手：客户端接收到(SYN+ACK)包后，发送回复确认包(ACK)，此时网络连接的握手成功，进行数据传递

数据传递：
第三次握手的同时，客户端会把真正HTTP数据(底层是TCP协议(底层是IP协议))发送给服务器，服务器接收到请求后，发送回复确认收到包(ACK)，同时查询数据结果返回给客户端
客户端接收到数据结果的时候通过浏览器渲染呈现在网页上，数据传递过程完成，此时，客户端把这次请求套接字socket关闭，进行四次挥手

四次挥手：
第一次挥手：客户端发送FIN+ACK关闭请求包                                                   （FIN sequence=0,ACK=0）0,0
第二次挥手：服务器接收到FIN+ACK请求包后，发送回复确认包ACK                                  （ACK=sequence+1）1
第三次挥手：服务器在发送FIN包的同时调用自己的socket.close()方法发送FIN请求关闭包             （FIN sequence=ACK+1）2
第四次挥手：客户端接收到ACK请求包后，发送回复确认包ACK，服务器接到ACK包后关闭此次套接字socket，
           客户端在2msl时间如果没有收到服务器请求说明服务器已经收到确认信息关闭服务器socket了，
           此时客户端就会关闭此次套接字socket，此时四次挥手过程成功                         （ACK=sequence+1）3

"""