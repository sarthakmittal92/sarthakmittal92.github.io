# Docker Scripts

CS747 Docker Instructions: https://tinyurl.com/5n7tawvw

CSE Virtual Lab: https://tinyurl.com/268wcw2a

In the [setup](./setup/) folder, run:
```js
chmod 755 *.sh
```

[Docker Setup](./setup/install.sh):
- install docker and other packages
- usage:
```js
./install.sh
```

[CS747 Docker Image](./setup/cs747.sh):
- pull CS747 docker image
- usage:
```js
./cs747.sh
```

In the [scripts](.) folder, run:
```js
chmod 755 *.sh
```

[Initialize](./init.sh):
- create and start new docker image
- arguments: docker image name
- usage:
```js
./init.sh cs747-assgn-1
```

[Run](./run.sh)
- start existing docker image
- arguments: docker image name
- usage:
```js
./run.sh cs747-assgn-1
```

[Quit](./quit.sh)
- stop existing docker image
- arguments: docker image name
- usage:
```js
./quit.sh cs747-assgn-1
```

[Delete](./delete.sh)
- delete existing docker image
- arguments: docker image name
- usage:
```js
./del.sh cs747-assgn-1
```

[List](./list.sh)
- list all existing docker images
- usage:
```js
./list.sh
```

Once a docker image is up and you have access to docker shell, your local files can be accessed at '/host'.