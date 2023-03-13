sudo apt-get update
sudo apt-get install docker.io
docker run -it --rm -d -p 80:80 --name web nginx
