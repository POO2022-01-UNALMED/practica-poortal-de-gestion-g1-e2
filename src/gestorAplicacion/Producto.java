package gestorAplicacion;

import java.io.Serializable;

public class Producto implements Iva, Serializable {
	private static final long serialVersionUID = 1L;
	
	private String nombre;
	private int cantidadDisponible;
	private Categoria categoria;
	private int precio;
	private int mesesGarantia;
	private int cantidadCarrito;

	public Producto(String nombre, int cantidadDisponible, Categoria categoria, int precio, int mesesGarantia) {
		this.nombre = nombre;
		this.cantidadDisponible = cantidadDisponible;
		this.categoria = categoria;
		this.precio = calcularPrecio(precio);
		this.mesesGarantia = mesesGarantia;
		cantidadCarrito = 0;
		Inventario.agregarProducto(this);
	}

	public Producto(String nombre, Categoria categoria, int garantia) {
		this(nombre, 0, categoria, 0, garantia);
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public Categoria getCategoria() {
		return categoria;
	}

	public void setCategoria(Categoria categoria) {
		this.categoria = categoria;
	}

	public int getPrecio() {
		return precio;
	}
	
	public void agregarCantidadCarrito(int num) {
		cantidadCarrito += num;
	}
	
	public void disminuirCantidadCarrito(int num) {
		cantidadCarrito -= num;
	}

	public void setPrecio(int precio) {
		this.precio = precio;
	}

	public int getMesesGarantia() {
		return mesesGarantia;
	}

	public void setMesesGarantia(int mesesGarantia) {
		this.mesesGarantia = mesesGarantia;
	}

	public int getCantidadDisponible() {
		return cantidadDisponible-cantidadCarrito;
	}

	public void reabastecer(int num) {
		cantidadDisponible += num;
	}

	public boolean verificarCantidad(int num) {
		return getCantidadDisponible() >= num;
	}

	public void vender(int num) {
		cantidadDisponible -= num;
		cantidadCarrito -= num;
	}

	public int calcularPrecio(int precio) {
		return (int) Math.round(precio + precio * IVA);
	}

}
