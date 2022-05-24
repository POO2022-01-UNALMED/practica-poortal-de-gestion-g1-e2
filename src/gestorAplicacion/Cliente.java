package gestorAplicacion;

import java.util.ArrayList;
import java.util.HashMap;
import java.time.LocalDate;

public class Cliente extends Persona {
	private static final long serialVersionUID = 1L;

	private HashMap<Producto, Integer> productos = new HashMap<Producto, Integer>();
	private HashMap<Servicio, Empleado> servicios = new HashMap<Servicio, Empleado>();

	public Cliente(String nombre, String telefono, String email, String identificacion,
			TipoDocumento tipoDeIdentificacion, Sexo sexo) {
		super(nombre, telefono, email, identificacion, tipoDeIdentificacion, sexo);
	}

	public HashMap<Servicio, Empleado> getServicios() {
		return servicios;
	}

	public HashMap<Producto, Integer> getProductos() {
		return productos;
	}

	public Factura pagar() {
		if (servicios.containsValue(null)) {
			throw new Error(
					"Actualmente tiene servicios sin empleado asignado, por favor seleccione empleados primero.");
		}
		Factura factura = new Factura(productos, servicios, identificacion);

		for (Producto i : productos.keySet()) {
			i.vender(productos.get(i));
		}

		productos.clear();
		servicios.clear();

		return factura;
	}

	public ArrayList<Servicio> obtenerServiciosSinEmpleado() {
		ArrayList<Servicio> serviciosSinEmpleado = new ArrayList<Servicio>();
		for (HashMap.Entry<Servicio, Empleado> i : servicios.entrySet()) {
			if (i.getValue() == null) {
				serviciosSinEmpleado.add(i.getKey());
			}
		}
		return serviciosSinEmpleado;
	}

	public void agregarProductoALaCanasta(Producto producto, int cantidad) {
		if (producto.verificarCantidad(cantidad)) {
			boolean productoExistente = false;
			for (HashMap.Entry<Producto, Integer> i : this.productos.entrySet()) {
				if (i.getKey() == producto) {
					productoExistente = true;
					this.productos.put(i.getKey(), i.getValue() + cantidad);
					break;
				}
			}
			if (!productoExistente) {
				productos.put(producto, cantidad);
			}
		} else {
			throw new Error("No hay productos suficientes en el inventario.");
		}
	}

	public void eliminarProductoDeLaCanasta(Producto producto) {
		boolean productoExistente = false;
		for (HashMap.Entry<Producto, Integer> i : this.productos.entrySet()) {
			if (i.getKey() == producto) {
				productoExistente = true;
				this.productos.put(i.getKey(), i.getValue() - 1);
				break;
			}
		}
		if (!productoExistente) {
			throw new Error("El producto solicitado no se encuentra actualmente en la canasta.");
		}
	}

	public void solicitarServicio(Servicio servicio) {
		if (servicios.containsKey(servicio)) {
			throw new Error("El servicio ya fue solicitado.");
		}
		servicios.put(servicio, null);
	}

	public void seleccionarEmpleado(Servicio servicio, Empleado empleado) {
		for (HashMap.Entry<Servicio, Empleado> i : servicios.entrySet()) {
			if (i.getKey() == servicio) {
				i.setValue(empleado);
			}
		}
	}

	public void eliminarServicioDeLaCanasta(Servicio servicio) {
		boolean servicioExistente = servicios.containsKey(servicio);

		if (servicioExistente) {
			servicios.remove(servicio);
		} else {
			throw new Error("El servicio solicitado no se encuentra actualmente en la canasta.");
		}
	}

	public static int devolverProducto(String nombreProducto, String identificacion, int cantidadADevolver, LocalDate fecha) {
		// Verificar que existe un producto con ese nombre

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
			throw new Error("No existen facturas con dicha informacion de compra asociada(producto/identificacion/fecha)");

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
			throw new Error("Intenta devolver más productos de los que fueron comprados");

		// Verificar que el tiempo de garantia aun se cumpla

		LocalDate tiempoMaximo = facturaCompra.getFechaExpedicion().plusMonths(productoComprado.getMesesGarantia());
		if (tiempoMaximo.isBefore(fechaProporcionada))
			throw new Error("Ya pasó el tiempo de garantia");

		// Modificar el total de la factura y la cantidad de productos

		int reembolso = productoComprado.getPrecio() * cantidadADevolver;
		facturaCompra.reajustarTotal(facturaCompra.getTotal() - reembolso);
		facturaCompra.retirarProducto(productoComprado, cantidadADevolver);

		// Retorna dinero de reembolso
		return reembolso;
	}

	public boolean carritoVacio() {
		if (productos.isEmpty() && servicios.isEmpty()) {
			return true;
		}
		return false;
	}

	public String mostrarInformacion() {
		return "Soy el cliente " + nombre + " con numero de identificacion: " + identificacion;
	}
}
