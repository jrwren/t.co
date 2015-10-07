# t.co
intercept t.co requests and add them to a silly file database

This is a silly hack that I did 2 years ago and I haven't touched it sense.
I was/am weary of twitter using t.co to mine behavior about me and I
thought it would be interesting to collect data about myself over time.
I wanted a collection of all the t.co redirects that I clicked. It would
be interesting to see which urls were popular, etc.

I wrote this with no scalability in mind, hence json file as a db.

I run household DNS and so redirect all of t.co for my household to
this proxy.

In my /etc/bind/named.conf.local, I include this line `zone "t.co" { type master; file "/etc/bind/t.co";};`. The file contents of `/etc/bind/t.co` are:
```
$TTL	604800
@	IN	SOA	t.co. jrwren.xmtp.net. (
			     3		; Serial
			 604800		; Refresh
			  86400		; Retry
			2419200		; Expire
			 604800 )	; Negative Cache TTL
;
@			IN	NS		t.co.
@			IN	A		192.168.1.2
```

192.168.1.2 is my home server.

This is good clean http interception fun.
