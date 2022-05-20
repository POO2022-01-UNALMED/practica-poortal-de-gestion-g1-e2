package gestorAplicacion;

import java.time.LocalDate;
import java.util.ArrayList;

public class Servicio implements Iva {
	private String nombre;
	private int precio;
	private Empleado empleadoAsignado;

	public Servicio(String nombre, int precio, Empleado empleadoAsignado) {
		this.nombre = nombre;
		this.precio = calcularPrecio(precio);
		this.empleadoAsignado = empleadoAsignado;
		Inventario.agregarServicio(this);
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public int getPrecio() {
		return precio;
	}

	public void setPrecio(int precio) {
		this.precio = precio;
	}

	public Empleado getEmpleadoAsignado() {
		return empleadoAsignado;
	}

	public void setEmpleadoAsignado(Empleado empleadoAsignado) {
		this.empleadoAsignado = empleadoAsignado;
	}

	public int calcularPrecio(int precio) {
		return (int) Math.round(precio * IVA);
	}

	public ArrayList<Empleado> consultarDisponibilidad(LocalDate fechaSolicitud) {
		ArrayList<Empleado> listaEmpleados = Inventario.getListadoEmpleados();
		ArrayList<Empleado> empleadosDisponibles = new ArrayList<Empleado>();
		for (Empleado empleado : listaEmpleados) {
			if (empleado.consultarDisponibilidadEmpleado(this, fechaSolicitud)) {
				empleadosDisponibles.add(empleado);
			}
		}
		return empleadosDisponibles;
	}
}
