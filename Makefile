define BACKEND_PACKAGES
python3-venv \
python3-dev \
tox \
endef


# Dependencies

install-dependencies: install-backend-dependencies
.PHONY: install-dependencies

install-backend-dependencies:
	sudo -E DEBIAN_FRONTEND=noninteractive apt -y install $(BACKEND_PACKAGES)
.PHONY: install-backend-dependencies