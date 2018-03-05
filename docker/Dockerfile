FROM ubuntu:artful

# choose a character set
RUN apt-get clean && apt-get update
RUN apt-get install locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

# misc prerequisites
RUN apt update
RUN apt install -y tcpdump net-tools locales \
  python3.6 python3-venv python3-pip

# pydatalog
RUN pip3 install pyDatalog sqlalchemy mypy coconut

EXPOSE 8182

CMD ["/bin/bash"]
