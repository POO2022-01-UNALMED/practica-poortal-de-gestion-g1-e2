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

	public void devolverProducto(int dinero, Empleado empleado) {

	}
}
