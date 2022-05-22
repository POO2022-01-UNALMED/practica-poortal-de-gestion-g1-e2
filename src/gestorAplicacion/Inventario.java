package gestorAplicacion;

import java.util.ArrayList;
import java.time.LocalDate;

public class Inventario {
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
		Persona.personasAContratar.add(persona);

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
			if (i.getFechaExpedicion() == date) {
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
}
