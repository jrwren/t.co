uwsgi_python -H . --socket 127.0.0.1:9001 -d uwsgi.log --module tco --callable app \
--stats 127.0.0.1:9002
