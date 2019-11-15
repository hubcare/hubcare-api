############################# Makefile ##########################
build:
	sudo docker-compose build

up:
	sudo docker-compose up

down:
	sudo docker-compose down --volume

test:
	sudo docker-compose up -d
	sudo docker-compose exec hubcare_api python manage.py test
	sudo docker-compose exec commit-metrics python manage.py test
	sudo docker-compose exec community-metrics python manage.py test
	sudo docker-compose exec issue-metrics python manage.py test
	sudo docker-compose exec pull-request-metrics python manage.py test

coverage:
	sudo docker-compose up -d
	sudo docker-compose exec hubcare_api coverage run --source='.' --omit=*/tests/*,*/tests.py,*/migrations/*,*/urls.py,*/settings.py,*/wsgi.py,manage.py manage.py test
	sudo docker-compose exec hubcare_api coverage report

	sudo docker-compose exec commit_metrics coverage run --source='.' --omit=*/tests/*,*/tests.py,*/migrations/*,*/urls.py,*/settings.py,*/wsgi.py,manage.py manage.py test
	sudo docker-compose exec commit_metrics coverage report

	sudo docker-compose exec community_metrics coverage run --source='.' --omit=*/tests/*,*/tests.py,*/migrations/*,*/urls.py,*/settings.py,*/wsgi.py,manage.py manage.py test
	sudo docker-compose exec community_metrics coverage report

	sudo docker-compose exec issue_metrics coverage run --source='.' --omit=*/tests/*,*/tests.py,*/migrations/*,*/urls.py,*/settings.py,*/wsgi.py,manage.py manage.py test
	sudo docker-compose exec issue_metrics coverage report

	sudo docker-compose exec pull_request_metrics coverage run --source='.' --omit=*/tests/*,*/tests.py,*/migrations/*,*/urls.py,*/settings.py,*/wsgi.py,manage.py manage.py test
	sudo docker-compose exec pull_request_metrics coverage report
	
style:
	sudo docker-compose up -d
	sudo docker-compose exec hubcare_api pycodestyle .

	sudo docker-compose exec commit_metrics pycodestyle .
	sudo docker-compose exec community_metrics pycodestyle .
	sudo docker-compose exec issue_metrics pycodestyle .
	sudo docker-compose exec pull_request_metrics pycodestyle .

build_nginx:
	cp nginx.conf /etc/nginx.conf
	docker run -d --name=nginx --restart=unless-stopped -p 80:80 -p 443:443 -v /etc/letsencrypt:/etc/letsencrypt -v /etc/nginx.conf:/etc/nginx/conf.d/default.conf --link=hubcare_api --link=issue-metrics --link=commit-metrics --link=community-metrics --link=pull-request-metrics --link=repository --net=hubcare-api_default nginx:1.11

create_certificate:
	certbot certonly

renew_certificate:
	certbot renew

reload_nginx:
	docker-compose -f docker-compose.production.yml exec nginx nginx -s reload