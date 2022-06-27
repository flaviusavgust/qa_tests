FROM budtmo/docker-android-x86-8.1:latest

EXPOSE 6080 5554 5555 4273

WORKDIR /root

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash

RUN apt-get update && apt-get install -y \
    apt-utils \
    nodejs \
    python3.8 \
 && rm -rf /var/lib/apt/lists/*

RUN npm install -g \
    appium@next \
    appium-doctor

RUN appium-doctor --android

RUN wget https://github.com/allure-framework/allurectl/releases/latest/download/allurectl_linux_386 -O ./allurectl \
 && chmod +x ./allurectl \
 && mv allurectl /bin

CMD ["/bin/sh", "-c", "/usr/bin/supervisord --configuration supervisord.conf"]
