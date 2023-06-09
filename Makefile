hello_world_server:
	uvicorn app.quickstart:app --reload

prediction_service:
	uvicorn app.prediction_service:app --reload

image:
	docker build -t prediction_service .

prediction_service_container:
	docker run --name prediction_service \
		--detach \
		-p 8000:8000 \
		prediction_service



.PHONY: hello_world_server prediction_service image