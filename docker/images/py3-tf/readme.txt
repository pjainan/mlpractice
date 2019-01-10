					Instructions to build and use this TensorFlow CPU docker image
					==============================================================

1. To build the docker image on the Ubuntu v18+, use the following command from the terminal:
	$ sudo docker build -t di-ubuntu-py3-tf .


2. Once the docker image is successfully build, use the following command to 'run' a container usuing the image
	$ sudo docker run -i -t --rm -v $(pwd):/remote:rw di-py3-tf-base /bin/bash

		The command has following options:
			-t: flag assigns a pseudo-tty or terminal inside the new container
			-i: flag allows you to make an interactive connection by grabbing the standard input (STDIN) of the container
			--rm: flag automatically removes the container when the process exits
			-d: Run the container as the daemon
			-v: is a volume mounting HOST DIRECTORY:CONTAINER DIRECTORY.
			-p: (*) is a ports mapping HOST PORT:CONTAINER PORT
