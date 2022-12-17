prisma-format:
	prisma format && prisma generate && prisma migrate dev --name init
