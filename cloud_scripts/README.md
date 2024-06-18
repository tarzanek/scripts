Various helper scripts
-------------------------

HTTP Server
-----------
Quick HTTP server mock, can listen on multiple ports and addresses
```
$ python3 listen_on_ports.py -a 10.0.2.15 -p 1111 -p 2222 -p 3333
```

```
$ curl 10.0.2.15:2222
up
```

Port Checker
------------
Checks for open ports, if they are listening(default timeout 2s, can be changed):
```
$ python3 check_ports.py -r 10.0.2.15 -p 2222 -p 1111 -p 3333
```

alt. use netcat
```
$ nc -zv 10.0.2.15 2222
Connection to 10.0.2.15 2222 port [tcp/*] succeeded!
```
