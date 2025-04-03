db.Usuarios.insertOne({
    nombre: "Juan Pérez",
    email: "juan@example.com",
    edad: 30
});

db.Usuarios.find({ edad: { $gt: 30 } })