# Run these commands from a fresh RHEL Ec2 Instance.
    # Installing jenkins
sudo yum check-update
sudo yum install wget
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
yum install fontconfig java-11-openjdk
yum install jenkins
sudo systemctl enable jenkins # I believe this allows jenkins to start when the ec2 boots.
sudo systemctl start jenkins # This one takes a bit to complete (duh)
    # Checking the status of jenkins
sudo systemctl status jenkins

sudo cat /var/lib/jenkins/secrets/initialAdminPassword # Gets the initial setup password, use this to unlock Jenkins
# I went ahead and installed the suggested plugins. They can be managed later.

    # User: jeff
    # Pass: qwer1234QWER!@#$
    # URL:  http://3.21.129.236:8080/

    # At this point in time I'm using the built in node.