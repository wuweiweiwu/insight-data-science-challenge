#!/usr/bin/env bash

# install dependencies for mac osx
if [ "$(uname)" == "Darwin" ]; then
    if ! type python3 > /dev/null; then
        #use brew to install python
        ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        #install python
        brew install python3
    fi
#linux os
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    if ! type python3 > /dev/null; then
        apt-get install -y python3
    fi
    if ! type pip3 > /dev/null; then
        apt-get install -y python3-pip
    fi
fi

#run digital wallet
python3 ./src/digital_wallet.py ./paymo_input/batch_payment.txt ./paymo_input/stream_payment.txt ./paymo_output/output1.txt ./paymo_output/output2.txt ./paymo_output/output3.txt
