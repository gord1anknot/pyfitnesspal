#!/bin/bash

echo "remember, you can run \"./create_venv.sh reset\" to reset your environment..."

if [ "$1" = "reset" ] ; then
	echo "resetting environment now..."
	rm -rf "./.venv"
	rm -f "./.env"
fi

if [ ! -d ".venv" ] ; then
	if [ -f "$(which virtualenv)" ] ; then
		virtualenv --python=python2.7 --prompt=\(pyfitnesspal\) .venv
		.venv/bin/pip install -r requirements.txt
		.venv/bin/pip install -r dev-requirements.txt
		cat>>.env<<-EOF
		DATABASE_URL="sqlite:///$(pwd)/db.sqlite3"
		SECRET_KEY="$(./.make_secret.py)"
		PYFITNESSPAL_USERNAME="demo"
		PYFITNESSPAL_PASSWORD="Passw0rd!"
		EOF
	else
		echo "Please ensure that virtualenv is installed and on the PATH."
	fi
fi

source .venv/bin/activate
if [ -s ".env" ] ; then
	# using 'eval' to treat the quotes in the .env file
	# using word-splitting. Having quotes around string
	# keys is good for honcho / foreman but not for
	# bash
	while read V; do eval "export $V" ; done < "./.env"
fi
