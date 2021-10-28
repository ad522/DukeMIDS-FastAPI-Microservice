install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_main.py

format:
	black *.py

run:
	python main.py

run-uvicorn:
	uvicorn main:app --reload

killweb:
	sudo killall uvicorn

lint:
	pylint --disable=R,C main.py


dockerbuild:
	docker build -t fantasyf1

dockerrun:
	docker run --name ff1 -d -p 1080:1080 fantasyf1

all: install lint