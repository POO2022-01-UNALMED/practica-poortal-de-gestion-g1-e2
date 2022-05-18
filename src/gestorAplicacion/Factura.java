package gestorAplicacion;

import java.util.ArrayList;
import java.util.HashMap;

public class Factura extends Documento {
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
		this.productos = productos;
		this.servicios = servicios;
		this.total = this.calcularCosto();
		this.identificador = generarIdentificador();
		this.expedidoPor = empleadoAleatorio();
		this.numeroIdentificacionPersona = numero;
	}

	private int calcularCosto() {
		int total = 0;
		for (Producto producto : productos.keySet()) {
			total += producto.getPrecio()*productos.get(producto);
		}
		for (Servicio servicio : servicios.keySet()) {
			total += servicio.getPrecio();
		}
		return total;
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

	public String informacionProductos() {
		if (!productos.isEmpty()) {
			String text = "";
			for (HashMap.Entry<Producto, Integer> m : productos.entrySet()) {
				text += "Se compro" + m.getValue() + "unidad(es) de" + m.getKey().getNombre() + "\n";
			}
			return text;
		}
		return "No se compraron productos";

	}

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
			return text;
		}
		return "No se compraron servicios";
	}

	String generarIdentificador() {
		String text = "";
		for (int i = 0; i < 5; i++) {
			text += ((int) (Math.random() * 10)) + "";
		}
		return text + "-" + consecutivo;
	}

	private Empleado empleadoAleatorio() {
		ArrayList<Empleado> listaEmpleadosActivos = new ArrayList<Empleado>();

		for (Empleado i : Inventario.getListadoEmpleados()) {
			if (i.isActivo()) {
				listaEmpleadosActivos.add(i);
			}
		}

		return listaEmpleadosActivos.get((int) Math.round((Math.random() * listaEmpleadosActivos.size())));
	}

}
