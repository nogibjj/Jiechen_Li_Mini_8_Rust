python_install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

python_test:
	python3 -m pytest -vv --cov=main test_*.py

python_format:	
	black *.py 

python_lint:
	pylint --disable=R,C,locally-disabled --ignore-patterns=test_.*?py *.py

# Rust-specific commands

# install_rust:
# 	cargo check

# test_rust:
# 	cargo test

# format_rust:
# 	cargo fmt

# lint_rust:
# 	cargo clippy

# # Rust-specific commands

# install-rust:
# 	cargo check

# test-rust:
# 	cargo test

# run-rust:
# 	cargo run 
		
# container-lint:
# 	docker run --rm -i hadolint/hadolint < Dockerfile

# refactor: format lint

# deploy:
# 	#deploy goes here
		
python_all: install lint test format 
