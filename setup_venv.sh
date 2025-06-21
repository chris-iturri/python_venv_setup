if python3.12 --version 2>&1 | grep -q "Python 3.12.7"; then
    echo "Python 3.12.7 is running."
else
    echo "Python 3.12.7 is not running."
fi
python3 -m pip install virtualenv
python3.12 -m virtualenv myvenv # create a new venv in ./venv
source ./myvenv/bin/activate # activate your new venv
