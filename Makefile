push:
	git add . 
	git commit --amend
	git push --force

build:
	docker build -t dagster-test-image:v1.0 . 