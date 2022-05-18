package gestorAplicacion;

import java.util.ArrayList;
import java.util.HashMap;
import java.time.LocalDate;

public class Cliente extends Persona {

	private HashMap<Producto, Integer> productos;
	private HashMap<Servicio, Empleado> servicios;

	public Cliente(String nombre, String telefono, String email, String identificacion,
			TipoDocumento tipoDeIdentificacion, Sexo sexo, ArrayList<Servicio> servicios,
			ArrayList<TuplaProducto> productos) {
		super(nombre, telefono, email, identificacion, tipoDeIdentificacion, sexo);
		this.servicios = servicios;
		this.productos = productos;
	}

	public Cliente(String nombre, String telefono, String email, String identificacion,
			TipoDocumento tipoDeIdentificacion, Sexo sexo) {
		super(nombre, telefono, email, identificacion, tipoDeIdentificacion, sexo);
	}

	public ArrayList<Servicio> getServicios() {
		return servicios;
	}

	public ArrayList<TuplaProducto> getProductos() {
		return productos;
	}

	public void pagar() {
		Factura factura = new Factura(productos, servicios, identificacion);
		Inventario.agregarFactura(factura);
		
		for(Producto i : productos.keySet()) {
			i.vender(productos.get(i));
		}
		
		productos.clear();
		servicios.clear();
	}

	public void agregarProductoALaCanasta(Producto producto, int cantidad) {
		if (producto.verificarCantidad(cantidad)) {
			boolean productoExistente = false;
			for (TuplaProducto i : productos) {
				if (i.getProducto() == producto) {
					productoExistente = true;
					i.setCantidad(i.getCantidad() + cantidad);
					break;
				}
			}
			if (!productoExistente) {
				productos.add(new TuplaProducto(producto, cantidad));
			}
		} else {
			throw new Error("No hay productos suficientes en el inventario.");
		}
	}

	public void eliminarProductoDeLaCanasta(Producto producto) {
		boolean productoExistente = false;
		for (TuplaProducto i : productos) {
			if (i.getProducto() == producto) {
				productoExistente = true;
				i.setCantidad(i.getCantidad() - 1);
				break;
			}
		}
		if (!productoExistente) {
			throw new Error("El producto solicitado no se encuentra actualmente en la canasta.");
		}
	}

	public void solicitarServicio(Servicio servicio, LocalDate fechaSolicitud) {
		for (Servicio i : servicios) {
			if (i == servicio) {
				throw new Error("El servicio ya fue solicitado.");
			}
		}
		if (servicio.consultarDisponibilidad(fechaSolicitud).size() > 1) {
			servicios.add(servicio);
		} else {
			throw new Error("El servicio solicitado no cuenta con disponibilidad.");
		}
	}
	
	public void eliminarServicioDeLaCanasta(Servicio servicio) {
		boolean servicioExistente = servicios.remove(servicio);
		
		if (!servicioExistente) {
			throw new Error("El servicio solicitado no se encuentra actualmente en la canasta.");
		}
	}

	public int devolverProducto(String nombreProducto, String identificacion, int cantidadADevolver, int dia, int mes, int anio) {
		// Verificar que existe un producto con ese nombre

		boolean productoEncontrado = false;
		Producto productoComprado = null;

		for (Producto producto : Inventario.getListadoProductos()) {
			if (producto.getNombre() == nombreProducto) {
				productoEncontrado = true;
				productoComprado = producto;
			}
		}

		if (!productoEncontrado) throw new Error("El producto no existe en nuestro inventario");

		// Verificar que existe una factura en ese dia con ese producto

		boolean facturaEncontrada = false;
		Factura facturaCompra = null;
		LocalDate fechaProporcionada = LocalDate.of(anio, mes, dia);
		// Encuentra factura que contiene ese producto y fue comprado por la persona que lo esta devolviendo y coincide en la fecha proporcionada

		for (Factura factura : Inventario.getListadoFacturas()) {
			if (factura.getNumeroIdentificacionPersona() == identificacion && Inventario.buscarFactura(fechaProporcionada) != null) {
				for (Producto producto : factura.getProductos().keySet()) {
					if (productoComprado == producto) {
						facturaEncontrada = true;
						facturaCompra = factura;
					}
				}
			}
		}

		if (!facturaEncontrada) throw new Error("No existen facturas con ese producto");

		// Verificar que los productos a devolver sean menores a los comprados

		boolean cantidadValida = false;
		for (HashMap.Entry<Producto, Integer> compra : facturaCompra.getProductos().entrySet()) {
			if (compra.getKey() == productoComprado){
				if (compra.getValue() > cantidadADevolver){
					cantidadValida = true;
				}
			}
		}

		if (!cantidadValida) throw new Error("No existen facturas con ese producto");
		
		// Verificar que el tiempo de garantia aun se cumpla

		LocalDate tiempoMaximo = facturaCompra.getFechaExpedicion().plusMonths(productoComprado.getMesesGarantia());
		if (tiempoMaximo.isBefore(fechaProporcionada)) throw new Error("Ya paso el tiempo de garantia");

		// Modificar el total de la factura y la cantidad de productos

		// Retorna dinero de reembolso
		return productoComprado.getPrecio() * cantidadADevolver;
	}
}
