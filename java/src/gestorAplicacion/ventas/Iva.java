package gestorAplicacion.ventas;

public interface Iva {
	public static final Double IVA = 0.19;

	public abstract int calcularPrecio(int precio);
}
