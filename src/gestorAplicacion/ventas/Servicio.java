package gestorAplicacion.ventas;

import java.time.LocalDate;
import java.util.ArrayList;

import gestorAplicacion.general.Inventario;
import gestorAplicacion.personas.Empleado;

import java.io.Serializable;

public class Servicio implements Iva, Serializable {
	private static final long serialVersionUID = 1L;

	private String nombre;
	private int precio;

	public Servicio(String nombre, int precio) {
		this.nombre = nombre;
		this.precio = calcularPrecio(precio);
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

	public int calcularPrecio(int precio) {
		return (int) Math.round(precio + precio * IVA);
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

	public String toString() {
		return nombre;
	}
}
