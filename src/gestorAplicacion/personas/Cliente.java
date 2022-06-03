package gestorAplicacion.personas;

import java.util.ArrayList;
import java.util.HashMap;

import gestorAplicacion.general.Inventario;
import gestorAplicacion.ventas.Factura;
import gestorAplicacion.ventas.Producto;
import gestorAplicacion.ventas.Servicio;

import java.time.LocalDate;

/**
 * Esta clase extiende de persona y se encarga de definir
 * todos los atributos y metodos necesarios para gestionar su carrito 
 * y realizar compras y devoluciones
 * 
 * @author Mateo Alvarez Lebrum
 * @author Alejandro Alvarez Botero
 * @author Miguel Angel Barrera Bustamante
 * @author Alejandra Barrientos Grisales
 */

public class Cliente extends Persona {
	private static final long serialVersionUID = 1L;

	private HashMap<Producto, Integer> productos = new HashMap<Producto, Integer>();
	private HashMap<Servicio, Empleado> servicios = new HashMap<Servicio, Empleado>();

	public Cliente(String nombre, String telefono, String email, String identificacion,
			TipoDocumento tipoDeIdentificacion, Sexo sexo) {
		super(nombre, telefono, email, identificacion, tipoDeIdentificacion, sexo);
	}

	/**
	 * Este metodo genera una factura con los productos que hay en el carrito
	 * @return Factura de compra
	 */
	public Factura pagar() {
		// Verifica que todos los servicios del carrito tengan empleado asignado
		if (servicios.containsValue(null)) {
			throw new Error(
					"\nActualmente tiene servicios sin empleado asignado, por favor seleccione empleados primero.\n\n");
		}

		// Se genera una factura asociada a la compra
		Factura factura = new Factura(productos, servicios, identificacion);

		// Por cada producto del carrito se ejecuta su metodo "vender" que disminuye su cantidad disponible en la tienda
		for (Producto i : productos.keySet()) {
			i.vender(productos.get(i));
		}

		// Se limpia el carrito de compras
		productos.clear();
		servicios.clear();

		return factura;
	}

	/**
	 * Este metodo busca dentro de los servicios del carrito cuales no tienen un empleado asignado
	 * @return lista de servicios sin empleados
	 */
	public ArrayList<Servicio> obtenerServiciosSinEmpleado() {
		ArrayList<Servicio> serviciosSinEmpleado = new ArrayList<Servicio>();
		
		// Recorre el hashmap correspondiente a servicio y ve cuales no tienen un objeto empleado como value
		for (HashMap.Entry<Servicio, Empleado> i : servicios.entrySet()) {
			if (i.getValue() == null) {
				serviciosSinEmpleado.add(i.getKey());
			}
		}

		if (serviciosSinEmpleado.isEmpty()) {
			throw new Error("\nEl cliente no tiene servicios a los cuales les deba asignar un empelado\n\n");
		}

		return serviciosSinEmpleado;
	}

	/**
	 * @param producto
	 * @param cantidad
	 */
	public void agregarProductoALaCanasta(Producto producto, int cantidad) {
		// Si el producto ya esta en el carrito de compras le suma la nueva cantidad
		// ingresada a la cantidad que ya tenia
		for (HashMap.Entry<Producto, Integer> i : this.productos.entrySet()) {
			if (i.getKey() == producto) {
				// Actualiza la cantidad del producto en los diferentes carritos
				producto.agregarCantidadCarrito(cantidad);

				this.productos.put(i.getKey(), i.getValue() + cantidad);
				return;
			}
		}

		// Si el producto no esta en el carrito lo agrega junto a su cantidad
		producto.agregarCantidadCarrito(cantidad);
		productos.put(producto, cantidad);

	}

	/**
	 * @param producto
	 */
	public void eliminarProductoDeLaCanasta(Producto producto) {
		// Actualiza la suma de las cantidades del productos en los diferentes carritos
		producto.disminuirCantidadCarrito(productos.get(producto));
		productos.remove(producto);
	}

	/**
	 * @param servicio
	 */
	public void solicitarServicio(Servicio servicio) {
		// Verifica que el servicio no se encuentre en el carrito
		if (servicios.containsKey(servicio)) {
			throw new Error("El servicio ya fue solicitado.");
		}
		servicios.put(servicio, null);
	}

	/** 
	 * Este metodo asigna un empleado a un servicio en el carrito
	 * @param servicio
	 * @param empleado
	 */
	public void seleccionarEmpleado(Servicio servicio, Empleado empleado) {
		for (HashMap.Entry<Servicio, Empleado> i : servicios.entrySet()) {
			if (i.getKey() == servicio) {
				i.setValue(empleado);
			}
		}
	}

	/**
	 * @param servicio
	 */
	public void eliminarServicioDeLaCanasta(Servicio servicio) {
		servicios.remove(servicio);
	}

