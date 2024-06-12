COMPOSE_FILE 	:= ./docker-compose.yml

.PHONY: all
all:	build

.PHONY: build
build:
	@docker compose -f $(COMPOSE_FILE) build

.PHONY: up
up:
	@docker compose -f $(COMPOSE_FILE) up -d

.PHONY: down
down:
	@docker compose -f $(COMPOSE_FILE) down

.PHONY: ps
ps:
	@docker compose -f $(COMPOSE_FILE) ps

.PHONY: logs
logs:
	@docker compose -f $(COMPOSE_FILE) logs -f -t -n 100

.PHONY: clean
clean:
	@docker system prune -f

.PHONY: fclean
fclean:
	@docker system prune -a --volumes

.PHONY: re
re:
	${MAKE} -s fclean
	${MAKE} -s build
