FROM python:3.9

ENV TZ=Asia/Bangkok
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
# RUN apt-get update
# RUN apt-get update -qq && apt-get install -y -qq --force-yes cron
# RUN apt-get update && apt-get install vim -y && apt-get install nmap -y

WORKDIR /usr/src/app

COPY . .

# RUN apt-get update
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# RUN service cron start
# RUN cron

EXPOSE 4000
