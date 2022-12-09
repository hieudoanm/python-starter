lock:
	pigar

serve:
	python3 main.py

prisma-format:
	prisma format && prisma generate && prisma migrate dev --name init
