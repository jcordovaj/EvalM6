# Introducción 

Este proyecto tiene como objetivo desarrollar una plataforma web para la venta de vehículos, permitiendo a los usuarios solicitar cotizaciones y recibir información detallada sobre los vehículos disponibles.

## Estructura del Proyecto

- **Apps:**
  - **cotizacion:** Gestiona las solicitudes de cotización, incluyendo un modelo para almacenar los datos de los solicitantes y un formulario para capturar la información.
  - **vehiculos:** Contiene el modelo Vehiculo para almacenar los detalles de cada vehículo (marca, modelo, año, etc.) y las imágenes asociadas.
  - **usuarios:** (Opcional) Si se requiere un sistema de autenticación más avanzado, se puede crear una app para gestionar usuarios, grupos y permisos.
- **Modelos:**
  - **Vehiculo:**
    - id (PK)
    - nombre
    - descripcion
    - imagen
    - precio
    - otros atributos relevantes
  - ***Cotizacion:** (deshabilitado)*
    - id (PK)
    - nombre (del solicitante)
    - email
    - mensaje
    - vehiculo (relación ForeignKey con Vehiculo), pendiente de implementar

**Funcionalidades**

- **Galería de de vehículos:** Mostrar tarjetas con vehículos disponibles en oferta y un botón para solicitar cotización, incluye imágenes y descripciones.
- **Formulario de cotización:** Permitir a los usuarios solicitar cotizaciones para vehículos específicos.
- **Listado de vehículos:** **Los usuarios std. pueden ver los vehículos. usuarios crud pueden agregar, y  los administradores pueden agregar, editar y eliminar vehículos.
- **Almacenamiento de cotizaciones:** Guarda las cotizaciones en la base de datos para su seguimiento.
- **Autenticación de usuarios:** Completo sistema de registro y login para permitir a los usuarios navegar por la aplicación de acuerdo a su perfil y acceder a información personalizada.

**Roadmap de Características Adicionales (Things To Do - TD2)**

- **Búsqueda de vehículos:** Implementar un sistema de búsqueda avanzado para permitir a los usuarios encontrar vehículos por marca, modelo, año, precio, etc.
- **Carrito de compras:** Permitir a los usuarios agregar vehículos a un carrito y realizar una compra.
- **Pagos en línea:** Integrar una pasarela de pago para procesar pagos.
- **Administración de inventario:** Permitir a los administradores agregar, editar y eliminar vehículos.
- **Reportes:** Generar reportes sobre las cotizaciones y ventas.
- **Diseño de la interfaz de usuario:** Mejorar la interfaz con un diseño atractivo y fácil de usar para la aplicación.
- **Optimización del rendimiento:** Implementar técnicas para mejorar el rendimiento de la aplicación, especialmente en la carga de imágenes y la búsqueda de vehículos.
- **Seguridad:** Implementar medidas de seguridad para proteger los datos de los usuarios y prevenir ataques como inyección SQL y XSS.
- **Pruebas:** Realizar pruebas exhaustivas para garantizar la calidad y estabilidad de la aplicación.
- **Documentación:** Crear una documentación detallada de la aplicación para facilitar el mantenimiento y futuras ampliaciones.

**Diagrama de Clases (UML)**

[Pendiente diagrama UML con las relaciones entre los modelos Vehiculo y Cotizacion]

**Herramientas Usadas:**

- **Framework:** Django
- **Base de datos:** Sqlite3
- **Front-end:** HTML, CSS, JavaScript, Bootstrap
- **Version control:** Git, Github

**Próximos Pasos:**

- **Requisitos detallados:** Elaborar una lista completa de funcionalidades y especificaciones técnicas.
- **Crear un diseño de la interfaz de usuario:** Diseñar la apariencia, "look & feel" y la experiencia del usuario.
- **Mejorar el backend:** Optimizar los modelos, vistas y URL.
- **Mejorar el frontend:** Actualizar las plantillas HTML y el código JavaScript necesario.
- **Realizar pruebas:** Probar la aplicación en diferentes navegadores y dispositivos.
- **Implementar la funcionalidad de correo electrónico:** Configurar un servidor SMTP para enviar correos.

**Administración:**

* **Usuario:** admin
* **Pass:** 123456
