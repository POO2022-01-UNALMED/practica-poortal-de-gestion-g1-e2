package gestorAplicacion;

import java.util.ArrayList;

public class Inventario {
	private static ArrayList<Producto> listadoProductos = new ArrayList<Producto>();
	private static ArrayList<Servicio> listadoServicios = new ArrayList<Servicio>();
	private static ArrayList<Factura> listadoFacturas = new ArrayList<Factura>();
	private static ArrayList<Empleado> listadoEmpleados = new ArrayList<Empleado>();
	

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
		return listadoEmpleados;
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
	
	public static void agregarEmpleado(Empleado empleado) {
		listadoEmpleados.add(empleado);
	}
	
	public static Producto buscarProducto(String nombre) {
		for (Producto i:listadoProductos) {
			if (i.getNombre().equals(nombre)) {
				return i;
			}
		}
		return null;
	}
	
	public static Servicio buscarServicio(String nombre) {
		for (Servicio i:listadoServicios) {
			if (i.getNombre().equals(nombre)) {
				return i;
			}
		}
		return null;
	}
	
	public static Empleado buscarEmpleado(String nombre) {
		for (Empleado i:listadoEmpleados) {
			if (i.getNombre().equals(nombre)) {
				return i;
			}
		}
		return null;
	}
	
	public static Factura buscarFactura(int num) {
		for (Factura i:listadoFacturas) {
			if (i.getConsecutivo() == num) {
				return i;
			}
		}
		return null;
	}
	
		
}
