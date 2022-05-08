package gestorAplicacion;

import java.util.ArrayList;

public class Cliente extends Persona {

	private ArrayList<Servicio> servicios = new ArrayList<Servicio>();
	private ArrayList<TuplaProducto> productos = new ArrayList<TuplaProducto>();

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

	public void pagar(int dinero, Empleado empleado) {

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

	public void solicitarServicio(Servicio servicio) {
		boolean servicioExistente = false;

		for (Servicio i : servicios) {
			if (i == servicio) {
				if (i.consultarDisponibilidad()) {
					servicioExistente = true;
				} else {
					throw new Error("El servicio solicitado no cuenta con disponibilidad.");
				}
				break;
			}
		}
		if (!servicioExistente) {
			servicios.add(servicio);
		} else {
			throw new Error("El servicio ya fue solicitado.");			
		}
	}

	public void devolverProducto(int dinero, Empleado empleado) {

	}
}
