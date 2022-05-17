package gestorAplicacion;

import java.util.HashMap;

public class Factura extends Documento {
	private static int numConsecutivos;

	private String identificador;
	private String consecutivo;
	private int total;
	private HashMap<Producto, Integer> productos;
	private HashMap<Servicio, Empleado> servicios;

	public Factura(HashMap<Producto, Integer> productos, HashMap<Servicio, Empleado> servicios) {
		Factura.numConsecutivos += 1;
		this.consecutivo = Factura.numConsecutivos + "";
		this.productos = productos;
		this.servicios = servicios;
		this.total = this.calcularCosto();
		this.identificador = generarIdentificador();
	}

	private int calcularCosto() {
		int total = 0;
		for (Producto producto : productos.keySet()) {
			total += producto.getPrecio();
		}
		for (Servicio servicio : servicios.keySet()) {
			total += servicio.getPrecio();
		}
		return total;
	}

	public String getConsecutivo() {
		return consecutivo;
	}

	public String getIdentificador() {
		return identificador;
	}

	public int getTotal() {
		return total;
	}

	public String getProductos() {
		String text = "";
		for (HashMap.Entry<Producto, Integer> m : productos.entrySet()) {
			text += "Se compro" + m.getValue() + "unidad(es) de" + m.getKey().getNombre() + "\n";
		}
		return text;

	}

	public String getServicios() {
		String text = "";
		for (HashMap.Entry<Servicio, Empleado> m : servicios.entrySet()) {
			Servicio servicio = m.getKey();
			Empleado empleado = m.getValue();
			text += "Se compro el servicio " + servicio.getNombre() + " que va a ser ejecutado por "
					+ empleado.getNombre() + " que lleva " + empleado.getContrato().cantidadDiasEmpresa()
					+ " dias en esta empresa" + "\n";
		}
		return text;
	}

	String generarIdentificador() {
		String text = "";
		for (int i = 0; i < 5; i++) {
			text += ((int) (Math.random() * 10)) + "";
		}
		return text + "-" + consecutivo;
	}

}
