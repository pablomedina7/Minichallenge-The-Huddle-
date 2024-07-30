--Actualizar registros: Escribe una consulta SQL para actualizar el nombre de un usuario específico en la tabla
UPDATE public.usuarios
	SET id=1, "nombre"= 'Pablo Adrian'
	WHERE "nombre"= 'PAXC';
