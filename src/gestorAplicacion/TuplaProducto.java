package gestorAplicacion;

public class TuplaProducto {
	private int cantidad;
	private Producto producto;
	
	public TuplaProducto(Producto producto, int Cantidad) {
		this.producto = producto;
		this.cantidad = cantidad;
	}

	public int getCantidad() {
		return cantidad;
	}
	
	public void setCantidad(int cantidad) {
		this.cantidad = cantidad;
	}

	public Producto getProducto() {
		return producto;
	}


}
