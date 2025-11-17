
# install clamav in yoir device (mac, linux, windows, ec2 machine )
# or run it as docker container

/opt/homebrew/etc/clamav/freshclam.conf 

bash```

# Comment out Example line
# Example

# Custom paths
DatabaseDirectory /Users/akhilesh/projects/python-for-devops-bootcamp/class3/clamav/db
UpdateLogFile /Users/akhilesh/projects/python-for-devops-bootcamp/class3/clamav/logs/freshclam.log
PidFile /Users/akhilesh/projects/python-for-devops-bootcamp/class3/clamav/freshclam.pid

# Database mirror
DatabaseMirror database.clamav.net

# Checks per day
Checks 24

```

mkdir -p /Users/akhilesh/projects/python-for-devops-bootcamp/class3/clamav/{db,logs}

vi /opt/homebrew/etc/clamav/freshclam.conf


# Update the db 

freshclam