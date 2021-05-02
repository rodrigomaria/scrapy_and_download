help: ## show this help
	@echo 'usage: make [target] [option]'
	@echo ''
	@echo 'Common sequence of commands:'
	@echo '- make black'
	@echo '- make isort'
	@echo '- make flake8'
	@echo ''
	@echo 'targets:'
	@egrep '^(.+)\:\ .*##\ (.+)' ${MAKEFILE_LIST} | sed 's/:.*##/#/' | column -t -c 2 -s '#'


.PHONY: black
black: ## run black over the code
	@ black execute/*.py

.PHONY: isort
isort: ## run isort over the code
	@ isort execute

.PHONY: flake8
flake8: ## run flake8 over the code
	@ flake8 execute