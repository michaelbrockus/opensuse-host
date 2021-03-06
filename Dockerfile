#
# author: Michael Brockus.
# gmail: mailto:michaelbrockus@gmail.com
#
FROM opensuse/tumbleweed:latest

ENV DEBIAN_FRONTEND noninteractive
ENV LANG 'C.UTF-8'
ENV CI 1

RUN zypper --non-interactive patch --with-update --with-optional && zypper --non-interactive update \
    && zypper install -y \
       python3-devel \
       python3-pip \
       python3-wheel \
       python3-setuptools \
       clang \
       git \
       ccache \
       cppcheck \
       gcc \
       gcc-c++ \
       gcc-d \
       rust \
       cargo \
       java-14-openjdk-devel \
       openssh \
    && zypper --non-interactive clean --all

RUN pip3 -q install --upgrade pip \
    && python3 -m pip -q install \
       meson==0.57.1 \
       pyinstaller==4.0 \
       ninja==1.10.0.post2 \
       cmake==3.18.2.post1 \
       PyQt5==5.15.1 \
       pytest==6.1.2 \
       pytest-mock==3.3.1 \
       pytest-xdist==2.1.0 \
       pytest-benchmark==3.2.3
