Descripción General
Este proyecto consiste en una aplicación de gestión de inventarios que permite realizar 
operaciones básicas de administración sobre productos. Las funcionalidades implementadas 
incluyen el registro, actualización, eliminación, búsqueda, y reporte de productos. 
La aplicación utiliza una base de datos SQLite para almacenar y gestionar los datos de los productos.

Requisitos Previos
Para ejecutar esta aplicación, es necesario tener instalado:

Python 3.7 o superior.
SQLite: Se utiliza para la base de datos, y ya está integrado con Python, por lo que no requiere 
instalación adicional.
Verificación de la Versión de Python
Para asegurarse de que tienes la versión adecuada de Python instalada, ejecuta el siguiente comando 
en tu terminal o línea de comandos:
python --version
Este proyecto utiliza SQLite, que es parte de Python, por lo que no se requieren dependencias adicionales.

Funcionalidades Implementadas
La aplicación cuenta con las siguientes funcionalidades:

1. Registrar Producto
Permite ingresar un nuevo producto al inventario. Cada producto incluye los siguientes atributos:

Nombre del producto.
Cantidad disponible.
Precio por unidad.
Descripción breve del producto.

2. Mostrar Todos los Productos
Muestra un listado con todos los productos registrados en la base de datos.

3. Actualizar Producto
Permite actualizar los detalles de un producto específico, como su cantidad disponible.

4. Eliminar Producto
Permite eliminar un producto del inventario especificando su ID único.

5. Buscar Producto por ID
Permite buscar un producto en la base de datos mediante su ID único. Se muestran los detalles del producto encontrado.

6. Generar Reporte de Bajo Stock
Muestra un listado de productos cuyo stock es menor a 5 unidades. Esta funcionalidad facilita la identificación de productos con bajo inventario para su reabastecimiento.

Instrucciones para Ejecutar la Aplicación

1. Abrir la Terminal
Accede a la terminal o línea de comandos y navega al directorio donde descargaste o clonaste el proyecto.

2. Ejecutar la Aplicación
Para iniciar la aplicación, utiliza el siguiente comando:

python main.py
Esto lanzará el programa y mostrará un menú de opciones en la terminal.

3. Interactuar con la Aplicación
Una vez que el programa esté en ejecución, verás un menú interactivo con las siguientes opciones:

Agregar Producto: Ingresa un nuevo producto en el inventario.
Mostrar Productos: Muestra todos los productos almacenados.
Actualizar: Actualiza los detalles de un producto existente.
Eliminar: Elimina un producto de la base de datos.
Buscar Producto: Busca y muestra un producto específico por su ID.
Reporte Bajo Stock: Muestra productos con stock inferior a 5 unidades.

Para seleccionar una opción, simplemente ingresa el número correspondiente y 
sigue las instrucciones en pantalla.

Consideraciones Adicionales
La aplicación utiliza SQLite para almacenar los productos de forma local. Cada vez que se ejecuta, 
los datos persisten en el archivo de base de datos.
Si la base de datos aún no existe, el programa la creará automáticamente al ejecutarse por primera vez.