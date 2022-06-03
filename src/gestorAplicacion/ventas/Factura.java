package gestorAplicacion.ventas;

import java.util.ArrayList;
import java.util.HashMap;

import gestorAplicacion.general.Documento;
import gestorAplicacion.general.Inventario;
import gestorAplicacion.personas.Empleado;

import java.io.Serializable;

/**
 * Esta clase extiende de Documento y se encarga de manejar las facturas de la aplicacion
 * los cuales se generan cada vez que hay un pago y se usan para 
 * efuectuar la devolucion de un producto
 * 
 * @author Mateo Alvarez Lebrum
 * @author Alejandro Alvarez Botero
 * @author Miguel Angel Barrera Bustamante
 * @author Alejandra Barrientos Grisales
 */

public class Factura extends Documento implements Serializable {
	private static final long serialVersionUID = 1L;

	private static int numConsecutivos;

	private Empleado expedidoPor;
	private String identificador;
	private String consecutivo;
	private int total;
	private String numeroIdentificacionPersona;
	private HashMap<Producto, Integer> productos;
	private HashMap<Servicio, Empleado> servicios;

	public Factura(HashMap<Producto, Integer> productos, HashMap<Servicio, Empleado> servicios, String numero) {
		Factura.numConsecutivos += 1;
		this.consecutivo = Factura.numConsecutivos + "";
		this.productos = new HashMap<Producto, Integer>(productos);
		this.servicios = new HashMap<Servicio, Empleado>(servicios);
		this.total = this.calcularCosto();
		this.identificador = generarIdentificador();
		this.expedidoPor = empleadoAleatorio();
		this.numeroIdentificacionPersona = numero;
		Inventario.agregarFactura(this);
	}

	/** Este metodo suma todos los precios de los productos y servicios que van a ser pagados
	 * @return total
	 */
	private int calcularCosto() {
		int total = 0;
		// Obtiene el precio de cada producto y lo multiplica por su cantidad
		for (Producto producto : productos.keySet()) {
			total += producto.getPrecio() * productos.get(producto);
		}
		// Obtiene el precio de cada servicio
		for (Servicio servicio : servicios.keySet()) {
			total += servicio.getPrecio();
		}
		return total;
	}

	/** Este metodo se emplea en la devolucion de producto
	 * @param total
	 */
	public void reajustarTotal(int total) {
		this.total = total;
	}

	/** Este metodo retira la cantidad especifica de un producto en una factura
	 * se usa en la funcionalidad de devolver producto
	 * @param productoARetirar
	 * @param cantidadARetirar
	 */
	public void retirarProducto(Producto productoARetirar, int cantidadARetirar) {
		for (HashMap.Entry<Producto, Integer> producto : this.productos.entrySet()) {
			if (producto.getKey() == productoARetirar) {
				this.productos.put(producto.getKey(), producto.getValue() - cantidadARetirar);
			}
		}
	}

	public String getConsecutivo() {
		return consecutivo;
	}

	public Empleado getExpedidoPor() {
		return expedidoPor;
	}

	public String getIdentificador() {
		return identificador;
	}

	public int getTotal() {
		return total;
	}

	public String getNumeroIdentificacionPersona() {
		return numeroIdentificacionPersona;
	}

	public HashMap<Producto, Integer> getProductos() {
		return productos;
	}

	public HashMap<Servicio, Empleado> getServicios() {
		return servicios;
	}

	/** Este metodo muestra informacion acerca de los productos y las unidades que se compraron
	 * @return Informacion de los productos
	 */
	public String informacionProductos() {
		
		if (!productos.isEmpty()) {
			String text = "";
			for (HashMap.Entry<Producto, Integer> m : productos.entrySet()) {
				text += "Se compro " + m.getValue() + " unidad(es) de " + m.getKey().getNombre() + "\n";
			}
			return text.substring(0, text.length() - 1);
		}
		return "No se compraron productos";

	}

	/** Este metodo muestra informacion acerca del nombre de los servicios,
	 *  el nombre del empleado asignado y se calcula la cantidad de dias que lleva en la empresa
	 *  dicho empleado que va a realizar el servicio
	 * @return
	 */
	public String informacionServicios() {
		if (!servicios.isEmpty()) {
			String text = "";
			for (HashMap.Entry<Servicio, Empleado> m : servicios.entrySet()) {
				Servicio servicio = m.getKey();
				Empleado empleado = m.getValue();
				text += "Se compro el servicio " + servicio.getNombre() + " que va a ser ejecutado por "
						+ empleado.getNombre() + " que lleva " + empleado.getContrato().cantidadDiasEmpresa()
						+ " dias en esta empresa" + "\n";
			}
			return text.substring(0, text.length() - 1);
		}
		return "No se compraron servicios";
	}

	/**
	 * Este metodo crea el identificador unico de cada factura
	 */
	protected String generarIdentificador() {
		String text = "";
		for (int i = 0; i < 5; i++) {
			text += ((int) (Math.random() * 10)) + "";
		}
		return text + "-" + consecutivo;
	}

	/** Este metodo asigna un empleado aleatorio que va a ser el que realice la factura
	 * @return
	 */
	private Empleado empleadoAleatorio() {
		ArrayList<Empleado> listaEmpleadosActivos = new ArrayList<Empleado>();

		// Se extraen solo los empleados activos
		for (Empleado i : Inventario.getListadoEmpleados()) {
			if (i.isActivo()) {
				listaEmpleadosActivos.add(i);
			}
		}

		// De los empleados activos se elige uno al azar
		return listaEmpleadosActivos.get((int) Math.round((Math.random() * (listaEmpleadosActivos.size() - 1))));
	}

	/**
	 * @return Informacion de la factura
	 */
	public String mostrarInformacion() {
		String text = "";

		text += "Factura: " + identificador + "\n";
		text += "La factura ha sido generada por " + expedidoPor.getNombre() + "\n\nDESCRIPCION\n";

		text += informacionProductos() + "\n";
		text += informacionServicios() + "\n";

		text += "\nTOTAL: " + total + "\n";

		text += "Gracias por la compra. Esperamos disfute de sus productos y servicios adquiridos.\n\n";

		return text;

	}

}
