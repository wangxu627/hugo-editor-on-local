### 启动flask
```
export FLASK_APP=app.py
nohup flask run -p 3201 &
```

### 设置静态网页路径
```
server {
        listen       3100;
        server_name  localhost;
        
        location / {
            root   /data/data/com.termux/files/home/app/hugo-editor-on-local/published;
            index  index.html index.htm;
        }

        location /admin {
            proxy_pass  http://127.0.0.1:3201; # 转发规则
            proxy_set_header Host $proxy_host; # 修改转发请求头，让8080端口的应用可以受到真实的请求
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
```




