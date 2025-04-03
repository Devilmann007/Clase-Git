Create table Usuarios(
    id int primary key,--identificamos la llave primaria esto hace que cada usuario tenga un identificador unico
    nombre varchar (100),
    email varchar(150) Unique, --Unique garantiza que el email sea unico para cada usuario
    fecha_registro date,
)

SELECT * FROM Usuarios
WHERE nombre LIKE 'A%';--Busca nombres que comiencen por la letra A;
--en postgre SQL; ILIKE que ignora mayusculas y minusculas,
-- % para que tome los caracteres despues de la A sin importar la cantidad

UPDATE Usuarios --indicamos la tabla a actualizar
SET email = 'nuevo_email@example.com' --SET cambia el valor del campo email
WHERE id = 1;--WHERE id solo actualiza el dato de usuario id=1
