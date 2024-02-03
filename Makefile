init:
	test -n "$(name)"
	rm -rf ./.git
	find ./ -type f -exec perl -pi -e 's/app-example/$(name)/g' *.* {} \;
	mv ./app-example ./$(name)

superuser:
	docker exec -it app-example ./manage.py createsuperuser

shell:
	docker exec -it app-example ./manage.py shell

makemigrations:
	docker exec -it app-example ./manage.py makemigrations

migrate:
	docker exec -it app-example ./manage.py migrate

initialfixture:
	docker exec -it app-example ./manage.py loaddata initial

testfixture:
	docker exec -it app-example ./manage.py loaddata test

test:
	docker exec -it app-example ./manage.py test

statics:
	docker exec -it app-example ./manage.py collectstatic --noinput

makemessages:
	docker exec -it app-example django-admin makemessages

compilemessages:
	docker exec -it app-example django-admin compilemessages
