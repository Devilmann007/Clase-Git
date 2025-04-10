// Frontend/src/main.tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import { Producto } from './components/Producto';

const productoMock = {
  _id: '1',
  nombre: 'Camiseta',
  descripcion: 'Camiseta blanca de algodón',
  precio: 25000,
  stock: 12,
  tallas: ['S', 'M', 'L'],
  colores: ['Blanco', 'Negro'],
  fechaCreacion: new Date().toISOString()
};

const handleEliminar = (id: string) => {
  console.log(`Eliminar producto con id: ${id}`);
};

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Producto producto={productoMock} onEliminar={handleEliminar} />
  </React.StrictMode>
);
