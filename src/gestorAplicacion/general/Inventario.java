package gestorAplicacion.general;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

import gestorAplicacion.personas.Cliente;
import gestorAplicacion.personas.Empleado;
import gestorAplicacion.personas.Persona;
import gestorAplicacion.ventas.Factura;
import gestorAplicacion.ventas.Producto;
import gestorAplicacion.ventas.Servicio;

import java.time.LocalDate;
import java.io.Serializable;

public class Inventario implements Serializable {

	private static final long serialVersionUID = 1L;

	private static ArrayList<Producto> listadoProductos = new ArrayList<Producto>();
	private static ArrayList<Servicio> listadoServicios = new ArrayList<Servicio>();
	private static ArrayList<Factura> listadoFacturas = new ArrayList<Factura>();
	private static ArrayList<Persona> listadoPersonas = new ArrayList<Persona>();

	public static ArrayList<Producto> getListadoProductos() {
		return listadoProductos;
	}

	public static ArrayList<Servicio> getListadoServicios() {
		return listadoServicios;
	}

	// Los servicios disponibles son aquellos en los que se hay al menos un empleado
	// trabajando en el
	public static ArrayList<Servicio> getServiciosDisponibles() {
		ArrayList<Servicio> serviciosDisp = new ArrayList<Servicio>();

		// De cada empleado se extrae su servicio y se agrega a la lista
		for (Empleado i : Inventario.getListadoEmpleados()) {
			if (!(i.getServicio() == null)) {
				serviciosDisp.add(i.getServicio());
			}
		}

		// Se eliminan los servicios repetidos
		Set<Servicio> hashSet = new HashSet<Servicio>(serviciosDisp);
		serviciosDisp.clear();
		serviciosDisp.addAll(hashSet);
		return serviciosDisp;
	}

	public static ArrayList<Factura> getListadoFacturas() {
		return listadoFacturas;
	}

	public static ArrayList<Empleado> getListadoEmpleados() {
		ArrayList<Empleado> empleados = new ArrayList<Empleado>();

		for (Persona i : listadoPersonas) {
			if (i instanceof Empleado) {
				empleados.add((Empleado) i);
			}
		}
		return empleados;
	}
	
	public static ArrayList<Empleado> getListadoEmpleadosActivos() {
		ArrayList<Empleado> empleadosActivos = new ArrayList<Empleado>();
		for (Empleado i : getListadoEmpleados()) {
			if (i.isActivo()) {
				empleadosActivos.add(i);
			}
		}
		return empleadosActivos;
	}

	public static void agregarProducto(Producto producto) {
		listadoProductos.add(producto);
	}

	public static void agregarServicio(Servicio servicio) {
		listadoServicios.add(servicio);
	}

	public static void agregarFactura(Factura factura) {
		listadoFacturas.add(factura);
	}

	public static void agregarPersona(Persona persona) {
		listadoPersonas.add(persona);

	}
	
	public static void eliminarPersona(Persona persona) {
		listadoPersonas.remove(persona);
	}

	public static ArrayList<Persona> getListadoPersonas() {
		return listadoPersonas;
	}

	public static Producto buscarProducto(String nombre) {
		for (Producto i : listadoProductos) {
			if (i.getNombre().equals(nombre)) {
				return i;
			}
		}
		throw new Error("No hay Productos que coincidan con el nombre especificado");
	}

	public static Servicio buscarServicio(String nombre) {
		for (Servicio i : listadoServicios) {
			if (i.getNombre().equals(nombre)) {
				return i;
			}
		}
		throw new Error("No hay Servicios que coincidan con el nombre especificado");
	}

	public static Empleado buscarEmpleado(String nombre) {
		for (Empleado i : getListadoEmpleados()) {
			if (i.getNombre().equals(nombre)) {
				return i;
			}
		}
		throw new Error("No hay Empleados que coincidan con el nombre especificado");
	}

	public static Factura buscarFactura(String num) {
		for (Factura i : listadoFacturas) {
			if (i.getConsecutivo().equals(num)) {
				return i;
			}
		}
		throw new Error("\nNo hay Facturas que coincidan con el consecutivo especificado\n\n");
	}

	public static Factura buscarFactura(LocalDate date) {
		for (Factura i : listadoFacturas) {
			if (i.getFechaExpedicion().isEqual(date)) {
				return i;
			}
		}
		throw new Error("No hay Facturas que coincidan con la fecha especificada");
	}

	public static ArrayList<Cliente> clientesConCarrito() {
		ArrayList<Cliente> clientes = new ArrayList<Cliente>();

		for (Persona i : listadoPersonas) {
			if (i instanceof Cliente && (!((Cliente) i).carritoVacio())) {
				clientes.add((Cliente) i);
			}
		}
		if (clientes.isEmpty()) {
			throw new Error("\nNo hay clientes con servicios o productos en su carrito de compra\n\n");
		}
		return clientes;
	}

	public static ArrayList<Cliente> getClientes() {
		ArrayList<Cliente> clientes = new ArrayList<Cliente>();
		for (Persona i : listadoPersonas) {
			if (i instanceof Cliente) {
				clientes.add((Cliente) i);
			}
		}

		if (clientes.isEmpty()) {
			throw new Error("\nNo hay clientes disponibles en este momento\n\n");
		}

		return clientes;
	}

	public static ArrayList<Producto> getProductosDisponibles() {
		ArrayList<Producto> productosDisp = new ArrayList<Producto>();

		// Solo se van a retornar los productos que tienen una cantidad disponible
		// superior a 0
		for (Producto i : listadoProductos) {
			if (i.getCantidadDisponible() > 0) {
				productosDisp.add(i);
			}
		}

		if (productosDisp.isEmpty()) {
			throw new Error("\nNo tenemos productos disponibles en este momento\n\n");
		}

		return productosDisp;
	}
}
