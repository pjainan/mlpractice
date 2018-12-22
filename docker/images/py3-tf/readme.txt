					Instructions to build and use this TensorFlow CPU docker image
					==============================================================

1. To build the docker image on the Ubuntu v18+, use the following command from the terminal:
	$ sudo docker build -t di-ubuntu-py3-tf .


2. Once the docker image is successfully build, use the following command to 'run' a container usuing the image
	$ sudo docker run -i -t di-ubuntu-py3-tf /bin/bash
