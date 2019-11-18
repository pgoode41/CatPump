FROM ubuntu


ARG '/opt/CatPump/'

ARG projectDir='/opt/CatPump/'
ENV var=${var}

RUN apt update -y
RUN apt upgrade -y
RUN apt install python3-pip -y
RUN pip3 install numpy
RUN pip3 install Flask
RUN pip3 install 



RUN mkdir ${projectDir}


ENV CATPUMPDIR=${projectDir}

ADD CodeStore /CodeStore

RUN chmod +x /CodeStore/installOpenCV4.sh
RUN chmod +x /CodeStore/kickstart.sh

RUN /CodeStore/installOpenCV4.sh
RUN cd /CodeStore

CMD [ "./kickstart.sh $CATPUMPDIR" ]