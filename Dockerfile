FROM jenkins/inbound-agent
USER root
RUN mkdir -p /home/jenkins && chown jenkins:jenkins /home/jenkins