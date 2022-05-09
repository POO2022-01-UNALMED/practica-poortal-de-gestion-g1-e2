package gestorAplicacion;

import java.util.ArrayList;
import java.time.LocalDate;

public class Factura {
	private static int consecutivos;
	private int consecutivo;
	private int total;
	private int cambio;
	private LocalDate fecha;
	private ArrayList<Producto> productos;
	private ArrayList<Servicio> servicios;

	public Factura(ArrayList<Producto> productos, ArrayList<Servicio> servicios) {
		Factura.consecutivos += 1;
		this.consecutivo = Factura.consecutivos;
		this.productos = productos;
		this.servicios = servicios;
		this.total = this.calcularCosto();
		this.fecha = LocalDate.now();
	}

	private int calcularCosto() {
		int total = 0;
		for (Producto producto : this.productos) {
			total += producto.getPrecio();
		}
		for (Servicio servicio : this.servicios) {
			total += servicio.getPrecio();
		}
		return total;
	}

	public int getConsecutivo() {
		return consecutivo;
	}

	public void setConsecutivo(int consecutivo) {
		this.consecutivo = consecutivo;
	}

	public int getTotal() {
		return total;
	}

	public void setTotal(int total) {
		this.total = total;
	}

	public int getCambio() {
		return cambio;
	}

	public void setCambio(int cambio) {
		this.cambio = cambio;
	}

	public ArrayList<Producto> getProductos() {
		return productos;
	}

	public void setProductos(ArrayList<Producto> productos) {
		this.productos = productos;
	}

	public ArrayList<Servicio> getServicios() {
		return servicios;
	}

	public void setServicios(ArrayList<Servicio> servicios) {
		this.servicios = servicios;
	}

	public LocalDate getFecha() {
		return fecha;
	}

}
