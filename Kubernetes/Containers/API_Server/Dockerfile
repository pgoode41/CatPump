FROM ubuntu


ARG '/opt/CatPump/'

ARG projectDir='/opt/CatPump/'
ENV var=${var}

RUN apt update -y
RUN apt upgrade -y
RUN apt install python3-pip -y
RUN apt install wget -y
RUN apt install unzip -y
RUN pip3 install numpy
RUN pip3 install Flask
RUN pip3 install requests



RUN mkdir ${projectDir}


ENV CATPUMPDIR=${projectDir}
ENV DEBIAN_FRONTEND=noninteractive

ADD CodeStore ${projectDir}
RUN mkdir ${projectDir}pre-dataset
RUN mkdir ${projectDir}dataset

RUN chmod +x ${projectDir}installOpenCV4.sh
RUN chmod +x ${projectDir}kickstart.sh

RUN ${projectDir}installOpenCV4.sh
RUN cd ${projectDir}

CMD [ "/opt/CatPump/kickstart.sh"]