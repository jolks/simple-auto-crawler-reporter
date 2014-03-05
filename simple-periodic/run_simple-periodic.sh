# Embed beat (periodic service) in 1 worker
#celery worker -B --app=execute --loglevel=info
dtach -n /tmp/crawl celery worker -B --app=execute
