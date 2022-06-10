package gestorAplicacion.ventas;

import java.time.LocalDate;
import java.util.ArrayList;

import gestorAplicacion.general.Inventario;
import gestorAplicacion.personas.Empleado;

import java.io.Serializable;
/**
 * Esta clase implementa la interface Iva y tiene como finalidad definir todos lo atributos y métodos de un servicio que
 * será adquirido por un cliente y prestado por un empleado
 * 
 * @author Mateo Alvarez Lebrum
 * @author Alejandro Alvarez Botero
 * @author Miguel Angel Barrera Bustamante
 * @author Alejandra Barrientos Grisales
 */

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

	/**
	 * Calcula el precio teniendo en cuenta el IVA
	 * @param precio
	 * @return precio con Iva
	 */
	public int calcularPrecio(int precio) {
		return (int) Math.round(precio + precio * IVA);
	}

	/**
	 * Separa los empleados que estén disponibles para prestar un servicio en una fecha determinada
	 * @param fechaSolicitud
	 * @return empleadosDisponibles
	 */
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