	/**
	 * @param nombreProducto
	 * @param identificacion
	 * @param cantidadADevolver
	 * @param fecha
	 * @return Mensaje con la informacion del dinero retornado al cliente
	 */
	public static String devolverProducto(String nombreProducto, String identificacion, int cantidadADevolver,
			LocalDate fecha) {
		
		// Verificar que existe un producto con ese nombre en el inventario
		
		boolean productoEncontrado = false;
		Producto productoComprado = null;
		for (Producto producto : Inventario.getListadoProductos()) {
			if (producto.getNombre().equals(nombreProducto)) {
				productoEncontrado = true;
				productoComprado = producto;
			}
		}

		if (!productoEncontrado)
			throw new Error("El producto no existe en nuestro inventario");

		// Verificar que existe una factura en ese dia con ese producto

		boolean facturaEncontrada = false;
		Factura facturaCompra = null;
		LocalDate fechaProporcionada = fecha;
		
		// Encuentra factura que contiene ese producto y fue comprado por la persona que
		// lo esta devolviendo y coincide en la fecha proporcionada
		
		for (Factura factura : Inventario.getListadoFacturas()) {
			if (factura.getNumeroIdentificacionPersona().equals(identificacion)
					&& Inventario.buscarFactura(fechaProporcionada) != null) {
				for (Producto producto : factura.getProductos().keySet()) {
					if (productoComprado == producto) {
						facturaEncontrada = true;
						facturaCompra = factura;
					}
				}
			}
		}

		if (!facturaEncontrada)
			throw new Error(
					"No existen facturas con dicha informacion de compra asociada(producto/identificacion/fecha)");

		// Verificar que los productos a devolver sean menores a los comprados

		boolean cantidadValida = false;
		for (HashMap.Entry<Producto, Integer> compra : facturaCompra.getProductos().entrySet()) {
			if (compra.getKey() == productoComprado) {
				if (compra.getValue() >= cantidadADevolver) {
					cantidadValida = true;
				}
			}
		}

		if (!cantidadValida)
			throw new Error("Intenta devolver mas productos de los que fueron comprados");

		// Verificar que el tiempo de garantia aun se cumpla

		LocalDate tiempoMaximo = facturaCompra.getFechaExpedicion().plusMonths(productoComprado.getMesesGarantia());
		if (tiempoMaximo.isBefore(fechaProporcionada))
			throw new Error("Ya paso el tiempo de garantia");

		// Modificar el total de la factura y la cantidad de productos

		int reembolso = productoComprado.getPrecio() * cantidadADevolver;
		facturaCompra.reajustarTotal(facturaCompra.getTotal() - reembolso);
		facturaCompra.retirarProducto(productoComprado, cantidadADevolver);

		// Retorna dinero de reembolso
		String texto = "\nLa devolucion se realizo exitosamente\n" + "\nSe han devuelto " + cantidadADevolver + " "
				+ nombreProducto + "(s) del cliente con identificacion: "
				+ facturaCompra.getNumeroIdentificacionPersona() + "\n" + "\nEl dinero retornado es " + reembolso
				+ "\n";

		return texto;
	}

	public boolean carritoVacio() {
		if (productos.isEmpty() && servicios.isEmpty()) {
			return true;
		}
		return false;
	}

	/** Muestra la informacion del cliente
	 *
	 */
	public String mostrarInformacion() {
		return "Soy el cliente " + nombre + " con numero de identificacion: " + identificacion;
	}

	/**
	 * @return String con la informacion de los productos y servicios en el carrito
	 */
	public String verCarrito() {
		String text = "";

		// Si el hashmap de productos tiene algun elemento, se agrega la informacion de
		// la cantidad disponible y el nombre, en caso contrario no se hace nada
		if (!productos.isEmpty()) {
			for (HashMap.Entry<Producto, Integer> i : productos.entrySet()) {
				text += i.getValue() + " unidad(es) del producto " + i.getKey().getNombre() + "\n";
			}
		}

		// Si el hashmap de servicios tiene algun elemento, se agrega l
		if (!servicios.isEmpty()) {
			for (HashMap.Entry<Servicio, Empleado> i : servicios.entrySet()) {
				if (i.getValue() == null) {
					text += "Servicio " + i.getKey().getNombre() + " que no tiene un empleado asignado aun\n";
				} else {
					text += "Servicio " + i.getKey().getNombre() + " que sera ejecutado por el empleado "
							+ i.getValue().getNombre() + "\n";
				}

			}
		}

		// Si no tiene ningun producto o servicio se retorna el siguiente mensaje
		if (text.equals("")) {
			return "No tiene productos ni servicios en su carrito";
		}

		return text;
	}

	public ArrayList<Servicio> getServicios() {
		ArrayList<Servicio> servicios = new ArrayList<Servicio>();
		for (Servicio i : this.servicios.keySet()) {
			servicios.add(i);
		}

		if (servicios.isEmpty()) {
			throw new Error("No tiene servicios en el carrito actualmente");
		}

		return servicios;
	}

	public ArrayList<Producto> getProductos() {
		ArrayList<Producto> productos = new ArrayList<Producto>();
		for (Producto i : this.productos.keySet()) {
			productos.add(i);
		}

		if (productos.isEmpty()) {
			throw new Error("No tiene productos en el carrito actualmente");
		}

		return productos;
	}
}
